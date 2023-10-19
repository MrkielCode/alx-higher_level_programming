-- To display top 3 cities temp on
-- month of july and August

SELECT city, AVG(value) AS avg_temp 
	FROM temperatures
	WHERE month IN (7, 8)
	GROUP BY city
	ORDER by avg_temp DESC
	LIMIT 3;
