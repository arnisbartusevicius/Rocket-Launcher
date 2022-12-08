# MADE BY ARNIS
# ARNIS#9033 (DISCORD)

import os
import time
import configparser

# Read configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Get directories from configuration file
bakkesmod_exe_dir = config['PATHS']['bakkesmod_exe_dir']
rocket_league_url_dir = config['PATHS']['rocket_league_url_dir']

# Check if the directories from the configuration file exist
# If not, search for the files
if not os.path.exists(bakkesmod_exe_dir):
    # Search for Bakkesmod.exe in C:\Program Files\BakkesMod
    bakkesmod_exe = ""
    for root, dirs, files in os.walk("C:\\Program Files\\BakkesMod"):
        if "BakkesMod.exe" in files:
            bakkesmod_exe = os.path.join(root, "BakkesMod.exe")
            break
    bakkesmod_exe_dir = bakkesmod_exe

if not os.path.exists(rocket_league_url_dir):
    # Search for Rocket League®.url on the C drive
    rocket_league_url = ""
    for root, dirs, files in os.walk("C:\\"):
        if "Rocket League®.url" in files:
            rocket_league_url = os.path.join(root, "Rocket League®.url")
            break
    rocket_league_url_dir = rocket_league_url

# Save directories to configuration file
config['PATHS']['bakkesmod_exe_dir'] = bakkesmod_exe_dir
config['PATHS']['rocket_league_url_dir'] = rocket_league_url_dir
with open('config.ini', 'w') as configfile:
    config.write(configfile)

# Launch Bakkesmod.exe
if bakkesmod_exe_dir:
    os.startfile(bakkesmod_exe_dir)

# Wait 2 seconds
time.sleep(2)

# Launch Rocket League®.url
if rocket_league_url_dir:
    os.startfile(rocket_league_url_dir)
