#!/usr/bin/python
import os
import json
import time


songs_file = "songs.json"
songs_directory = os.path.join(os.getcwd(), "downloads")

empty_db = {
    "now_playing": {},
    "queue": [],
    "history": [],
}

empty_record = {
    "url": "",
    "title": "",
    "author": "",
    "duration": 0,
    "video_id": "",
    "view_count": "",
    "thumbnail_url": "",
    "local_filepath": "",
}


def get_songs_db():
    """Returns entire songs db (now playing, queue and history)"""
    with open(songs_file) as f:
        complete_db = json.load(f)
    return complete_db


def update_songs_db(songs_db):
    """Update songs db with given content"""
    with open(songs_file, 'w') as f:
        json.dump(songs_db, f, indent=4)
    return True


def queue_song(song):
    """Queue given song"""
    songs_db = get_songs_db()
    songs_db["queue"].append(song)
    return update_songs_db(songs_db)


def get_next_song():
    """Get next song from queue"""
    songs_db = get_songs_db()
    if songs_db["queue"]:
        next_song = songs_db["queue"].pop(0)
        update_songs_db(songs_db)
        return next_song
    else:
        return None


def add_song_to_history(song):
    """Add given song to db history"""
    songs_db = get_songs_db()
    songs_db["history"].append(song)
    update_songs_db(songs_db)


def update_now_playing(song):
    """Add given song as now playing"""
    songs_db = get_songs_db()
    song['start_time'] = time.time()
    songs_db["now_playing"] = song
    return update_songs_db(songs_db)


def backup_songs_db():
    """Backup current songs db"""
    with open(songs_file+'.bkp', 'w') as f:
        json.dump(get_songs_db(), f)
    return True


def flush_db():
    """Clears everything (now playing, queue and history)"""
    backup_songs_db()
    update_songs_db(empty_db)
