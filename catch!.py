import iptv 

    # Load the list of channels from the specified file
    channels = iptv.load_channels("channels.txt")

    # Sort the channels by name in ascending order
    channels.sort(key=lambda x: x.name)

    # Print the list of channels
    print("Available Channels:")
    for channel in channels:
        print(f"{channel.number}. {channel.name}")
        print(f"  - URL: {channel.url}")
        print(f"  - Description: {channel.description}")
        print()
