# 🎵 Playlist Management System
A simple Playlist Management System built with Python. For Capstone 2 Submission.

# 👩‍💻 Project Overview
This project is a CRUD-based playlist management system that allows users to manage playlist and song records through a menu-driven program.

The system allows users to:
- View playlists & songs
- Add new playlists
- Update playlist names and descriptions
- Add songs to a playlist
- Delete playslists
- View playlist and music statistics

# ✨ Features
# 📖 Read
- View all playlists
- View songs within a selected playlist using its Playlist ID
- Display playlist details, including: Playlist ID, Name, Description
- Display song details, including: Song ID, Title, Artist, Duration, Genre

# ➕ Create
- Add a new playlist to the system
- Check for duplicate Playlist IDs
- Add a playlist name and description
- Display the updated playlist list after creation
  
# 🔄 Update
- Update an existing playlist's name or description
- Add new songs to a selected playlist
- Check whether the Playlist ID exists
- Check for duplicate Song IDs
- Display updated playlist or song information

# 🗑️ Delete
- Delete a playlist using its Playlist ID
- Confirm before deleting a playlist
- Display the updated playlist list after deletion
- Handle Playlist IDs that don't exist

# 📊 Playlist Statistics
- Display the total number of playlists & songs
- Calculate the number of songs per genre
- Identify the most popular genre based on song count
- Handle cases where no songs are available

# 🗂️ Data Structure
The playlist data is stored using **nested dictionaries**.

Each playlist record contains:

* `Playlist ID` — Primary Key
* `Playlist Name`
* `Description`
* `Songs` — A nested dictionary containing song records

Each song record contains:

* `Song ID` — Primary Key
* `Title`
* `Artist`
* `Duration`
* `Genre`

Example:

```python
dictDictPlaylist = {
    "PL001": {
        "playlist": "Morning Routine",
        "desc": "what i need every morning",
        "songs": {
            "SG001": {
                "title": "Like Jennie",
                "artist": "JENNIE",
                "duration": "02:04",
                "genre": "K-Pop"
            }
        }
    }
}
```
