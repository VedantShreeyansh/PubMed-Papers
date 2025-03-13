import requests
import csv
import argparse
import sys
import re
import xml.etree.ElementTree as ET

def fetch_pubmed_query(query: str):
    """Fetch PubMed article IDs based on a search query."""
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 50 
    }
    
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("esearchresult", {}).get("idlist", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching PMIDs: {e}")
        return []

def fetch_pubmed_details(pmids: list):
    """Fetch detailed information for PubMed articles (using efetch for full details)."""
    if not pmids:
        return ""

    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml"
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        return response.text  
    except requests.exceptions.RequestException as e:
        print(f"Error fetching paper details: {e}")
        return ""

def is_pharma_biotech_affiliation(affiliation: str) -> bool:
    """Check if an affiliation belongs to a pharmaceutical or biotech company."""
    pharma_keywords = ["pharmaceutical", "biotech", "biosciences", "therapeutics", "pharma", "laboratories", "inc", "ltd", "corp", "gmbh", "sa", "llc"]
    return any(re.search(rf"\b{word}\b", affiliation, re.IGNORECASE) for word in pharma_keywords)

def parse_papers(xml_data: str):
    """Extract relevant data from the PubMed XML response."""
    results = []
    root = ET.fromstring(xml_data)

    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID", "Unknown")
        title = article.findtext(".//ArticleTitle", "Unknown")
        pub_date = article.findtext(".//PubDate/Year", "Unknown")
        
        pharma_authors = []
        companies = []
        corresponding_email = "N/A"

        for author in article.findall(".//Author"):
            name = " ".join(filter(None, [author.findtext("ForeName", ""), author.findtext("LastName", "")]))
            affiliation = author.findtext(".//Affiliation", "")

            if affiliation and is_pharma_biotech_affiliation(affiliation):
                pharma_authors.append(name)
                companies.append(affiliation)
        
        
        corresponding_author = article.find(".//AuthorList/Author[@ValidYN='Y'][Position='first']")
        if corresponding_author is not None:
            corresponding_email = corresponding_author.findtext(".//AffiliationInfo/Affiliation", "N/A")

        if pharma_authors:  
            results.append([pmid, title, pub_date, ", ".join(pharma_authors), ", ".join(companies), corresponding_email])

    return results

def save_to_csv(results, file_name="papers.csv"):
    """Save results to a CSV file."""
    if not results:
        print("No results to save.")
        return
    
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["PubMed ID", "Title", "Publication Date", "Pharma/Biotech Author(s)", "Company Affiliation(s)", "Corresponding Author(s) Email"])
        writer.writerows(results)
    
    print(f"Results written to {file_name}")

def main():
    parser = argparse.ArgumentParser(description="Fetch and filter PubMed research papers.")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="Filename to save results (default: papers.csv)")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    
    args = parser.parse_args()
    
    if args.debug:
        print(f"Fetching PubMed articles for query: {args.query}")
    
    pmids = fetch_pubmed_query(args.query)
    if args.debug:
        print(f"Found {len(pmids)} PMIDs")

    xml_data = fetch_pubmed_details(pmids)
    results = parse_papers(xml_data)

    if args.file:
        save_to_csv(results, args.file)
    else:
        for row in results:
            print("\t".join(row))

if __name__ == "__main__":
    main()
