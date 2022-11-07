-- Listing all cities
SELECT c.id, c.name, s.name
FROM cities AS C
INNER JOIN states AS S
ON C.state_id = S.id
ORDER BY c.id;
