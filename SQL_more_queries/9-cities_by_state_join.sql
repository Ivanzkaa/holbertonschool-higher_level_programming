-- Listing all cities
SELECT id, name
FROM states
WHERE cities.id, cities.name, states.name
ORDER BY id;
