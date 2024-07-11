-- SQL script that ranks country origins
-- of bands by the number of fans, based on the provided table dump
SELECT origin, SUM(fans) AS nb_fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY nb_fans DESC;