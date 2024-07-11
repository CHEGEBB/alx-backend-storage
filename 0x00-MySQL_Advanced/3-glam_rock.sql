-- Select bands with Glam rock as their main style, compute their lifespan, and rank by lifespan
SELECT
    band_name,
    IFNULL(YEAR('2022-01-01') - YEAR(formed), 0) AS lifespan
FROM
    metal_bands
WHERE
    main_style = 'Glam rock'
ORDER BY
    lifespan DESC;