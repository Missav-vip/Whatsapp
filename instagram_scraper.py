import requests
from bs4 import BeautifulSoup
import json

# Fungsi untuk mengambil ID pengguna dari URL
def get_instagram_profile(url):
    """
    Mendapatkan data profil pengguna dari URL Instagram tanpa login
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    # Mengirim permintaan ke URL Instagram
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # Mengambil konten HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Mencari informasi terkait pengguna (misalnya nama, follower, following)
        script = soup.find('script', text=lambda t: t.startswith('window._sharedData'))
        if not script:
            print("Gagal mengambil data profil. Pastikan URL valid.")
            return

        shared_data = script.string.split(' = ', 1)[1].rstrip(';')
        
        try:
            data = json.loads(shared_data)
            user_info = data['entry_data']['ProfilePage'][0]['graphql']['user']
            
            # Menampilkan beberapa data dasar
            print(f"Username: {user_info['username']}")
            print(f"Full Name: {user_info['full_name']}")
            print(f"Followers: {user_info['edge_followed_by']['count']}")
            print(f"Following: {user_info['edge_follow']['count']}")
            print(f"Biography: {user_info['biography']}")
            print(f"Profile Picture URL: {user_info['profile_pic_url_hd']}")
        except json.JSONDecodeError:
            print("Error parsing JSON data. Struktur halaman mungkin telah berubah.")
    else:
        print(f"Error: Tidak bisa mengambil data dari URL (status code: {response.status_code}).")

# Ganti dengan URL pengguna Instagram yang valid
url = "https://www.instagram.com/mrobotfx/"
get_instagram_profile(url)
