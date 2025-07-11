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
# 🧬 get-papers: PubMed Research Extractor

[![Python](https://img.shields.io/badge/python-3.10+-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PubMed API](https://img.shields.io/badge/data-PubMed-orange?logo=pubmed)](https://pubmed.ncbi.nlm.nih.gov/)

> A CLI tool to fetch PubMed papers using full query syntax, filter those with ≥1 **pharma/biotech** author, and export results to CSV.

---

## 📄 Description

This tool lets you:
- 🔍 Query PubMed using complex queries (e.g., `cancer therapy AND 2024[DP]`)
- 🏢 Identify papers with **non-academic (industry) authors**
- 📦 Export to CSV (including authors, affiliations, emails)

---

## 📦 Setup

```bash
poetry install

