# Nanopubs analysis

The following [SPARQL](https://www.w3.org/TR/rdf-sparql-query/) query was executed on the full [Nanopubs repository](https://zenodo.org/record/1213293):

`
select ?p  (count(?p) as ?count) where {
	?s ?p ?o .
}
group by ?p
order by DESC(?count)
`

This returned a list of unique properties used in Nanopubs assertions and the frequency of their usage e.g.:

sio:SIO_000001													"30325084"^^xsd:integer

http://www.w3.org/ns/prov#wasGeneratedBy						"25312475"^^xsd:integer
	
http://purl.org/net/provenance/ns#usedData						"21960320"^^xsd:integer

http://swan.mindinformatics.org/ontologies/1.2/pav/authoredBy	"21384377"^^xsd:integer

http://purl.org/pav/authoredBy									"19649940"^^xsd:integer

http://www.w3.org/ns/prov#wasDerivedFrom						"15585707"^^xsd:integer

http://purl.org/nanopub/x/includesElement						"14499431"^^xsd:integer