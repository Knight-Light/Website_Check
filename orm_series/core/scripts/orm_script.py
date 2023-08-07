import json

from core.models import Court
from django.utils import timezone
from django.db import connection

court_info = json.load(open('court_data.json'))


def run():
    for i in range(len(court_info['Court Name'])):
        Court.objects.create(
           Court_Name=court_info['Court Name'][i],
           Court_Link=court_info['Court Link'][i],
           Scrap_Type=court_info['Scrap Type'][i],
           Site_Status=court_info['Status'][i],
           Response_Code=court_info['Response Code'][i],
           Date_and_Time=court_info['Date and Time'][i]
        )

