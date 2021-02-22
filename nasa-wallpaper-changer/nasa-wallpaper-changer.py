#!/usr/bin/env python3

import getpass
import os
import subprocess
import time
import urllib.request as url

import schedule
from bs4 import BeautifulSoup

USER = getpass.getuser()
ROOT_URL = "https://apod.nasa.gov/apod/"
IMG_DIR = "/home/" + USER + "/Pictures/nasa-image/"
IMG_STUB = ""


def get_nasa_iotd_site():
    print("Connecting to NASA's Astronomy Picture Of The Day page...")
    file = url.urlopen(ROOT_URL + "astropix.html")
    print("Successfully connected to NASA's Astronomy Picture Of The Day page")
    site = file.read().decode("UTF-8")
    print("Successfully decoded NASA's Astronomy Picture Of The Day page")
    file.close()
    print("Closing connection...")
    return site


def extract_iotd_from_nasa_iotd_site():
    site = get_nasa_iotd_site()
    print("Parsing site...")
    parser = BeautifulSoup(site, "html.parser")
    img = parser.find("img")
    return img["src"]


def set_gnome_wallpaper(file_path_):
    subprocess.Popen(
        "DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format(
            file_path_
        ),
        shell=True,
    )


def main():
    print("Starting nasa-wallpaper-changer service...")
    image = extract_iotd_from_nasa_iotd_site()
    image_url = ROOT_URL + image
    print("Image URL: " + image_url)
    image_data = url.urlopen(image_url).read()
    try:
        os.mkdir(IMG_DIR)
    except FileExistsError:
        pass
    onlyfiles = next(os.walk(IMG_DIR))[2]
    IMG_STUB = "nasa-iotd-" + str(len(onlyfiles)) + ".jpg"
    image_disk = open(
        IMG_DIR + IMG_STUB, "bw+"
    )  # Open file in binary and overwrite mode
    image_disk.write(image_data)
    image_disk.close()
    print("Successfully written to destination directory")
    print("Attempting to set as background...")
    try:
        set_gnome_wallpaper(IMG_DIR + IMG_STUB)
        print("Successfully set as background")
    except:
        print("Failed to set as background")


if __name__ == "__main__":
    schedule.every().hour.do(main)
    while True:
        schedule.run_pending()
        time.sleep(120)
