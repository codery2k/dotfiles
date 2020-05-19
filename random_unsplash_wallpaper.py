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
        os_arch="macos"
    # TODO replace expr with python processing of uname command
    elif (uname_output.stdout.strip()=="Linux"):
        os_arch="linux"
    return os_arch

def get_display_resolution(os_arch):
    if(os_arch=="macos"):
        display_resolution=MACOS_DISPLAY_RESOLUTION
    elif(os_arch=="linux"):
        display_resolution=LINUX_DISPLAY_RESOLUTION
    return display_resolution

def download_image(display_resolution):
    random_int=random.randrange(10000)
    download_url=UNSPLASH_SOURCE_API_URL+display_resolution+"?"+SEARCH_STRING+"/"+str(random_int)
    # print(download_url)
    response=requests.get(download_url)
    if (response.status_code==requests.codes.ok):
        redirect_url=response.url
        filename=redirect_url.replace(UNSPLASH_IMAGE_URL,'').split('?')[0]+".jpg"
        with open(WALLPAPER_DIR+"/"+filename, 'wb') as f:
            f.write(response.content)
    else:
        print("Wallpaper not downloaded. Request to unsplash returned with status code "+str(response.status_code))
    return filename

def set_wallpaper(filename, os_arch):
    if(os_arch=="macos"):
        set_wallpaper_for_macos(filename)
    elif(os_arch=="linux"):
        set_wallpaper_for_linux(filename)

def set_wallpaper_for_macos(filename):
    applescript="""osascript -e \"tell application  \\"System Events\\" to set picture of every desktop to \\\"""" +WALLPAPER_DIR+"/"+filename+ """\\"  \" """
    subprocess.run(applescript, shell=True)
    subprocess.run("killall Dock", shell=True)

def set_wallpaper_for_linux(filename):
    script="""gsettings set org.gnome.desktop.background picture-uri file://"""+WALLPAPER_DIR+"/"+filename
    subprocess.run(script, shell=True)

if __name__ == "__main__":
    os_arch=get_os()
    # print(os)
    display_resolution=get_display_resolution(os_arch)
    # print(display_resolution)
    filename=download_image(display_resolution)
    set_wallpaper(filename, os_arch)
