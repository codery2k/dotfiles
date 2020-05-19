#!/usr/bin/env python3
import subprocess
import os
import requests
import random

WALLPAPER_DIR=os.getenv("WALLPAPER_DIR", default="$HOME/Pictures/Wallpapers")
UNSPLASH_SOURCE_API_URL= "https://source.unsplash.com/featured/"
UNSPLASH_IMAGE_URL="https://images.unsplash.com/"
SEARCH_STRING="wallpaper"
MACOS_DISPLAY_RESOLUTION="2880x1800"
LINUX_DISPLAY_RESOLUTION="1920x1080"



def get_os():
    uname_output=subprocess.run("uname", capture_output=True, text=True)
    # TODO remove all occurrences of following check and set a common env var
    if(uname_output.stdout.strip()=="Darwin"):
        os="macos"
    # TODO replace expr with python processing of uname command
    elif (uname_output.stdout.strip()=="Linux"):
        os="linux"
    return os

def get_display_resolution(os):
    if(os=="macos"):
        display_resolution=MACOS_DISPLAY_RESOLUTION
    elif(os=="linux"):
        display_resolution=LINUX_DISPLAY_RESOLUTION
    return display_resolution

def download_image(display_resolution):
    random_int=random.randrange(10000)
    download_url=UNSPLASH_SOURCE_API_URL+display_resolution+"?"+SEARCH_STRING+"/"+str(random_int)
    print(download_url)
    response=requests.get(download_url)
    redirect_url=response.url
    filename=redirect_url.replace(UNSPLASH_IMAGE_URL,'').split('?')[0]+".jpg"
    with open(WALLPAPER_DIR+"/"+filename, 'wb') as f:
        f.write(response.content)

def process_image():
    pass

def set_wallpaper():
    pass

if __name__ == "__main__":
    os=get_os()
    # print(os)
    display_resolution=get_display_resolution(os)
    # print(display_resolution)
    download_image(display_resolution)
    process_image()
    set_wallpaper()
