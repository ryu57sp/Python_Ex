import shutil
import os
shutil.copy('message.txt', 'message2.txt')
os.rename('message2.text', 'message3.text')
os.remove('message3.txt')
