import os
from whoosh.fields import *
from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser
from pathlib import Path
from whoosh.analysis import StemmingAnalyzer
from whoosh.qparser import FuzzyTermPlugin, PrefixPlugin


# Open index
print("Opening index...")
ix = open_dir("index_dir")

# Partial matching
# parser = QueryParser("content", ix.schema)
# parser.add_plugin(FuzzyTermPlugin())
# parser.add_plugin(PrefixPlugin())

# Get user input for keyword
#keyword = input("Enter your search keyword: ")


# Create searcher obeject and query
with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("This")
    results = searcher.search(query)
    if results:
        for hit in results:
            print(hit)
    else:
        print("No result found")

# Perform a search for multiple results 
from whoosh.query import Or, Term

with ix.searcher() as searcher:
    query_str = "artificiall intelligence"
    query_str = query_str.lower().split()  # Split the query into individual words

    # Create an Or query with all query terms
    query = Or([Term("content", term) for term in query_str])

    results = searcher.search(query, limit=None) # Set limit to None to retrieve all


    if len(results) >= 0:
        print(f"Found {len(results)} documents:")
        for hit in results:
            print(f"Document ID: {hit['doc_id']}")
            print(f"Title: {hit['title']}")
            print("____")
    else:
        print("No matching document found!")


