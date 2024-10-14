import show category options

def get_show_category_options():
    return ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Thriller"]

def display_show_category_options():
    options = get_show_category_options()
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

def get_user_choice():
    display_show_category_options()
    choice = input("Enter your choice (1-6): ")
    try:
        return int(choice)
    except ValueError:
        return None
    
    def get_show_category_from_choice(choice):
        options = get_show_category_options()
        if 1 <= choice <= len(options):
            return options[choice - 1]
        else:
            return None
        
        def display_search_results(shows):
            if len(shows) == 0:
                print("No shows found.")
            else:
                for i, show in enumerate(shows, start=1):
                    print(f"{i}. {show['title']}")

                    def search_shows_by_title():
                        title = input("Enter the title of the show: ")
                        shows = filter_shows_by_title(title)
                        display_search_results(shows)

                        def filter_shows_by_title(title):
                            filtered_shows = [show for show in shows if title.lower() in show['title'].lower()]
                            return filtered_shows
                        
                        def search_shows_by_category():
                            category = get_user_choice()
                            if category:
                                shows = filter_shows_by_category(category)
                                display_search_results(shows)

                                def filter_shows_by_category(category):
                                    filtered_shows = [show for show in shows if show['category'] == category]
                                    return filtered_shows
                                
                                def search_shows_by_rating():
                                     rating = input("Enter the minimum rating (0-5): ")
                                     try:
                                         rating = float(rating)
                                     except ValueError:
                                         print("Invalid rating. Please enter a number between 0 and 5.")
                                         return
                                     shows = filter_shows_by_rating(rating)
                                     display_search_results(shows)
                                     return
                                
                                     def filter_shows_by_rating(rating):
                                         filtered_shows = [show for show in shows if show['rating'] >= rating]
                                         return filtered_shows
                                     
                                     def display_show_details(show):
                                         print(f"Title: {show['title']}")
                                         print(f"Category: {show['category']}")
                                         print(f"Rating: {show['rating']}")
                                         print(f"Description: {show['description']}")

                                         def get_user_action():
                                             print("\nChoose an action:")
                                             print("1. Watch")
                                             print("2. Add to Favorites")
                                             print("3. Return to Search")
                                             choice = input("Enter your choice (1-3): ")
                                             try:
                                                 return int(choice)
                                             except ValueError:
                                                 return None
                                             
                                             def watch_show():
                                                 print("Watching...")
                                                 # Simulate watching the show
                                                 print("Show ended.")

                                                 def add_to_favorites():
                                                     print("Added to Favorites.")
                                                     # Simulate adding the show to favorites

                                                     def main():
                                                         while True:
                                                             choice = get_user_choice()
                                                             if choice == 1:
                                                             search_shows_by_title()
                                                             elif choice == 2:
                                                             search_shows_by_category()
                                                             elif choice == 3:
                                                             search_shows_by_rating()
                                                             elif choice == 4:
                                                             display_show_details(shows[0])
                                                             elif choice == 5:
                                                             watch_show()
                                                             elif choice == 6:
                                                             add_to_favorites()
                                                             elif choice == 7:
                                                             break
                                                             else:
                                                             print("Invalid choice. Please try again.")