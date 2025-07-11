import csv

COMPANY_KEYWORDS = ["pharma", "biotech", "therapeutics",
                    "inc", "ltd", "corp", "gmbh", "labs",
                    "medicines", "biosciences"]

def is_company_affiliation(affil: str) -> bool:
    return affil and any(k.lower() in affil.lower() for k in COMPANY_KEYWORDS)

def filter_non_academic_authors(papers: list) -> list:
    output = []
    for p in papers:
        nonacad = [a["name"] for a in p["authors"] if is_company_affiliation(a["affiliation"])]
        companies = {a["affiliation"] for a in p["authors"] if is_company_affiliation(a["affiliation"])}
        emails = [a["email"] for a in p["authors"] if a["email"]]
        if nonacad:
            output.append({
                "PubmedID": p["pmid"],
                "Title": p["title"],
                "Publication Date": p["date"],
                "Non-academic Author(s)": "; ".join(nonacad),
                "Company Affiliation(s)": "; ".join(companies),
                "Corresponding Author Email": "; ".join(emails),
            })
    return output

def write_to_csv(papers: list, filename: str):
    keys = ["PubmedID", "Title", "Publication Date", 
            "Non-academic Author(s)", "Company Affiliation(s)", 
            "Corresponding Author Email"]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(papers)
