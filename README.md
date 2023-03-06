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
2. Design a query to find the most-active stations (that is, the stations that have the most rows).
   - List the stations and observation counts in descending order.
   - Find the station id with the greatest number of observations. 
3. Design a query that calculates the lowest, highest and average temperatures that filters on the most-active station id found in the previous query. 
4. Design a query to get the previous 12 months of temperature observation (TOBS) data.
   - Filter by the station that has the greatest number of observations. 
   - Query the previous 12 months of TOBS data for that station. 
   - Plot the results as a histogram with `bins=12`
5. Close your session. 


## Design Your Climate App

Now that the initial analysis is complete, design a Flask API based on the queries that were developed. 
Flask was used to create routes

1. `/` 
   - Start at the homepage.
   - List all the available routes.
2. `/api/v1.0/precipitation`
   - Convert the query results from the precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using `date` as the key and `prcp`
as the value. 
   - Return the JSON representation of your dictionary. 
3. `/api/v1.0/stations`
   - Return a JSON list of stations from the dataset. 
4. `/api/v1.0/tobs`
   - Query the dates and temperature observations of the most-active station for the previous year of data. 
   - Return a JSON list of temperature observation for the previous year. 
5. `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
   - Return a JSON list of the minimum temperature, the average temperature and the maximum temperature for a specified start or start-end range.
   - For a specified start, calculate `TMIN`, `TAVG`, and `TMAX` for all the dates greater than or equal to the start date. 
   - For a specified start date and end date, calculate `TMIN`, `TAVG`, and `TMAX` for the dates from the start date to the end date, inclusive.
