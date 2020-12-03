import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as dt

#############################################
#DB Setup
#############################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#############################################
#Flask Setup
#############################################

app = Flask(__name__)


##############################################
#Flask Routes
##############################################
@app.route('/')
def home():
    """List all available api routes."""
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"Enter Starting Date for Min Temp, Max Temp, and Average Temp recorded on or after date ######DATE MUST BE IN YYYY/MM/DD format####</br/>"
        f"/api/v1.0/<start>/<end></br/>"
        f"Enter Starting Date/End Date for Min Temp, Max Temp, and Average Temp recorded on or between dates ######DATE MUST BE IN YYYY/MM/DD format####"
    )


@app.route('/api/v1.0/precipitation')
def precipitation():
    #create session from Python to DB
    session=Session(engine)

    #query date and prcp
    results=session.query(Measurement.date,Measurement.prcp).\
            filter(Measurement.date>='2016-08-23').all()
    
    session.close()

    #create dictionary for date as key and prcp as value
    
    measurement_dict={}
    for date, prcp in results:
        measurement_dict[date]=prcp
    return jsonify(measurement_dict)


@app.route('/api/v1.0/stations')
def stations():
    session=Session(engine)

    #query date and prcp
    results=session.query(Station.name).all()
    session.close()

    station_names=[]
    for name in results:
        station_names.append(name[0])
    return jsonify(station_names)
    

@app.route('/api/v1.0/tobs')
def tobs():
    session=Session(engine)

    results=session.query(Measurement.tobs).\
    filter(Measurement.station=='USC00519281').\
    filter(Measurement.date>='2016-08-18').all()

    session.close()

    tobs_list=[]
    for temp in results:
        tobs_list.append(temp[0])
    return jsonify(tobs_list)

@app.route('/api/v1.0/<start>')
def start_date(start):
    normalized = dt.datetime.strptime(start, '%Y-%m-%d')
    session=Session(engine)
    results=session.query(func.min(Measurement.tobs), func.max(Measurement.tobs),func.avg(Measurement.tobs)).\
        filter(Measurement.date>=normalized).all()
    

    stats_list=[]
    for result in results:
        stats_list.append(result)
    return jsonify(stats_list)

@app.route('/api/v1.0/<start>/<end>')
def start_end_date(start,end):
    normalized_start = dt.datetime.strptime(start, '%Y-%m-%d')
    normalized_end = dt.datetime.strptime(end, '%Y-%m-%d')
    session=Session(engine)
    results=session.query(func.min(Measurement.tobs), func.max(Measurement.tobs),func.avg(Measurement.tobs)).\
        filter(Measurement.date>=normalized_start).\
        filter(Measurement.date<=normalized_end).all()
    

    stats_list=[]
    for result in results:
        stats_list.append(result)
    return jsonify(stats_list)

if __name__ == '__main__':
    app.run(debug=True)