-- Select bands with Glam rock as their main style
SELECT 
    band_name,
    -- Calculate lifespan in years until 2022
    YEAR('2022-01-01') - YEAR(Formed) AS lifespan
FROM 
    bands
WHERE 
    FIND_IN_SET('Glam rock', Split) > 0
ORDER BY 
    lifespan DESC;
