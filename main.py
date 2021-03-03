from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver = "C:\Projects\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

sign_in_btn = driver.find_element_by_class_name("nav__button-secondary")
sign_in_btn.click()

email_input = driver.find_element_by_id("username")
email_input.send_keys("your_email@yahoo.com")

password_input = driver.find_element_by_id("password")
password_input.send_keys("your_password_password.")

sign_into_linkdin_btn = driver.find_element_by_class_name("btn__primary--large")
sign_into_linkdin_btn.click()

job_apply_button = driver.find_element_by_class_name("jobs-apply-button")
job_apply_button.click()

next_btn = driver.find_element_by_class_name("artdeco-button__text")
next_btn.click()

next_btn = driver.find_element_by_class_name("artdeco-button__text")
next_btn.click()

redux_js = driver.find_element_by_class_name("ember-text-field")
redux_js.send_keys("3")

submit_button = driver.find_element_by_css_selector("footer button")
submit_button.click()

