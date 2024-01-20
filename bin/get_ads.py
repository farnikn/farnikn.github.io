# pylint: disable=trailing-whitespace
import ads

def make_bib(author, outfile="cv.bib"):
    '''
    fetch all files on ads and make a bibtext file from it

    Parameters
    ----------
    author : string

    Examples
    ----------    
    first author papers
    >> make_bib("^Last name, first_name")

    all papers
    >> make_bib("Last name, first_name") # note the removed

    Notes:     
    '''
    papers = list(
        ads.SearchQuery(
                q=f'=author:\"{author}\"',
                fl=[
                    "citation_count",
                    "bibcode",
                ]
        )
        )
    
    with open(outfile,"w+")as out:
        for p in papers:
            bibquery = ads.ExportQuery(p.bibcode)
            bibs = bibquery.execute()
            out.write(bibs)

if __name__ == '__main__':
    make_bib("^Nikakhtar, Farnik", outfile='_bibliography/papers.bib')