DROP TABLE IF EXISTS artworks;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
    artist_name TEXT PRIMARY KEY,
    origin_country TEXT, 
    image_link TEXT
);

CREATE TABLE artworks (
    artwork_name TEXT PRIMARY KEY,
    artist_name TEXT REFERENCES artists(artist_name),
    medium TEXT
);