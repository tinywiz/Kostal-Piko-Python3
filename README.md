Reads data from Kostal Piko Inverters
Dependencies are 'Requests' and 'lxml'

Needs full URL, login and password
Defaults are:

  url = http://192.168.1.99/index.fhtml
  login = pvserver
  pwd = pvwr
  
Returns kostal data as seen from webpage in string format.
The following data is returned:

CurrentAC
DailyEnergy
L1V
L1W
L2V
L2W
L3V
L3W
String1A
String2V
String2A
String1V
TotalEnergy
status

Check status before processing data!

status = 'True' if OK
status = 'Fail' if data could not be retrieved for any reason

Example based on my Kostal Piko 7:  
kostalData('http://192.168.1.99/index.fhtml', 'pvserver', 'pvwr')

Returns:

{'CurrentAC': '1268',
 'DailyEnergy': '36.35',
 'L1V': '235',
 'L1W': '417',
 'L2V': '234',
 'L2W': '417',
 'L3V': '235',
 'L3W': '434',
 'String1A': '1.12',
 'String1V': '623',
 'String2A': '1.12',
 'String2V': '630',
 'TotalEnergy': '40948',
 'status': True}
