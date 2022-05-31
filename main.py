from selenium import webdriver
from selenium.webdriver.common.by import By
import time


data = []
names = []
driver = webdriver.Chrome()
driver.get('https://russia.zarplata.ru/vacancy/vrach?limit=100')
time.sleep(5)


for j in range(10):
    w = driver.find_elements(By.CLASS_NAME, 'list_1KKpD')
    # print('w', len(w))

    for dry in w:
        time.sleep(5)
        sit = dry.find_element(By.PARTIAL_LINK_TEXT, 'Контакты').get_attribute('href')
        time.sleep(5)

        driver.execute_script("window.open ()")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(sit)
        time.sleep(5)

        try:
            driver.find_element(By.CLASS_NAME, 'link-button_2sNwl').click()
            number = driver.find_element(By.CLASS_NAME, 'link_1izHq').text
        except Exception:
            number = 'Номер отсутствует!'

        time.sleep(5)

        org = driver.find_element(By.CLASS_NAME, 'item_1Ohuq').text
        name = driver.find_element(By.CLASS_NAME, 'hr_cY2do').text
        print(org, number, sit)
        print()
        if name not in names:
            data.append([org, number, sit])
            names.append(name)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    driver.find_element(By.CLASS_NAME, 'next_d7TPs').click()
    time.sleep(5)

time.sleep(3)
driver.quit()