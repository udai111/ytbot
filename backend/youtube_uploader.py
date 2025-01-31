import time
import os
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils import enable_tor_proxy, get_random_user_agent, random_sleep

def setup_browser(headless=True):
    options = webdriver.ChromeOptions()
    # user-agent
    ua = get_random_user_agent()
    options.add_argument(f"--user-agent={ua}")
    if headless:
        options.add_argument("--headless")
    # Optionally disable sandboxing for certain environments
    # options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1280, 800)
    return driver

def login_youtube(driver, email, password):
    driver.get("https://accounts.google.com/signin")
    random_sleep(2, 4)
    driver.find_element(By.NAME, "identifier").send_keys(email + Keys.RETURN)
    random_sleep(2, 4)
    driver.find_element(By.NAME, "password").send_keys(password + Keys.RETURN)
    random_sleep(5, 8)

def upload_video(driver, video_path, title="Untitled", description=""):
    driver.get("https://www.youtube.com/upload")
    random_sleep(5, 8)
    file_input = driver.find_element(By.XPATH, "//input[@type='file']")
    file_input.send_keys(os.path.abspath(video_path))
    random_sleep(15, 25)
    
    # Optionally fill out Title & Desc if the elements are found:
    # title_box = driver.find_element(By.ID, 'title-textarea')
    # ...
    # Publish or next steps

    # Wait a bit more for processing
    random_sleep(10, 20)
