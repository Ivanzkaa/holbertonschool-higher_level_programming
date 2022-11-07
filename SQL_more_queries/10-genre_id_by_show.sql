-- Listing all shows in the shows database
SELECT t_s.title, t_s_g.genre_id
FROM tv_show_genres AS t_s_g
INNER JOIN tv_shows AS t_s
ON t_s_g.show_id = t_s.id
ORDER BY t_s.title ASC,
t_s_g.genre_id;
