import catch! iptv player
from catch! iptv player

class Catch!IptvPlayer:
    def __init__(self):
        self.channels = []
        self.current_channel = 0
        self.is_playing = False

    def add_channel(self, name, url):
        self.channels.append({"name": name, "url": url})
        if len(self.channels) == 1:
            self.current_channel = 0
            self.is_playing = True
            print(f"Added channel: {name}")

            self.play_stream()