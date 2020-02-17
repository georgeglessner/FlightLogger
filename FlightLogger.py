from datetime import datetime
from datetime import date
from config import IP_ADDR
import requests
import os
import csv

today = date.today()
month = datetime.now().strftime("%B")
year = datetime.now().strftime("%Y")
time = datetime.now().strftime("%H:%M:%S")

# file setup
filename = "{}.csv".format(today)
rootFolder = "flights/"
subFolder = "{}-{}/".format(month, year)
filepath = rootFolder + subFolder + filename

# create root folder and sub folder
if not os.path.isdir(rootFolder):
    os.mkdir(rootFolder)

if not os.path.isdir(rootFolder + subFolder):
    os.mkdir(rootFolder + subFolder)

# check if files exists
file_exists = os.path.isfile(filepath)

# get all flights tracked to check against for duplicates
flights = ""
if file_exists:
    with open(filepath, "r") as fp:
        flights = fp.read()


# get json data
json_dump = requests.get("http://{}:8080/data/aircraft.json".format(IP_ADDR)).json()

# write unique flights for the day to csv file
with open(filepath, "a", newline="") as file:
    writer = csv.writer(file)
    fieldnames = ["flight", "date", "time"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # create headers if first time writing to file
    if not file_exists:
        writer.writeheader()

    # add unique flights for the day
    for entry in json_dump["aircraft"]:
        if (
            "flight" in entry
            and "{},{}".format(entry["flight"].strip(), today) not in flights
        ):
            writer.writerow(
                {"flight": entry["flight"].strip(), "date": today, "time": time}
            )
