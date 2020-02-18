# FlightLogger

A Python 3 script used to store unique flights per day from dump1090 as a CSV file. 

## Usage

Before you can successfully run `FlightLogger.py` you will need to create a file called `config.py`. The file should be formatted as such:

```
IP_ADDR = 'Host IP Address'
```

Once you have created the config file, you can run `python3 FlightLogger.py`. You should see the output in the `flights/` folder in the corresponding month.

The best use of this script would be to run it as a cron job or something similar. 

Have a suggestion? [Please submit an issue](https://github.com/georgeglessner/FlightLogger/issues/new)! 
