-- To list all bands with Glam rock as their main style, ranked by
SELECT band_name, 
       IFNULL(DATEDIFF('2022-01-01', SUBSTRING_INDEX(lifespan, '-', 1)), 0)
  AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;

