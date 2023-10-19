-- to display all genere and its link

SELECT g.name
FROM tv_shows s
JOIN tv_show_genres sg
ON s.id = sg.show_id
JOIN tv_genres g
ON g.id = sg.genre_id
Where s.title = 'Dexter'
