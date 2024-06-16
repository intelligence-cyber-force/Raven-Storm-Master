#!/usr/bin/python3

# Password protection
import sys
import getpass
import os
from datetime import datetime, timedelta

# Password check
password = "Neuclear@"
attempt = getpass.getpass("Enter the password: ")

if attempt != password:
    print("Contact by ICF")
    sys.exit(1)

# Trial period check
trial_file = 'trial_start.txt'

# Check if the trial start file exists
if os.path.exists(trial_file):
    with open(trial_file, 'r') as file:
        start_date = datetime.strptime(file.read().strip(), '%Y-%m-%d %H:%M:%S')
else:
    # Create the trial start file with the current date and time
    start_date = datetime.now()
    with open(trial_file, 'w') as file:
        file.write(start_date.strftime('%Y-%m-%d %H:%M:%S'))

# Calculate the end date of the trial (1 day later)
end_date = start_date + timedelta(days=1)

# Check if the trial period has expired
if datetime.now() > end_date:
    print("Are you want to get Lifetime? So Contact ICF!")
    sys.exit(1)  # Exit the script

# Rest of the script

# 2024
# The Raven-Storm Toolkit was programmed and developed by ICF.
# The Raven-Storm Toolkit is published under the MIT Licence.
# The Raven-Storm Toolkit is based on the CLIF-Framework.
# The CLIF-Framework is programmed and developed by ICF.
# The CLIF-Framework is published under the MIT Licence.

# This script is a shortcut for everyone who does not want to install Raven-Storm to the bin path.

from importlib import import_module
from sys import path

path.insert(1, "./Raven-Storm/")
main = import_module("Raven-Storm.main")

main.run()
