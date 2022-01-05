import requests
from bs4 import BeautifulSoup

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

def getRequestPeriod():
    months=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
    requestMonths=months*3+months[:1]
    requestYears=[2019]*12+[2020]*12+[2021]*12+[2022]
    return zip(requestMonths,requestYears)

def saveData(filePath):
    file=open(filePath,'w')
    for month,year in getRequestPeriod():
        url=f'https://dolarhistorico.com/cotizacion-dolar-blue/mes/{month}-{year}'
        response=requests.get(url)
        rows=getTableRows(response.text)
        for row in rows: saveRow(row,file)
    file.close()