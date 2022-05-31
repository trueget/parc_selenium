from selenium import webdriver
from selenium.webdriver.common.by import By
import time


data = []
driver = webdriver.Chrome()
driver.get('https://russia.zarplata.ru/vacancy/vrach?limit=100')
time.sleep(3)
c = 0
for j in range(100):
    r = driver.find_elements(By.CLASS_NAME, 'info-column_ncvfz')

    for dri in r:


        dri.find_element(By.CLASS_NAME, 'vacancy-title').click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)
        org = driver.find_element(By.CLASS_NAME, 'title_7MBDL').find_element(By.TAG_NAME, 'a').text

        try:
            driver.find_element(By.CLASS_NAME, 'item_2PkbF').find_element(By.TAG_NAME, 'button').click()
            num = driver.find_element(By.CLASS_NAME, 'item_2PkbF').find_element(By.TAG_NAME, 'a').text
            adress = driver.find_element(By.CLASS_NAME, 'address_3E_Ck').text
            name = driver.find_element(By.CLASS_NAME, 'hr_cY2do').text

        except Exception:

            num = 'номер отсутствует!'
            adress = 'адрес не указан'
            name = 'имя отсутствует'

        vacancy = driver.find_element(By.CLASS_NAME, 'title_3Kcyd').find_element(By.TAG_NAME, 'h1').text
        firm = driver.find_element(By.CLASS_NAME, 'title_7MBDL').find_element(By.TAG_NAME, 'a').text

        data.append([org, name, num, adress, vacancy])
        print(c+1, data[c])
        c += 1
        time.sleep(1)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    driver.find_element(By.CLASS_NAME, 'next_d7TPs').click()
    time.sleep(1)


time.sleep(10)
driver.quit()
print(data)

