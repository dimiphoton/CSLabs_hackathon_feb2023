import pprint

import rdflib.plugins.sparql.parser


def test_parser_structure() -> None:
    def t(q):
        print(q)
        pprint.pprint(rdflib.plugins.sparql.parser.parseQuery(q))

    t("SELECT * WHERE { ?s ?p ?o, ?o2 ; ?p2 ?o3 . ?s2 ?p ?o .} ")

    t("SELECT * WHERE { ?s ?p ?o, ?o2 ; ?p2 ?o3 ; ?p3 [ ?p ?o ] . ?s2 ?p ?o .} ")
