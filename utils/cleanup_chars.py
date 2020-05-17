ch = 'Õ'

import os

rootDir = '.'
for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        if ".txt" in fname:
            text = open(f'{dirName}/{fname}', encoding="Latin-1").read()

            error = False
            text = text.replace(chr(133), "...").replace(chr(145), "'").replace(chr(146), "'").replace(chr(226)+chr(128)+chr(147), "-").replace(chr(147), "'").replace(chr(148), "'").replace(chr(150), "-").replace(chr(208), '--').replace(chr(210), '"').replace(chr(211), '"').replace(chr(212), "'").replace(chr(213), "'").replace(chr(226)+chr(128)+chr(153), "'").replace(chr(226)+chr(128)+chr(156), "'").replace(chr(226)+chr(128)+chr(157), "'")

            for ch in text:
                if ord(ch) > 127:
                # if ord(ch) in [210, 211]:
                    error = True
                    print(ch, ord(ch))

            if error:
                print('=====')
                print(text)
                print(text.encode('utf-8'))

            open(f'{dirName}/{fname}', 'w').write(text)
