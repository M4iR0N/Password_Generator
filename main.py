####
import random
import string
from progress.bar import IncrementalBar

def randomString(stringLength=10):
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(stringLength))
while True:
    ans = input('How long should your password be?'
            """
            16 bits
            32 bits
            64 bits
            128 bits
            256 bits
            512 bits
            """)
    if ans == '16':
    #incbar = IncrementalBar('Processing', max=100)
    #for i in range(100):
        #incbar.next()
    #incbar.finish()
        print('Your 16 Bit Password is \n', randomString(16))
        print('=======================================================')
    elif ans == '32':
        print('Your 32 Bit Password is \n', randomString(32))
        print('=======================================================')
    elif ans == '64':
        print('Your 64 Bit Password is \n', randomString(64))
        print('=======================================================')
    elif ans == '128':
        print('Your 128 Bit Password is \n', randomString(128))
        print('=======================================================')
    elif ans == '256':
        print('Your 256 Bit Password is \n', randomString(256))
        print('=======================================================')
    elif ans == '512':
        print('Your 512 Bit Password is \n', randomString(512))
        print('=======================================================')
        # Exit
        exit = input('Continue? ' '')
    elif ans != '':
        print('Incorrect input selected try again...')
        continue
    if exit == 'n':
        break
    elif exit == 'y':
        continue

randomString()
