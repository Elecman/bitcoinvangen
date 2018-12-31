from multiprocessing import Process, Value
from ctypes import c_bool
from time import time, sleep
import sys
from bit import Key

def startGenerating(name, caseSens, thread, running):
    timestamp = int(time())
    rate = times = 0

    while True:
        if not running.value:
            sys.exit()

        if int(time()) == timestamp + 1:
            timestamp += 1
            if times < 10: times += 0 
            if times == 10: print(f'Thread {thread} is generating ~{rate} addresses per second.')
            times += 1
            rate = 0

        rate += 1
        
        key = Key()
        address = key.address

        if (not caseSens and address[1:len(name) + 1].lower() == name.lower()) or (caseSens and address[1:len(name) + 1] == name):
            privkey = key.to_wif()
            running.value = False
            print('-'*100)
            print(f'''\nAdress successfully generated!\n\nAddress: {address}\nPrivate key: {privkey}\n''')
            print('-'*100)
            print('\nThe private key gives total access to your coins, so NEVER share it with anyone.')
            print("Store the private key in a safe place IMMEDIATELY.\n\nThanks for using keepler's VanGen.\nYou can contribute to this project at github.com/Keepler/bitcoinvangen")
            
if __name__ == '__main__':
    print("\nWelcome to keepler's Bitcoin VanGen\n\nThe name can't contain upper case O, lower case L, upper case i, digit zero, symbols or more than 32 characters.")

    while True:
        name = str(input('Input a name (the longer the name, the longer it takes): '))
        valid = True

        for x in name:
            if x not in 'abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ123456789' or len(name) > 32:
                valid = False
                print('Invalid name.')
            else:
                break
                
        if valid: break

    while True:
        caseSens = str(input('Case sensitive? (takes longer) (y/n) '))
        if caseSens.lower() == 'y':
            caseSens = True
            break
        elif caseSens.lower() == 'n':
            caseSens = False
            break
        else:
            print('Your answer must be "y" or "n".')

    while True:
        try:
            threads = int(input('How many CPU threads do you want to use? '))
            break
        except:
            print('It must be a number.')

    print("\nIt's highly recommended turning your internet connection off during this process.\nGenerating, it may take a long time...\n")
    
    running = Value(c_bool, True)
    processes = []
    for x in range(0, threads):
        processes.append(Process(target=startGenerating, args=(name, caseSens, x, running,)))
        
    for x in processes:
        x.start()
