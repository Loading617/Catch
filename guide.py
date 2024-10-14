import epg guide
from epg guide

def main():
    # Create an EPG guide object
    epg = EPGGuide()

    # Set the source of the EPG data
    epg.set_source("epg_guide.xml")
    
    # Load the EPG data
    epg.load()
    
    # Search for events by title
    search_result = epg.search_by_title("Game of Thrones")
    for event in search_result:
        print(f"Title: {event.title}")
        print(f"Start time: {event.start_time}")
        print(f"End time: {event.end_time}")
        print(f"Description: {event.description}")
        print("---")