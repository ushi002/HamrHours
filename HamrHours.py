__author__ = 'ludek'

import urllib.request
from html.parser import HTMLParser
import time
import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup

class MyParser(HTMLParser):
    #def handle_starttag(self, tag, attrs):
        #print("Encountered a start tag:", tag)
    row_of_interest = 0
    col_avail_idx = 3
    col_idx = 1
    half_hour_cnt = 0
    # select half hours:
    hh_list = []
    found_free_hour = False
    date_of_interest = 0
    available_hours = []

    def set_date(self, date):
        self.date_of_interest = date

    def load_halfhours(self, half_hours_list):
        for hh in half_hours_list:
            self.hh_list.append(int((hh-7)*2))
        # print(self.hh_list)

    def handle_starttag(self, tag, attrs):
        if tag == 'div' and self.row_of_interest == 1:
            # print(attrs)
            for hh in self.hh_list:
                if hh == self.half_hour_cnt:
                    available = attrs[0][1][-4:]
                    # print("CHECK THIS:", available)
                    if available.find("free") >= 0:
                        self.found_free_hour = True
                        self.available_hours.append(hh/2+7)
            self.half_hour_cnt += 1

            # for name, value in attrs:
            #     print("->Name, Value:", name, value)


    def handle_data(self, data):
        if data.find(self.date_of_interest) >= 0 and self.row_of_interest == 0:
            # print("Pocatek:", self.get_starttag_text())
            self.row_of_interest = 1
        elif data.find(self.date_of_interest) >= 0 and self.row_of_interest == 1:
            # print("Konec:", self.get_starttag_text())
            self.row_of_interest = 0
    #
    #     if self.row_of_interest == 1:
    #         if self.col_idx == self.col_avail_idx:
    #             print("Data:", data)
    #             self.col_idx = 1
    #         else:
    #             print("IDX:", self.col_idx, data)
    #             self.col_idx += 1




url = 'http://hodiny.hamrsport.cz/Login.aspx?r=NOTLOGGED'
req = urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0')
resp = urllib.request.urlopen(req)

cookies = resp.getheader('Set-Cookie')
sessionId = cookies[21:45]
print(sessionId)
cookie = 'HamrOnline$SessionId=' + sessionId

