SELECT 
osm_pts.name AS st_name,
COUNT(osm_pts.name) as st_count,
zip_codes.zip_code AS zip,
zip_codes.name AS community
FROM zip_codes
JOIN osm_pts
ON ST_Contains(zip_codes.geom, osm_pts.geom)
GROUP BY osm_pts.name, zip_codes.zip_code, zip_codes.name
ORDER BY osm_pts.name
;