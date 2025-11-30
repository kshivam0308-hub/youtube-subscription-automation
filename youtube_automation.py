from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Load CSV
file_path = r"C:\Users\Shivam\Desktop\subscriptions.csv"
df = pd.read_csv(file_path)
urls = df.iloc[:, 1].dropna().tolist()

# Brave browser location
brave_path = r"C:\Users\Shivam\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = brave_path

# Use existing Brave profile
chrome_options.add_argument(r"user-data-dir=C:\Users\Shivam\AppData\Local\BraveSoftware\Brave-Browser\User Data")
chrome_options.add_argument("profile-directory=Default")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def fast_subscribe_js():
    js_code = """
    let buttons = document.querySelectorAll("button");
    for (let b of buttons) {
        let text = (b.innerText || "").toLowerCase();
        let aria = (b.getAttribute("aria-label") || "").toLowerCase();

        // Skip if already subscribed
        if (text.includes("subscribed")) return "already";

        // Click Subscribe button
        if (text.includes("subscribe") || aria.includes("subscribe")) {
            b.click();
            return "clicked";
        }
    }
    return "not_found";
    """
    return driver.execute_script(js_code)

def subscribe_channel(url):
    print("\nOpening:", url)
    driver.get(url)

    # tiny delay for JS injection (fastest possible)
    time.sleep(0.8)

    result = fast_subscribe_js()

    if result == "already":
        print("✔ Already subscribed")
    elif result == "clicked":
        print("🔥 Subscribed instantly!")
    else:
        print("❌ Subscribe button not found")

    # move ASAP
    time.sleep(0.3)

# Run all URLs
for url in urls:
    subscribe_channel(url)

print("\n🚀 Done! (INSANE FAST MODE)")
driver.quit()
