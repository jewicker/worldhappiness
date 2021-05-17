# worldhappiness
This Dash app interactively plots happiness score as a function of GDP per capita from 2015 to 2021 using data from the World Happiness Report

The user can hold their mouse over a particular datapoint and the corresponding name of the country or region will appear. The name of the file is “worldhappiness.py”. The data were originally compiled as described at the website: https://worldhappiness.report/. I downloaded separate datasets from all years considered here from Kaggle.com. Some definitions of the data columns changed between the various years, for example, the names of the columns changed between various datasets. As a result, I had to do some preprocessing at the beginning of the program in order to concatenate all the years into a single usable Pandas dataframe, and in order to facilitate better memory management and possible future extendibility, I defined a function named “produce_df” that reads data from the datafiles and generates the correct form for the data.

The issued World Happiness Report is quite extensive, but as far as I can ascertain, the variable “GDP per capita” represents the log of a country or region’s per capita GDP measured in US dollars.

The datasets that are read into this program should be stored in a subdirectory named “datafiles”.

The file worldhappiness_test.py is in the test_file directory. This file confirms of the data are being read correctly and have the correct form. In order to run this program, it needs to be placed one directory above the datafiles directory.

This program runs in Python 3.8.
