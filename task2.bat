python convert_utf8.py

psql -h localhost -p 5432 -U postgres -d test_joins -q -c "TRUNCATE TABLE roads;"

psql -h localhost -p 5432 -U postgres -d test_joins -q -f roads_wkt_utf8.sql

