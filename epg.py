import epg 
from epg

# Create a new EPG instance

epg_instance = epg.EPG()

# Add a new channel

epg_instance.add_channel('Channel 1', 'Channel 1', 'http://example.com/channel1.m3u8')

# Add a new program

epg_instance.add_program('Channel 1', 'Program 1', '2022-01-01 10:00:00', '2022-01-01 11:00:00', 'Description of Program 1')

# Update a program

epg_instance.update_program('Channel 1', 'Program 1', '2022-01-01 10:00:00', '2022-01-01 11:00:00', 'Updated description of Program 1')

# Remove a program

epg_instance.remove_program('Channel 1', 'Program 1')

# Get all programs for a channel

programs = epg_instance.get_programs('Channel 1')

for program in programs:

    print(f'Program: {program["title"]}, Start Time: {program["start_time"]}, End Time: {program["end_time"]}')

    print(f'Description: {program["description"]}')
    print('---')

    # Get the EPG for a specific program

    epg_for_program = epg_instance.get_epg_for_program('Channel 1', program['title'])
    
    for event in epg_for_program:
        print(f'Event: {event["title"]}, Start Time: {event["start_time"]}, End Time: {event["end_time"]}')
        print(f'Description: {event["description"]}')
        print('---')

        # Get the schedule for a specific event

        schedule = epg_instance.get_schedule_for_event('Channel 1', event['title'])
        
        for session in schedule:
            print(f'Session: {session["title"]}, Start Time: {session["start_time"]}, End Time: {session["end_time"]}')
            print(f'Description: {session["description"]}')
            print('---')
            print()