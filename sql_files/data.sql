CREATE  TABLE car_data(
    ID int,
    img_link VARCHAR(100),
    Name VARCHAR(80),
    Price INT,
    Region VARCHAR(80),
    Description VARCHAR(250),
    Use VARCHAR(50),
    Gearbox VARCHAR(50),
    Mileage INT,
    Town VARCHAR ,
    region1 VARCHAR,
    Year_of_manufacture VARCHAR,
    CC VARCHAR

);
\COPY "car_data" FROM 'C:\Users\Collins\Desktop\webscraping2.0\webscraping-data-store\clean_data.csv' DELIMITER ',' CSV HEADER;
/*
'Unnamed: 0', 'img_link', 'Name', 'price', 'region', 'description',
       'use', 'gearbox', 'mileage', 'town', 'Region', 'Year_of_manufacture',
       'CC'*/