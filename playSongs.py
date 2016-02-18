import subprocess
import time
import json
from pprint import pprint

while True:
    with open('songs.json', 'r') as data_file:    
        data = json.load(data_file)
        # data_file.close()

    if len(data) > 0:
        url = data[0]
        data.pop(0)
        with open('songs.json', 'w') as data_file:
            json.dump(data, data_file)
        subprocess.call("mpsyt playurl " + url, shell=True)

    time.sleep(2)
