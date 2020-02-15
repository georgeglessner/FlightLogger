from datetime import datetime
from datetime import date
from config import IP_ADDR
import requests
import os
import csv

filename = "flights.csv"

# check if files exists
file_exists = os.path.isfile(filename)

# get all flights tracked to check against for duplicates
flights = ""
if file_exists:
    with open(filename, "r") as fp:
        flights = fp.read()

today = date.today()
time = datetime.now().strftime("%H:%M:%S")

# get json data
json_dump = requests.get("http://{}:8080/data/aircraft.json".format(IP_ADDR)).json()

# write unique flights for the day to csv file
with open(filename, "a", newline="") as file:
    writer = csv.writer(file)
    fieldnames = ["flight", "date", "time"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # create headers if first time writing to file
    if not file_exists:
        writer.writeheader()

    # add unique flights for the day
    for entry in json_dump["aircraft"]:
        # print( f'{entry['flight'].strip()}, {date.today()}')
        if "flight" in entry and "{},{}".format(entry['flight'].strip(), today) not in flights:
            writer.writerow(
                {"flight": entry["flight"].strip(), "date": today, "time": time}
            )
