# Dynamic-Web-Scraping
### This Project is aim to scrape income statement of the stock in SET.
### This Code is applied from "Intermediate Data Engineering by GBDi Training Code".

# Requirement
- Chromedriver : https://chromedriver.chromium.org/
- BeautifulSoup
- pandas

# Steps to run
1. Download `Chromedriver` locate at the same folder with this code.
2. Input stocks name.
3. Type `f` when finish.
4. Type `E` if want to export to excel or Type `S` if want to show result.

# Workflow
1. import `webdriver`, `BeautifulSoup` and `pandas`
2. Use for loops to let chromdriver open stock's fact sheet on browser and scrape all `HTML` one-by-one
3. Find income statement and extract header and body of the table
4. Clean data to calculate last record growth 
    - Convert `-` into `0`  
    - Convert datatype from string to float 
5. Create new column named `last record growth` (growth of the last quarter or last half-yearly that show in the statement)
6. Export to excel or show on screen
---
<h2><div align="center">Thank you (づ￣ 3￣)づ</div></h2>
