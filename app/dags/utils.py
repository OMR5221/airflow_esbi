import requests
from datetime import datetime, timedelta, date
from bs4 import BeautifulSoup
import pathlib


def pull_api_data(**kwargs):
    server_name = kwargs['server_name']
    tag_name = kwargs['tag_name']
    start_time_str = kwargs['start_time']
    end_time_str = kwargs['end_time']

    start_datetime = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
    end_datetime = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')

    time_diff = (end_datetime - start_datetime)
    day_diff = int(time_diff.days)

    if day_diff > 0:
        days_to_mins = (day_diff * 24) * 60
    else:
        days_to_mins = 0

    secs_to_mins = (time_diff.seconds / 60) + 1

    interval = str(int(days_to_mins + secs_to_mins))

    url="http://api.source.dummy.url.com"
    headers = {'content-type': 'text/xml'}
    body = """<?xml version="1.0" encoding="utf-8"?>
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:fpl="http://dummy.url/">
       <soapenv:Header/>
       <soapenv:Body>
          <fpl:GetInterpolatedValues>
             <!--Optional:-->
             <fpl:serverName>{ServerName}</fpl:serverName>
             <!--Optional:-->
             <fpl:pointName>{TagName}</fpl:pointName>
             <!--Optional:-->
             <fpl:startTime>{StartTime}</fpl:startTime>
             <!--Optional:-->
             <fpl:endTime>{EndTime}</fpl:endTime>
             <fpl:intervals>{Interval}</fpl:intervals>
          </fpl:GetInterpolatedValues>
       </soapenv:Body>
    </soapenv:Envelope>""".format(ServerName=server_name,TagName=tag_name,StartTime=start_time_str,EndTime=end_time_str,Interval=interval)
    response = requests.post(url,data=body,headers=headers,verify=False,
                             proxies={  "https":"https://proxyjb.com:8080",
                                      "http": "http://proxyjb.com:8080"})
    xml = response.content
    soup = BeautifulSoup(xml, 'lxml')
    print(soup)
