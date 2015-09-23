from bs4 import BeautifulSoup
import urllib.request

url = 'http://hodiny.hamrsport.cz/Login.aspx?r=NOTLOGGED'
req = urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0')
resp = urllib.request.urlopen(req)

cookies = resp.getheader('Set-Cookie')
sessionId = cookies[21:45]
print(sessionId)
cookie = 'HamrOnline$SessionId=' + sessionId
#html1 = resp.read()
#soup = BeautifulSoup(html1)
#eventvalidation = soup.select('#__EVENTVALIDATION')[0]['value']

#print('Eventvalidation: ')
#print(eventvalidation)

print("Setting LOCALITY...")
#set Locality
payload = urllib.parse.urlencode({
    'ctl00$ToolkitScriptManager' : 'ctl00$workspace$upResGridTools|ctl00$workspace$ddlLocality',
    'ctl00_ToolkitScriptManager_HiddenField' : ';;AjaxControlToolkit, Version=3.5.7.123, Culture=neutral, PublicKeyToken=28f01b0e84b6d53e:en-US:5214fb5a-fe22-4e6b-a36b-906c0237d796:de1feab2:f9cec9bc:a67c2700:f2c8e708:720a52bf:589eaa30:8613aea7:3202a5a2:ab09e3fe:87104b7c:be6fb298',
    '__VIEWSTATE' : '',
    'ctl00$toolboxRight$tbLoginUserName' : '',
    'ctl00$toolboxRight$tbLoginPassword' : '',
    'ctl00$workspace$ddlLocality' : '171',
    'ctl00$workspace$ddlSport' : '137', 
    '__EVENTTARGET' : 'ctl00$workspace$ddlLocality',
    '__EVENTARGUMENT' : '',
    '__LASTFOCUS' : '',
    '__EVENTVALIDATION' : '/wEWGQL+raDpAgKvz6a4CALr2Kn3DQLwz4vcBwLDgoKdDAKz/tyyAgLfs+yXBgLfs/CXBgKDws6WDALims6iCAKa0KWLCQLV8I58AtXwknwC1fe/oA4Cyora7wgCpc/G/wMCuIzUnwoCsfugHwKjzLuXCQKmuvzIBQK3oLnDBQLeltWgAgLitvv/BQLOu/iCCwKfvKSQCZdk0J5TCjvCWtaJ4XnLQ+3w/3O4',
    '__ASYNCPOST' : 'true'
    })

pbinary = payload.encode('UTF-8')
req = urllib.request.Request(url, data=pbinary)
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0')
#req.add_header('Cookie', '_ga=GA1.2.1315628644.1442951353; __utma=74282507.1315628644.1442951353.1442953312.1442959139.3; __utmz=74282507.1442953312.2.2.utmcsr=hamrsport.cz|utmccn=(referral)|utmcmd=referral|utmcct=/cs/kontakty-branik/; HamrOnline$SessionId=0lpotu45dbisnw45nb3ms045; __utmc=74282507; __utmb=74282507.1.10.1442959139; __utmt=1')
req.add_header('Cookie', cookie)
#req.add_header('Connection', 'keep-alive')
#req.add_header('Cache-Control', 'max-age=0')
res = urllib.request.urlopen(req)
print('Status: ')
print(res.status)

#r2 = requests.post(url, data=payload)
h2 = res.read()
s2 = BeautifulSoup(h2)

#print(soup.find_all('option'))
print('Nova odezva: ')
print(s2.find_all('option'))
data = s2.find_all('option')

if len(data) == 0:
  print(s2.text)

print("Setting SPORT...")
#set Sport
payload = urllib.parse.urlencode({
    'ctl00$ToolkitScriptManager' : 'ctl00$workspace$upResGridTools|ctl00$workspace$ddlLocality',
    'ctl00_ToolkitScriptManager_HiddenField' : ';;AjaxControlToolkit, Version=3.5.7.123, Culture=neutral, PublicKeyToken=28f01b0e84b6d53e:en-US:5214fb5a-fe22-4e6b-a36b-906c0237d796:de1feab2:f9cec9bc:a67c2700:f2c8e708:720a52bf:589eaa30:8613aea7:3202a5a2:ab09e3fe:87104b7c:be6fb298',
    '__VIEWSTATE' : '',
    'ctl00$toolboxRight$tbLoginUserName' : '',
    'ctl00$toolboxRight$tbLoginPassword' : '',
    'ctl00$workspace$ddlLocality' : '171',
    'ctl00$workspace$ddlSport' : '140', 
    '__EVENTTARGET' : 'ctl00$workspace$ddlSport',
    '__EVENTARGUMENT' : '',
    '__LASTFOCUS' : '',
    '__EVENTVALIDATION' : '/wEWGQL+raDpAgKvz6a4CALr2Kn3DQLwz4vcBwLDgoKdDAKz/tyyAgKa0KGLCQLfs/CXBgKmrai8BgLs/uXWDQLV8I58AtXwknwC9+nH/QcC1fe/oA4Cyora7wgCpc/G/wMCuIzUnwoCsfugHwKjzLuXCQKmuvzIBQK3oLnDBQLeltWgAgLitvv/BQLOu/iCCwKfvKSQCWMTWe5YbUpYCy84ueKeVCvvtcIv',
    '__ASYNCPOST' : 'true'
    })

pbinary = payload.encode('UTF-8')
req = urllib.request.Request(url, data=pbinary)
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0')
#req.add_header('Cookie', '_ga=GA1.2.1315628644.1442951353; __utma=74282507.1315628644.1442951353.1442953312.1442959139.3; __utmz=74282507.1442953312.2.2.utmcsr=hamrsport.cz|utmccn=(referral)|utmcmd=referral|utmcct=/cs/kontakty-branik/; HamrOnline$SessionId=0lpotu45dbisnw45nb3ms045; __utmc=74282507; __utmb=74282507.1.10.1442959139; __utmt=1')
req.add_header('Cookie', cookie)
#req.add_header('Connection', 'keep-alive')
#req.add_header('Cache-Control', 'max-age=0')
res = urllib.request.urlopen(req)
print('Status: ')
print(res.status)

#r2 = requests.post(url, data=payload)
h2 = res.read()
s2 = BeautifulSoup(h2)

#print(soup.find_all('option'))
print('Nova odezva: ')
print(s2.find_all('option'))
data = s2.find_all('option')

if len(data) == 0:
  print(s2.text)
