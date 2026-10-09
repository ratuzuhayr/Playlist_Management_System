# DATA INITIALIZATION
dictDictPlaylist = {
    # Playlist Data: Playlist ID (Primary Key), Playlist Name, Playlist Description, Songs.
    "PL001":{
        "playlist" : "Morning Routine",
        "desc" : "what i need every morning",
        # Songs Data: Song ID (Primary Key), Song Title, Song Artist, Song Duration.
        "songs":{
            "SG001": {"title": "Like Jennie", "artist": "JENNIE", "duration": "02:04", "genre": "K-Pop"},
            "SG002": {"title": "CRASH", "artist": "ALL DAY PROJECT", "duration": "02:53", "genre": "K-Pop"},
            "SG003": {"title": "Bang Bang Bang", "artist": "BIGBANG", "duration": "03:40", "genre": "K-Pop"}
        }
    },
     "PL002":{
        "playlist" : "Night Drive",
        "desc" : "driver's only",
        "songs":{
            "SG004": {"title": "LEGEND", "artist": "JANNABI", "duration": "03:47", "genre": "Indie"},
            "SG005": {"title": "THE WEEKEND", "artist": "88 Risings, BIBI", "duration": "02:48", "genre": "R&B"},
        }
    }
}

# Function: print playlist -> to display existing playlist
def printPlaylist():
    print("="*80)
    print("\t\t\tPLAYLIST")
    print("="*80)
    print(f"| {'Index':<6} | {'PID':<8} | {'Playlist Name':<20} | {'Description':<33} |")
    print("="*80)
    index = 0
    for i in dictDictPlaylist.items():
        print(f"| {index:<6} | {i[0]:<8} | {i[1]['playlist']:<20} | {i[1]['desc']:<33} |")
        index = index + 1
    print("="*80)

# Function: print song table inside a playlist -> to display songs inside the playlist
def printSongs(playlistID):
    if playlistID in dictDictPlaylist:
        print("="*88)
        print(f"\t\t PLAYLIST: {dictDictPlaylist[playlistID]['playlist']}")
        print(f"\t\t {dictDictPlaylist[playlistID]['desc']}")
        print("="*88)
        print(f"| {'Index':<6} | {'SID':<8} | {'Title':<20} | {'Artist':<20} | {'Duration':<8} | {'Genre':<8} |")
        print("="*88)
        song_index = 0
        for song in dictDictPlaylist[playlistID]['songs'].items():
            print(f"| {song_index:<6} | {song[0]:<8} | {song[1]['title']:<20} | {song[1]['artist']:<20} | {song[1]['duration']:<8} | {song[1]['genre']:<8} |")
            song_index = song_index + 1
        print("="*88)

# Functionn: to print latest playlist that is already updated by user
def printLatest():
    # PRINT UPDATED PLAYLIST
        print("="*72)
        print(f"\t\t LATEST PLAYLIST")
        print("="*72)
        print(f"| {'Index':<6} | {'PID':<8} | {'Playlist Name':<20} | {'Description':<25} |")
        print("="*72)
        index = 0
        for i in dictDictPlaylist.items():
            print(f"| {index:<6} | {i[0]:<8} | {i[1]['playlist']:<20} | {i[1]['desc']:<25} |")
            index = index + 1
        print("="*72)

# OPTION 1 : Show Playlist (READ)
def readPlaylist():
    while True:
        submenu = input('''
        1. Show Playlist & Songs
        2. Back to Main Menu

        Your Choice: ''')

        if submenu == "1":
            # Call print playlist function to display playlist data
            printPlaylist()
            # User can choose to view the songs inside the chosen playlist.
            checker = input("Do you want to see the songs inside the playlist? (YES/NO): ").upper()
            if checker == "YES":
                # Keep asking user to input the valid Playlist ID
                while True:
                    playlistID = input("Input Playlist ID (Ex. PL001): ").upper()
                    if playlistID in dictDictPlaylist:
                        printSongs(playlistID)
                        break       
                    else:
                        print("\nPlaylist ID Cannot be Found!")
            
            else:
                print("\nPlease Answer with 'YES' or 'NO")
                    
        elif submenu == "2":
            break

        else:
            print("\nThe Option You Entered is Not Valid. Please Enter the Submenu Number.")


# OPTION 2 : Add Playlist (CREATE)
def createPlaylist():
    while True:
        while True:
            playlistID = input(f"\nInput New Playlist ID (Ex. PL001): ").upper()
            if playlistID in dictDictPlaylist:
            # If the user entered existing ID, the system will print alert.
                print("Playlist ID Already Existed! Please Enter a New One.")
            elif playlistID == "":
                print("Playlist ID Cannot be Empty!")
            else:
                break
                
        playlistName = input("Input New Playlist Name: ")
        playlistDesc = input("Input Playlist Description: ")
        
        # Saving inputted data to the database.
        dictDictPlaylist[playlistID] = {'playlist': playlistName, 'desc': playlistDesc, 'songs':{}}

        # Print latest playlist
        print("\n Your New Playlist has been Successfully Added!")
        printLatest()

    # Asking user if they want to add another playlist
        while True:
            addAgain = input("\nDo you want to add another playlist? (YES/NO): ").upper()
            if addAgain == "YES":
                break
            elif addAgain == "NO":
                return
            else:
                print("Please Answer with 'YES' or 'NO'.")

