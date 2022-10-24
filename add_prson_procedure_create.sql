-- FOR CREATING A TESTING PROCEDURE

-- PROCEDURE: public.add_person(character varying, character varying, integer)

-- DROP PROCEDURE public.add_person(character varying, character varying, integer);

CREATE OR REPLACE PROCEDURE public.add_person(
	first_name character varying,
	last_name character varying,
	points integer)
LANGUAGE 'sql'

AS $BODY$
INSERT INTO person (etunimi, sukunimi, tehopisteet) VALUES (first_name, last_name, points)
$BODY$;

COMMENT ON PROCEDURE public.add_person
    IS 'Esimekki proseduuri, joka luo käyttäjän';