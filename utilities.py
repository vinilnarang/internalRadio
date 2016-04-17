#!/usr/bin/python
import os
import re
import copy
import json
from pytube import YouTube
from player import empty_record
from pprint import pformat, pprint


youtube_base_url = "https://www.youtube.com/watch?v="


def is_valid_youtube_url(url=""):
    """Validates if the given URL/video_id is a valid YouTube video URL"""
    regex = r'(http:|https:)?(\/\/)?(www\.)?(youtube.com|youtu.be)\/(watch)?(\?v=)(?P<video_id>\S+)'
    match_object = re.match(regex, url)
    if not match_object:
        return ""
    else:
        return youtube_base_url + match_object.groupdict()['video_id']


def get_song_info(given_url=""):
    """Returns song info for given YouTube url"""
    url = is_valid_youtube_url(given_url)
    yt = YouTube(url)
    raw_info = yt.get_video_data()
    if 'args' in raw_info:
        song_info = copy.copy(empty_record)
        song_info['url'] = url
        song_info['title'] = raw_info['args']['title']
        song_info['author'] = raw_info['args']['author']
        song_info['video_id'] = raw_info['args']['vid']
        song_info['duration'] = int(raw_info['args']['length_seconds'])
        song_info['view_count'] = int(raw_info['args']['view_count'])
        song_info['thumbnail_url'] = raw_info['args']['thumbnail_url']
        return song_info
    else:
        return None


def download_song(given_url="", local_dir="", quality=1):
    """
    Downloads the video song for given YouTube URL
    to the given local_dir (default os.getcwd())
    of given quality (1 to 5, with 1 being lowest & 5 highest quality)
    """
    url = is_valid_youtube_url(given_url)
    yt = YouTube(url)
    if not local_dir:
        local_dir = os.getcwd()
    filter_index = int(round(quality/5.0 * len(yt.filter()))) - 1
    video = yt.filter()[filter_index]
    local_file_name = "{0}.{1}".format(yt.filename, video.extension)
    local_file_path = os.path.join(local_dir, local_file_name)
    if not os.path.exists(local_file_path):
        video.download(local_dir)
    return local_file_path
