#!/usr/bin/python
import copy
import time
import json
import subprocess
from pprint import pprint
import player
import vlc


sleep_time = 1 # in seconds


if __name__ == '__main__':
    """
    Continuously checks the songs file
    1. If no song in queue, sleep
    2. If no song is being played and at least 1 song in queue, play queued song
    """
    last_song = None
    next_song = None
    vlc_instance = vlc.MediaPlayer()
    while True:
        if not vlc_instance.is_playing() == 1:
            if next_song:
                last_song = copy.copy(next_song)
                player.add_song_to_history(last_song)
            next_song = player.get_next_song()
            if next_song:
                player.update_now_playing(next_song)
                if vlc_instance:
                    vlc_instance.stop()
                pprint('Playing - %s'%next_song['title'])
                vlc_instance = vlc.MediaPlayer('file://%s'%next_song['local_filepath'])
                vlc_instance.play()
        time.sleep(sleep_time)
