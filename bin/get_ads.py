import ads, re
ads.config.token = '7replqPUN61x00aeBUdB2s78ufN8YYAo8l6fJaHH'


# Function to determine the kind value based on the entry's type and title content
def determine_kind(bibtex_entry):
    if bibtex_entry.strip().startswith('@ARTICLE'):
        return "Peer Reviewed Journals"
    elif bibtex_entry.strip().startswith('@INPROCEEDINGS'):
        return "Conference Proceedings"
    elif 'data release' in bibtex_entry.lower() or 'database' in bibtex_entry.lower():
        return "Data Release Papers"
    else:
        return None


def add_kind_to_bibtex(bibtex_entry, kind_value):
    # Determine where to insert the new keyword
    last_comma_index = bibtex_entry.rfind(",")
    kind_keyword_line = f"       kind = {{{kind_value}}},\n"
    # Insert the kind keyword
    updated_entry = bibtex_entry[:last_comma_index+1] + "\n" + kind_keyword_line + bibtex_entry[last_comma_index+1:]
    return updated_entry


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

            new_keyword = "       bibtex_show = {true},\n"
            last_comma_index = bibs.rfind(",")
            bibs = bibs[:last_comma_index+1] + "\n" + new_keyword + bibs[last_comma_index+1:]

            kind_value = determine_kind(bibs)  # Determine the kind based on the entry
            bibs = add_kind_to_bibtex(bibs, kind_value)

            out.write(bibs)


if __name__ == '__main__':
    make_bib("Nikakhtar, Farnik", outfile='_bibliography/papers.bib')