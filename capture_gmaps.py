# -*- coding: utf-8 -*-
"""
Captures real Google Maps route screenshots for Days 1 through 5.
"""

import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image

routes = {
    'day1': 'https://www.google.com/maps/dir/Eslead+Hotel+Namba+South+1/Tsutenkaku/Den-Den+Town/Shinsaibashisuji/Dotonbori/Hozenji+Yokocho/@34.662,135.503,14z',
    'day2': 'https://www.google.com/maps/dir/Eslead+Hotel+Namba+South+1/Osaka+Castle/Kuromon+Ichiba+Market/Namba+Yasaka+Shrine/Takashimaya+Osaka/Abeno+Harukas/@34.665,135.512,13z',
    'day3': 'https://www.google.com/maps/dir/VIP+Villa+Namba/Fushimi+Inari+Taisha/Kinkaku-ji/Arashiyama+Bamboo+Grove/Nara+Park/@34.85,135.75,10z',
    'day4': 'https://www.google.com/maps/dir/Eslead+Hotel+Namba+South+1/Universal+Studios+Japan/Universal+CityWalk+Osaka/@34.66,135.47,13z',
    'day5': 'https://www.google.com/maps/dir/Eslead+Hotel+Namba+South+1/Osaka+Aquarium+Kaiyukan/Namba+Parks/MEGA+Don+Quijote+Shinsekai/Kansai+International+Airport/@34.55,135.38,11z'
}

options = Options()
options.add_argument('--headless')
options.add_argument('--window-size=1280,800')
options.add_argument('--lang=en')

driver = webdriver.Chrome(options=options)
output_dir = r'c:\Users\Desktop\Documents\antigravity\amazing-tesla\images'

for day, url in routes.items():
    print(f'Loading {day}...')
    driver.get(url)
    time.sleep(5)
    
    # Try to collapse side panel if present
    try:
        btns = driver.find_elements(By.TAG_NAME, 'button')
        for b in btns:
            aria = b.get_attribute('aria-label') or ''
            tooltip = b.get_attribute('data-tooltip') or ''
            if 'Collapse' in aria or 'Collapse' in tooltip:
                b.click()
                time.sleep(1.5)
                break
    except Exception as e:
        pass

    fname = os.path.join(output_dir, f'gmap_route_{day}.png')
    driver.save_screenshot(fname)
    
    # Also save as JPEG with good quality
    with Image.open(fname) as im:
        jpg_name = os.path.join(output_dir, f'gmap_route_{day}.jpg')
        im.convert('RGB').save(jpg_name, 'JPEG', quality=88, optimize=True)
    
    print(f'Captured {day} -> {fname}')

driver.quit()
print('All Google Maps route screenshots saved successfully!')
