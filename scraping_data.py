import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.trivago.in/en-IN/srl/hotels-hyderabad-india?search=200-64958;dr-20240428-20240429;so-5")
time.sleep(3)

try:
    driver.find_element(By.XPATH, "//button[@class='absolute right-0 m-4 z-5']").click()
except Exception as e:
    print("Pop-up handling error:", e)
time.sleep(5)
hotels = driver.find_elements(By.XPATH,"//div[@class='AccommodationItem_infoWrapper_oVE0d AccommodationItem_infoSection_ZiwDE flex-1']")

with open('hotel_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Hotel Name', 'Hotel Rating', 'Review Rating', 'Wifi in Lobby', 'Free WiFi', 'Pool', 'Spa', 'Parking',
                  'Pets', 'A/C', 'Restaurant', 'Hotel Bar', 'Price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for hotel in hotels:
        try:
            name = hotel.find_element(By.XPATH, ".//span[@itemprop='name']").text
            rrating = hotel.find_element(By.XPATH, ".//span[@itemprop='ratingValue']").text

            try:
                star_rating = hotel.find_element(By.XPATH, ".//meta[@itemprop='ratingValue']").get_attribute("content")
            except Exception:
                star_rating = "NaN"

            try:
                price = ""
                p = hotel.find_element(By.XPATH, ".//span[@class='StandardDatesArea_fromLabel__YE_Kn']").text.split()[1].strip()
                for k in p:
                    if k.isalnum():
                        price += k
            except Exception:
                price = "NaN"
            writer.writerow({
                'Hotel Name': name,
                'Hotel Rating': star_rating,
                'Review Rating': rrating,
                'Wifi in Lobby': 'na',
                'Free WiFi': 'na',
                'Pool': 'na',
                'Spa': 'na',
                'Parking': 'na',
                'Pets': 'na',
                'A/C': 'na',
                'Restaurant': 'na',
                'Hotel Bar': 'na',
                'Price': price
            })

        except Exception as e:
            print(f"Error extracting data for hotel {name if 'name' in locals() else 'Unknown'}: {e}")
            
driver.quit()