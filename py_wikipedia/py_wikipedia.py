import wikipedia
from googletrans import Translator

surov=wikipedia.search('python')
# obekt qaytaradi
print(wikipedia.page(surov))
# lest qaytaradi
print(wikipedia.search(surov))
# surov haqidagi malumot qaytaradi
print(wikipedia.summary(surov[0]))
# malumot=wikipedia.summary(surov[0])
# tarjima=Translator().translate(malumot,dest='uz')
# print(tarjima.text)