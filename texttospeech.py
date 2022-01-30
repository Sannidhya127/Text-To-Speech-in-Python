from gtts import gTTS

# If you don't have gtts go to the terminal and write pip install gtts
import os

# Reading the files
f = open("3.txt", "r")
x = f.read()

# Specifying language:
language = 'en'  # You can specify any language. Reffer to the gtts documentation
# simply write this down for better sound
audio = gTTS(text=x, lang=language, slow=False)

# Now save the audio file
# You can save by any name you wish
# When I play the file you won't be able to hear it as my recorder is not working but I am sure this code works
audio.save("3.wav")
os.system("3.wav")
