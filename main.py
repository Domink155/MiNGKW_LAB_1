import re
import pandas as pd


##---regex_list---
tabelka=[]
tabelka.append("(?<=iss\.\s)\d*\s*|(?<=no\.\s)\d*\s*|(?<=No\.\s)\d*\s*|(?<=issue\s)\d*\s*|(?<=Issue\s)\d*\s*")
tabelka.append("(?<=vol\.\s)\d*|(?<=Vol\.\s)\d*")
tabelka.append("(?<=nr\sart\.)\s\w*")
tabelka.append("(?<=\ss\.\s)(?:\d+\-\d+)|(?<=S\.\s)(?:\d+\-\d+)")
tabelka.append("(?<=\:\s)(\s*\D+(?=\,))")
tabelka.append("(?:(\w*\;*)+)")
tabelka.append("(?<=\,\s)(?:\d{4})(?=\;)")


def regular_expressions(line, regex):
    match = re.search(regex, line)
    if match:
        return match.group(0)
    else:
        return ""

def run_maszynko():

    ##--- stworzenie nagłówków dla pliku wyjściowego ---
    tabliczka = ['no', 'vol', 'article no', 'pages in range', 'publisher name', 'publisher location', 'publisher year']
    results_df = pd.DataFrame(columns=tabliczka)

    ## --- przypisanie funkcji do zmniennej na potrzeby odwołania ---

    details_df = pd.read_csv(
        "details.csv",
        sep=";",
        encoding='unicode_escape',
    )
    details_series = details_df["Column1"] + ";" + details_df["Column2"]
    #print(details_series)
    for index in range(len(tabliczka)):
        results_df[tabliczka[index]] = details_series.apply(lambda text: regular_expressions(text, tabelka[index]))
        #print(results_df[tabliczka[index]])
    results_df.to_csv("results.csv")

run_maszynko()