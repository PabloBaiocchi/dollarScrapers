import requests
from bs4 import BeautifulSoup
import datetime as dt

def parseRow(row):
    cells=[td.text for td in row.find_all('td')]
    for i in [1,2]: 
        cells[i]=cells[i].replace(',','.') 
    return [cell for cell in cells[:3]]

def saveRow(row,file):
    data=parseRow(row)
    file.write(f"{','.join(data)}\n")
    
def getTableRows(html):
    soup=BeautifulSoup(html,'html.parser')
    table=soup.find('table')
    tbody=table.find('tbody')
    return tbody.find_all('tr')

def getRequestYears(startingYear,today):
    requestYears=[]
    for year in range(startingYear,today.year):
        requestYears=requestYears+[year]*12
    return requestYears+[today.year]*today.month

def getRequestMonths(startingYear,today):
    months=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
    years=today.year-startingYear
    return months*years+months[:today.month]

def getRequestPeriod(startingYear):
    today=dt.datetime.now()
    requestMonths=getRequestMonths(startingYear,today)
    requestYears=getRequestYears(startingYear,today)
    return zip(requestMonths,requestYears)

def saveData(filePath,startingYear):
    file=open(filePath,'w')
    for month,year in getRequestPeriod(startingYear):
        url=f'https://dolarhistorico.com/cotizacion-dolar-blue/mes/{month}-{year}'
        response=requests.get(url)
        rows=getTableRows(response.text)
        for row in rows: saveRow(row,file)
    file.close()