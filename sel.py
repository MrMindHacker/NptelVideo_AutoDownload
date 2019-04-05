from selenium import webdriver as wb
import time
from selenium.webdriver.common.keys import Keys

browser = input("""
Select Browser:
            1) Chrome
            2) Firefox
        Enter Browser: """)
link = input("Enter Page Link: ")
link_text = input("Enter Link Text: ")

if browser == '1':
    k = wb.Chrome("./chromedriver")
elif browser == '2':
    profile = wb.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", 'E:\\Work\\codes\\Nptel\\Downloads\\')
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

    k = wb.Firefox(firefox_profile=profile)

k.get("https://nptel.ac.in/courses/nptel_download.php?subjectid=106106145")
l = k.find_elements_by_link_text("MP4 Download")
for i in l:
    i.click()













"""
box = k.find_element_by_id("identifierId")
box.send_keys("sonarkeyur")
box.send_keys(Keys.RETURN)
time.sleep(6)
box = k.find_element_by_name("password")
box.send_keys("")
box.send_keys(Keys.RETURN) """


# Nptel Download Link = https://nptel.ac.in/courses/nptel_download.php?subjectid=106106145
# https://www.edureka.co/community/2170/can-we-use-selenium-to-work-with-already-open-browser-session
# https://softwaretestingboard.com/q2a/1911/how-use-already-opened-browser-for-testing-instead-opening#axzz5gTQfQeoy
# https://www.google.com/search?q=send+click+on+link+selenium+python&ie=utf-8&oe=utf-8&client=firefox-b-ab#kpvalbx=1

"""
    # binary = FirefoxBinary('/usr/bin/firefox')
    # driver = webdriver.Firefox(firefox_binary=binary)
"""
