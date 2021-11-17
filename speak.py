import gtts
# google module for text speak
from playsound import playsound


with open('frase.txt','r') as arquivo:
    for j in arquivo:
        speak = gtts.gTTS(j, lang='pt-br')
        speak.save('phrase.mp3')
        playsound('phrase.mp3')