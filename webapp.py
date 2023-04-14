######################################################################################################################
# Name: Group 1 
# Date: 
# Description: CSC 132 Final Project
######################################################################################################################

from flask import Flask, render_template
import json
import time
#import board
from adafruit_seesaw.seesaw import Seesaw
from multiprocessing import Process

# The code to get and display the soil moisture and temperature data.

#i2c_bus = board.I2C()  # uses board.SCL and board.SDA

#ss = Seesaw(i2c_bus, addr=0x36)


# Helper function to easly  parallelize multiple functions
def parallelize_functions(*functions):
    processes = []
    for function in functions:
        p = Process(target=function)
        p.start()
        processes.append(p)
    for p in processes:
        p.join()

# Constants for the webapp
HOST = "localhost"
PORT = 1234
DEBUG = True

# Variables for the different plant variables
tempData = []
moisData = []

# instantiates the app
app = Flask(__name__)

# Landing page function
@app.route("/")
def landingPageIndex():
    return render_template("index.html")

# Temperature page function
@app.route("/temp")
def temperaturePageIndex():
    # data = tempData

    data = [
        (123,123),
        (123,13),
        (123,50),
        (150,23),
        (123,123),

    ]
    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template("temp.html", labels=labels, values=values)

# Moisture page function
@app.route("/moisture")
def moisturePageIndex():
    return render_template("moisture.html")

# Light page function
@app.route("/light")
def lightPageIndex():
    return render_template("light.html")


# A function that gets the temperature of the plant perpetually
def getMoisTemp():
    while True:

        # Gets the current time in the proper format
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)

        # Reads the current moisture from the sensor
        # mois = ss.moisture_read()
        mois = 0

        # read temperature from the temperature sensor
        # temp = ss.get_temp()
        temp = 0

        # Adds the data to a dictonary and assigns the new data to the graph
        tempData.append((current_time, temp))
        temperaturePageIndex()

        moisData.append((current_time, mois))

        # Prints the data 
        print("temp: " + str(tempData) + "  moisture: " + str(moisData))
        time.sleep(30)


# A function to run the app
def run_app():
    app.run(debug=DEBUG,host=HOST,port=PORT)

# To run the app
if __name__ == "__main__":
    # parallelize_functions(getMoisTemp, run_app)
    app.run(host=HOST,port=PORT,debug=DEBUG)