print("Setting LOCALITY...")
#set Locality
payload = urllib.parse.urlencode({
    'ctl00$ToolkitScriptManager' : 'ctl00$workspace$upResGridTools|ctl00$workspace$ddlLocality',
    'ctl00_ToolkitScriptManager_HiddenField': ';;AjaxControlToolkit, Version=3.5.7.123, Culture=neutral, PublicKeyToken=28f01b0e84b6d53e:en-US:5214fb5a-fe22-4e6b-a36b-906c0237d796:de1feab2:f9cec9bc:a67c2700:f2c8e708:720a52bf:589eaa30:8613aea7:3202a5a2:ab09e3fe:87104b7c:be6fb298',
    '__VIEWSTATE': '',
    'ctl00$toolboxRight$tbLoginUserName': '',
    'ctl00$toolboxRight$tbLoginPassword': '',
    'ctl00$workspace$ddlLocality': '171',
    'ctl00$workspace$ddlSport': '137',
    '__EVENTTARGET': 'ctl00$workspace$ddlLocality',
    '__EVENTARGUMENT': '',
    '__LASTFOCUS': '',
    '__EVENTVALIDATION': '/wEWGQL+raDpAgKvz6a4CALr2Kn3DQLwz4vcBwLDgoKdDAKz/tyyAgLfs+yXBgLfs/CXBgKDws6WDALims6iCAKa0KWLCQLV8I58AtXwknwC1fe/oA4Cyora7wgCpc/G/wMCuIzUnwoCsfugHwKjzLuXCQKmuvzIBQK3oLnDBQLeltWgAgLitvv/BQLOu/iCCwKfvKSQCZdk0J5TCjvCWtaJ4XnLQ+3w/3O4',
    '__ASYNCPOST': 'true'
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
s2 = BeautifulSoup(h2, 'html.parser')

#print(soup.find_all('option'))
print('Nova odezva: ')
print(s2.find_all('option'))
data = s2.find_all('option')

if len(data) == 0:
    print(s2.text)
    exit(0)

print("Setting SPORT...")
payload = urllib.parse.urlencode({
    'ctl00$ToolkitScriptManager': 'ctl00$workspace$upResGridTools|ctl00$workspace$ddlLocality',
    'ctl00_ToolkitScriptManager_HiddenField': ';;AjaxControlToolkit, Version=3.5.7.123, Culture=neutral, PublicKeyToken=28f01b0e84b6d53e:en-US:5214fb5a-fe22-4e6b-a36b-906c0237d796:de1feab2:f9cec9bc:a67c2700:f2c8e708:720a52bf:589eaa30:8613aea7:3202a5a2:ab09e3fe:87104b7c:be6fb298',
    '__VIEWSTATE': '',
    'ctl00$toolboxRight$tbLoginUserName': '',
    'ctl00$toolboxRight$tbLoginPassword': '',
    'ctl00$workspace$ddlLocality': '171',
    'ctl00$workspace$ddlSport': '140',
    '__EVENTTARGET': 'ctl00$workspace$ddlSport',
    '__EVENTARGUMENT': '',
    '__LASTFOCUS': '',
    '__EVENTVALIDATION': '/wEWGQL+raDpAgKvz6a4CALr2Kn3DQLwz4vcBwLDgoKdDAKz/tyyAgKa0KGLCQLfs/CXBgKmrai8BgLs/uXWDQLV8I58AtXwknwC9+nH/QcC1fe/oA4Cyora7wgCpc/G/wMCuIzUnwoCsfugHwKjzLuXCQKmuvzIBQK3oLnDBQLeltWgAgLitvv/BQLOu/iCCwKfvKSQCWMTWe5YbUpYCy84ueKeVCvvtcIv',
    '__ASYNCPOST': 'true'
    })

pbinary = payload.encode('UTF-8')
req = urllib.request.Request(url, data=pbinary)
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0')
#req.add_header('Cookie', '_ga=GA1.2.1315628644.1442951353; __utma=74282507.1315628644.1442951353.1442953312.1442959139.3; __utmz=74282507.1442953312.2.2.utmcsr=hamrsport.cz|utmccn=(referral)|utmcmd=referral|utmcct=/cs/kontakty-branik/; HamrOnline$SessionId=0lpotu45dbisnw45nb3ms045; __utmc=74282507; __utmb=74282507.1.10.1442959139; __utmt=1')
req.add_header('Cookie', cookie)

res = urllib.request.urlopen(req)
print('Status: ')
print(res.status)

#r2 = requests.post(url, data=payload)
h2 = res.read()
s2 = BeautifulSoup(h2, 'html.parser')

#print(soup.find_all('option'))
print('Nova odezva: ')
print(s2.find_all('option'))
data = s2.find_all('option')

if len(data) == 0:
    print(s2.text)
    exit(0)

# hledej_datum = "17.09.2015"
# hledej_hodiny = [19.5, 20, 20.5]
hledej_datum = "24.09.2015"
hledej_hodiny = [20, 20.5, 21]

for i in range(0, 3):
    # fajl = open('x.html', 'r')
    # html = fajl.read()
    html = h2
    parser = MyParser()
    parser.set_date(hledej_datum)
    parser.load_halfhours(hledej_hodiny)
    parser.feed(str(html))
    # fajl.close()

    if parser.found_free_hour:
        print("Nasli jsme volne hodiny: ")
        print(parser.available_hours)
        msg = MIMEText('Ahoj kraliku')
        msg['Subject'] ='Pokusny kralik'
        msg['From'] = 'ludek@vbox-ledora.ufa'
        msg['To'] = 'ludek.uhlir@gmail.com'
        #send the message
        try:
            s = smtplib.SMTP('mail.ufa.cas.cz')
            # s.set_debuglevel(1)
            #s.send_message(msg)
            s.quit()
        except smtplib.SMTPException:
            print("Unable to send email")
        exit(0)
    else:
        print("Bohuzel zadne volne hodiny...")
        print(parser.available_hours)

    time.sleep(1)
