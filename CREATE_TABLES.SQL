--SQL used to create new PostGIS tables
--DATABASE TEST_JOINS

-- Table: zip_codes

-- DROP TABLE zip_codes;

CREATE TABLE zip_codes
(
  gid integer NOT NULL DEFAULT nextval('zip1_gid_seq'::regclass),
  objectid numeric(10,0),
  zip_code character varying(10),
  geom geometry(MultiPolygon,4326),
  name character varying(100),
  CONSTRAINT zip1_pkey PRIMARY KEY (gid)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE zip_codes
  OWNER TO postgres;

-- Index: zip1_geom_idx

-- DROP INDEX zip1_geom_idx;

CREATE INDEX zip1_geom_idx
  ON zip_codes
  USING gist
  (geom);


-- Table: roads

-- DROP TABLE roads;

CREATE TABLE roads
(
  gid integer NOT NULL DEFAULT nextval('road_gid_seq'::regclass),
  name character varying(80),
  geom geometry(LineString,4326),
  CONSTRAINT road_pkey PRIMARY KEY (gid)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE roads
  OWNER TO postgres;

-- Index: road_geom_idx

-- DROP INDEX road_geom_idx;

CREATE INDEX road_geom_idx
  ON roads
  USING gist
  (geom);

