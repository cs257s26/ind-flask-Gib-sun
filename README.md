Run the program:
python3 app.py

Then enter URLs in your browser:

To find the creator of an artwork:
http://127.0.0.1:PORT/creator/Mickey%20Mouse

To find how many stolen works an artist has:
http://127.0.0.1:PORT/stolen_count/Pablo%20Picasso

Replace PORT with the number shown when running the app.
=====================================================================================

SQL:

\copy artworks(artwork_name, artist_name, medium) FROM 'interpol_classified_stolen_art.csv' DELIMITER ',' CSV HEADER;

\copy artists(artists_name, origin, image_link) FROM 'artists.csv' DELIMITER ',' CSV HEADER;

For my database design, I divided the dataset into two tables: an artists table and an artworks table. 
I chose two tables because the data naturally separated into information about artists and information about individual artworks. This structure helps avoid repeating artist information multiple times for every artwork and makes the database more organized. 
The artists table stores the artist’s name, country of origin, and an image link for the artist, while the artworks table stores the artwork name, artist name, and medium of the artwork.
I selected the TEXT datatype for most columns because names, countries, mediums, and links can vary in length and formatting. 
The primary key for the artists table is artist_name, and the primary key for the artworks table is artwork_name. 
I also used a foreign key relationship between artworks.artist_name and artists.artist_name to connect the two tables but I kept running into an error - so I deleted it for now.
The first query represents the user story: “As a user, I want to find all stolen artworks by a particular artist like Pablo Picasso so I can see how often his work was stolen and what works.” This query searches the artworks table for rows where the artist name matches the user’s input and returns the names of the artworks. This allows users to explore which artworks by a specific artist are included in the stolen art dataset. 
The second query represents the user story: “As a user, I want to know how many artists in the database are from a specific country such as France so I know what counties have more stolen art.” This query searches the artists table for artists whose origin_country matches the user’s input and uses the SQL COUNT function to return the total number of matching artists. Together, these queries demonstrate different ways users can interact with and explore the dataset.