# sqlalchemy-challenge

## Background
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis
about the area. The following sections outline the steps you need to take to accomplish the task. 

## Analyze and Explore Climate Data

#### Reflect Tables into SQLAlchemy ORM
To connect to the SQLite database, the SQLAlchemy function `create_engine()` was used. 
```ruby
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")
``` 


Tables were reflected into classes and then references were saved to the classes named `station` and `measurement`. 
```ruby
Base = automap_base()
Base.prepare(autoload_with=engine)
measurement = Base.classes.measurement
station = Base.classes.station
```

Then Python was linked to the database by creating a SQLAlchemy session. 
```ruby
session = Session(engine)
```

#### Precipitation Analysis
1. Find the most recent date in the datatset.
2. Using that date, get the previous 12 months of preceipitation data by querying the previous 12 months of data (without using the date as a variable).
3. Select only the 'date' and 'prcp' values.
4. Load the query results into a Pandas DataFrame and set the index to the 'date' column. 
5. Sort the DataFrame values by 'date'. 
6. Plot the results using the DataFram plot method.
7. Use Pandas to print the sumamry statistics for the precipitation data. 

#### Station Analysis
1. Design a query to calculate the total number of stations in the dataset. 
2. Design a query to find the most-active stations (that is, the stations that have the most rows)
   - List tje stations and observation counts in descending order
   - Find the station id with the greatest number of observations. 
