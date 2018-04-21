import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Station = Base.classes.stations
Measurement = Base.classes.measurements

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/passengers"
    )


@app.route("/api/v1.0/precipitation")
def prcp_dates():
    # Query precipitation dates last 12 months
    results_prcp = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >='2016-09-01').\
    filter(Measurement.prcp != None).\
    order_by(Measurement.date.desc()).all()

   # Create a dictionary from the row data and append to a list 
    
    last_year_prcp = []
    for prcp in results_prcp:
        prcp_dict = {}
        prcp_dict["date"] = prcp.date
        prcp_dict["tobs"] = prcp.prcp
        last_year_prcp.append(prcp_dict)

    return jsonify(last_year_prcp)


@app.route("/api/v1.0/stations")
def stations():
    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    results_stations = session.query(Station.station).all()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_stations = list(np.ravel(results_stations))

    return jsonify(all_stations)



if __name__ == '__main__':
    app.run(debug=True)

