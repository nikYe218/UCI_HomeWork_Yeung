#############################################
#Flask API - Climate App
#############################################
import numpy as np
import sqlalchemy
import datetime as dt
from datetime import datetime, timedelta 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


from flask import Flask, jsonify

### DB Setup

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measure = Base.classes.measurement
Station = Base.classes.station

##################################################
# Flask Setup
##################################################

app = Flask(__name__)

##################################################
# Flask Routes
##################################################

@app.route("/")

def welcome():
    """List all routes that are available."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&ltstart&gt<br/>"
        f"/api/v1.0/&ltstart&gt/&ltend&gt"
        
    )

@app.route("/api/v1.0/precipitation")
def precepitation():
    session = Session(engine)
    
    results = session.query(Measure.date, Measure.prcp).\
              order_by(Measure.date).all()
    
    session.close()

    precip_data = []
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        precip_data.append(precipitation_dict)
   
    return jsonify(precip_data)

    
@app.route("/api/v1.0/stations")
def stations():
    session=Session(engine)
    
    results = session.query(Measure.station).\
                            group_by(Measure.station).all()
    session.close
    
    all_stations = list(np.ravel(results))
    
    return jsonify(all_stations)
    
    
    
@app.route("/api/v1.0/tobs")
def tobs():
    session= Session(engine)

    top_temp = session.query(Measure.station,func.max(Measure.date)).\
                          group_by(Measure.station).\
                          order_by(func.count(Measure.station).desc()).first()

    
        
    highCntSta = top_temp[0]
    date_time_str = top_temp[1]
  
    enddt = dt.datetime.strptime(date_time_str, '%Y-%m-%d').date().replace(month=1, day=1)   
    begdt = enddt - timedelta(366)
  
    

    high_temp_results = session.query(Measure.date,Measure.tobs).\
                            filter(Measure.date>=begdt ,Measure.date< enddt,Measure.station==highCntSta).\
                            order_by(Measure.date.asc()).all()
     
    session.close
  
    
    return jsonify(high_temp_results)
    


@app.route("/api/v1.0/<start>")
def rs_start(start):
    session= Session(engine)
  
    results = session.query(Measure.date,func.min(Measure.tobs),func.avg(Measure.tobs),func.max(Measure.tobs)).\
                           filter(Measure.date >= start).\
                           group_by(Measure.date).\
                           order_by(Measure.date.desc()).all()
    
    session.close
    
    calc_results = []
    
    for date, tmin, tavg, tmax in results:
        start_dict = {}
        start_dict["Date"] = date
        start_dict["TMIN"] = tmin
        start_dict["TAVG"] = tavg
        start_dict["TMAX"] = tmax
        
        calc_results.append(start_dict)
        
    return jsonify(calc_results)
 
    
@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):
    session= Session(engine)
    
    results = session.query(Measure.date,func.min(Measure.tobs),func.avg(Measure.tobs),func.max(Measure.tobs)).\
                filter(Measure.date >= start, Measure.date <=end).\
                group_by(Measure.date).\
                order_by(Measure.date.desc()).all()
    
    session.close
    
    calc_results = []
    
    for date, tmin, tavg, tmax in results:
        start_dict = {}
        start_dict["Date"] = date
        start_dict["TMIN"] = tmin
        start_dict["TAVG"] = tavg
        start_dict["TMAX"] = tmax
        
        calc_results.append(start_dict)
        
    return jsonify(calc_results)
 
                            
                            
  
if __name__ == '__main__':
    app.run(debug=True)