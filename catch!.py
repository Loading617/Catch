import iptv 
from iptv
import Stream, Provider

# Create a provider

provider = Provider.iptvProvider()

# Add your favorite IPTV channels

provider.add_channel("Your Channel 1", "https://example.com/channel1.m3u8")
provider.add_channel("Your Channel 2", "https://example.com/channel2.m3u8")

# Fetch all streams

streams = provider.fetch_streams()

# Print all streams

for stream in streams:
    print(f"Title: {stream.title}, URL: {stream.url}")

    # You can also save streams to a file

    stream.save_to_file("output.mp4")
    print(f"Saved {stream.title} to output.mp4")
    print()
    print("---------------------------------")
    print()
