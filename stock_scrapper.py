from bs4 import BeautifulSoup
import requests
import mysql.connector

#Create connection
config = {
  'user': 'root',
  'password': 'tasha123',
  'host': '127.0.0.1',
  'database': 'googlefinance_db',
  'raise_on_warnings': True
}

db = mysql.connector.connect(config)
c = db.cursor()

#Create tables
c.execute('''CREATE TABLE most_active_stocks(Stock_Symbol TEXT, Stock_Name TEXT, Stock_Price TEXT, Price_Change TEXT, Percentage_Price_Change TEXT, Link TEXT)''')
c.execute('''CREATE TABLE gainers(Stock_Symbol TEXT, Stock_Name TEXT, Stock_Price TEXT, Price_Change TEXT, Percentage_Price_Change TEXT, Link TEXT)''')
c.execute('''CREATE TABLE losers(Stock_Symbol TEXT, Stock_Name TEXT, Stock_Price TEXT, Price_Change TEXT, Percentage_Price_Change TEXT, Link TEXT)''')

def most_active_stock():
    html_text = requests.get('https://www.google.com/finance/markets/most-active?hl=en').text

    base_url = "https://www.google.com/finance"

    soup = BeautifulSoup(html_text, 'lxml')
    stocks = soup.find_all('li')

    for stock in stocks:
        stock_symbol = stock.find('div', class_='COaKTb').text
        stock_name = stock.find('div', class_='ZvmM7').text
        stock_price = stock.find('div', class_='YMlKec').text
        stock_price_change = stock.find('div', class_='SEGxAb').text
        percentage_price_change = stock.find('div', class_='JwB6zf').text
        link = stock.find('a').get('href').replace('.', '')
        stock_link = base_url + link

        if stock_price_change[0] == "-":
            percentage_price_change = "-" + percentage_price_change
        else:
            percentage_price_change = "+" + percentage_price_change

        #Insert scrapped data into table
        c.execute('''INSERT INTO most_active_stocks VALUES(?,?,?,?,?,?)''', (stock_symbol, stock_name, stock_price, stock_price_change, percentage_price_change, stock_link))

def gainers():
    html_text = requests.get('https://www.google.com/finance/markets/gainers?hl=en').text

    base_url = "https://www.google.com/finance"

    soup = BeautifulSoup(html_text, 'lxml')
    stocks = soup.find_all('li')

    for stock in stocks:
        stock_symbol = stock.find('div', class_='COaKTb').text
        stock_name = stock.find('div', class_='ZvmM7').text
        stock_price = stock.find('div', class_='YMlKec').text
        stock_price_change = stock.find('div', class_='SEGxAb').text
        percentage_price_change = stock.find('div', class_='JwB6zf').text
        link = stock.find('a').get('href').replace('.', '')
        stock_link = base_url + link

        if stock_price_change[0] == "-":
            percentage_price_change = "-" + percentage_price_change
        else:
            percentage_price_change = "+" + percentage_price_change

        #Insert scrapped data into table
        c.execute('''INSERT INTO gainers VALUES(?,?,?,?,?,?)''', (stock_symbol, stock_name, stock_price, stock_price_change, percentage_price_change, stock_link))

def losers():
    html_text = requests.get('https://www.google.com/finance/markets/losers?hl=en').text

    base_url = "https://www.google.com/finance"

    soup = BeautifulSoup(html_text, 'lxml')
    stocks = soup.find_all('li')

    for stock in stocks:
        stock_symbol = stock.find('div', class_='COaKTb').text
        stock_name = stock.find('div', class_='ZvmM7').text
        stock_price = stock.find('div', class_='YMlKec').text
        stock_price_change = stock.find('div', class_='SEGxAb').text
        percentage_price_change = stock.find('div', class_='JwB6zf').text
        link = stock.find('a').get('href').replace('.', '')
        stock_link = base_url + link

        if stock_price_change[0] == "-":
            percentage_price_change = "-" + percentage_price_change
        else:
            percentage_price_change = "+" + percentage_price_change

        #Insert scrapped data into table
        c.execute('''INSERT INTO losers VALUES(?,?,?,?,?,?)''', (stock_symbol, stock_name, stock_price, stock_price_change, percentage_price_change, stock_link))

most_active_stock()
gainers()
losers()

#Commit changes to the database
db.commit()
print('Complete')

#Close connection
db.close()
