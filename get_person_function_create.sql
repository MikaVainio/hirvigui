-- FOR CREATING A TESTING FUNCTION

-- FUNCTION: public.get_person_by_id(integer)

-- DROP FUNCTION public.get_person_by_id(integer);

CREATE OR REPLACE FUNCTION public.get_person_by_id(
	person_id integer)
    RETURNS SETOF person 
    LANGUAGE 'sql'

    COST 100
    VOLATILE 
    ROWS 1000
AS $BODY$
SELECT * 
FROM public.person
WHERE person.id = person_id;
$BODY$;

ALTER FUNCTION public.get_person_by_id(integer)
    OWNER TO sovellus;