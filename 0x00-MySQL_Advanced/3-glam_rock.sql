-- To list all bands with Glam rock as their main style, ranked by
SELECT band_name,
       (IFNULL(SPLIT, 2022), formed)
  AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;

