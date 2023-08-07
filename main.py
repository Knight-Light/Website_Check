import requests
import urllib3
from Collected_data import court_data
urllib3.disable_warnings()
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from datetime import datetime
import json
import schedule
import time


def fetch():
    for link in court_data['Court Link']:
        r = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        r.mount('http://', adapter)
        r.mount('https://', adapter)

        try:
            r = requests.get(link, verify=False, allow_redirects=True)
            if r.status_code == 200:
                court_data['Status'].append('up')
                court_data['Response Code'].append(r.status_code)
                now = datetime.now()
                date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                court_data['Date and Time'].append(date_time)
                print(link, r.status_code)

            elif r.status_code % 100 != 2:
                court_data['Status'].append('down')
                court_data['Response Code'].append(r.status_code)
                now = datetime.now()
                date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                court_data['Date and Time'].append(date_time)
                print(link, r.status_code)


        except requests.exceptions.HTTPError as err:
            court_data['Status'].append(f'An HTTP error occurred')
            court_data['Response Code'].append({err})
            now = datetime.now()
            date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            court_data['Date and Time'].append(date_time)
            print(link, err)

        except requests.exceptions.ConnectionError as err1:
            court_data['Status'].append(f'A Connection error occurred')
            court_data['Response Code'].append("Error occured")
            now = datetime.now()
            date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            court_data['Date and Time'].append(date_time)
            print(link, err1)


#fetch()
schedule.every(2).hours.at("08:00").do(fetch)

while True:
    schedule.run_pending()


#fetch(court_data)
#with open("court_data.json", "w") as final:
   # final.write(json.dumps(court_data, indent=2))

#final.close()

