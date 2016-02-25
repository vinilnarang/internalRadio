#!/usr/bin/python
import subprocess
import time
import json
from pprint import pprint
from .radio import songs_file

while True:
    with open(songs_file) as f:
        data = json.load(f)

    if len(data) > 0:
        url = data[0]
        data.pop(0)
        with open(songs_file, 'w') as f:
            json.dump(data, f)
        subprocess.call("mpsyt playurl " + url, shell=True)

    time.sleep(2)
