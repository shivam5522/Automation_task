import os

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def download_pdf(url, folder="notices/"):
    response = requests.get(url)
    if response.status_code == 200:
        if not os.path.exists(folder):
            os.makedirs(folder)

        filename = url.split("/")[-1]

        with open(os.path.join(folder, filename), "wb") as pdf_file:
            pdf_file.write(response.content)
    else:

        pass


driver = webdriver.Chrome()

driver.get("https://digitalscr.in/bzadiv/circulars/forms/index.php")
driver.implicitly_wait(10)
final_links = []
links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    final_links.append(link.get_attribute("href"))


for (
    link
) in (
    final_links
):  # Here were accessing all the notices from the NTA website. And as mentioned we only need the lastest pdf so breaking the loop.
    print(link)
    try:
        if link.endswith(".pdf"):
            download_pdf(link)
    except:
        print("ERROR")
        continue
    break
