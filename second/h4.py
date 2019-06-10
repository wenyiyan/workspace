# -*- coding: UTF-8 -*-

import time
import warnings 
warnings.filterwarnings("ignore")
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import pytesseract

browser = webdriver.Chrome("./chromedriver")
url = "https://egov.uscis.gov/casestatus/landing.do"
browser.get(url)