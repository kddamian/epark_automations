
#1
from selenium import webdriver
import pyautogui
import smtplib, ssl
import time
import os

username = ""
password = ""

url = "url"

driver = webdriver.Safari(port=0, executable_path="/usr/bin/safaridriver")
driver.maximize_window()
time.sleep(1)

driver.get(url)

driver.find_element_by_id("email").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_xpath("//*[contains(text(), 'Login')]").click()
time.sleep(5)
driver.get("url")
time.sleep(5)
driver.find_element_by_xpath("//div[contains(@class, 'flex space-x-4')]").click()
time.sleep(5)
driver.find_element_by_xpath("//*[contains(text(), 'Disabled')]").click()
time.sleep(5)
driver.get("url")
time.sleep(5)
driver.find_element_by_xpath("//div[contains(@class, 'flex space-x-4')]").click()
time.sleep(5)
driver.find_element_by_xpath("//*[contains(text(), 'Disabled')]").click()
time.sleep(5)
driver.get("url")
time.sleep(5)
driver.find_element_by_xpath("//div[contains(@class, 'flex space-x-4')]").click()
time.sleep(5)
pyautogui.click(1240, 205)
time.sleep(5)
driver.close()

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

server.login('e-mail', 'password')

server.sendmail(
    'e-mail', 
    'recipient', 
    'text message')

server.quit()

print ('Mail sent')

#2
from selenium import webdriver
import pyautogui
import smtplib, ssl
import time
import os

username = ""
password = ""

url = "url"

driver = webdriver.Safari(port=0, executable_path="/usr/bin/safaridriver")
driver.maximize_window()
time.sleep(1)

driver.get(url)

driver.find_element_by_id("email").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_xpath("//*[contains(text(), 'Login')]").click()
time.sleep(5)
driver.get("url")
time.sleep(5)
driver.find_element_by_xpath("//div[contains(@class, 'flex space-x-4')]").click()
time.sleep(5)
driver.find_element_by_xpath("//*[contains(text(), 'Disabled')]").click()
time.sleep(5)
driver.get("url")
time.sleep(5)
driver.find_element_by_xpath("//div[contains(@class, 'flex space-x-4')]").click()
time.sleep(5)
driver.find_element_by_xpath("//*[contains(text(), 'Disabled')]").click()
time.sleep(5)
driver.get("url")
time.sleep(5)
driver.find_element_by_xpath("//div[contains(@class, 'flex space-x-4')]").click()
time.sleep(5)
pyautogui.click(1240, 205)
time.sleep(5)
driver.close()

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

server.login('e-mail', 'password')

server.sendmail(
    'e-mail', 
    'recipient', 
    'text message')

server.quit()

print ('Mail sent')

#3
from selenium import webdriver
import pyautogui
import smtplib, ssl
import time
import os

username = ""
password = ""

url = ""

driver = webdriver.Safari(port=0, executable_path="/usr/bin/safaridriver")
driver.maximize_window()
time.sleep(1)

driver.get(url)

driver.find_element_by_id("email").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_xpath("//*[contains(text(), 'Login')]").click()
time.sleep(5)
driver.get("url")
time.sleep(5)
driver.find_element_by_xpath("//div[contains(@class, 'flex space-x-4')]").click()
time.sleep(5)
driver.find_element_by_xpath("//*[contains(text(), 'Disabled')]").click()
time.sleep(5)
driver.get("url")
time.sleep(5)
driver.find_element_by_xpath("//div[contains(@class, 'flex space-x-4')]").click()
time.sleep(5)
pyautogui.click(1240, 205)
time.sleep(5)
driver.get("url")
time.sleep(5)
driver.find_element_by_xpath("//div[contains(@class, 'flex space-x-4')]").click()
time.sleep(5)
pyautogui.click(1240, 205)
time.sleep(5)
driver.close()

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

server.login('e-mail', 'password')

server.sendmail(
    'e-mail', 
    'recipient', 
    'text message')

server.quit()

print ('Mail sent')

#4
from selenium import webdriver
import pyautogui
import smtplib, ssl
import time
import os

username = ""
password = ""

url = ""

driver = webdriver.Safari(port=0, executable_path="/usr/bin/safaridriver")
driver.maximize_window()
time.sleep(1)

driver.get(url)

driver.find_element_by_id("email").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_xpath("//*[contains(text(), 'Login')]").click()
time.sleep(5)
driver.get("url")
time.sleep(5)
driver.find_element_by_xpath("//div[contains(@class, 'flex space-x-4')]").click()
time.sleep(5)
driver.find_element_by_xpath("//*[contains(text(), 'Disabled')]").click()
time.sleep(5)
driver.get("url")
time.sleep(5)
driver.find_element_by_xpath("//div[contains(@class, 'flex space-x-4')]").click()
time.sleep(5)
pyautogui.click(1240, 205)
time.sleep(5)
driver.close()

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

server.login('e-mail', 'password')

server.sendmail(
    'e-mail', 
    'recipeint', 
    'text message')

server.quit()

print ('Mail sent')

#5
from selenium import webdriver
import pyautogui
import smtplib, ssl
import time
import os

username = ""
password = ""

url = ""

driver = webdriver.Safari(port=0, executable_path="/usr/bin/safaridriver")
driver.maximize_window()
time.sleep(1)

driver.get(url)

driver.find_element_by_id("email").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_xpath("//*[contains(text(), 'Login')]").click()
time.sleep(5)
driver.get("url")
time.sleep(5)
driver.find_element_by_xpath("//div[contains(@class, 'flex space-x-4')]").click()
time.sleep(5)
driver.find_element_by_xpath("//*[contains(text(), 'Disabled')]").click()
time.sleep(5)
driver.get("url") 
time.sleep(5)
driver.find_element_by_xpath("//div[contains(@class, 'flex space-x-4')]").click()
time.sleep(5)
pyautogui.click(1240, 205)
time.sleep(5)
driver.get("url")
time.sleep(5)
driver.find_element_by_xpath("//div[contains(@class, 'flex space-x-4')]").click()
time.sleep(5)
pyautogui.click(1240, 205)
time.sleep(5)
driver.close()

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

server.login('e-mail', 'password')

server.sendmail(
    'e-mail', 
    'receipient', 
    'text message')

server.quit()

print ('Mail sent')

#6
from selenium import webdriver
import pyautogui
import smtplib, ssl
import time
import os

username = ""
password = ""

url = ""

driver = webdriver.Safari(port=0, executable_path="/usr/bin/safaridriver")
driver.maximize_window()
time.sleep(1)

driver.get(url)

driver.find_element_by_id("email").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_xpath("//*[contains(text(), 'Login')]").click()
time.sleep(5)
driver.get("url")
time.sleep(5)
driver.find_element_by_xpath("//div[contains(@class, 'flex space-x-4')]").click()
time.sleep(5)
driver.find_element_by_xpath("//*[contains(text(), 'Disabled')]").click()
time.sleep(5)
driver.get("url")
time.sleep(5)
driver.find_element_by_xpath("//div[contains(@class, 'flex space-x-4')]").click()
time.sleep(5)
pyautogui.click(1240, 205)
time.sleep(5)
driver.close()

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

server.login('e-mailm', 'password')

server.sendmail(
    'e-mail', 
    'recipient', 
    'text message')

server.quit()

print ('Mail sent')