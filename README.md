# Internal Radio :D

### Steps for setting up

#### Install dependencies

    # If you don't have pip installed, then run the following command
    sudo apt-get install python-pip
    # Now install dependencies with pip
    pip install -r requirements.txt

#### Host the Flask server

    # Following helps receive requests from intranet connections
    python server.py
    # This will typically host the server at http://local_ip_address:5000

#### Playing the songs being queued

    # Following runs the vlc daemon (in a separate terminal)
    python play_songs.py
