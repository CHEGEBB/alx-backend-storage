-- sql script to create a table metal_bands
-- with columns band_name, formed, origin, style, and fans
SELECT band_name, (IFNULL(split, '2024') - formed) AS lifespan
    FROM metal_bands
    WHERE FIND_IN_SET('Glam rock', IFNULL(style, "")) > 0
    ORDER BY lifespan DESC;
