import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")
#same as jupyter
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

app = Flask(__name__)

@app.route("/")
def mainpage():
	return(f"/api/v1.0/precipitation")

@app.route("/api/v1.0/precipitation")
def precipitation():
	oneyear = dt.date(2011,1,3) - dt.timedelta(days=365)
	framing = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > oneyear).all()

	#for date and rain in function, jsonfiy
	json = {date:prcp for date, prcp in precipitation}
	return jsonify(json)

if __name__ == '__main__':
    app.run()
