Run the program:
python3 app.py

Then enter URLs in your browser:

To find the creator of an artwork:
http://127.0.0.1:PORT/creator/Mickey%20Mouse

To find how many stolen works an artist has:
http://127.0.0.1:PORT/stolen_count/Pablo%20Picasso

Replace PORT with the number shown when running the app.

SQL:

\copy artworks(artwork_name, artist_name, medium) FROM 'interpol_classified_stolen_art.csv' DELIMITER ',' CSV HEADER;

\copy artists(artists_name, origin, image_link) FROM 'artists.csv' DELIMITER ',' CSV HEADER;