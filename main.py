import os
import domaincrackee
import time


#colors
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'
CHOICE1 = ['1','2','3','4']
CHOICE2 = ['1','2','3', '0']
NAVI = ['b', 'q']


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def banner():
    clear()
    print(('''{}
        ████████╗ ██████╗  ██████╗ ██╗     ██████╗  ██████╗ ██╗  ██╗ by Oskar
        ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔══██╗██╔═══██╗╚██╗██╔╝
           ██║   ██║   ██║██║   ██║██║     ██████╔╝██║   ██║ ╚███╔╝ 
           ██║   ██║   ██║██║   ██║██║     ██╔══██╗██║   ██║ ██╔██╗ 
           ██║   ╚██████╔╝╚██████╔╝███████╗██████╔╝╚██████╔╝██╔╝ ██╗
   v.0.1   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝

         {}''').format(RED, END))

def main():
    while True:
        banner()

        print('''
        [1] {}InstagramAccs{}        [2] {}subDomainSpoof{}
        [3] {}ProxyGenerator{}       [4] {}ProxyTester{}
        
        
        {}You can type anytime b for main menu and q for quit.{}
        '''.format(BLUE,END,BLUE,END,BLUE,END,BLUE,END,YELLOW,END)
        )
        EINGABE = input('{}Type your choice >> {}'.format(RED,END))
        if EINGABE in CHOICE1 or EINGABE in NAVI:
            if EINGABE == '1':
                pass
            if EINGABE == '2':
                DOMAINSPOOF()
            if EINGABE == '3':
                PROXYGEN()
            if EINGABE == '4':
                PROXYCHECK()
            if EINGABE == 'b':
                go_back()
            if EINGABE == 'q':
                close()
        else:
            pass

def DOMAINSPOOF():
    CODES = []
    clear()
    banner()
    print('''
                [0] {}If you want to use Normal Proxys{}
                [1] {}If you want to use SocksAuth Proxys{}
                [2] {}If you want to use NormalAuth Proxys{}
                [3] {}If you want to use no Proxys{}{}(only for testing){}
                '''.format(BLUE, END, BLUE, END, BLUE, END, BLUE, END, YELLOW, END))
    TYPE = input('{}Type your choice >> {}'.format(RED, END))
    clear()
    banner()
    WORDL = input('{}Type in the name of your wordlist(MUST BE IN PATH ~/Wordlists/)\n if you dont have one type 0 >> {}'.format(RED,END))
    clear()
    banner()
    URL = input('{}Type in the URL >> {}'.format(RED,END))
    for code in input('{}Write the CODEs you want to accept(zb. 200 301 404) >> {}'.format(RED,END)).split():
        CODES.append(int(code))
    #TODO this input



def PROXYCHECK():
    clear()
    banner()
    f = input("{}Write the filename with the proxys >> {}".format(RED,END))
    if f.lower() == 'q':
        close()
    if f.lower() == 'b':
        go_back()
    wpro = domaincrackee.connect_test(f)
    clear()
    banner()
    eingabe = input('{}Do you want to write the working Proxys in a new file? y/n >> {}'.format(RED,END))
    if eingabe.lower() == 'y':
        name = input('{}Filname (DONT FORGET .txt)>>{}'.format(RED,END))
        with open(name, 'a') as FILE:
            for prox in wpro:
                FILE.write(str(prox) + '\n')
            FILE.flush()
            FILE.close()
        print('{}Done.{}'.format(RED,END))
        go_main()
    if eingabe.lower() == 'b':
        go_back()
    if eingabe.lower() == 'q':
        close()

    go_main()

def PROXYGEN():
    clear()
    banner()
    proxlist = domaincrackee.get_Proxy()
    eingabe = input("{}Do you want to safe the Proxys? y/n >> {}".format(RED,END))
    if eingabe.lower() == 'y':
        clear()
        banner()
        fname = input("{}Type in the filename >> {}".format(RED,END))
        with open(fname + '.txt', 'a') as f:
            for prox in proxlist:
                f.write(str(prox) + '\n')
            f.flush()
            f.close()
        print('{}Proxylist is written in {}{}'.format(BLUE,fname + '.txt',END))
        time.sleep(2)
        main()
    if eingabe.lower() == 'b':
        go_back()
    if eingabe.lower() == 'q':
        close()
    else:
        print('{}Going back to main menu..{}'.format(BLUE,END))
        time.sleep(2)
        main()

def go_back():
    main()

def close():
    print("{}THANKS FOR USING HUNTER{}".format(RED,END))
    exit()
def go_main():
    print('{}Going back to main menu..{}'.format(BLUE, END))
    time.sleep(2)
    main()


if __name__ == '__main__':
    DOMAINSPOOF()