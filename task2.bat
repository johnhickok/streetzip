echo begin task 2 >> log1.txt
echo %time% >> log1.txt

python convert_utf8.py
echo cleaned up csv >> log1.txt
echo %time% >> log1.txt

psql -h localhost -p 5432 -U postgres -d test_joins -q -c "TRUNCATE TABLE roads;"
echo truncated table >> log1.txt
echo %time% >> log1.txt

psql -h localhost -p 5432 -U postgres -d test_joins -q -c "DROP INDEX roads_geom_idx;"
echo dropped spatial index >> log1.txt
echo %time% >> log1.txt

psql -h localhost -p 5432 -U postgres -d test_joins -q -f roads_wkt_utf8.sql
echo loaded data >> log1.txt
echo %time% >> log1.txt

psql -h localhost -p 5432 -U postgres -d test_joins -q -c "VACUUM ANALYZE roads;"
echo vacuumed roads >> log1.txt
echo %time% >> log1.txt

psql -h localhost -p 5432 -U postgres -d test_joins -q -c "CREATE INDEX roads_geom_idx ON roads USING gist(geom);"
echo created spatial index >> log1.txt
echo %time% >> log1.txt

psql -h localhost -p 5432 -U postgres -d test_joins -q -o streetz.csv -A -t -f street_zip_summary.sql
echo extracted csv >> log1.txt
echo %time% >> log1.txt

python make_sqlite_db.py
echo created sqlite, imported csv >> log1.txt
echo %time% >> log1.txt
