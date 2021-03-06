# Import the required module for text  

# to speech conversion 
# yozuvni avidio yozuvga ugirib berdigan dastur kodi
from gtts import gTTS



# This module is imported so that we can  

# play the converted audio 

import os



# The text that you want to convert to audio 

mytext = 'Salom Sanjar'



# Language in which you want to convert 
# bu tilni tanlash
language = 'ru'



# Passing the text and language to the engine,  

# here we have marked slow=False. Which tells  

# the module that the converted audio should  

# have a high speed 

myobj = gTTS(text=mytext, lang=language, slow=True)


# Saving the converted audio in a mp3 file named 

# welcome  
# avidio nomi
myobj.save("audio.mp3")

# Playing the converted file

#os.system("mpg321 welcome.mp3")