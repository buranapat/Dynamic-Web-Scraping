from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

#function to calculate last record growth
def growth(a,b): 
    if a==0 and b ==0:
        g = 0
    elif a==0 and b!=0:
        g = -100
    elif a !=0 and b==0:
        g = 100
    elif a<0 and b<0:
        g = ((b/a) - 1)*100
    else: g = ((a/b)-1)*100
    return f"{g:.2f} %"

# Create blank list to get stocks
stocks = []
i = ""
print("press 'f' when finish ")
while i != "f":
    stock = input("stock name (onestock):").lower()
    i = stock
    if i == "f":
        break
    stocks += [stock] 


state = input("Export to excel (E) or Show (S):").lower()

for stock in stocks:
    # open fact sheet of the stock to scrape data and store it in variable named soup
    driver = webdriver.Chrome()
    url = f"https://www.set.or.th/th/market/product/stock/quote/{stock}/factsheet"
    driver.get(url)
    outerhtml = driver.execute_script(
        "return document.documentElement.outerHTML;"
    )

    soup = BeautifulSoup(outerhtml,'html.parser')
    driver.quit()
    iserror=0
    try:
        table = soup.findChildren(
                     'div',
                     class_ = "mb-1 table-lg-noresponsive"
                   )[1].findChildren(
                     'table',
                    class_ = "table b-table table-custom-field table-custom-field--cnc table-hover-underline b-table-no-border-collapse"
        )
    except:
        # If there is not stock, print this message and run next stock
        print(f"Don't have stock name {stock}, please try again")
        continue
        
    header1 = table[0].find(
             'thead',
              role = 'rowgroup'
                    ).find(
             'tr',
             class_ = 'thead-top'
    )
    lsheader1 =[]

    for i in header1:
        lsheader1 += [i.text.strip()]
    lsheader1 = ['ประเภทงบ'] + lsheader1[2:]

    body = table[0].find(
             'tbody',
              role = 'rowgroup'
                  ).findChildren(
              'tr')

    ans = []
    for j in range(len(body)):
        cols ={}
        row = body[j].findChildren(
                      'td'
        )
        cols[lsheader1[0]]= row[0].text.replace("\n","").strip()
        for i in range (1,len(row)):
            if row[i].text.replace("\n","").replace(",","").strip() == '-': # convert "-" to 0
                cols[lsheader1[i]] = 0
            else:cols[lsheader1[i]]= float(row[i].text.replace("\n","").replace(",","").strip()) # convert string to float
        ans += [cols]

    
    ans = pd.DataFrame(ans)
    ans['last record growth'] = ans.apply(lambda x: growth(x[1],x[2]), axis = 1 )
    if state == 's' :
        print(stock)
        print(ans)
    else:ans.to_excel(f"{stock.upper()}.xlsx")
    
print("Thank you")