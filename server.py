#!/usr/bin/python
import json
import subprocess
from flask import Flask, render_template, request, redirect, url_for
import player


app = Flask(__name__)


@app.route('/')
def index():
    songs_db = player.get_songs_db()
    return render_template('index.html', songs_db=songs_db)


@app.route('/get_song_info', methods=['GET', 'POST'])
def get_song_info():
    if request.method == 'GET':
        return render_template('get_song_info.html')
    elif request.method == 'POST':
        url = request.form['url']
        return redirect(url_for('add_song'))


@app.route('/add_song', methods=['GET', 'POST'])
def add_song():
    if request.method == 'GET':
        return render_template('add_song.html')
    elif request.method == 'POST':
        song = {key:request.form[key] for key in player.empty_record.keys()}
        player.queue_song(song)
        return redirect(url_for('index'))


@app.route('/history')
def history():
    songs_history = player.get_songs_db()['history']
    return render_template('history.html', locals())


if __name__ == '__main__':
    if not raw_input("Clear data from old queue? (Y/n) - ").lower().startswith('n'):
        player.flush_db()
    app.run(debug=True, host='0.0.0.0')
