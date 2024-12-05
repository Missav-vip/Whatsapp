const { default: makeWASocket, useSingleFileAuthState } = require('@whiskeysockets/baileys');
const { unlinkSync } = require('fs');
const qrcode = require('qrcode-terminal');

// Simpan autentikasi
const { state, saveState } = useSingleFileAuthState('./auth_info.json');

async function startBot() {
    const sock = makeWASocket({
        auth: state,
        printQRInTerminal: true,
    });

    sock.ev.on('connection.update', (update) => {
        const { connection, qr } = update;

        if (connection === 'open') {
            console.log('Bot WhatsApp 082222222222 berhasil terhubung!');
        } else if (qr) {
            console.log('Scan QR code di bawah dengan WhatsApp di nomor 082222222222:');
            qrcode.generate(qr, { small: true });
        } else if (connection === 'close') {
            console.log('Koneksi terputus. Coba sambungkan ulang...');
            startBot(); // Reconnect jika koneksi terputus
        }
    });

    sock.ev.on('creds.update', saveState);

    // Respon pesan masuk
    sock.ev.on('messages.upsert', async (msg) => {
        const message = msg.messages[0];
        if (!message.message || message.key.fromMe) return;

        const sender = message.key.remoteJid;
        const text = message.message.conversation || message.message.extendedTextMessage?.text;

        console.log(`Pesan diterima dari ${sender}: ${text}`);

        // Logika balasan otomatis
        if (text.toLowerCase() === 'halo') {
            await sock.sendMessage(sender, { text: 'Hai! Ada yang bisa saya bantu?' });
        } else if (text.toLowerCase().includes('jam berapa')) {
            const now = new Date();
            await sock.sendMessage(sender, { text: `Sekarang pukul ${now.getHours()}:${now.getMinutes()}` });
        } else if (text.toLowerCase() === 'gambar') {
            await sock.sendMessage(sender, {
                image: { url: './image.jpg' }, // Pastikan file `image.jpg` ada di direktori yang sama
                caption: 'Ini adalah gambar contoh!',
            });
        } else if (text.toLowerCase() === 'dokumen') {
            await sock.sendMessage(sender, {
                document: { url: './file.pdf' }, // Pastikan file `file.pdf` ada di direktori yang sama
                mimetype: 'application/pdf',
                fileName: 'Contoh Dokumen.pdf',
            });
        } else {
            await sock.sendMessage(sender, { text: `Maaf, saya tidak mengerti perintah "${text}".` });
        }
    });
}

startBot();
