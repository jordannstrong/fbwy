'''
Created on December 13, 2017

@author: Jordan Strong
'''

from selenium import webdriver
from bs4 import BeautifulSoup
import time

login_page = 'https://bby-wfmr.jdadelivers.com/retail/rp/login?redirectUrl=%2Fretail%2Frp%2F7080%2FESS4%23bbb-custom-Taskflow.ESS-four%3AmtSchedule'
schedule_page = 'https://bby-wfmr.jdadelivers.com/retail/rp/7080/ESS4#bbb-custom-Taskflow.ESS-four:mtSchedule'

# Assign your username and password
username = ''
password = ''

driver = webdriver.PhantomJS()
driver.set_window_size(1280, 720)

driver.get(schedule_page)

# Login if not already logged in
if driver.current_url == login_page:
    driver.find_element_by_id('userName').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('ext-gen28').click()

# Ensure page is fully loaded before continuing
time.sleep(15)

bs = BeautifulSoup(driver.page_source, 'lxml')

hours = ['', 'Off', 'Off', 'Off', 'Off', 'Off', 'Off', 'Off',]
days = ['', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

tablerow = bs.find('tr', attrs={'id':'container-1105'})

# Loop through each cell in the table row and store the hours
for index, td in enumerate(tablerow.findChildren('td')):
    if td.findChild('span'):
        hour = td.find('span')
        hours[index] = hour.renderContents()
        
# Print the hours for each day with the day as a label
for x in range(1,8):
    print(days[x] + ': ' + str(hours[x]))