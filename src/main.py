from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

#service = Service(executable_path='C:\Chromedriver\chromedriver')

#browser = webdriver.Chrome(service=service)

options = webdriver.ChromeOptions() # create a ChromeOptions object to configure the browser

 # for staying the browser open
options.add_experimental_option("detach", True) # set detach option to True to keep the browser window open

# Create a new Chrome webdriver with specific options and executable path
browser = webdriver.Chrome(options=options,executable_path='C:\Chromedriver\chromedriver')


browser.get('https://www.google.com') # navigate to google homepage
time.sleep(2) # wait for 2 seconds allow the page to load

browser.find_element(By.NAME,'q').send_keys('selenium') # locate the search box by its name and enter 'selenium' 
time.sleep(1) # wait for 1 seconds

browser.find_element(By.CSS_SELECTOR,'input[type=submit]').click() # locate the search button by its css selector attribute and click it

time.sleep(5) # wait for 5 seconds