import pandas as pd
data = pd.read_excel("./webscraping-data-store/car_data.xlsx")
#checking for null values in the data data
data.isna().sum()
#filling null values
data.mileage.fillna("0",inplace=True)
duplicated_Data = data[data.duplicated(['img_link'])]
duplicated_Data
data.drop_duplicates(['img_link'],inplace=True)
type(data.price[0])
data["mileage"] = data["mileage"].map(lambda x :int(x.replace("km","")))
data.mileage
data["price"] = data["price"].map(lambda x :int(x.replace("KSh","").replace(",","")))
data["town"] = data["region"].map(lambda x:x.split(",")[1:][0])
data["Region"] = data["region"].map(lambda x:x.split(",")[:1][0])
import re
pattern = "\d{4}"
data["Year_of_manufacture"] =data["Name"].map(lambda x:re.findall(pattern,x)[0])
pattern2 = "\d{4}cc"
pattern3 = "\d{4}CC"
pattern4 = "\d{4} CC"
#data["CC"] = data["description"].map(lambda x:getCC(x))
def getCC(data):
    if(re.findall(pattern3,data)):
        return re.findall(pattern3,data)[0]
    elif(re.findall(pattern2,data)):
        return re.findall(pattern2,data)[0]
    elif(re.findall(pattern4,data)):
        return re.findall(pattern4,data)[0] 
    else:
        return "Not specified"


data["CC"] = data["description"].map(lambda x:getCC(x))
data.drop(columns={"Unnamed: 0"},inplace =True)
ID =[]
for i in range(0,len(data)):
    ID.append(i)

data.insert(loc=0,column="ID",value= ID)  
data.to_csv("webscraping-data-store/clean_data2.csv")