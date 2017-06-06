# CRAWLR

POC to scrape job listing sites

### To run:

Right click parameterizedRun.py, select "run"

-or-

`python parameterizedRun.py`

Follow the prompt to add query parameters and the results
will output to `crawlr/data/`

### Complications:

    The lack of insight into business rules relating to job postings makes
    it difficult to write utility code that may reduce code duplication
    across CareerBuilder / Monster / etc.
___
    For example: company X has four similar positions to fill.  The final CSV
    output should not combine postings across sites in the same file because
    there's no way to know definitively whether these are unique positions
    (did company X post two positions to CareerBuilder and two to Monster?
    Did they duplicate all four postings on both sites?)  Assumtions about
    the ways an employer creates a posting will likely result in misleading
    output.
___
    Another example: the "distance from searched zipcode" query parameter
    accepts different values on Monster than it does on CareerBuilder (as
    well as a different query parameter key.)  This makes it difficult to
    reduce code duplication in in the model objects, and difficult to write
    mindful code for future additions to the list of sites we scrape.

### Proposed backlog:

1) Unit tests
2) Other job posting websites (Indeed / ZipRecruiter / etc.)
3) Further CSV handling: aggregate functions are currently handled manually via 
Google sheets, specifically counting job postings per company.  This could be
done within `crawlr/scraper/processing/`