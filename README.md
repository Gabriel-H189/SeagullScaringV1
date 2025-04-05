# Seagull Scaring V1
By Gabriel Alonso-Holt.

A seagull scaring program with CLI interface written in Python.

The days of having me run around scaring seagulls manually are over!
With Seagull Scaring, you can just start the program, choose a time to scare seagulls for, and relax as the seagulls fly away when you want.

**Before you proceed, sound effects are not included!**

Recommended settings: 2700 seconds (timer), 60 seconds (min time), 300 seconds (max time), seagull (sound).

### About this project
Seagull Scaring was created to stop the biggest problem plaguing my school since I can’t remember when. 
It has been tested to have a 98% success rate against seagulls (or shall I say gulls) of all shapes and sizes! 
The recommended settings are meant to be used during 1 lunchtime.

### Install instructions
1. Unzip the program folder.
2. Set up the virtual environment and install dependencies. (see below)
3. Copy a `media.zip` to the program folder, then unzip it with your program of choice.

### Installing dependencies
1. Run this command to create a virtual environment: `python -m venv .venv`
2. Activate the environment: `.venv\Scripts\activate.bat`
3. Install dependencies: `pip install -r requirements.txt`
4. Run program: `python main.py`

### Config file documentation
In the program directory, there is a file called `ss_config.ini`.

You may edit this file as you desire.

**All settings must go in the [main] section.**

Valid settings: 

`scaring_time (int)`: How long to run the program for.

`min_time (int)`: Minimum time to wait.

`max_time (int)`: Maximum time to wait.

`default_volume (int)`: Default volume from 0-100.

`default_sound (str)`: Seagull sound to use. Valid options: seagull, sad seagull, angry seagull, confused seagull, disgust seagull, robot seagull, alarm seagull, Seagull 2, sea gull.

`autostart (str)`: Enable/disable autostart feature. Valid options: yes/no.

`autostart_delay (int)`: Delay seconds for the autostart feature. Not working as of 17/02/2025.

`use_this_config (str)`: Whether or not to use the config file. Valid options: yes/no.

`ask_log_file (str)`: Whether or not to ask to save the results to a log file. Valid options: yes/no.
