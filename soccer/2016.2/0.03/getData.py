#sina


import xlrd
import xlwt
import urllib2
from bs4 import BeautifulSoup
import json

def getHtml(url):
    page = urllib2.urlopen(url)
    html_doc = page.read()
    html_doc=html_doc.decode('utf-8','ignore')
    return html_doc;

#xlsx
workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('sheet1')
num=0
for a in range(1,26,1):
    astr='%d' %a;
    url="http://league.aicai.com/league/scoreresult!ajaxscoreResult.htm?leagueId=23&season=2015-2016&round="+astr+"&matchType=0";
    html=getHtml(url)
    data=json.loads(html);



    for i in data['result']['matchList']:
        print i;
        print
        worksheet.write(num, 0,  i['hostRank'])
        worksheet.write(num, 1,  i['hostTeamName'])
        worksheet.write(num, 2,  i['awayRank'])
        worksheet.write(num, 3,  i['awayTeamName'])
        worksheet.write(num, 4,  i['hostHalfScore'])
        worksheet.write(num, 5,  i['awayHalfScore'])
        worksheet.write(num, 6,  i['hostScore'])
        worksheet.write(num, 7,  i['awayScore'])
        worksheet.write(num, 8,  i['matchResult'])
        worksheet.write(num, 9,  i['winOdds'])
        worksheet.write(num, 10,  i['drawOdds'])
        worksheet.write(num, 11,  i['loseOdds'])
        worksheet.write(num, 12,  i['europOddsResult'])
        num=num+1;

workbook.save('result3.xlsx')