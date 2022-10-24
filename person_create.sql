-- FOR CREATING TESTING TABLE PERSON

-- Table: public.person

-- DROP TABLE public.person;

CREATE TABLE public.person
(
    id integer NOT NULL DEFAULT nextval('person_id_seq'::regclass),
    etunimi character varying(20) COLLATE pg_catalog."default" NOT NULL,
    sukunimi character varying(20) COLLATE pg_catalog."default" NOT NULL,
    tehopisteet integer,
    CONSTRAINT person_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.person
    OWNER to sovellus;
COMMENT ON TABLE public.person
    IS 'Esimerkkitaulu psycopg2-ajurien testaamiseen';