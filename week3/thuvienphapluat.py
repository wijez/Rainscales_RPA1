from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import csv
import os
import pandas as pd
from saucedemo import setup, teardown

tax_code = r'//*[@id="dvResultSearch"]/table/tbody/tr[{index}]/td[2]'
company_name = r'//*[@id="dvResultSearch"]/table/tbody/tr[{index}]/td[3]/div'
date = r'//*[@id="dvResultSearch"]/table/tbody/tr[{index}]/td[4]'
next_page = r'/html/body/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div/div[2]/nav/ul/li[6]/a'

def download(driver, max_pages=4):
    all_sheets = {}
    for page in range(1, max_pages + 1):
        data = []
        print(f"Đang thu thập dữ liệu trang {page}...")
        for i in range(1, 50):
            try:
                tax_code_text = driver.find_element(By.XPATH, tax_code.format(index=i)).text
                company_name_text = driver.find_element(By.XPATH, company_name.format(index=i)).text
                date_text = driver.find_element(By.XPATH, date.format(index=i)).text
                data.append({
                    "tax_code": tax_code_text,
                    "company_name": company_name_text,
                    "date": date_text
                })
            except Exception as e:
                break
        df = pd.DataFrame(data)
        all_sheets[f"Trang_{page}"] = df
        try:
            next_btn = driver.find_element(By.XPATH, next_page)
            next_btn.click()
            time.sleep(2)
        except Exception as e:
            print(f"Không tìm thấy nút 'Sau' ở trang {page}, dừng lại.")
            break
    return all_sheets

if __name__ == "__main__":
    driver = setup("https://thuvienphapluat.vn/ma-so-thue/tra-cuu-ma-so-thue-doanh-nghiep")
    sheets = download(driver)
    with pd.ExcelWriter("tax_codes.xlsx", engine="xlsxwriter") as writer:
        for sheet_name, df in sheets.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    print("Đã lưu dữ liệu ra file tax_codes.xlsx")