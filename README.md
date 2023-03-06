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
```ruby
session.query(measurement.date).order_by(measurement.date.desc()).first()
```
2. Using that date, get the previous 12 months of preceipitation data by querying the previous 12 months of data (without using the date as a variable).
   - Select only the 'date' and 'prcp' values.
```ruby
precipitation_query = []
precipitation_query = session.query(measurement.date, measurement.prcp).filter(measurement.date >= '2016-08-23').all()
```
3. Load the query results into a Pandas DataFrame and set the index to the 'date' column. 
   - Sort the DataFrame values by 'date'. 
```ruby
df = pd.DataFrame(precipitation_query, columns=['date', 'precipitation'])
df.set_index(df['date'], inplace=True)
print(df)
df= df.sort_index()
#Drop the null values from the DataFrame
precipitation_df = df.dropna()
print(precipitation_df)
```
4. Plot the results using the DataFram plot method.
```ruby
plt.figure(figsize= (11.5, 8))
plt.bar(precipitation_df['date'], precipitation_df['precipitation'], color='midnightblue', label= "Precipitation", width=2.5)
plt.xticks(precipitation_df['date'], rotation=90, fontsize= 18)
plt.yticks(np.arange(0, 7.5, 1), fontsize = 18)
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
#plt.gcf().autofmt_xdate()
plt.xlim()
plt.xlabel("Date", fontsize= 18, fontweight= 'bold')
plt.ylabel("Precipitation (Inches)", fontsize = 18, fontweight = 'bold')
plt.legend(fontsize=18, loc="upper right")
```
![image](https://user-images.githubusercontent.com/115905663/223168077-36144a97-b170-476c-9b3c-91abc51434f8.png)

5. Use Pandas to print the sumamry statistics for the precipitation data. 
```ruby
precipitation_df.describe()
``` 
![image](https://user-images.githubusercontent.com/115905663/223168507-3236ac6f-ee71-4e67-9764-0cf874f36c8d.png)

#### Station Analysis
1. Design a query to calculate the total number of stations in the dataset. 
```ruby
station_count = session.query(station).distinct().count()
print(station_count)
```

2. Design a query to find the most-active stations (that is, the stations that have the most rows).
   - List the stations and observation counts in descending order.
   - Find the station id with the greatest number of observations. 
```ruby
session.query(measurement.station, func.count(measurement.station)).\
group_by(measurement.station).order_by(func.count(measurement.station).desc()).all()
```

3. Design a query that calculates the lowest, highest and average temperatures that filters on the most-active station id found in the previous query. 
```ruby
session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
filter(measurement.station == 'USC00519281').all()
```

4. Design a query to get the previous 12 months of temperature observation (TOBS) data.
   - Filter by the station that has the greatest number of observations. 
   - Query the previous 12 months of TOBS data for that station. 
   - Plot the results as a histogram with `bins=12`
```ruby
temperature_results = session.query(measurement.tobs).\
filter(measurement.station == 'USC00519281').\
filter(measurement.date.between('2016-08-23', '2017-0823')).all()
#Save results to a dataframe that will be used to make the histogram
temperature_df = pd.DataFrame(temperature_results, columns=['tobs'])
print(temperature_df)
```
```ruby
temperature_df.plot.hist(bins=12)
plt.xlabel('Temperature')
```
![image](https://user-images.githubusercontent.com/115905663/223169483-a7bf24da-eab1-48e3-ba07-c59cc69c64c8.png)

5. Close your session. 
```ruby
session.close()
```

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
