import sys
import os
import json
from selenium import webdriver
from subprocess import call

fileExist = True

if (os.path.exists("./info.json")):
    with open("info.json") as json_file:
        data = json.load(json_file)
        print(data)
        userDir = str(data["userDir"])
        userName = str(data["userName"])
        gitEmail = str(data["email"])
        gitPass = str(data["password"])
else:
    fileExist = False
    userDir = "Null"
    userName = "Null"
    gitEmail = "Null"
    gitPass = "Null"
browser = webdriver.Chrome("C:\createProj\chromedriver_win32\chromedriver.exe")

try:
    sys.argv[1]
    sys.argv[2]
except NameError:
    print("You must specify two arguments for this program to function properly.")
    exit()
projName = sys.argv[1]
projType = sys.argv[2]
def main():
    print("Creating Project...")
    if (fileExist == False):
        createData()
        if (os.path.exists("./info.json")):
            with open("info.json") as json_file:
                data = json.load(json_file)
                userDir = str(data["userDir"])
                userName = str(data["Name"])
                gitEmail = str(data["email"])
                gitPass = str(data["password"])
    else:
        print("Baaaaaaaad")
    logIn()
    createGitRepo()
    createLocalRepo()
    print("Success!!!")
    browser.quit()

def createData():
    print("No data file exists yet :( probably because this is the first time you have run this program, please input the required values, to be stored in a Json file for this program to work.")
    newJson = {"userDir" : "Null", "userName" : "Null", "email" : "Null", "password" : "Null"}
    lUsrName = ""
    lUsrDir = ""
    lEmail = ""
    lPassword = ""
    print("Add data (Enter all details accuratly, as this is the only chance you will have to do so outside of manually deleting the file) \n")
    lUsrName = str(input("Enter your GitHub username: "))
    lEmail = str(input("Enter Email: "))
    lPassword = str(input("Enter Password: "))
    lUsrDir = str(input("Enter User directory name.  Can be found in C:\\Users\\yourdirectory"))
    print("\n")
    newJson["userDir"] = lUsrDir
    newJson["userName"] = lUsrName
    newJson["email"] = lEmail
    newJson["password"] = lPassword
    userDir = lUsrDir
    userName = lUsrName
    gitEmail = lEmail
    gitPass = lPassword
    with open('info.json', 'w') as outfile:
        json.dump(newJson, outfile)

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

def createGitRepo():
    print("Creating Github Repository...")
    pythonButton = browser.find_element_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div[2]/div/h2/a')
    pythonButton.click()
    pythonButton = browser.find_element_by_xpath('//*[@id="repository_name"]')
    pythonButton.send_keys(projName)
    pythonButton = browser.find_element_by_css_selector('#new_repository > div.js-with-permission-fields > button')
    pythonButton.submit()
    print("Github Repository Created!!")
    
def createLocalRepo():
    dir = os.path.join("C:\\","Users",userDir, "source", "repos", projName)
    if not os.path.exists(dir):
        os.mkdir(dir)
        os.chdir(dir)
    print("Creating local Repository...")
    call(["git", "config", "--global", gitEmail])
    call(["git", "config", "--global", userName])
    call(["git", "init"])
    call(["git", "add", "README.md"])
    if(projType == "DNCWebsite"):
        print("Creating ASP.NET Core Website")
        call(["dotnet", "new", "webapp", "-lang", "C#"])
    elif(projType == "Python"):
        print("Creating Python Project...")
        with open("./main.py", "w") as f:
            f.write("#! python3")
    call(["git", "commit", "-m", "Initial Commit"])
    call(["git", "remote", "add", "origin", f"https://github.com/{userName}/{projName}.git"])
    call(["git", "push", "-u", "origin", "master"])
    print("Local Repository Created!!")

if __name__ == "__main__":
    main()