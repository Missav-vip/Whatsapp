from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Menjalankan di background (tanpa UI)

# Ganti path ke chromedriver sesuai sistem Anda
driver_path = "path_to_chromedriver"

# Setup driver
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Login ke Instagram (gunakan cookies atau login manual untuk mencegah pemblokiran akun)
def login_instagram(username, password):
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(3)

    # Masukkan username dan password untuk login
    username_field = driver.find_element(By.NAME, 'username')
    password_field = driver.find_element(By.NAME, 'password')

    username_field.send_keys(username)
    password_field.send_keys(password)
    
    password_field.submit()
    time.sleep(5)

# Follow pengguna berdasarkan URL profil
def follow_user(profile_url):
    driver.get(profile_url)
    time.sleep(3)

    try:
        # Klik tombol Follow jika belum mengikuti
        follow_button = driver.find_element(By.XPATH, "//button[text()='Follow']")
        follow_button.click()
        print("User followed successfully.")
    except Exception as e:
        print("Follow button not found or already following.")

# Main function untuk mengotomatiskan semua proses
def main():
    # Masukkan kredensial Instagram Anda
    username = "your_username"  # Ganti dengan username Instagram Anda
    password = "your_password"  # Ganti dengan password Instagram Anda

    # Login ke Instagram
    login_instagram(username, password)

    # URL profil yang ingin di-follow
    profile_url = "https://www.instagram.com/mrobotfx"  # Ganti dengan URL profil yang ingin di-follow

    # Follow pengguna
    follow_user(profile_url)

    # Setelah selesai, tutup driver
    driver.quit()

if __name__ == "__main__":
    main()
