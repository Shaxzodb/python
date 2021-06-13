#pip install pytube Urnatish kerak
from pytube import YouTube
from pprint import pprint


myVideo=YouTube("https://youtu.be/ZiLa_O8BQX0")

print('**********Video Nomi***********')
print("Video Nomi:"+myVideo.title)

print("\n")

print('**********Video Rasmi manzili internetdagi***********')
print(myVideo.thumbnail_url)

print("\n")

print('**********Video Malumotlari***********')
pprint(myVideo.streams.all)
print("\n")
print('**********Video Yuklab Olish***********')


# video sifatini berish 
# my=myVideo.streams.get_by_resolution('720p')
my=myVideo.streams.first()
print(my)

print("\n")
my.download()
# my.download("output_path='C:/'")

 
    
print('video yuklandi...')