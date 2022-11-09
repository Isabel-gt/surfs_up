# Surfs_up 

## Overview of the Project
<p align="justify">The purpose of this project was to analyze the weather data from an island in Hawaii to determine if opening a surfing shop on the island is a good idea to invest. 
During this analysis SQL Lite and SQL Alchemy were used, as well as Flask. The objective of using Flask was to create an app and build a web page for the surfing shop.</p>

## Results
Before extracting the temperatures from the dataset, all the dependencies from sqlalchemy had to be imported. Also, an engine and a session link were created. 
For the first part of the analysis, the dates and the temperatures from June had to be extracted from the data set called *Hawaii.sqlite*. To extract this information, a query was written, as it is shown in the image below:

<img width="587" alt="1" src="https://user-images.githubusercontent.com/111388644/200943508-2b19ced5-25d3-456d-bbfc-513921ed0972.png">

Next, the temperatures were transformed into a list.

<img width="254" alt="2" src="https://user-images.githubusercontent.com/111388644/200943555-5128bdad-f407-439a-b6a8-4cd788b2dfa6.png">

After, a Data Frame was created from the list of temperatures.

<img width="420" alt="3" src="https://user-images.githubusercontent.com/111388644/200943581-ff131381-7d12-464d-beda-ae647be6bb4d.png">

Finally, the summary statistics were calculated. 

<img width="139" alt="4" src="https://user-images.githubusercontent.com/111388644/200943624-1ff2d37f-367d-474a-9209-59d50d629952.png">

The exact steps were taken in order to extract the temperature for the month of December. The results of the second part of the analysis are the ones shown below:

<img width="109" alt="5" src="https://user-images.githubusercontent.com/111388644/200943655-3ea7287b-f488-4650-bc85-45fa72bd6581.png">

## Summary
<p align="justify">According to the statistics calculated for the month of June, the maximum temperature on the island is 85 degrees, and the minimum is 64 degrees. Also, the average temperature is 74.9 degrees, which is not a bad temperature for surfing.</p>

<p align="justify">From the results for the month of December, it can be concluded that for a winter month the temperatures are acceptable. The analysis shows an average temperature of 71 degrees. It also displays a maximum temperature of 83 degrees, and a minimum of 56 degrees.</p>

<p align="justify">Another query that could be helpful was to extract the precipitation on the island. This is an important factor since that could impact the amount of people that go surfing, therefore, it impacts the revenue of the surfing shop.</p>

<p align="justify">Lastly, the statistics for the elevation should be calculated as well, since elevation has a direct influence on the weather.</p> 

