import requests
from time import sleep
from tqdm import tqdm
from xml.etree import ElementTree as ET

EMAIL = "naveenpyla20@gmail.com"

def fetch_papers(query: str, max_results: int = 100, debug: bool = False):
    base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    search_params = {
        "db": "pubmed", "term": query,
        "retmax": max_results, "retmode": "json", "email": EMAIL
    }
    resp = requests.get(base + "esearch.fcgi", params=search_params)
    resp.raise_for_status()
    ids = resp.json()["esearchresult"]["idlist"]
    if debug:
        print(f"[DEBUG] Found {len(ids)} IDs")

    papers = []
    for i in tqdm(range(0, len(ids), 10), desc="Fetching papers"):
        batch = ids[i:i+10]
        fetch_params = {"db": "pubmed", "id": ",".join(batch), "retmode": "xml", "email": EMAIL}
        resp2 = requests.get(base + "efetch.fcgi", params=fetch_params)
        resp2.raise_for_status()
        root = ET.fromstring(resp2.text)

        for art in root.findall(".//PubmedArticle"):
            pmid = art.findtext(".//PMID")
            title = art.findtext(".//ArticleTitle") or ""
            year = art.findtext(".//PubDate/Year")
            medline = art.find(".//MedlineDate")
            pub_date = year or (medline.text if medline is not None else "")
            authors = []
            for au in art.findall(".//Author"):
                last = au.findtext("LastName") or ""
                fore = au.findtext("ForeName") or ""
                name = f"{last} {fore}".strip()
                aff = ""
                for affinfo in au.findall(".//AffiliationInfo"):
                    aff = affinfo.findtext("Affiliation") or aff
                    if aff:
                        break
                email = ""
                if aff and "@" in aff:
                    email = aff.split()[-1]
                authors.append({"name": name, "affiliation": aff, "email": email})
            papers.append({"pmid": pmid, "title": title, "date": pub_date, "authors": authors})
        sleep(0.4)
    return papers
