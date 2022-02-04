import threading
import csv
import time
from scrapping import WebSc
import scrapping
from datetime import datetime


start_time = datetime.now()

ws = WebSc()

ws.putFilter()
ws.setNrOfEl()

nrp = ws.getNrOfPages()
nre = ws.getNrOfElements()


t = 0
lst= []
lst1=[]
nrcount = 1

print (nrp)
print (nre)
while (t < int(nrp)): 

    if (nrcount == int(nre)):
            break
    i = 1
    while (i < 51):
            
        print (nrcount)
        print (i)
        l = ws.getElInfo(i)
        
        lst.append(l)
        i = i + 1
        if (nrcount == int(nre)):
            break
        nrcount = nrcount + 1
    t = t + 1
    ws.nextPageButton()
    

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

header= ['Numar anunt', 'Data publicare', 'Tip procedura', 'Tipul contractului', 'Stare procedura', 'Modalitate de desfasurare', 'Modalitate de atribuire', 'CPV', 'Autoritate contractuala', 'Data limita depunere', 'Valoare estimata']    
n=0
with open('Files/date2.csv',  'w', encoding="utf-8") as f:  
    writer = csv.writer(f,lineterminator='\n')
    writer.writerow(header)
    while (n<int(nre)):
        x=0

        writer.writerow(lst[n])   
  
        n = n+1

f.close()
ws.drvClose()

        
        
        