.read lab12.sql

CREATE TABLE smallest_int_having AS
  SELECT time, smallest
  FROM students GROUP BY smallest
  HAVING COUNT(smallest) == 1;

CREATE TABLE fa19favpets AS
  SELECT pet, COUNT(*) as count
  FROM students GROUP by pet
  ORDER BY count DESC;


CREATE TABLE fa19dog AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


CREATE TABLE obedienceimages AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
