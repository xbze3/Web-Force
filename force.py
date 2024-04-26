import requests
import argparse

parser = argparse.ArgumentParser(prog='python force.py', description="Web Directory Bruteforcer")

parser.add_argument("-u", "--url", type=str, required=True ,help="Target URL (https://example.com/)")
parser.add_argument("-w", "--wordlist", type=str, required=True, help="Wordlist Location")
parser.add_argument("-c", "--code", type=int, help="Desired Status Code", default=000)

args = parser.parse_args()

wordlist = open(f'{args.wordlist}', 'r')
wordlist = wordlist.readlines()

print("""
 ______ ___________  _____  _____ 
 |  ___|  _  | ___ \/  __ \|  ___|
 | |_  | | | | |_/ /| /  \/| |__  
 |  _| | | | |    / | |    |  __| 
 | |   \ \_/ / |\ \ | \__/\| |___ 
 \_|    \___/\_| \_| \____/\____/ 
 ---------------------------------""")

for entry in wordlist:
    url = f'{args.url}{entry.strip()}'

    x = requests.get(url)

    if args.code == 000:
        print(" [{}]: /{}".format(x.status_code, entry.strip()))
    
    elif x.status_code == args.code:
        print(" [{}]: /{}".format(x.status_code, entry.strip()))
