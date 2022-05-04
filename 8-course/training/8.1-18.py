class Album:

    def __init__(self, artist, title, tracks):
        self.artist = artist
        self.title = title
        self.tracks = tracks


album_1 = Album("Queen", "Killer Queen", ["Brighton rock", "Killer Queen", "Tenement Funster"])

album_2 = Album("Metallica", "Black Album", ["Brighton rock", "Killer Queen", "Tenement Funster"])

# Не удаляйте этот код, он нужен для проверки

print(album_1.artist, album_1.title, len(album_1.tracks), "треков")
print(album_2.artist, album_2.title, len(album_2.tracks), "треков")
