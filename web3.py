import threading
import csv
import time
from scrapping import WebSc
import scrapping
from datetime import datetime


start_time = datetime.now()
# do your work here

ws = WebSc()
#ws1 = WebSc()
#time.sleep(5)
#ws.setDate()
#time.sleep(20)
ws.putFilter()
ws.setNrOfEl()
#ws1.putFilter()

nrp = ws.getNrOfPages()
nre = ws.getNrOfElements()

#nrp1 = ws.getNrOfPages()
#nre1 = ws.getNrOfElements()


t = 0
lst= []
lst1=[]
nrcount = 1

print (nrp)
print (nre)
while (t < int(nrp)): #int(nrp)):
    #time.sleep(1)
    #print (t)
    #print (ws.getNrOfPages())
    if (nrcount == (int(nre) + 1 )):
            break
    i = 1
    while (i < 51):
            
        print (nrcount)
        print (i)
        l = ws.getElInfo(i)
        
        lst.append(l)
        i = i + 1
        if (nrcount == (int(nre) + 1 )):
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
        '''
        while (x < 5):
            writer.writerow(lst[n][x])
            x = x + 1
        '''    
        n = n+1

f.close()
 

        
        
        