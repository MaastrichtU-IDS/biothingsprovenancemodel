# BioThings Provenance Model

This repository contains files involved in the development of a model for capturing provenance information for assertions made about chemical substances. The goal is to implement this model on the [BioThings](http://biothings.io/) suite of APIs to provide a standardized way to represent provenance information in the results of user-submitted queries.

## File listing and information

1. `mists\README.MD` 										
Information about our analysis on selected [Minimal Information Standards](https://fairsharing.org/collection/MIBBI) for reporting biomedical studies 

2. `nanopubs\README.MD`
Information about our analysis on the provenance usage in [Nanopublications](http://nanopub.org/wordpress/)

3. `wikidata\code\WikiDataExtraction.ipynb`
[Python](https://www.python.org/) notebook for extracting data for all [chemical compounds](https://query.wikidata.org/#%23Cats%0ASELECT%20%3Fitem%20%3FitemLabel%20WHERE%20%7B%0A%20%20%3Fitem%20wdt%3AP31%20wd%3AQ11173.%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%0A%7D) from [WikiData](https://www.wikidata.org/wiki/Wikidata:Main_Page) in [JSON](http://www.json.org/) format

4. `wikidata\code\wikidatajsonfileparser.py`
[Python](https://www.python.org/) script to extract the provenance information from the JSON files in Point 3. and store it in a file `wikidata\data\wikidata_provenance_results.csv`

5. `wikidata\code\WikiDataProvenanceAnalysis.ipynb`
[Python](https://www.python.org/) notebook using the file generated in Point 4. to determine and plot the usage frequency of each provenance property

6. `wikidata\data\wikidata_chemicalcompounds.csv`
[CSV](https://en.wikipedia.org/wiki/Comma-separated_values) file storing a list of identifiers for each chemical compound in WikiData (used in Point 3. to extract the JSON data)

7. `wikidata\provenancemodel\wikidata_example.json`
Example snippet of a [JSON](http://www.json.org/) file about a chemical compound from WikiData, demonstrating the claims and references provenance structure

8. `wikidata\provenancemodel\wikidata_provenance.png`
Schematic which shows by example the structure of WikiData's provenance model

9. `BioThingsProvenanceModel.xlsx`
Spreadsheet with our detailed analysis and interpretation of the results, as well as our provenance proposal for BioThings

10. `jsonldexample.json`
Example [JSON-LD](https://json-ld.org/) file implementing our provenance model for a single assertion

11. `rdfexample.json`
Example [RDF](https://www.w3.org/RDF/) file (using [Turtle syntax](https://www.w3.org/TR/turtle/)) implementing our provenance model for a single assertion

12. `README.MD`
This file

<!--7. wikidata\data\wikidata_jsondata.zip					: 	Archive containing all the JSON data for each chemical compound in WikiData (used in Point 4. to extract provenance properties)-->

<!--8. wikidata\data\wikidata_provenance_results.csv		: 	[CSV](https://en.wikipedia.org/wiki/Comma-separated_values) file storing all the provenance information for each chemical compound from WikiData in a structured way (analysed in Point 5.)-->