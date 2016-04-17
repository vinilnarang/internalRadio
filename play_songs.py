#!/usr/bin/python
import time
import json
import subprocess
from pprint import pprint
import player


sleep_time = 2 # in seconds


if __name__ == '__main__':
    """
    Continuously checks the songs file
    1. If no song in queue, sleep
    2. If no song is being played and at least 1 song in queue, play queued song
    """
    while True:
        if player.is_now_playing_finished():
            new_song = player.get_next_song()
            if new_song:
                player.play(new_song)

        time.sleep(sleep_time)
