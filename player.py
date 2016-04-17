#!/usr/bin/python
import json
import subprocess
from pytube import YouTube
from pprint import pformat, pprint


songs_file = "songs.json"

empty_db = {
    "now_playing": {},
    "queue": [],
    "history": [],
}

empty_record = {
    "url": "",
    "title": "",
    "duration": 0,
    "author": "",
    "view_count": "",
    "thumbnail_url": "",
}


def get_songs_db():
    """Returns entire songs db (now playing, queue and history)"""
    with open(songs_file) as f:
        complete_db = json.load(f)
    return complete_db


def update_songs_db(songs_db):
    """Update songs db with given content"""
    with open(songs_file) as f:
        json.dump(songs_db, f)
    return True


def queue_song(song):
    """Queue given song"""
    songs_db = get_songs_db()
    songs_db["queue"].append(song)
    return update_songs_db(songs_db)


def get_next_song(song):
    """Get next song from queue"""
    songs_db = get_songs_db()
    if songs_db["queue"]:
        next_song = songs_db["queue"].pop(0)
        update_songs_db(songs_db)
        return next_song
    else:
        return None


def update_now_playing(song):
    """Add given song as now playing"""
    songs_db = get_songs_db()
    song['start_time'] = time.time()
    songs_db["now_playing"] = song
    return update_songs_db(songs_db)


def is_now_playing_finished():
    """Check if now playing song has finished playing"""
    song = get_songs_db()["now_playing"]
    if not song:
        return False
    else:
        if time.time() - song["start_time"] > song["duration"]:
            return True
        else:
            return False


def flush_db():
    """Clears everything (now playing, queue and history)"""
    update_songs_db(empty_db)
