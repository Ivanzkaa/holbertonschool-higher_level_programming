--
SELECT t_g.name
FROM tv_show_genres AS t_s_g
INNER JOIN tv_shows AS t_s
ON t_s_g.show_id = t_s.id
INNER JOIN tv_genre_id = t_g.id
WHERE t_s.title = "Dexter"
ORDER BY t_g.name ASC;
