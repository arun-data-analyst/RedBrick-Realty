from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def scrape_realtor_url(neighborhood, transaction_type, min_price, max_price, min_beds, min_baths):
    driver = webdriver.Chrome()

    url = (
        f"https://www.realtor.ca/map?TransactionTypeId={'2' if transaction_type == 'rent' else '1'}"
        f"&MinPrice={min_price}&MaxPrice={max_price}"
        f"&Beds={min_beds}-{min_beds}&Baths={min_baths}-{min_baths}"
        f"&GeoName={neighborhood}, Ottawa, ON"
    )
    print(f"\n🌐 Loading URL:\n{url}\n")

    driver.get(url)
    wait = WebDriverWait(driver, 30)

    try:
        # Wait for listing wrapper
        wait.until(EC.presence_of_element_located((By.ID, "mapSidebarBodyCon")))

        # Wait for at least one listing card
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mapSidebarBodyCon .listingCard")))
        time.sleep(3)  # Let all listings render

        cards = driver.find_elements(By.CSS_SELECTOR, "#mapSidebarBodyCon .listingCard")
        print(f"✅ Total listings scraped: {len(cards)}")

        data = []
        for card in cards:
            try:
                address = card.find_element(By.CSS_SELECTOR, ".listingCardAddress").text
                price = card.find_element(By.CSS_SELECTOR, ".listingCardPrice").text
                details = card.find_element(By.CSS_SELECTOR, ".listingCardDetails").text
                data.append({
                    "address": address,
                    "price": price,
                    "details": details
                })
            except:
                continue

        return data

    except Exception as e:
        print("❌ Error scraping listings:", e)
        return []

    finally:
        input("Press Enter to close browser...")
        driver.quit()
