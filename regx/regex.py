import re
# bu modil andozaga yaqin qiymatlarni olib beradi
andoza="^s...m$"
wordl=["salom","sndam","sdam"]
for word in wordl:
    if re.match(andoza,word):
        print(True)
    else:
        print(False)