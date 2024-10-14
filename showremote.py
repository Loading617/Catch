import show remote

# Create a show remote object

remote = show remote.ShowRemote()

# Set show name

remote.set_show_name("Game of Thrones")

# Add episodes

remote.add_episode("Episode 1", "Season 1", "1/1/2020")
remote.add_episode("Episode 2", "Season 1", "2/1/2020")
remote.add_episode("Episode 3", "Season 1", "3/1/2020")

remote.add_episode("Episode 4", "Season 2", "4/1/2020")

# Get episodes

episodes = remote.get_episodes()

for episode in episodes:
    print(f"Title: {episode['title']}, Season: {episode['season']}, Airdate: {episode['airdate']}")

    # Mark an episode as watched
    
    remote.mark_episode_as_watched(episode['title'])
    
    # Get watched episodes
    
    watched_episodes = remote.get_watched_episodes()
    
    for watched_episode in watched_episodes:
        print(f"Watched: {watched_episode['title']}")

        # Delete an episode
        
        remote.delete_episode(watched_episode['title'])

        # Get episodes after deletion
        
        remaining_episodes = remote.get_episodes()
        
        for remaining_episode in remaining_episodes:
            print(f"Title: {remaining_episode['title']}, Season: {remaining_episode['season']}, Airdate: {remaining_episode['airdate']}")