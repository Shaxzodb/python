from googletrans import Translator

#tarjima=Translator()
matin="salom hammaga"

t=Translator().translate(matin,dest="ru")
print(t)
print(t.origin)
print(t.text)