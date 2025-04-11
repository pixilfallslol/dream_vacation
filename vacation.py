from playwright.sync_api import sync_playwright
import random
import time

def random_sleep(min_time=0.5, max_time=2.5):
    time.sleep(random.uniform(min_time, max_time))

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=random.randint(50, 150)) 
    page = browser.new_page()

    page.goto("https://www.kayak.com/flights")
    random_sleep()
    
    x_button = page.locator(".c_neb-item-button")
    x_button.click()
    flying_from = page.locator("input[placeholder='From?']")
    time.sleep(.1)
    flying_from.fill("LAX")
    time.sleep(1)
    flying_from.press("Enter")
    
    time.sleep(3)