import argparse
from get_papers.pubmed import fetch_papers
from get_papers.utils import filter_non_academic_authors, write_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic authors")
    parser.add_argument("query", help="PubMed query string")
    parser.add_argument("-f", "--file", help="Output CSV filename")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug info")
    args = parser.parse_args()

    if args.debug:
        print(f"[DEBUG] Query: {args.query}")

    results = fetch_papers(args.query, debug=args.debug)
    filtered = filter_non_academic_authors(results)

    if args.file:
        write_to_csv(filtered, args.file)
        print(f"✅ Results saved to {args.file}")
    else:
        import pandas as pd
        print(pd.DataFrame(filtered).to_string(index=False))

if __name__ == "__main__":
    main()
