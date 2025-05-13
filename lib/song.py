class Song:
    # Class attributes to track the counts and lists
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.genre = genre
        self.artist = artist

        # Add the song to various class-level attributes
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        # Increment the total count of songs
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        # Add genre to the list if it doesn't already exist
        if genre and genre not in cls.genres:
            cls.genres.append(genre)
            print(f"Added {genre} to genres list")
        elif genre:
            print(f"{genre} already exists in genres list")
        else:
            print("Invalid genre name provided.")

    @classmethod
    def add_to_artists(cls, artist):
        # Add artist to the list if it doesn't already exist
        if artist and artist not in cls.artists:
            cls.artists.append(artist)
            print(f"Added {artist} to artists list")
        elif artist:
            print(f"{artist} already exists in artists list")
        else:
            print("Invalid artist name provided.")

    @classmethod
    def add_to_genre_count(cls, genre):
        # Add or update the genre count
        if genre:
            if genre in cls.genre_count:
                cls.genre_count[genre] += 1
            else:
                cls.genre_count[genre] = 1
            print(f"Updated genre count for '{genre}': {cls.genre_count[genre]}")
        else:
            print("Invalid genre name provided.")

    @classmethod
    def add_to_artist_count(cls, artist):
        # Add or update the artist count
        if artist:
            if artist in cls.artist_count:
                cls.artist_count[artist] += 1
            else:
                cls.artist_count[artist] = 1
            print(f"Updated artist count for '{artist}': {cls.artist_count[artist]}")
        else:
            print("Invalid artist name provided.")

