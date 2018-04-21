<!--lint disable no-heading-punctuation-->
# SQL ORM Analysis - Hawaii Climate
<!--lint enable no-heading-punctuation-->

<img src='images/surfs-up.jpeg' />


## File Composition

- data_engineering: Contains activities of cleaning data. 
  There are NaNs values in "prcp" column, however it's not good idea to delete all these rows because we could lost valuable data ("tobs" column). For specific metrics and charts of precipitation, we are going to filter NaN values.
 The only data I will delete will be rows without date. But, this is not the case.
 
 On the other hand, instead of deleting data, I add an autoincrement ID as primary key on Measurement table. 

---

- database_engineering: Contains activities of mapping data into ORM objects. 
  After cleaning data, it's time save this data into a DB. This is going to be hawaii.sqlite.
  In this case, we create each class: Measurements and Stations, specifying each data type.
  

---


---






