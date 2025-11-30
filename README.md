# youtube-subscription-automation
A Python + Selenium automation tool that auto-subscribes to YouTube channels using URLs from a CSV file.

📘 YouTube Subscription Automation (Python + Selenium + Brave Browser)

This project automates the process of subscribing to a list of YouTube channels using Python, Selenium, and your existing Brave/Chrome browser profile.
Originally built to migrate subscriptions from an old YouTube account to a new one, it evolved into a practical real-world automation tool demonstrating browser automation, dynamic DOM handling, and efficient scripting.

🚀 Project Overview

YouTube does not offer a way to transfer subscriptions between accounts.
Manually subscribing to hundreds of channels is slow, repetitive, and error-prone.
 
This tool solves the problem by:

Reading channel URLs from a CSV file
Opening YouTube using your logged-in Brave browser profile
Automatically clicking the Subscribe button using JavaScript
Handling dynamic UI, delays, and layout differences
Processing hundreds of channels in minutes

🧠 Key Concepts Demonstrated

✔ Selenium WebDriver Automation
Using Selenium to control Brave/Chrome with custom profiles.

✔ DOM Scraping + JS Execution
Injecting JavaScript to find and click Subscribe buttons instantly.

✔ Real-World Dynamic Element Handling
YouTube uses delayed rendering, shadow DOM containers, and changing HTML structures.
The script overcomes all of them.

✔ CSV Data Extraction
Reading and iterating through large subscription lists using pandas.

✔ Optimizing Automation for Speed
Eliminating unnecessary waits and delays, reducing runtime from ~20s per channel to ~1s.

🛠 Tech Stack

Python 3.10+
Selenium WebDriver
Brave Browser (or Chrome)
WebDriver Manager
pandas

📂 5. Project Structure

project-folder/
│── main.py
│── channels.csv
│── README.md
│── requirements.txt

⚙️ Setup Instructions

1️⃣ Install dependencies
pip install selenium webdriver-manager pandas

2️⃣ Verify Browser path
Check and verify the default installation path

3️⃣ Place your subscriptions.csv
 Place the CSV file at a defined path and mention it in the code, if the default path is changed
 Ensure URLs are in the 2nd column.
 
 4️⃣ Run the script
 python youtube_automation.py

 🧩 How the Automation Works Internally
 
🔹 Step 1 — Load CSV
Reads list of channel URLs into memory.

🔹 Step 2 — Launch Brave with Your Login
Loads your actual YouTube account (no need to log in again).

🔹 Step 3 — Visit Each Channel
The browser navigates channel-by-channel.

🔹 Step 4 — Ultra-Fast JavaScript Click
The script injects JS to:
Scan all buttons
Find the one containing “Subscribe”
Bypass overlay / animations
Click instantly

🔹 Step 5 — Move to Next Channel
Minimal delay (0.3–1 sec).
