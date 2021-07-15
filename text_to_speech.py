from gtts import gTTS
import os

my_text = input('Enter the text you want to hear:  ')

language = 'en'

output = gTTS(text=my_text, lang=language, slow=False)

output.save('ronnie.mp3')

os.system('start ronnie.mp3')

input('press ENTER to exit')