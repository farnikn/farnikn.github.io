import ads, re
ads.config.token = '7replqPUN61x00aeBUdB2s78ufN8YYAo8l6fJaHH'


# Function to determine the kind value based on the entry's type and title content
def determine_kind(bibtex_entry):
    # Check for @ARTICLE or @INPROCEEDINGS at the beginning of the entry
    if bibtex_entry.strip().startswith('@ARTICLE'):
        kind_value = "Peer Reviewed Journals"
    elif bibtex_entry.strip().startswith('@INPROCEEDINGS'):
        kind_value = "Conference Proceedings"
    else:
        kind_value = None
    
    # Extract the title using a regular expression
    title_match = re.search(r"title\s*=\s*\{([^\}]+)\}", bibtex_entry, re.IGNORECASE)
    if title_match:
        title = title_match.group(1).lower()  # Get the title in lowercase for case-insensitive matching
        # Check if the title contains 'data release' or 'database'
        if 'data release' in title or 'database' in title:
            kind_value = "Data Release Papers"

    return kind_value


def add_kind_to_bibtex(bibtex_entry, kind_value):
    # Determine where to insert the new keyword
    last_comma_index = bibtex_entry.rfind(",")
    insertion_point = last_comma_index + 1 if last_comma_index != -1 else len(bibtex_entry)
    # Prepare the kind keyword line, only add if kind_value is not None
    if kind_value:
        kind_keyword_line = f"       kind = {{{kind_value}}},\n"
        # Insert the kind keyword
        updated_entry = bibtex_entry[:insertion_point] + "\n" + kind_keyword_line + bibtex_entry[insertion_point:]
    else:
        # If no kind_value is determined, return the entry unchanged
        updated_entry = bibtex_entry
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