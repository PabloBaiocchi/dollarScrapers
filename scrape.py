import dolarBlueScraper as dbs
import dolarMayoristaScraper as dms

dolarBlueFile='/Users/pablo/Desktop/posgradoFinanzas/dolarBlue2011.csv'
dbs.saveData(dolarBlueFile,2011)

dolarMayoristaHtmlFile='/Users/pablo/Desktop/posgradoFinanzas/dolarMayorista.html'
dolarMayoristaSaveFile='/Users/pablo/Desktop/posgradoFinanzas/dolarMayorista2011.csv'
dms.saveData(dolarMayoristaHtmlFile,dolarMayoristaSaveFile)
