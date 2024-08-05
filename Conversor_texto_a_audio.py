from gtts import gTTs
import os

text = "Hola me llamo Baltasar y vos?"
language = "es-us"
speech = gTTs(text = text, lang = language, slow = False)

speech.save("texto.mp3")

os.system("start texto.mp3")