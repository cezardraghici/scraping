from cgitb import text
from datetime import datetime
from lib2to3.pgen2 import driver
from select import select
import time
from unittest import TextTestResult
from urllib import request
from gevent import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import gettext
import csv
import requests
from bs4 import BeautifulSoup

class WebSc : 
    def __init__(self):
        self.self = self
    
    url = 'https://e-licitatie.ro/pub/notices/contract-notices/list/2/1'
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu') 
    driver = webdriver.Chrome(service=Service('Driver/chromedriver.exe'), options=options)
    driver.implicitly_wait(10)
    driver.get(url)
    

    def setDate(self):
        
        self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container-sizing"]/div[7]/div[2]/ng-transclude/div[1]/div[2]/div[4]/div/div[1]/div[2]/button'))))    
        self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container-sizing"]/div[7]/div[2]/ng-transclude/div[1]/div[2]/div[4]/div/div[1]/div[1]/span/span/span')))) 
        self.driver.find_element(By.CSS_SELECTOR, 'k-picker-wrap k-state-default k-state-focused k-state-activ k-state-border-down k-state-hover').send_keys('02/01/2022')
        #
        #self.driver.find_element(By.XPATH, '//*[@id="container-sizing"]/div[7]/div[2]/ng-transclude/div[1]/div[2]/div[4]/div/div[1]/div[1]/span/span/input').send_keys('02/01/2022')
        
        
        
    def putFilter(self):
        
        self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container-sizing"]/div[7]/div[2]/ng-transclude/div[1]/div[1]/div[1]/h4/input'))))
        self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container-sizing"]/div[7]/div[2]/ng-transclude/div[1]/div[1]/div[3]/h4/input'))))
        self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container-sizing"]/div[7]/div[2]/ng-transclude/div[1]/div[1]/div[4]/h4/input'))))
        self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container-sizing"]/div[7]/div[2]/ng-transclude/div[1]/div[1]/div[5]/h4/input'))))
        self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container-sizing"]/div[7]/div[2]/ng-transclude/div[1]/div[1]/div[6]/h4/input'))))
        self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="THE-SEARCH-BUTTON"]'))))
    
    def setNrOfEl(self):
        #WebDriverWait(self.driver,  20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[6]/div/div/span[2]/span/input')))
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="container-sizing"]/div[9]/div[2]/div[6]/div/div/span[2]/span/input').send_keys('0')
        self.driver.find_element(By.XPATH, '//*[@id="container-sizing"]/div[9]/div[2]/div[6]/div/ul/li[1]/a').click()
    
    def detButton(self, i):
        try:
            self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container-sizing"]/div[9]/div[2]/div[' + str(i) + ']/div/div/div[2]/h2/a'))))
        except:
            time.sleep(5)
            self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container-sizing"]/div[9]/div[2]/div[' + str(i) + ']/div/div/div[2]/h2/a'))))
        
    def backButton(self):
        try:
            self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[2]/div/div[4]/div/div/button[4]'))))
        except:
            time.sleep(5)
            self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[2]/div/div[4]/div/div/button[4]'))))
    
    def nextPageButton(self):
        try:
            self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[51]/div/ul/li[4]/a'))))
        except:
            time.sleep(5)
            self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[51]/div/ul/li[4]/a'))))
    
    def verifyIfExist(self, path):
        ver = self.driver.find_element(By.XPATH, path).is_enabled()
        return ver
        
    def getElInfo(self, i):
        
        wait = WebDriverWait(self.driver,  20)
      
        start_time = datetime.now()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[' + str(i) + ']/div/div/div[1]/div[1]/strong')))
        except:
            time.sleep(5)
            
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        
        try:
            id = self.driver.find_element(By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[' + str(i) + ']/div/div/div[1]/div[1]/strong').text
        except:
            id = '-'
        print (id)    
        start_time = datetime.now()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[' + str(i) + ']/div/div/div[1]/div[2]')))
        except:
            time.sleep(5)
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        try:
            data = self.driver.find_element(By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[' + str(i) + ']/div/div/div[1]/div[2]').text
        except:
            data = '-'
        start_time = datetime.now()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[' + str(i) + ']/div/div/div[2]/div/div[1]/strong[1]')))
        except:
            time.sleep(5)
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        try:
            tipP = self.driver.find_element(By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[' + str(i) + ']/div/div/div[2]/div/div[1]/strong[1]').text
        except:
            tipP = '-'
        start_time = datetime.now()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[' + str(i) + ']/div/div/div[2]/div/div[1]/strong[2]')))
        except:
            time.sleep(5)
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        try:
            tipC = self.driver.find_element(By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[' + str(i) + ']/div/div/div[2]/div/div[1]/strong[2]').text
        except:
            tipC = '-'
        start_time = datetime.now()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[' + str(i) + ']/div/div/div[2]/div/div[1]/strong[3]')))
        except:
            time.sleep(5)
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        try:
            stare = self.driver.find_element(By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[' + str(i) + ']/div/div/div[2]/div/div[1]/strong[3]').text
        except:
            stare = '-'
        start_time = datetime.now()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[' + str(i) + ']/div/div/div[2]/div/div[1]/strong[4]')))
        except:
            time.sleep(5)
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        try:
            modDes = self.driver.find_element(By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[' + str(i) + ']/div/div/div[2]/div/div[1]/strong[4]').text
        except:
            modDes = '-'
        start_time = datetime.now()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[' + str(i) + ']/div/div/div[2]/div/div[2]/strong[1]')))
        except:
            time.sleep(5)
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        try:
            modAT = self.driver.find_element(By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[' + str(i) + ']/div/div/div[2]/div/div[2]/strong[1]').text
        except:
            modAT = '-'
        start_time = datetime.now()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[' + str(i) + ']/div/div/div[2]/div/div[2]/strong[2]')))
        except:
            time.sleep(5)
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))                                                
        try:
            cpv = self.driver.find_element(By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[' + str(i) + ']/div/div/div[2]/div/div[2]/strong[2]').text
        except:
            cpv = '-'
            
        start_time = datetime.now()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[' + str(i) + ']/div/div/div[2]/div/div[2]/div/strong')))
        except:
            time.sleep(5)                                                
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
                            
        try:
            aut =  self.driver.find_element(By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[' + str(i) + ']/div/div/div[2]/div/div[2]/div/strong').text
        except:
            aut = '-'
        print ( aut)
        start_time = datetime.now()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[' + str(i) + ']/div/div/div[2]/div/div[3]/strong')))
        except:
            time.sleep(5)
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        try:
            datalim = self.driver.find_element(By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[' + str(i) + ']/div/div/div[2]/div/div[3]/strong').text
        except:
            datalim = '-'
        start_time = datetime.now()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[' + str(i) + ']/div/div/div[3]/div[1]')))
        except:
            time.sleep(5)
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        try:    
            suma = self.driver.find_element(By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[' + str(i) + ']/div/div/div[3]/div[1]').text
        except:
            suma = '-'
        
        
        self.detButton(i)
        
        start_time = datetime.now()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="section-2"]/div[2]/ng-transclude/div[4]/div')))
        except:
            time.sleep(5)
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        
        try:
            des=self.driver.find_element(By.XPATH,'//*[@id="section-2"]/div[2]/ng-transclude/div[4]/div').text
        except:
            des='-'
        start_time = datetime.now()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="section-4"]/div[2]')))
        except:
            time.sleep(5)
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        
        try:    
            ts=self.driver.find_element(By.XPATH,'//*[@id="section-4"]/div[2]').text
        except:
            ts='-'
        
        informatii = [id , data, tipP, tipC, stare, modDes, modAT, cpv, aut, datalim, suma, des, ts]
        i = i + 1
        
        self.backButton()  
        
        return informatii       

    def getNrOfPages(self):
       
        WebDriverWait(self.driver, timeout=20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[51]/div/ul/li[3]/a')))
        nr = self.driver.find_element(By.XPATH, '//*[@id="container-sizing"]/div[9]/div[2]/div[51]/div/ul/li[3]/a').text[5:]
        return nr
        
    def getNrOfElements(self):
        
        WebDriverWait(self.driver, timeout=20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container-sizing"]/div[9]/div[2]/div[51]/div/div/span[4]')))
        nr2 = self.driver.find_element(By.XPATH, '//*[@id="container-sizing"]/div[9]/div[2]/div[51]/div/div/span[4]').text
        return nr2
   
    def drvClose(self):
        self.driver.close()
    ''' 
    time.sleep(3)
  
    
    time.sleep(3)
    r=requests.get('https://e-licitatie.ro/pub/notices/contract-notices/list/2/1')
    c=r.content
    
    
    soup = BeautifulSoup(c,'html.parser')
    
    
    
    time.sleep(3)
    #all=soup.find_all(class_='u-items-list__item__properties')
    all=soup.find_all("div", {"class":'u-items-list'})
    al = soup.find(class_ = 'row ng-scope')
    print(al)
    for x in all:
        print(x)
        print ("hei")
    time.sleep(30)
    
    '''
   
    