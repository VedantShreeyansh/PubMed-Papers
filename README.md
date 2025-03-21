﻿# PubMed Research Papers Fetcher

This project is a command-line tool for retrieving PubMed paper IDs based on a user-provided search query. It uses the NCBI Entrez API to fetch results and is managed using Poetry for dependency management.
The search results contains papers with at least one author affiliated with a pharmaceutical or biotech
 company and return the results as a CSV file.

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

        git clone "your git repo url"
        cd "working directory"

        Install the dependencies

        poetry install

(iii) Execution of the Program

        Run the script using following terminal command

        python test.py "cancer treatment" -f results.csv --debug

        cancer treatment is the user provided search query here. It can be anything. test.py is the main script file to
        be executed and results.csv is the csv file containing the main output.

        An output file is already created for the reference. You can create a new output file by running the above code in the terminal meanwhile adjusting the "retmax" parameter in the main script file accordingly.

(iv) Tools and Libraries Used

        Python (>=3.12) – Programming language ("https://www.python.org/downloads/")

        Poetry – Dependency and package management ("https://python-poetry.org/docs/")

        Requests Library – Used to make HTTP requests to the PubMed API ("https://www.w3schools.com/python/module_requests.asp")

        NCBI Entrez API – Fetches PubMed paper data ("https://www.ncbi.nlm.nih.gov/home/develop/api/")
        
        Chat GPT - For optimizing the implementation and resolving the errors faster and understanding the significance of various files in the dependency management. 
 
 (v) Additional Notes    

       The script retrieves up to 50 PubMed paper IDs per search but it will filter the search results thus decreasing the number of results in the output file.

       You can Modify the retmax parameter in test.py to increase or decrease the number of results.
