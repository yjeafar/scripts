#!/usr/bin/python3
import requests
from PIL import Image
from io import BytesIO
import shutil, os

path = os.path.join('/home/mayter/Pictures/Wallpapers/')
collection = 1262111, 225 # id of collections
count = 5

def linkFetch():
    url = f"https://api.unsplash.com/photos/random?client_id=*****={collection}&count={count}"

    response = requests.get(url)
    pictures=[]
    data = response.json()
    for i in data:
        pictures.append(i["urls"]["raw"]) # Adds the url for each image to the list
    return pictures

def resize(): # Resizes all images in folder
    dirs = os.listdir(path)
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((4500,3000), Image.ANTIALIAS)
            imResize.save(f + 'resized.jpg', 'JPEG', quality=90)

def downloadPictures():
    img_url = linkFetch()
    for value in img_url: # Loop through each item in list and get the image
        response = requests.get(value)
        filename = (value.split('/')[-1]) + '.jpg' # Make the name more readable, adds .jpg extension at the end of it
        if response.status_code == 200:
            with open(os.path.join(path,filename),'wb') as f:
                response.raw.decode_content = True
                shutil.copyfileobj(BytesIO(response.content),f) # Downloads content to path above
    resize()

downloadPictures()
