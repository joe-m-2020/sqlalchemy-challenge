import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

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
        f"/api/v1.0/<start>/<end>"
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


if __name__ == '__main__':
    app.run(debug=True)