# OPTION 3 : Delete Playlist (DELETE)
def deletePlaylist():
    printPlaylist()

    playlistID = input("\nInput Playlist ID to Delete (Ex. PL001): ").upper()
    # If the Playlist ID is existed in the database, then it will be successfully deleted.
    if playlistID in dictDictPlaylist:
        # Deletion confirmation
        confirm = input("Are you sure you want to delete this playlist? (YES/NO): ").upper()
        if confirm == "YES":
            del dictDictPlaylist[playlistID]
            print("\nYour Playlist has been Successfully Deleted!")
            printLatest()
        elif confirm == "NO":
            print("\nSorry, the Deletion Process is Cancelled")
        else:
            print("Please Answer with 'YES' or 'NO'.")
    else:
        print("\nPlaylist ID Cannot Be Found!")


# OPTION 4 : Update Playlist (UPDATE)
def updatePlaylist():
    while True:
        submenu = input('''
        1. Update Playlist Name/Description
        2. Add Songs to Playlist
        3. Back to Main Menu

        Your Choice: ''')

        if submenu == "1":
            printPlaylist()
            playlistID = input("\nInput Playlist ID to Update (Ex. PL001): ").upper()
            if playlistID in dictDictPlaylist:
                column = input("Which Column Would You Like to Update? (playlist/desc): ").lower()
                if column == "playlist" or column == "desc":
                    newValue = input("Input Update: ")
                    dictDictPlaylist[playlistID][column] = newValue
                    print("\nYour Playlist has been Successfully Updated!")
                    printLatest()
                else:
                    print("\nInvalid Column! Please Choose 'playlist or 'desc'.")
            else:
                print("\nThere's No Such Playlist! Try Again.")

        elif submenu == "2":
            printPlaylist()
            playlistID = input("\nInput Playlist ID to Update (Ex. PL001): ").upper()
            if playlistID in dictDictPlaylist:
                while True:
                    songID = input("\nInput Song ID (Ex. SG001): ").upper()
                    if songID in dictDictPlaylist[playlistID]['songs']:
                        print("This Song ID is Already Existed! Input a New One")
                    elif songID == "":
                        print("Song ID Cannot be Empty!")
                    else:
                        break

                songTitle = input("Input Song Title: ")
                songArtist = input("Input Song Artist: ")
                songDuration = input("Input Song Duration (Ex. 03:28): ")
                songGenre = input("Input Song Genre: ")

                # All inputted new song values will be saved inside inputted Song ID.
                dictDictPlaylist[playlistID]['songs'][songID] = {
                    'title': songTitle,
                    'artist': songArtist,
                    'duration': songDuration,
                    'genre': songGenre
                }

                print("\nYour New Song has been Successfully Added!")
                printSongs(playlistID)

            else:
                print("\nThere's No Such Playlist! Try Again.")

        elif submenu == "3":
            break
        else:
            print("\nThe Option You Entered is Not Valid. Please Enter the Submenu Number.")

# OPTION 5 : Playlist & Songs Statistics
def showStatistic():
    totalPlaylist = len(dictDictPlaylist)
    totalSong = 0
    dictGenre = {} # To save count songs per genre

    for playlist in dictDictPlaylist.values():
        for song in playlist['songs'].values():
            totalSong = totalSong + 1
            genre = song['genre'].lower()
            if genre in dictGenre:
                dictGenre[genre] = dictGenre[genre] + 1
            else:
                dictGenre[genre] = 1

    print("="*50)
    print("\t\t STATISTIC")
    print("="*50)
    
    print(f"\nTotal Playlist : {totalPlaylist}")
    print(f"Total Songs    : {totalSong}")

    print("\nSongs per Genre:")
    for genre, count in dictGenre.items():
        print(f"- {genre} : {count} songs")

    if totalSong == 0:
        print("\nMost Popular Genre : No songs available yet.")
    else:
        maxCount = max(dictGenre.values())  # To find the highest number of songs in one genre
        for genre, count in dictGenre.items():
            if count == maxCount:
                print(f"\nMost Popular Genre : {genre} ({maxCount} songs)\n")
    print("="*50)


# MAIN MENU
while True:
    chooseMenu = input( '''
    Welcome to the Playlist Management System

    Menu:
    1. Show Playlist
    2. Add Playlist
    3. Delete Playlist
    4. Update Playlist
    5. Statisctics
    6. Exit Program

    Choose Menu: ''' )

    if chooseMenu == "1":
        readPlaylist()
    elif chooseMenu == "2":
        createPlaylist()
    elif chooseMenu == "3":
        deletePlaylist()
    elif chooseMenu == "4":
        updatePlaylist()
    elif chooseMenu == "5":
        showStatistic()
    elif chooseMenu == "6":
        print("Thank You for Using Our Playlist Management System! Hope You Had FUN!\n")
        break
    else:
        print("\nThe Option You Entered is Not Valid.")
