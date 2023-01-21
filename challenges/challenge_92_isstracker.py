#!/usr/bin/env python3
import requests
import datetime

url = "http://api.open-notify.org/iss-now.json"

def main():
    data = requests.get(url).json()
    date_time = datetime.datetime.fromtimestamp(data['timestamp'])  
    print('CURRENT LOCATION OF THE ISS:')
    print('Timestamp: ', date_time)
    print('Lon: ', data['iss_position']['longitude'])
    print('Lat: ', data['iss_position']['latitude'])

if __name__ == "__main__":
    main()
