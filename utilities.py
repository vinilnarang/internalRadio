#!/usr/bin/python
import os
import re
import copy
import json
from pytube import YouTube
from player import empty_record
from pprint import pformat, pprint


youtube_base_url = "https://www.youtube.com/watch?v="
cur_dir = os.getcwd()


def get_filter_index(quality=1, len_filter=1):
    """
    Returns the pytube filter index according to the given quality rating
    (1 to 5, with 1 being lowest & 5 highest quality)
    """
    return int(round(quality/5.0 * len_filter)) - 1


def is_valid_youtube_url(url=""):
    """Validates if the given URL/video_id is a valid YouTube video URL"""
    regex = r'(http:|https:)?(\/\/)?(www\.)?(youtube.com|youtu.be)\/(watch)?(\?v=)(?P<video_id>[a-zA-Z0-9_-]+)'
    match_object = re.match(regex, url)
    if not match_object:
        return ""
    else:
        return youtube_base_url + match_object.groupdict()['video_id']


def get_song_info(given_url="", local_dir=cur_dir, quality=1):
    """Returns song info for given YouTube url"""
    url = is_valid_youtube_url(given_url)
    yt = YouTube(url)
    raw_info = yt.get_video_data()
    if 'args' in raw_info:
        song_info = copy.copy(empty_record)
        song_info['url'] = url
        song_info['title'] = raw_info['args']['title']
        song_info['author'] = raw_info['args']['author']
        try:
            song_info['video_id'] = raw_info['args']['vid']
        except KeyError:
            song_info['video_id'] = url.replace(youtube_base_url, '')
        song_info['duration'] = int(raw_info['args']['length_seconds'])
        song_info['view_count'] = int(raw_info['args']['view_count'])
        song_info['thumbnail_url'] = raw_info['args']['thumbnail_url']
        filter_index = get_filter_index(quality, len(yt.filter()))
        video = yt.filter()[filter_index]
        local_file_name = "{0}.{1}".format(yt.filename, video.extension)
        local_file_path = os.path.join(local_dir, local_file_name)
        if os.path.exists(local_file_path):
            song_info['local_file_path'] = local_file_path
        return song_info
    else:
        return None


def download_song(given_url="", local_dir=cur_dir, quality=1):
    """
    Downloads the video song for given YouTube URL
    to the given local_dir (default os.getcwd()) of given quality
    """
    url = is_valid_youtube_url(given_url)
    yt = YouTube(url)
    filter_index = get_filter_index(quality, len(yt.filter()))
    video = yt.filter()[filter_index]
    local_file_name = "{0}.{1}".format(yt.filename, video.extension)
    local_file_path = os.path.join(local_dir, local_file_name)
    if not os.path.exists(local_file_path):
        video.download(local_dir)
    return local_file_path
