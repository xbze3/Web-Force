import requests
import argparse
import pyfiglet
import threading

global run
run = True

parser = argparse.ArgumentParser(prog='python force.py', description="Web Directory Bruteforcer")

parser.add_argument("-u", "--url", type=str, required=True ,help="Target URL (https://example.com/)")
parser.add_argument("-w", "--wordlist", type=str, required=True, help="Wordlist Location")
parser.add_argument("-c", "--code", type=int, help="Desired Status Code", default=000)
parser.add_argument("-e", "--extension", type=str, help="File Extension (.php)", default="null")

args = parser.parse_args()

ascii_banner = pyfiglet.figlet_format("WEB-FORCE")
print(ascii_banner)

print("=" * 60)
print(" Web-Force")
print(" by @xbze3 on GitHub")
print("-" * 60)
print(" Target URL: " + args.url + "WORDLIST")
print(" Wordlist: " + args.wordlist)
print("=" * 60)

wordlist = open(f'{args.wordlist}', 'r')
wordlist = wordlist.readlines()

wordlistSplit = len(wordlist) // 3

def thread1Normal(num, list, code, url):

    for entry in range(0, num):
        if(run):
            url = f'{url}{list[entry].strip()}'

            x = requests.get(url)

            if code == 000:
                print(" [{}]: /{}".format(x.status_code, list[entry].strip()))
            
            elif x.status_code == code:
                print(" [{}]: /{}".format(x.status_code, list[entry].strip()))
        else:
            return 0


def thread2Normal(num, list, code, url):

    for entry in range(num, num * 2):
        if(run):
            url = f'{url}{list[entry].strip()}'

            x = requests.get(url)

            if code == 000:
                print(" [{}]: /{}".format(x.status_code, list[entry].strip()))
            
            elif x.status_code == code:
                print(" [{}]: /{}".format(x.status_code, list[entry].strip()))

        else:
            return 0

def thread3Normal(num, list, code, url):

    for entry in range(num * 2, len(list)):
        if(run):
            url = f'{url}{list[entry].strip()}'

            x = requests.get(url)

            if code == 000:
                print(" [{}]: /{}".format(x.status_code, list[entry].strip()))
            
            elif x.status_code == code:
                print(" [{}]: /{}".format(x.status_code, list[entry].strip()))

        else:
            return 0

def extensionChecker(list, code, url, ext):

    for entry in range(0, len(list)):
        if(run):
            url = f'{url}{list[entry].strip()}{ext}'

            x = requests.get(url)

            if code == 000:
                print(" [{}]: /{}{}".format(x.status_code, list[entry].strip(), ext))
            
            elif x.status_code == code:
                print(" [{}]: /{}".format(x.status_code, list[entry].strip(), ext))
        else:
            return 0

if args.extension != "null":

    print(f"Extension: {args.extension}")

    thread1 = threading.Thread(target=thread1Normal, args=(wordlistSplit, wordlist, 000, args.url))
    thread2 = threading.Thread(target=thread2Normal, args=(wordlistSplit, wordlist, 000, args.url))
    thread3 = threading.Thread(target=thread3Normal, args=(wordlistSplit, wordlist, 000, args.url))
    extensionCheck = threading.Thread(target=extensionChecker, args=(wordlist, 000, args.url, args.extension))

    thread1.start() 
    thread2.start() 
    thread3.start()
    extensionCheck.start()

    try:
        input("")
    except KeyboardInterrupt:
        run = False
        thread1.join() 
        thread2.join() 
        thread3.join()
        extensionCheck.join()
        print("\n [CTRL+C] Detected | Closing Web-Force")

else:

    thread1 = threading.Thread(target=thread1Normal, daemon=True, args=(wordlistSplit, wordlist, 000, args.url))
    thread2 = threading.Thread(target=thread2Normal, daemon=True, args=(wordlistSplit, wordlist, 000, args.url))
    thread3 = threading.Thread(target=thread3Normal, daemon=True, args=(wordlistSplit, wordlist, 000, args.url))
    
    thread1.start() 
    thread2.start() 
    thread3.start()

    try:
        input("")
    except KeyboardInterrupt:
        run = False
        thread1.join() 
        thread2.join() 
        thread3.join()
        print("\n [CTRL+C] Detected | Closing Web-Force")
