import ads, re

# Function to determine the kind value based on the entry's type and title content
def determine_kind(bibtex_entry):
    isARTICLE = bibtex_entry.strip().startswith('@ARTICLE')
    isINPROCEEDINGS = bibtex_entry.strip().startswith('@INPROCEEDINGS')

    title_regex = r'title\s*=\s*"\{([^}]+)\}"'
    title = re.search(title_regex, bibtex_entry, re.IGNORECASE).group(1)

    hasDR = 'data release' in title.lower()
    hasDB = 'database' in title.lower()
    hasTheli = 'theli pipeline' in title.lower()

    if isARTICLE and not hasDR and not hasDB and not hasTheli:
        kind = "Peer Reviewed Journals"
    elif isINPROCEEDINGS or hasTheli:
        kind = "Conference Proceedings"
    elif hasDR or hasDB:
        kind = "Data Release Papers"

    return kind


def add_kind_to_bibtex(bibtex_entry, kind_value):
    # Determine where to insert the new keyword
    last_comma_index = bibtex_entry.rfind(",")
    kind_keyword_line = f"       kind = {{{kind_value}}},"
    # Insert the kind keyword
    updated_entry = bibtex_entry[:last_comma_index+1] + "\n" + kind_keyword_line + bibtex_entry[last_comma_index+1:]
    return updated_entry

def replace_journal_name(bibtex_entry):
    journal_dict = {'\\prl':'Physical Review Letters',
                    '\\prd':'Physical Review D',  
                    '\\pre':'Physical Review E',
                    '\\apjl':'Astrophysical Journal, Letters', 
                    '\\apj':'Astrophysical Journal', 
                    '\\apjs':'Astrophysical Journal, Supplement', 
                    '\\jcap':'Journal of Cosmology and Astroparticle Physics', 
                    '\\mnras':'Monthly Notices of the RAS'
                    }
    isARTICLE = bibtex_entry.strip().startswith('@ARTICLE')
    if isARTICLE:
        journal_regex = r'journal\s*=\s*\{([^}]+)\}'
        journal = re.search(journal_regex, bibtex_entry, re.IGNORECASE).group(1)
        if journal in journal_dict:
            updated_entry = bibtex_entry.replace(journal, journal_dict[journal])
            return updated_entry
    return bibtex_entry

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

            new_keyword = "       bibtex_show = {true},"
            last_comma_index = bibs.rfind(",")
            bibs = bibs[:last_comma_index+1] + "\n" + new_keyword + bibs[last_comma_index+1:]

            kind_value = determine_kind(bibs)  # Determine the kind based on the entry
            bibs = add_kind_to_bibtex(bibs, kind_value)
            bibs = replace_journal_name(bibs)

            out.write(bibs)


if __name__ == '__main__':
    make_bib("Nikakhtar, Farnik", outfile='_bibliography/papers.bib')