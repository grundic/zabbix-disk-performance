#!/usr/bin/python

import json
import subprocess

if __name__ == '__main__':
    process = subprocess.Popen("cat /proc/diskstats | awk '{print $3}' | grep -v 'ram\|loop\|sr'", shell=True, stdout=subprocess.PIPE)
    output = process.communicate()[0]
    data = list()
    for line in output.split("\n"):
        if line:
            data.append({"{#DEVICE}": line, "{#DEVICENAME}": line.replace("/dev/", "")})

    print(json.dumps({"data": data}, indent=4))
