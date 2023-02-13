from email.mime import base
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from time import sleep
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
import os
import time
from bs4 import BeautifulSoup


#set up driver, make chrome_path equal to location of your chromedriver.exe
chrome_path = r"C:/Users/Collins/Desktop/chromedriver_win32/chromedriver"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_path)
#the site which has the long scrolling page
category = "cars"
search_Query = "mazda Demio"
partitioned_search = search_Query.partition(" ")
filter_1 = partitioned_search[0]
filter_2 = partitioned_search[2]
year_max = ""
year_min = ""
base_url = f"https://jiji.co.ke/{category}?query={search_Query}&filter_attr_1_make={filter_1}&filter_attr_2_model={filter_2}&filter_attr_119_year_of_manufacture__min={year_min}&filter_attr_119_year_of_manufacture__max={year_max}"
driver_url = "C:/Users/Collins/Desktop/chromedriver_win32/chromedriver"
driver.get(base_url)

#if a button is blocking it from being done automatically, find its name and put it in **here**. For example instagram uses "Load more".
#elm = driver.find_element_by_link_text('**here**')
#driver.implicitly_wait(5)
#elm.click()

lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
                lastCount = lenOfPage
                time.sleep(5)
                lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                if lastCount==lenOfPage:
                    match=True

with open("html_scripts/test.html", "wb") as file:
    file.write(driver.page_source.encode('utf-8')) 

with open("html_scripts/test.html","rb") as file:
    context = file.read()
    soup = BeautifulSoup(context,'lxml')
    main_div = soup.findAll("div", attrs={"class":"b-list-advert__item-wrapper"})
    item_attr = []
    price = []
    c = 0
    attr_only=[]
    for i in main_div:
        attr = i.findAll("div", attrs={"class":"b-list-advert__item-attr"})
        price= i.findAll('div',attrs={"class":"qa-advert-price"})  
        attr_names = i.findAll('div',attrs={"class":"b-advert-title-inner qa-advert-title b-advert-title-inner--h3"})
        #img= i.findAll("source", attrs = {"class":""})
        #link = i.find("a",attrs = {"class":"js-handle-click-ctr"}).attrs['href']
        #link = "jiji.co.ke"+link
        #region = i.find("span",attrs = {"class":"b-list-advert__region__text"})
        #description = i.find("div", attrs = {"class": "b-list-advert__description"})
        all_attr=[attr_names,price,attr]
        item_attr.append(all_attr)
        attr_only.append(attr)
        c+=1          

import csv
from csv import writer
for i in range(len(item_attr)):
    with open("html_scripts/test2.html","wb") as file:
    

        file.write((f"{item_attr[i]}").encode('utf-8'))

        file.close()
        with open("html_scripts/test2.html","r") as file:
            content = file.read()
            soup = BeautifulSoup(content,"lxml")
            x = soup.findAll("div")
            img_source = soup.findAll("img",attrs={"class":""})
            j2=[]
            
            for i in x:
                #print(i.text)
                j2.append(i.text.replace("\n","").replace("    ",""))
    
            with open('jiji.csv', 'a') as f_object:

                # Pass this file object to csv.writer()
                # and get a writer object
                writer_object = writer(f_object)

                # Pass the list as an argument into
                # the writerow()
                writer_object.writerow(j2)

                #Close the file object
                f_object.close()                    