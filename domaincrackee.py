import requests
from bs4 import BeautifulSoup
import threading
import time


WPROXY = []
threadsonline = []
threadsonline2 = []
WORKINGURL = []



BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', \
                                                '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'





def get_Proxy():
    PROXYS = []
    CHARLISTE = []
    r = requests.get('https://www.netzwelt.de/proxy/index.html')
    soup = BeautifulSoup(r.text, 'html.parser')
    found = str(soup.find_all('td',{'class' : 'ta-c'}))
    for i in range(len(found)):
        if found[i:i+5] == 'title':
            CHARLISTE.append('+')
            for i in found[i:i+35]:
                if not i == ' ':
                    CHARLISTE.append(i)
                else:
                    break
        else:
            pass

    for i in range(len(CHARLISTE)):
        ACCEPT = '0123456789:.'
        NOPLUS = True
        J = -1
        PROXY = ""
        if CHARLISTE[i] == '"':
            while NOPLUS:
                J += 1
                try:
                    CHARLISTE[i+J] != '+'
                except:
                    break
                if not CHARLISTE[i+J] == '+':


                    if CHARLISTE[i+J] in ACCEPT:

                        PROXY = PROXY + CHARLISTE[i+J]

                    else:
                        pass

                else:
                    PROXYS.append(PROXY)
                    NOPLUS = False
    print('{} found.'.format(len(PROXYS)))
    print(PROXYS)
    return PROXYS





def connect_test(FILE):
    PROXYS = []
    try:
        f = open(FILE, 'r')
    except:
        print("{}FILE NOT FOUND{}".format(RED,END))
        return
    text = f.readlines()
    for line in text:
        PROXYS.append(line.strip())
    for proxy in PROXYS:
         print('{}Thread starting..{}'.format(YELLOW, END))
         t = threading.Thread(target=testing(proxy))
         threadsonline.append(t)
         print('{}{} threads are running.{}'.format(BLUE,len(threadsonline + 1), END))
    for t in threadsonline:
        t.join()

    WORKINGPROXYS = WPROXY
    WPROXY.clear()
    threadsonline.clear()
    print('{}{} threads are running.{}'.format(BLUE, len(threadsonline + 1), END))
    return WORKINGPROXYS


def testing(PROXY):
    print('Start Connection Testing')
    print('{}testing {}...{}'.format(YELLOW,PROXY,END))
    proxies = {
        'http': 'http://{}'.format(PROXY),
        'https': 'http://{}'.format(PROXY),
    }
    try:
        s = requests.Session()
        s.get('https://www.google.de/', proxies=proxies)
        print('{}{} working.{}'.format(GREEN,PROXY,END))
        WPROXY.append(PROXY)
        return
    except:
        print('{}Connection failed{}'.format(RED,END))
        return


def start(PROXIES, AMP, CODES, URL, TYPE, WORDLIST = None):
    WORDS = []
    if WORDLIST != None:
        try:
            file = open('~/Wordlists/' + str(WORDLIST), 'r')
            print('{} custom Wordlist used. {}'.format(YELLOW,END))
        except:
            exit('{}Wordlist not found check your ~/Wordlists/{} path.{}'.format(RED,WORDLIST,END))
    else:
        try:
            file = open('common.txt', 'r')
            print('{}standart Wordlist used {}'.format(YELLOW,END))
        except:
            exit('{} No Wordlist {}'.format(RED,END))
    TEXT = file.readlines()
    for line in TEXT:
        WORDS.append(line.strip())
    if not TYPE == 3:
        Threadsrun = round(len(WORDS)/AMP)
        for i in range(Threadsrun):
            print('{}{} Thread starting..{}'.format(YELLOW,i,END))
            t = threading.Thread(target=attack(CODES, WORDS[(i*AMP):((i+1) * AMP)], URL, TYPE,PROXIES[i]))
            t.start()
            threadsonline2.append(t)
        for t in threadsonline2:
            t.join()
    else:
        Threadsrun = round(len(WORDS) / AMP)
        for i in range(Threadsrun):
            print('{}{} Thread starting..{}'.format(YELLOW, i, END))
            t = threading.Thread(target=attack(CODES, WORDS[(i * AMP):((i + 1) * AMP)], URL, TYPE))
            t.start()
            threadsonline2.append(t)
        for t in threadsonline2:
            t.join()

    exit('{}[FINISHED] {} URLS FOUND{}'.format(MAGENTA,len(WORKINGURL),END))








def attack(CODES, WORDS, URL, TYPE, PROXY = None):
    if TYPE == 0:
        proxies = {
            'http': 'http://{}'.format(PROXY),
            'https': 'https://{}'.format(PROXY),
        }
    elif TYPE == 1:
        PROXY = PROXY.split(':')
        proxies = {
            'http': 'socks5://{}:{}@{}:{}'.format(PROXY[0], PROXY[1], PROXY[2], PROXY[3]),
            'https': 'socks5://{}:{}@{}:{}'.format(PROXY[0], PROXY[1], PROXY[2], PROXY[3]),
        }
    elif TYPE == 2:
        PROXY = PROXY.split(':')
        proxies = {
            'http': 'http://{}:{}@{}:{}'.format(PROXY[0], PROXY[1], PROXY[2], PROXY[3]),
            'https': 'https://{}:{}@{}:{}'.format(PROXY[0], PROXY[1], PROXY[2], PROXY[3]),
        }
    elif TYPE == 3:
        PROXY = None

    for word in WORDS:
        try:
            if not PROXY == None:
                r = requests.get(str(URL) + '/' + str(word), proxies=proxies)
                if r.status_code in CODES:
                    print('{}[SUCCESS]{} with StatusCode {}{}.'.format(GREEN, str(URL) + '/' + str(word), r.status_code, END))
                    WORKINGURL.append(str(URL) + '/' + str(word))
                else:
                    pass
            else:
                r = requests.get(str(URL) + '/' + str(word))
                if r.status_code in CODES:
                    print('{}[SUCCESS]{} with StatusCode {}{}.'.format(GREEN, str(URL) + '/' + str(word), r.status_code,END))
                    WORKINGURL.append(str(URL) + '/' + str(word))
                else:
                    pass

        except:
            pass
    print('{}Wordlist {} finished.{}'.format(YELLOW, WORDS, END))



if __name__ == '__main__':
    pass

