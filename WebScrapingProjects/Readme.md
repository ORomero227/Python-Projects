# WebScraping Projects

Welcome to my Web Scraping Projects repository! Here, you'll find a curated collection of my practice projects focused on web scraping. Dive into the world of data extraction as I tackle various challenges, from parsing structured information to navigating complex websites. Each project showcases efficient code and effective solutions, employing popular libraries such as BeautifulSoup and Selenium.

# Authors

- [@ORomero227](https://www.github.com/ORomero227)

# **Projects**
- [DataEntry Automation](#DataEntryAutomation)
- [Music Time Machine](#MusicTimeMachine)
- [Top100 Movies](#Top100Movies)

# Data Entry Automation

This project is a simplified replica of the Zillow platform, displaying real estate property listings. It utilizes web scraping and automation techniques to retrieve data from the original page.
It uses BeautifulSoup for web scraping and Selenium for form automation.

#### Features
- Extraction of property listing links.
- Retrieval of property prices.
- Address cleaning for presentation.

# Music Time Machine
This Python script leverages Spotipy and Beautiful Soup to automatically create a Spotify playlist based on the Billboard Hot 100 chart for a specified date. The key steps include Spotify authentication, Billboard chart data extraction, Spotify song search, and the creation/population of a new playlist on the user's account. Users input the desired year, and the script takes care of the rest.

Features
- Spotify Authentication:
    Utilizes SpotifyOAuth for authentication, requiring client ID, client secret, redirect URI, and necessary scopes.
- Billboard Chart Data Extraction:
    Fetches the Billboard Hot 100 chart for a specific date using the requests library.
    Utilizes Beautiful Soup for HTML parsing to extract song titles.
- User Interaction:
    Prompts the user to input the desired year in the format YYYY-MM-DD.
- Spotify Song Search:
    Searches for each song on Spotify using the Spotipy library.
    Queries include the track name and year to narrow down the search.
- Playlist Creation:
    Creates a new private playlist on the user's Spotify account, named after the specified year and "Billboard 100."
- Song Addition to Playlist:
    Adds songs (using their Spotify URIs) to the newly created playlist.

# Top100 Movies
This Python script utilizes the requests library and BeautifulSoup to scrape and extract movie titles from a specific URL. The example provided targets Empire Online's list of "best movies." The titles are then reversed and saved to a text file named movies.txt.

Features
- Web Scraping:
    Utilizes the requests library to fetch the HTML content of the specified URL.
    Employs BeautifulSoup for HTML parsing to extract movie titles.
- Title Extraction:
    Finds all h3 elements with the class "title" on the webpage.
    Reverses the order of movie titles for the text file.
- Output to File:
    Writes the reversed movie titles to a text file named movies.txt.

Usage
- Run the script to fetch and extract movie titles.
- The titles are saved in movies.txt in reverse order.
