-- Listing all of the shows in a database without a genre linked
SELECT t_s.title, t_s_g.genre_id
FROM tv_show_genres AS t_s_g
RIGHT JOIN tv_shows AS t_s
ON t_s_g.show_id = t_s.id
WHERE t_s_g.genre_id is NULL
ORDER BY t_s.title ASC,
t_s_g.genre_id;
