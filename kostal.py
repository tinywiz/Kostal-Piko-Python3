# Gets basic data from Kostal inverters

import requests
from lxml import html

def kostalData(url="http://192.168.1.99/index.fhtml",login='pvserver',pwd='pvwr'):
    """
	Needs full URL, login and password
    Defaults are:

        url = http://192.168.1.99/index.fhtml
        login = pvserver
        pwd = pvwr

    Returns kostal data as seen from webpage in string format
    status = True if OK
    status = Fail if data could not be retrieved
	"""
    try:
        response = html.fromstring(requests.get( url , auth = ( login, pwd )).content )
        data = [v.text.strip() for v in response.xpath("//td[@bgcolor='#FFFFFF']")]
        kostal = {
        'CurrentAC' : data[0],
        'TotalEnergy' : data[1],
        'DailyEnergy' : data[2],
        'String1V' : data[3],
        'L1V' : data[4],
        'String1A' : data[5],
        'L1W' : data[6],
        'String2V' : data[7],
        'L2V' : data[8],
        'String2A' : data[9],
        'L2W' : data[10],
        'L3V' : data[11],
        'L3W' : data[12],
        'status' : True
        }
        return kostal

    except:
        kostal = {}
        kostal = {'status': False}
        return kostal
