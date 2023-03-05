import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy as db
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = db.create_engine('sqlite:///hawaii.sqlite')

connection = engine.connect()

metadata = db.MetaData()

Measurement = db.Table('measurement', metadata, autoload=True, autoload_with=engine)

#print(Measurement.columns.keys())

Station = db.Table('station', metadata, autoload=True, autoload_with=engine)

print(Station.columns.keys())

session = Session(engine)

app= Flask(__name__)

# define route
@app.route("/")

# Create function
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')