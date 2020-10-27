
'''
Uncomment to select target bot
'''
namer='@Litecoin_click_bot'
#namer='@Zcash_click_bot'
# namer='@BCH_clickbot'
# namer='@BitcoinClick_bot'
# namer='@Dogecoin_click_bot'

#Enter phone number 
#eg: +2348111111
phone_number=''

#Enter your Telegram Api ID and Hash
api_id = 00000#'id is an interger'
api_hash = 'hash is a string'
'''
This script depends on telethon, beautifulsoup and requests.
'''
api_id = 717425
api_hash = '322526d2c3350b1d3530de327cf08c07'



from telethon.tl.types import InputPeerUser
from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError
from time import sleep
import json,re,sys,os,dill
from datetime import datetime
from threading import Thread 
try:
   import requests
   from bs4 import BeautifulSoup
except:
   print ("\033[1;30m# \033[1;31mEither requests or beautifulsoup library not installed\n\033[1;30m# \033[1;31mTo install Please Type pip install requests and pip install bs4")
   sys.exit()

banner = "\033[0;34m YANDE\033[1;31m CREATIVE LAB\n"
total=0
win=0
fail=0
		
	

def countdown(x):
   sys.stdout.write("\r")
   sys.stdout.write("                                                               ")
   for remaining in range(x, 0, -1):
      sys.stdout.write("\r")
      sys.stdout.write("\033[1;30m#\033[1;0m{:2d} \033[1;32mseconds remaining".format(remaining))
      sys.stdout.flush()
      sleep(1)

def next(term=0):
	global client
	if term==1:
		z=input('\nQuit\nType 1 for yes\nType 0 for no\n---- ')
		
		try:
			z=int(z)
		except:
			print('\nInvalid option')
			next(1)
		if z==1:
			client.disconnect()
			sys.exit()
		elif z==0:
			return 0
		else:
			print('\nInvalid option')
			next(1)
		
	z=input('\nContinue ?\nType 1 for yes\nType 0 for no\n---- ')
	try:
		z=int(z)
	except:
		print('\nInvalid option')
		next()
	if z==1:
		return 1
	elif z==0:
		sys.exit()
	else:
		print('\nInvalid option')
		next()

def stats(win_,first=0):
   global total
   global win
   global fail
   global banner
   if win_==':':
   	return ':'
   if first==2:
      print(banner)
   if first == 0:
      total+=1
   if win_==0:
      fail+=1
   elif win_==1:
      win+=1
   
   print('\033[0;35mwins: \033[1;31m{0}\n\033[0;35mfails: \033[1;31m{2}\n\033[0;35mtotal: \033[1;31m{1}'.format(win,total,fail))#\033[0;35mfails: \033[1;31m{1}\



c = requests.Session()

if not os.path.exists("session"):
   os.makedirs("session")

os.system("clear")
stats(2,2)

