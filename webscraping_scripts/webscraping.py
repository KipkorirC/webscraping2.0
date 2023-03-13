import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import numpy as np
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#driver = webdriver.Chrome(options=options)
category = "cars"
search_Query = "mazda axela"
partitioned_search = search_Query.partition(" ")
filter_1 =partitioned_search[0]
filter_2 = partitioned_search[2]
year_max = ""
year_min = ""
base_url = f"https://jiji.co.ke/{category}?query={search_Query}&filter_attr_1_make={filter_1}&filter_attr_2_model={filter_2}&filter_attr_119_year_of_manufacture__min={year_min}&filter_attr_119_year_of_manufacture__max={year_max}"
base_url2 = "https://jiji.co.ke/cars"
driver_url = r"/webdriver/geckodriver"
wd = webdriver.Firefox(executable_path=driver_url)
wd.get(base_url)
time.sleep(2)  # Allow 2 seconds for the web page to open
scroll_pause_time = 10 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = wd.execute_script("return window.screen.height;")  
i=1
while True:
    # scroll one screen height each time
    wd.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = wd.execute_script("return document.body.scrollHeight;")  
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break


with open("html_scripts/test.html", "wb") as file:
    file.write( wd.page_source.encode('utf-8')) 

with open("./html_scripts/test.html","rb") as file:
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
        img= i.findAll("source", attrs = {"class":""})
        link = i.find("a",attrs = {"class":"js-handle-click-ctr"})
        #link = "jiji.co.ke"+link
        region = i.findAll("div",attrs = {"class":"b-list-advert__region"})
        description = i.find("div", attrs = {"class": "b-list-advert__description-text"})

        all_attr=[attr_names,price,region,description,img,attr]
        item_attr.append(all_attr)
        c+=1          

import csv
from csv import writer
for i in range(len(item_attr)):
    with open("./html_scripts/test2.html","wb") as file:
    

        file.write((f"{item_attr[i]}").encode('utf-8'))

        file.close()
        with open("./html_scripts/test2.html","r" ,encoding="UTF-8") as file:
            content = file.read()
            soup = BeautifulSoup(content,"lxml")
            x = soup.findAll("div")
            img_source = soup.findAll("img",attrs={"class":""})
            j2=[]
            j3 =[]    
            for z in img_source:
                j2.append(z.attrs['src'])      

            for i in x:
                #print(i.text)
                j2.append(i.text.replace("\n","").replace("    ",""))

            with open('./csv_files/jiji.csv', 'a') as f_object:

                # Pass this file object to csv.writer()
                # and get a writer object
                writer_object = writer(f_object)

                # Pass the list as an argument into
                # the writerow()
                writer_object.writerow(j2)

                
                #Close the file object
                f_object.close()

                                


# code to write the data to postgresql
#from sqlalchemy import create_engine
#engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')
#df.to_sql('table_name', engine)           