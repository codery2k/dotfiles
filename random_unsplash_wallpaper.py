#!/usr/bin/env python3
import subprocess

WALLPAPER_DIR=""
UNSPLASH_SOURCE_API_URL= ""
SEARCH_STRING=""


def get_os():
    uname_output=subprocess.run("uname", capture_output=True, text=True)
    # TODO remove all occurrences of following check and set a common env var
    if(uname_output.stdout.strip()=="Darwin"):
        os="macos"
    # TODO replace expr with python processing of uname command
    # elif (subprocess.run("expr substr $(uname -s) 1 5")=="Linux"):
    #     os="linux"
    return os

def get_display_resolution():
    pass

def download_image():
    pass

def process_image():
    pass

def set_wallpaper():
    pass

if __name__ == "__main__":
    os=get_os()
    print(os)
    get_display_resolution()
    download_image()
    process_image()
    set_wallpaper()
