# Show Me Where project

A **project showing me where things** are.

# About the dataset

The U.S. State Department tracks all refugees entering the country on a daily basis. It also tracks their country of origin, religion, ethnicity, language spoken, and destination. The dataset includes refugees who entered the U.S. October 1, 2015 to December 31, 2015, who were resettled in California alone. It contains roughly 130 records, and its fields include the country of origin, destination city, the total number of refugees accepted to the U.S. during that time period, the total number of refugees accepted from each country of origin, and the total number resettled in each California city.  

## Basic facts about the dataset

- The source of the data: [U.S. State Department, Wrapsnet.org](http://www.wrapsnet.org/Reports/InteractiveReporting/tabid/393/Default.aspx)
- The data's landing page: [Arrival Reports](http://www.wrapsnet.org/Reports/InteractiveReporting/tabid/393/EnumType/Report/Default.aspx?ItemPath=/rpt_WebArrivalsReports/MX%20-%20Arrivals%20by%20Destination%20and%20Nationality)
- Direct link to the data: [http://www.wrapsnet.org/Reports/InteractiveReporting/tabid/393/EnumType/Report/Default.aspx?ItemPath=/rpt_WebArrivalsReports/MX%20-%20Arrivals%20by%20Destination%20and%20Nationality](http://www.wrapsnet.org/Reports/InteractiveReporting/tabid/393/EnumType/Report/Default.aspx?ItemPath=/rpt_WebArrivalsReports/MX%20-%20Arrivals%20by%20Destination%20and%20Nationality)
- The data format: CSV
- Number of rows: 127

## Description of data fields

#### Textbox 87 

Defines beginning of date range for data

#### Textbox 82 

Defines end of date range for data

#### nat_definition

defines destination U.S. State (California for all)

#### region_name

defines whether time period is in terms of calendar or fiscal year

#### textbox37  

gives the total number of refugees who entered U.S. during specified time period


#### Category3 

defines country of origin

#### textbox39

defines total number of refugees from country of origin

#### Assur_Destin

defines destination city

## Cases3

defines total number of refugees from country of origin who settled in specific city

## Anticipated Data Wrangling

I will need to geotag the countries of origin and the destination cities in terms of latitude and longitude, instead of their current names