ua={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"}


client = TelegramClient("session/"+phone_number, api_id, api_hash)
client.disconnect()
client.connect()



if 'check' in sys.argv:
	check=client.is_user_authorized() 
	if check==False:
		print('User not signed In')
		
	else:
		print('User is signed in')
	next()
     
if 'auth' in sys.argv:
   print('User not Authorized, initiating that now')
   sleep(2)
   try:
      client.send_code_request(phone_number)
      me = client.sign_in(phone_number, input('\n\n\n\033[1;0mEnter Your Code : '))
   except SessionPasswordNeededError:
      passw = input("\033[1;0mYour 2fa Password : ")
      me = client.start(phone_number,passw)
      next()
else:
   print('User is authorized!')

print ("\033[1;32m\nWelcome To Yande_Tbot ")

print ("\n\n\033[1;37mConnecting......!\n")


if 'cache' in sys.argv:
   lq=client.get_input_entity(namer)
   channel_username=namer
   with open('bch_id.txt','w') as fd:
      try:
         fd.write(str(lq.user_id))
         channel_id=lq.user_id
         print(type(channel_id))
      except:
         fd.write(str(lq.user_id))
         channel_id=lq.user_id
         print('I was wrong')
   with open('bch_hash.txt','w') as fg:
   	fg.write(str(lq.access_hash))
   	channel_hash=lq.access_hash
   	print(type(channel_hash))
   channel_entity = InputPeerUser(channel_id, channel_hash)
   next()
else:
   
   with open('bch_id.txt','r') as fd:
      channel_id=fd.read()
   with open('bch_hash.txt','r') as fg:
      channel_hash= fg.read()
   channel_username=namer
   channel_entity = InputPeerUser(int(channel_id), int(channel_hash))
secondchance=False
def rep():
   global api_id
   global api_hash
   global phone_number
   global channel_entity
   global client
   global channel_username
   global ua
   global c
   
   param=True
   paramt=1
   visitsite="/visit"
   firstclick=True
   global secondchance
   if secondchance==True:
   	client.disconnect()
   	client.connect()

   while True:
      
      for i in range(5000000):
         #send visit
         if firstclick!=True:
         	lastmsg=client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0)).messages[0].message
         	if "Sorry, there are no new ads available" in lastmsg or visitsite in lastmsg or 'Sorry, that task is no longer valid' in lastmsg:
         		client.send_message(entity=channel_entity,message=visitsite)
         		print('\nAds finished\nvisiting')
         		sleep(3)
         	else:
         		print('\nUsing New Ad')
         else:
         	client.send_message(entity=channel_entity,message=visitsite)
         	sleep(3)
         	
         while True:
         	if param==True:
         		print("\033[1;30m# \033[1;33mRetrieving URL")
         	
         	posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
         	out= posts.messages[0].message
         	
         	if paramt>=11:
         		paramt=2
         		param=True
         		break
         	if out==visitsite :
         		param=False
         		print('***')
         	
         		paramt+=1
         		sleep(3)
         	else:
         		param=True
         		paramt=1
         		break
         if paramt==2:
         	param=True
         	paramt=1
         	continue
         firstclick=False	
         
         #NoAds
         if posts.messages[0].message.find("Sorry, there are no new ads available") != -1:
            print('\nNo new ad....')
            stats(':')
            print('\nretrying in 5 seconds')
            countdown(5)
            print('\n')
            
         
         #Ads
         else:
            try:
               #go to site and scrape
               url = posts.messages[0].reply_markup.rows[0].buttons[0].url
               sys.stdout.write("\r")
               sys.stdout.write("\033[1;30m# \033[1;33mVisit "+url)
               sys.stdout.flush()
               id = posts.messages[0].id
               r = c.get(url, headers=ua, allow_redirects=True,timeout=15 )
               soup = BeautifulSoup(r.content,"html.parser")
               
               #GoodSearch 
               if soup.find("div",class_="g-recaptcha") is None and soup.find('div', id="headbar") is None:
                  sleep(2)
                  stale1=1
                  #######
                  print('\nGoodSearch1')
                  while stale1<=10:
                  	
                  	posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
                  	message = posts.messages[0].message
                  
                  	if "You must stay" in message or "Please stay on" in message:
                  		stale1=100
                  	else:
                  		sleep(1)
                  		
                  		stale1+=1
                  	
                  		
                  if posts.messages[0].message.find("You must stay") != -1 or posts.messages[0].message.find("Please stay on") != -1:
                     sec = re.findall( r'([\d.]*\d+)', message)
                     countdown(int(sec[0]))
                     sleep(1)
                     posts = client(GetHistoryRequest(peer=channel_entity,limit=2,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
                     messageres = posts.messages[1].message
                     sleep(2)
                     sys.stdout.write("\r\033[1;30m# \033[1;32m"+messageres+"\n")
                     stats(1)
                  else:
                     print('Bot1....I can handle this!')
                     stats(1)

               #GoodSearch
               elif soup.find('div', id="headbar") is not None:
                  nos=1
                  lenn=len(soup.find_all('div',class_="container-fluid"))
                  print('\nGoodSearch2')
                  print('post_event',lenn)
                  for dat in soup.find_all('div',class_="container-fluid"):
                     code = dat.get('data-code')
                     timer = dat.get('data-timer')
                     tokena = dat.get('data-token')
                     print(nos,' out of ',lenn)
                     countdown(int(timer))
                     r = c.post("https://dogeclick.com/reward",data={"code":code,"token":tokena}, headers=ua, timeout=15, allow_redirects=True)
                     js = json.loads(r.text)
                     sys.stdout.write("\r\033[1;30m# \033[1;32mYou earned "+js['reward']+" ZEC for visiting a site!\n")
                     stats(1)   
               
               #Captcha
               else:
                  sys.stdout.write("\r")
                  sys.stdout.write("                                                                ")
                  sys.stdout.write("\r")
                  sys.stdout.write("\033[1;30m# \033[1;31mCaptcha Detected")
                  sys.stdout.flush()
                  sleep(2)
                  client(GetBotCallbackAnswerRequest(channel_username,id,data=posts.messages[0].reply_markup.rows[1].buttons[1].data))
                  sys.stdout.write("\r\033[1;30m# \033[1;31mSkip Captcha...!       \n")
                  sleep(2)
                  stats(0)
            
            except:
               print('\nGoodSearch 3')
               sleep(3)
               stale2=1
               while stale2<=10:
               	posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
               	message = posts.messages[0].message
               	if "You must stay" in message or "Please stay on" in message:
               		stale2=100
               	else:
               		print(stale2)
               		sleep(1)
               		stale2+=1
               	
               if posts.messages[0].message.find("You must stay") != -1 or posts.messages[0].message.find("Please stay on") != -1:
                  sec = re.findall( r'([\d.]*\d+)', message)
                  countdown(int(sec[0]))
                  sleep(1)
                  posts = client(GetHistoryRequest(peer=channel_entity,limit=2,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
                  messageres = posts.messages[1].message
                  sleep(2)
                  sys.stdout.write("\r\033[1;30m# \033[1;32m"+messageres+"\n")
                  stats(1)
               else:
               	print(' Bot2......requires manual clicking!')
               	stats(0)
                  


if not 'inf' in sys.argv:
	while True:
		
		try:
			rep()
		except:
			print('Program ended abruptly\nRestarting!')
			secondchance=True
			
else:
	try:
		rep()
	except:
		print('Goodbye')