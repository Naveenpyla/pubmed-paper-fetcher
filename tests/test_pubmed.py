from get_papers.pubmed import fetch_papers
from get_papers.utils import filter_non_academic_authors

def test_fetch_and_filter():
    papers = fetch_papers("aspirin", max_results=5, debug=False)
    filtered = filter_non_academic_authors(papers)
    assert isinstance(filtered, list)
    for entry in filtered:
        assert "PubmedID" in entry
        assert "Company Affiliation(s)" in entry
