import pyautogui as pya
pya.PAUSE = .5
import os

######PROTOTYPES#########
'''
sender = str(input('From: '))
recipients = list(input('To: '))
subject = str(input('Subject: '))
message = str(input('Message: '))
'''
app = pya.confirm(text='App of Choice',buttons=['Messages','Mail'])
sendername = pya.prompt('Your Name')
recipientname = pya.prompt("Recipient's Name")
recipient = pya.confirm(text="Choose One",buttons=["Recipient's Contact / # / Email","SKIP (Same as contact name)"])
if recipient == "SKIP (Same as contact name)":
    recipient = recipientname
elif recipient == "Recipient's Contact / # / Email":
    recipient = pya.prompt("Recipient's Contact / # / Email")
subject = pya.prompt('Subject')
message = pya.prompt('Message')
pya.sleep(1)

def hot_key(a1,a2,a3=''):
    if a3 == '':
        pya.sleep(.3)
        pya.keyDown(a1)
        pya.keyDown(a2)
        pya.sleep(.3)
        pya.keyUp(a1)
        pya.keyUp(a2)
        pya.sleep(.3)
    elif a3 != '':
        pya.sleep(.3)
        pya.keyDown(a1)
        pya.keyDown(a2)
        pya.keyDown(a3)
        pya.sleep(.3)
        pya.keyUp(a1)
        pya.keyUp(a2)
        pya.keyUp(a3)
        pya.sleep(.3)


############## SENDING FOR MSG APPS #############
##################### CODE ######################

os.system(f"open /System/Applications/{app}.app")
pya.sleep(1)

if app == 'Messages':
    hot_key('command','n')
    print('hotkey worked')
    pya.write(recipient)
    pya.sleep(1)
    pya.press('Tab')
    pya.sleep(.3)
    pya.write(subject)
    hot_key('Shift','Enter')
    pya.sleep(.5)
    hot_key('Shift','Enter')
    pya.write(recipientname+',')
    hot_key('Shift','Enter')
    pya.write(message)
    hot_key('Shift','Enter')
    hot_key('Shift','Enter')
    pya.write('From '+sendername)
    pya.sleep(.1)
    pya.press('Enter')

elif app == 'Mail':
    hot_key('command','n')
    print('hotkey worked')
    pya.write(recipient)
    pya.sleep(1)
    pya.press('Tab')
    pya.press('Tab')
    pya.sleep(.1)
    pya.write(subject)
    pya.press('Tab')
    pya.write(recipientname+',')
    pya.press('Enter')
    pya.press('Enter')
    pya.press('Tab')
    pya.write(message)
    pya.sleep(.1)
    pya.press('Enter')
    pya.press('Enter')
    pya.write('From '+sendername)
    hot_key('command','Shift','d')

