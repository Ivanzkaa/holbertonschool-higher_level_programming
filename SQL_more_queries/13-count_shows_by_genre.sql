-- Listing all of the genres from the database and displays the number of shows linked to each
SELECT g.name AS genre,
COUNT(s_g.genre_id) AS number_of_shows
FROM tv_genres AS t_g
INNER JOIN tv_show_genre AS s_g
ON g.id = s_g.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;