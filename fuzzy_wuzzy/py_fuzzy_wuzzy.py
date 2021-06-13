from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# qancha foiz uxshashligini aniqlaydi
print(fuzz.ratio("salom","assalom"))

# yaqin qiymatlar limetga nechtaligi yoziladi
a=["assalom","alaykum","salomidin"]
s="salom"
m=process.extract(s,a,limit=3)
print(m)

# eng yaqin qiymat yagona
k=process.extractOne(s,a)
print(k)