# -*- coding: UTF-8 -*-

import time
import warnings 
warnings.filterwarnings("ignore")
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import pytesseract

def case_status(case_number):
    browser = webdriver.Chrome("./chromedriver")
    url = "https://egov.uscis.gov/casestatus/landing.do"
    browser.get(url)
    
    time.sleep(1)
    browser.find_element_by_id("receipt_number").click()
    time.sleep(1)
    browser.find_element_by_id("receipt_number").send_keys(case_number)
    time.sleep(1)
    browser.find_element_by_name("initCaseSearch").click() 
    
    body = browser.find_element_by_tag_name("body")
    content = body.text
    browser.close()
    
    case_status = content.encode('ascii','ignore').split('\n')[11:13]
    
    return case_status


import smtplib
def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login('wenyi.gausscode@gmail.com', 'SuperGirl@022')  
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail('wenyi.gausscode@gmail.com', ['wyywenyi@gmail.com','frederickwu2012@gmail.com'],message)
        server.quit()
        print("Success: Email sent!")
    except:
       print("Email failed to send.")



h4_ead_status = case_status('WAC1990070403')
h4_visa_status = case_status('WAC1990053959')

send_email('H4_EAD', h4_ead_status)
send_email('H4_status', h4_visa_status)
