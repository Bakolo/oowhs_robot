from selenium import webdriver
from time import sleep
import sys
import time
browser = webdriver.Chrome()
#browser.get('https://shwoo.gov.taipei/shwoo/product/product00/product?AUID=570844')
link_path="URL of the stuff"
browser.get(link_path)
user_name = "your username"
user_pw = "your password"

#check already login or not
uname = browser.find_element_by_id('ACCOUNT')
if uname.is_displayed():
	#not login
	uname.send_keys(user_name)
	browser.find_element_by_id('PASSWORD').send_keys(user_pw)
	while True:
		uname = browser.find_element_by_id('ACCOUNT')
		if not uname.is_displayed():
			break
		time.sleep(1)	

#refresh button
upreload = browser.find_element_by_class_name('pd_t')
reload = upreload.find_element_by_class_name("search_btn")

print("01===count down==========")
print("Wait 12:00:00")
t = browser.find_element_by_class_name('time_end')
t_end = t.text.split("天")[0][-2:] + t.text.split("時")[0][-2:] + t.text.split("分")[0][-2:]+ t.text.split("秒")[0][-2:]
while int(t_end) == 0:
	t_end = t.text.split("天")[0][-2:] + t.text.split("時")[0][-2:] + t.text.split("分")[0][-2:]+ t.text.split("秒")[0][-2:]
	sleep(1)

t = browser.find_element_by_class_name('time_end')
while int(t_end) > 600:
	t_end = t.text.split("天")[0][-2:] + t.text.split("時")[0][-2:] + t.text.split("分")[0][-2:]+ t.text.split("秒")[0][-2:]
	print(t.text)
	time.sleep(60)

while int(t_end) > 10:
	t_end = t.text.split("天")[0][-2:] + t.text.split("時")[0][-2:] + t.text.split("分")[0][-2:]+ t.text.split("秒")[0][-2:]
	print(t.text)
	time.sleep(5)

while int(t_end) > 3:
	t_end = t.text.split("天")[0][-2:] + t.text.split("時")[0][-2:] + t.text.split("分")[0][-2:]+ t.text.split("秒")[0][-2:]
	print(t.text)
	time.sleep(1)

while int(t_end) > 1:
	time.sleep(0.25)
	t_end_tmp = time.time()
	t_end = t.text.split("天")[0][-2:] + t.text.split("時")[0][-2:] + t.text.split("分")[0][-2:]+ t.text.split("秒")[0][-2:]
	print(f"[{t_end_tmp}]---[{t.text}]---[{time.time()}]")
##expect start at 59.7
#time.sleep(0.2)

#while time.asctime().split()[3] != "11:59:59":
#	time.sleep(0.25)

print("02==go============")
print(time.time())
#while True:
#	if (time.time() * 1000) % 1000 >= 600:
#		break
#print("==============")
#print(time.time())

#click refresh
while True:
	try:
		reload.click()
		price = browser.find_element_by_id('bidprice')
		price.send_keys(price.text.split()[-1])
#price.send_keys(price.text.split()[0])


		GO = browser.find_element_by_id('bidButton')
		GO.click()
		break
	except:
		print('try again')
		pass
print("03===got it===========")
print(time.time())
print(time.asctime())
time.sleep(60)

#idx = 1
#while True:
#	price = browser.find_element_by_id('bidprice')
#	if idx == 4:
#		break
#	print("wait")
#	idx = (idx+1)%5
#	sleep(0.5)

	
