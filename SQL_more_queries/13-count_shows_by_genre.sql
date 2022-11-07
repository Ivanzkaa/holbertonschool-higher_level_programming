-- Listing all of the genres from the database and displays the number of shows linked to each
SELECT t_g.name AS genre,
COUNT(t_s_g.show_id) AS number_of_shows
FROM tv_shows_genres as t_s_g
LEFT JOIN tv_genres AS t_g
ON t_s_g.genre_id = t_g.id
GROUP BY t_g.name
ORDER BY number_of_shows DESC;
