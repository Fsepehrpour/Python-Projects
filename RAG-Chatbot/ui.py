import streamlit as st
import os
from pathlib import Path
from whoosh.fields import Schema, TEXT, ID
from whoosh import index
from whoosh.analysis import StemmingAnalyzer
from whoosh.qparser import QueryParser, MultifieldParser
from whoosh.query import Or, Term

# Function to create or open the index (cashed)
@st.cache_resource()
def open_index():
    print("Opening index ...")
    return index.open_dir("/Users/fatemeh/Documents/Programming/Mentorship/RAG-Chatbot/src/app/index_dir")


# Streamlit UI
def main():
    st.title("Document Search")

    # Search input
    query_str = st.text_input("Enter your query")

    # Open or create the inodex
    ix = open_index()

    if query_str:
        with ix.searcher() as searcher:
            query_terms = query_str.split()
            query = Or([Term("content", term) for term in query_terms])
            results = searcher.search(query, limit=None)

            if len(results) > 0:
                st.subheader(f"Found {len(results)} documents.")
                for hit in results:
                    st.write(f"Title: {hit['title']}")
                    st.write(f"Content: {hit['content']}")
                    st.write("____")
            else:
                st.write("No matching document found!")

if __name__ == "__main__":
    main()
