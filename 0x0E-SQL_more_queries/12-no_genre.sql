-- to display all title and genere

SELECT s.title, g.genre_id
FROM tv_shows s
LEFT JOIN tv_show_genres g
ON s.id = g.show_id 
WHERE g.genre_id IS NULL
ORDER by s.title, g.genre_id ASC;
