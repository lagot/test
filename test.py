#!/usr/bin/python
import json
import time
import RPi.GPIO as GPIO
from datetime import datetime, time as datetime_time, timedelta


print("_________________________________________________")
print("Config file:")
for deviceName in config_data:
    stateMachine[cntr] = False
    for deviceRow in config_data[deviceName]:
        devOn = datetime.strptime(deviceRow["on"],"%H:%M").time()
        devOff = datetime.strptime(deviceRow["off"],"%H:%M").time()

        stateMachine[cntr] = check(devOn,devOff)
        print(deviceName + "  On: " + str(devOn) + "  Off: " + str(devOff) + " Turn On: " + str(stateMachine[cntr]))
        if str(stateMachine[cntr]) == 'True':
            dict[deviceName] = 'True'
            break
    cntr += 1
print("_________________________________________________\n")


print("_________________________________________________")

print("Current State:")
for dnm in dict:
    if str(dict[dnm]) == "True":
        turnOnOff(dnm, False)    #False == On  True == Off
        print(dnm + ": Is On")
    else:
        turnOnOff(dnm, True)    #False == On  True == Off
print("_________________________________________________")

#endregion
