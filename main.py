import requests, time, os, sys, random, json, threading
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
import socket
import socks
from keep_alive import keep_alive


def prco():

  servernord = [
    'amsterdam.nl.socks.nordhold.net', 'atlanta.us.socks.nordhold.net',
    'dallas.us.socks.nordhold.net', 'los-angeles.us.socks.nordhold.net',
    'nl.socks.nordhold.net', 'se.socks.nordhold.net',
    'stockholm.se.socks.nordhold.net', 'us.socks.nordhold.net'
  ]
  s = requests.Session()
  svrnrd = random.choice(servernord)
  prix = {
    'http': 'socks5://ratbagy037@gmail.com:Jrkazu99@' + svrnrd + ':1080',
    'https': 'socks5://ratbagy037@gmail.com:Jrkazu99@' + svrnrd + ':1080'
  }
  #prix ={'https':'socks5://zachlb74@gmail.com:Zach2002@dallas.us.socks.nordhold.net:1080'}
  software_names = [SoftwareName.CHROME.value]
  operating_systems = [OperatingSystem.WINDOWS.value]
  user_agent_rotator = UserAgent(software_names=software_names,
                                 operating_systems=operating_systems,
                                 limit=10000)
  user_agent = user_agent_rotator.get_random_user_agent()
  url = 'https://apis.adsalo.com/v2/ca/ads?client=ca-pub-gfmnzz-00000003759&slot=n70a5nhna4&ref=becafara.blogspot.com'
  head = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9,id;q=0.8",
    "Connection": "keep-alive",
    "Host": "apis.adsalo.com",
    "If-None-Match": 'W/"fb-YZn9whA5MsvCc613FfbYBYnsmJ0"',
    "Origin": "https://becafara.blogspot.com",
    "Referer": "https://becafara.blogspot.com/",
    "Sec-Fetch-Dest": "empty",
    "User-Agent": user_agent
  }
  #
  if os.name == 'nt': os.system('cls')
  else: os.system('clear')
  try:
    #print("UserAgent : ", user_agent)
    #print("IP : ",proxy)
    #,proxies={"http": 'http://'+proxy, "https": 'https://'+proxy}
    response = s.get(url, headers=head, proxies=prix).text
    stats = json.loads(response)
    print("Server Nord : ", svrnrd)
    print(stats['message'])
    print(stats['status'])

  except Exception as e:
    print(e)
    response = s.get(url, headers=head).text
    stats = json.loads(response)
    print(stats['status'])
    print("Skipping. Connnection error")
    pass
    #return prco


if __name__ == '__main__':
  keep_alive()
  while True:
    try:
      threads = []
      for i in range(50):
        tz = threading.Thread(target=prco)
        tz2 = threading.Thread(target=prco)
        tz3 = threading.Thread(target=prco)
        #threads.append(tz)
        #time.sleep(0.01)
        #for th in threads:
        tz.start()
        tz2.start()
        tz3.start()
        time.sleep(0.01)
        threads.append(tz)
        threads.append(tz2)
        threads.append(tz3)
        for th in threads:
          th.join()
          th.join()
          th.join()
          #time.sleep(5)
          th.start()
          th.start()
          th.start()
    except Exception as e:
      continue