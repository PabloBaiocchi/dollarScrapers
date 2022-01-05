def parsePrice(priceString):
    digits=filter(lambda x: x.isdigit(),priceString)
    digitString=''.join(digits)
    return digitString[:-2]+'.'+digitString[-2:]

def parseBody(tbody):
    cells=tbody.find_all('td')
    cells=[td.text for td in cells]
    cells[1]=parsePrice(cells[1])
    return cells

def getData(htmlFilePath):
    file=open(htmlFilePath,'r')
    soup=BeautifulSoup(file.read(),'html.parser')
    bodies=soup.find_all('tbody')
    return [parseBody(tbody) for tbody in bodies]

def saveData(htmlFilePath,saveFilePath):
    rows=getData(htmlFilePath)
    file=open(saveFilePath,'w')
    for row in rows: file.write(f"{','.join(row)}\n")
    file.close()