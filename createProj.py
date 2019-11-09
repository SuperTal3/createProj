import sys
from selenium import webdriver
import time

gitEmail = "talkelley3@outlook.com"
gitPass = "~Tal82554048"
browser = webdriver.Chrome("C:\createProj\chromedriver_win32\chromedriver.exe")
projectName = sys.argv[1]
def main():
    print("Creating Project...")
    logIn()
    createRepo()
    print("Success!!!")
    browser.quit()

def logIn():
    print("Logging in to GitHub...")
    browser.get("https://github.com/login")
    #browser.switch_to_frame(browser.find_element_by_xpath('//*[@id="login"]/form'))
    pythonButton = browser.find_element_by_xpath('//*[@id="login_field"]')
    pythonButton.send_keys(gitEmail)
    pythonButton = browser.find_element_by_xpath('//*[@id="password"]')
    pythonButton.send_keys(gitPass)
    pythonButton = browser.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[8]')
    pythonButton.click()
    print("Logged In to GitHub")

def createRepo():
    print("Creating Github Repository...")
    pythonButton = browser.find_element_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div[2]/div/h2/a')
    pythonButton.click()
    pythonButton = browser.find_element_by_xpath('//*[@id="repository_name"]')
    pythonButton.send_keys(projectName)
    pythonButton = browser.find_element_by_css_selector('#new_repository > div.js-with-permission-fields > button')
    pythonButton.submit()
    print("Repository Created!!")

if __name__ == "__main__":
    main()