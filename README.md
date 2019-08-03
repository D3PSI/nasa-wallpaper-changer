# nasa-wallpaper-changer
This little tool changes your Linux wallpaper to NASA's Image Of The Day

# Installing
Execute the following commands:
    
    sudo git clone https://github.com/D3PSI/nasa-wallpaper-changer.git
    sudo ./install.sh
    
And then run the tool like so (not as superuser!):

    python3 /usr/local/bin/nasa-wallpaper-changer/nasa-wallpaper-changer.py
    
And you are ready to go. The tool will run every hour, at reboots and every day at 0:00 to check, if NASA has released a new Astronomy Image Of The Day. For that purpose, it will install 3 crontabs.

# Uninstalling

To uninstall the tool execute the following:
 
    sudo rm -r /usr/local/bin/nasa-wallpaper-changer

After this, uninstall the automatically installed crontabs by typing:

    sudo crontab -e
    
and removing the following three lines:

    @reboot python3 /usr/local/bin/nasa-wallpaper-changer/nasa-wallpaper-changer.py
    @hourly python3 /usr/local/bin/nasa-wallpaper-changer/nasa-wallpaper-changer.py
    0 0 * * * python3 /usr/local/bin/nasa-wallpaper-changer/nasa-wallpaper-changer.py
    
Thank you for downloading! Feedback is always welcome, and so are ideas and contributions!
    
