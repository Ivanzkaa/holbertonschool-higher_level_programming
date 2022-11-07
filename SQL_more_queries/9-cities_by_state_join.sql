-- Listing all cities
SELECT cities.id, cities.name, states.name
FROM cities AS C
INNER JOIN states AS S
ON C.state_id = S.id
ORDER BY c.id ASC;
