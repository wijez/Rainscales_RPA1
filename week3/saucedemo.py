from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import os

cart_name = r'//*[@id="item_{index}_title_link"]/div'
cart_price = r'//*[@id="inventory_container"]/div/div[{index}]/div[2]/div[2]/div'

def setup(link):
    driver = webdriver.Edge()
    driver.get(link)
    return driver

def teardown(driver):
    driver.quit()
    
def login(driver, username, password):
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(5)
    
def download(driver): 
    file_path = "cart_items.csv"
    name_indexes = [4, 0, 1, 5, 2, 3]
    if not os.path.exists(file_path):
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "price"])
            writer.writeheader()
    for i, name_idx in enumerate(name_indexes):
        try:
            print(f"Đang lấy tên sản phẩm với name_idx={name_idx}...")
            name = driver.find_element(By.XPATH, cart_name.format(index=name_idx)).text
            print(f"  -> Tên: {name}")
        except Exception as e:
            print(f"Lỗi khi lấy tên sản phẩm tại name_idx={name_idx}: {e}")
            continue
        time.sleep(1)
        try:
            print(f"Đang lấy giá sản phẩm với price_idx={i+1}...")
            price = driver.find_element(By.XPATH, cart_price.format(index=i+1)).text
            print(f"  -> Giá: {price}")
        except Exception as e:
            print(f"Lỗi khi lấy giá sản phẩm tại price_idx={i+1}: {e}")
            continue
        time.sleep(1)
        try:
            with open(file_path, "a", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["name", "price"])
                writer.writerow({"name": name, "price": price})
            print(f"Đã ghi vào file: {name} - {price}")
        except Exception as e:
            print(f"Lỗi khi ghi file: {e}")
    

if __name__ == "__main__":
    driver = setup("https://www.saucedemo.com")
    login(driver, "standard_user", "secret_sauce")
    download(driver)
    teardown(driver)

