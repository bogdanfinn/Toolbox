from itertools import combinations_with_replacement
from requests import get, status_codes
import sys

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', \
                                                '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def namewithi(name, lencomb):
    proxies = {
        "http" : "http://209.250.234.89:8080",
        "https": "https://209.250.234.89:8080"

    }
    work = {}
    biog = {}
    l = []
    f = open('allinstaacc.txt', 'a')
    for c in name:
        l.append(c)
    alpha = list('abcdefghijklmnopqrstuvwxyz123456789_.')

    accs = list(combinations_with_replacement(alpha, lencomb))
    for i in range(len(accs)):
        comb = "".join(accs[i])
        try:
            print("{}searching one acc..{}".format(YELLOW,END))
            r = get('https://www.instagram.com/' + str(name) + str(comb) + '/')
            if r.status_code == 200:
                work[name + comb] = 'https://www.instagram.com/' + str(name) + str(comb) + '/'
                print("{}found{}".format(GREEN,END))
                s = r.text.split('biography":')
                bio = s[1].split('blocked_by_viewer')
                biog[name + comb] = bio[0]
                f.write("\n" + str(name+comb) + ":" + str(work[name+comb]) + ":" + str(biog[name+comb]))
            else:
                pass
        except:
            pass
    f.flush()
    f.close()
    return work, biog




if __name__ == '__main__':
    a,b = namewithi('oskar', 4)
    print(a)
    print(b)






