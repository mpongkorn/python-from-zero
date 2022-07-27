# temperature.py
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def writetocsv(data):
	date = datetime.now().strftime('%Y-%m-%d')
	with open('data-temperature-{}.csv'.format(date), 'a', newline='',encoding='utf-8') as file:
		filewriter = csv.writer(file)
		filewriter.writerow(data)

alldata = {}

def checktemp(city_id):
	url = 'http://www.tmd.go.th/province.php?id='+str(city_id)

	webopen = urlopen(url) #เปิดเว็บโดยไม่ต้องเปิด browser
	html_page = webopen.read() #อ่านข้อมูลในเว็บ
	webopen.close() #ปิดเว็บ

	data = BeautifulSoup(html_page,'html.parser') #แปลงโค้ดให้ bs4 ช่วยแปล

	temp_web = data.find('td',{'class':'strokeme'})
	title_web = data.find('span',{'class':'title'})
	date_web = data.find('td', {'class':'PRH'})

	try:
		location = title_web.text.strip() # .strip() เป็นการตัด space ออก
		temperature = temp_web.text #ตัดอันอื่นที่ไม่เอาออก เอาแค่ text ที่เราสนใจ
		date = date_web.text.strip()
		print(city_id, 'วันที่ '+date, 'จังหวัด'+location, 'อุณหภูมิ '+temperature)
		alldata[location] = temperature
	except:
		print(city_id, 'ไม่พบข้อมูลอุณหภูมิของจังหวัด'+str(location))

for i in range(1,82):
	checktemp(i)

#print(alldata['สงขลา'])

for k,v in alldata.items():
	data = [k,v]
	writetocsv(data)

print('saved')