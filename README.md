# get-papers

## 📄 Description  
Fetch PubMed research papers using full PubMed query syntax, identify papers with ≥1 author from a pharmaceutical/biotech firm, and export results.

## 📦 Setup

```bash
poetry install
```

## 🚀 Usage

```bash
poetry run get-papers-list "cancer therapy AND 2024[DP]" -f output.csv
poetry run get-papers-list "gene therapy" --debug
```

### Arguments

- `query`: PubMed query string (supports full syntax)
- `-f, --file`: CSV output filename (if omitted, prints to console)
- `-d, --debug`: Enable debug logging

## 📁 Structure

- `main.py`: CLI entrypoint
- `pubmed.py`: PubMed API fetch + XML parsing
- `utils.py`: Filters and CSV functions
- `tests/`: Basic unit test

## ✅ Output Columns

- PubmedID  
- Title  
- Publication Date  
- Non-academic Author(s)  
- Company Affiliation(s)  
- Corresponding Author Email  

## 🧪 Testing

```bash
poetry run pytest
```
