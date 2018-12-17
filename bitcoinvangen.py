from hashlib import sha256
from numpy.random import bytes
from multiprocessing import Process
from time import time
import sys
import bitcoin

def generate(thread):
    timestamp = int(time())
    rate = times = 0

    while True:
        if int(time()) == timestamp + 1:
            timestamp += 1
            if times < 10: times += 0 
            if times == 10: print(f'Thread {thread} is generating ~{rate} wallets per second.')
            rate = 0

        rate += 1

        random_bytes = bytes(32)

        privkey = sha256(random_bytes).hexdigest()
        pubkey = bitcoin.privtopub(privkey)
        address = bitcoin.pubtoaddr(pubkey)

        if not caseSens and address[1:len(name) + 1].lower() == name.lower():
            walletData = f'''Address: {address}\nPrivate key: {privkey}'''

            with open('wallet.txt', 'w+') as file:
                file.write(walletData)
                file.close()

            print('Your vanity wallet was generated and was saved to wallet.txt.')
            sys.exit()

        if caseSens and address[1:len(name) + 1] == name:
            walletData = f'Address: {address}\nPrivate key: {privkey}'

            with open('wallet.txt', 'w+') as file:
                file.write(walletData)
                file.close()
            
            print('Your vanity wallet was generated and was saved to wallet.txt.')
            sys.exit()

if __name__ == '__main__':

    while True:
        print("The name can't contain maiuscle O, minuscle L, maiuscle i or zero, nor be more than 32 characters long.")
        name = str(input('Input a name (the longer the name be, more time it will take): '))

        if 'abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ123456789' not in name and len(name) > 32:
            print('Invalid name.')
        else:
            break

    while True:
        caseSens = str(input('Case sensitive? (takes longer) (y/n) '))

        if caseSens.lower() == 'y' or caseSens.lower() == 'n':
            break
        else:
            print('Your answer must be "y" or "n".')

    while True:
        try:
            threads = int(input('How many CPU threads do you want to use? '))
            break
        except:
            print('It must be a number.')

    print('Generating...\nIt may take a long time.')

    processes = []
    for x in range(0, threads):
        processes.append(Process(target=generate, args=(x,)))

    for x in processes:
        x.start()
