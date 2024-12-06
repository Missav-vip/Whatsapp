from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

# Ganti dengan path ke ChromeDriver Anda
driver_path = 'path/to/chromedriver'

# Fungsi untuk login ke Instagram
def login_to_instagram(username, password):
    driver = webdriver.Chrome(driver_path)
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(3)
    
    # Temukan elemen input untuk username dan password
    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')
    
    # Masukkan username dan password
    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)
    return driver

# Fungsi untuk menemukan pengguna Korea berdasarkan hashtag atau lokasi
def search_korean_users(hashtag, num_users=10):
    search_url = f'https://www.instagram.com/explore/tags/{hashtag}/'
    driver.get(search_url)
    time.sleep(3)
    
    # Temukan post berdasarkan hashtag
    posts = driver.find_elements(By.XPATH, '//a[contains(@href, "/p/")]')
    post_links = [post.get_attribute('href') for post in posts[:num_users]]
    
    # Ambil usernames dari postingan yang ditemukan
    usernames = []
    for link in post_links:
        driver.get(link)
        time.sleep(2)
        user = driver.find_element(By.XPATH, '//a[@href and @title]')
        usernames.append(user.text)
        print(f'Found User: {user.text} | Post Link: {link}')
    
    return usernames

# Fungsi untuk follow pengguna yang ditemukan
def follow_users(usernames):
    for username in usernames:
        driver.get(f'https://www.instagram.com/{username}/')
        time.sleep(2)
        
        try:
            # Klik tombol follow jika tombol Follow ditemukan
            follow_button = driver.find_element(By.XPATH, '//button[text()="Follow"]')
            follow_button.click()
            print(f'Followed {username}')
        except Exception as e:
            print(f'Error following {username}: {e}')
        time.sleep(random.randint(5, 10))  # Jeda acak untuk menghindari deteksi bot

# Fungsi utama
def main():
    # Ganti dengan username dan password akun Instagram Anda
    username_real = 'mrobotfx'
    password_real = '$22dolar'
    
    # Login ke Instagram menggunakan akun nyata
    global driver
    driver = login_to_instagram(username_real, password_real)

    # Tentukan hashtag atau lokasi Korea
    korean_hashtag = 'korea'  # Bisa diubah ke hashtag yang relevan

    # Tentukan jumlah pengguna yang ingin di-follow
    num_followers_to_add = 100000  # Tentukan jumlah followers yang ingin ditambahkan

    # Scrape pengguna yang memposting dengan hashtag Korea
    usernames_to_follow = search_korean_users(korean_hashtag, num_users=10)

    # Pastikan untuk menambahkan jumlah followers sesuai keinginan
    usernames_to_follow = usernames_to_follow[:num_followers_to_add]

    # Follow pengguna yang ditemukan
    follow_users(usernames_to_follow)

    # Tutup browser setelah selesai
    driver.quit()

# Jalankan skrip utama
if __name__ == "__main__":
    main()
