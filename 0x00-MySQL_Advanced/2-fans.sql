-- SQL script that ranks country origins
-- of bands by the number of fans, based on the provided table dump
SELECT origin, SUM(nb_fans) AS nb_fans
FROM bands
GROUP BY origin
ORDER BY nb_fans DESC;