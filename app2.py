import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Set Up the Database
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the database into our classes


# reflect the database (tables?)





# save our references to each table
#Measurement = Base.classes.measurement
#Station = Base.classes.station

#
#session = Session(engine)
