import os
from whoosh.fields import *
from whoosh.index import create_in
from whoosh.qparser import QueryParser
from pathlib import Path
from whoosh.analysis import StemmingAnalyzer
from whoosh.qparser import FuzzyTermPlugin, PrefixPlugin

# Build schema of the indexing
schema = Schema(
    title=TEXT(stored=True),
    content=TEXT(analyzer=StemmingAnalyzer(), stored=True),
    path=ID(stored=True, unique=True)
)

# Check if the index directory exists to creat it 
if not os.path.exists("index_dir"):
    print("There is no such a directory.Creating ...")
    os.mkdir("index_dir")
else:
    print("This directory already exist.")


# Create index
ix = create_in("index_dir", schema)

# Create writer object to add documents to the index 
writer = ix.writer()

writer.add_document(
    title=u"First Document",
    path=u"/a",
    content=u"This is a trying to create a search engine by whoosh."
)

writer.add_document(
    title=u"Second Document",
    path=u"/b", 
    content=u"It is a very applicable software to automate simple tasks."
)

writer.add_document(
    title=u"Third Document",
    path=u"/c",
    content=u"This library made it very easy without need for deep knowledge of software engineering."
)

writer.commit()

