-- Listing all Comdey show

SELECT s.title FROM tv_genres g
	JOIN tv_show_genres sg ON g.id = sg.genre_id
	JOIN tv_shows s ON s.id = sg.show_id
	WHERE g.name = 'Comedy'
	ORDER BY s.title
