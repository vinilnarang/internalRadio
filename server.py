#!/usr/bin/python
import json
import time
import subprocess
from flask import Flask, render_template, request, redirect, url_for
import player
import utilities
from play_songs import sleep_time


app = Flask(__name__)
DL_QUALITY = 1


@app.route('/')
def index():
    songs_db = player.get_songs_db()
    now_playing = songs_db['now_playing']
    if now_playing:
        now_playing['start_time'] = time.ctime(now_playing['start_time'])
    songs_queued = songs_db['queue']
    return render_template('index.html', now_playing=now_playing, songs_queued=songs_queued)


@app.route('/get_song_info', methods=['GET', 'POST'])
def get_song_info():
    if request.method == 'GET':
        return render_template('get_song_info.html')
    elif request.method == 'POST':
        url = request.form['url']
        song = utilities.get_song_info(
            url, player.songs_directory, DL_QUALITY
        )
        song_json = json.dumps(song)
        return render_template('add_song.html', song=song, song_json=song_json)


@app.route('/add_song', methods=['POST'])
def add_song():
    if request.method == 'POST':
        song = json.loads(request.form['song_json'])
        local_filepath = utilities.download_song(
            song['url'], player.songs_directory, DL_QUALITY
        )
        song['local_filepath'] = local_filepath
        player.queue_song(song)
        time.sleep(sleep_time+0.1)
        return redirect(url_for('index'))


@app.route('/history')
def history():
    songs_history = player.get_songs_db()['history']
    return render_template('history.html', songs_history=songs_history)


if __name__ == '__main__':
    player.flush_db() # also backs up current one
    app.run(debug=True, host='0.0.0.0')
