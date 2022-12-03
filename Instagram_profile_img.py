from instaloader import Instaloader


L=Instaloader()

a=input('Name:')

L.download_profile(a,profile_pic_only=True)
