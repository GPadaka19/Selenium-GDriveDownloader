from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Lokasi di mana Anda menempatkan msedgedriver.exe
edge_driver_path = 'D:\\msedgedriver.exe'

# Membuat instance service
service = Service(edge_driver_path)

# Membuat instance Microsoft Edge (Chromium) browser
options = EdgeOptions()
# Atur preferensi agar file otomatis terdownload ke lokasi yang ditentukan
prefs = {
    "download.default_directory": r"D:\OneDrive - UNIVERSITAS AMIKOM YOGYAKARTA\!SAGASITAS\SLB DKI 24"
}
options.add_experimental_option("prefs", prefs)

# Daftar tautan file Google Drive
drive_links = [
   # BLABLABLA
]

# Data nama file sesuai dengan daftar yang diberikan
file_names = [
   # BLABLABLA
]

# Fungsi untuk mendownload file dari URL menggunakan browser Edge
def download_file(url, filename):
    try:
        # Mengakses URL
        driver.get(url)
        # Menunggu beberapa saat untuk memastikan halaman dimuat sepenuhnya
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Download']"))
        ).click()
        # Menunggu beberapa saat agar proses unduh selesai
        time.sleep(10)
    except Exception as e:
        print(f"Failed to download {filename} from {url}: {e}")

# Membuat instance Microsoft Edge (Chromium) browser
driver = webdriver.Edge(service=service, options=options)

# Mendownload semua file
for i, (link, file_name) in enumerate(zip(drive_links, file_names)):
    filename = f"{file_name}.zip"  # Menambahkan ekstensi file .zip
    download_file(link, filename)
    print(f"Downloaded {filename} from {link}")

# Menutup browser dan service setelah selesai
driver.quit()
service.stop()
