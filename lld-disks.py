#!/usr/bin/python

import json
import subprocess

if __name__ == '__main__':
    output = subprocess.check_output("/bin/ls /dev/sd*", shell=True)
    data = list()
    for line in output.split("\n"):
        if line:
	    data.append({"{#DEVICE}": line, "{#DEVICENAME}": line.replace("/dev/", "")})

    print(json.dumps({"data": data}))
