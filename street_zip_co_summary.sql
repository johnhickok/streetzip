SELECT 
roads.name AS st_name,
zip_codes.name AS community,
zip_codes.zip_code AS zip,
counties.name as county,
COUNT(roads.name) as st_count
FROM counties
join zip_codes
ON ST_intersects(counties.geom, zip_codes.geom)
join roads
ON ST_intersects(zip_codes.geom, roads.geom)
GROUP BY roads.name, zip_codes.zip_code, zip_codes.name, counties.name
ORDER BY roads.name
;