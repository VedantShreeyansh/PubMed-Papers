# PubMed Research Papers Fetcher

This project is a command-line tool for retrieving PubMed paper IDs based on a user-provided search query. It uses the NCBI Entrez API to fetch results and is managed using Poetry for dependency management.

Code Organization

The project follows a simple structure:

pubmed_papers/
  (i) test.py    # Main script containing the code
  (ii) pyproject.toml # Poetry configuration file
  (iii) README.md # Project documentation
  (iv) poetry.lock # Used for dependency management 

test.py – Implements the function to fetch PubMed paper IDs based on a search query.
pyproject.toml – Defines dependencies and the executable Poetry script.
README.md – Provides documentation on installation, usage, and dependencies.
poetry.lock - It acts as a snapshot of your project's dependencies at a given time, ensuring that all installations remain stable, reproducible, and conflict-free.

Installation Instructions

(i) Prerequisites

Ensure you have Python 3.12+ installed. Additionally, install Poetry (if not already installed)

pip install poetry

(ii) Installing Dependencies

Clone the repository:


