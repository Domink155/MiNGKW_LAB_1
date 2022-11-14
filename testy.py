import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from main import regular_expressions

class Testy(unittest.TestCase):

    def test_regular_expresions1_no(self):
        tabelka = []
        tabelka.append("(?<=iss\.\s)\d*\s*|(?<=no\.\s)\d*\s*|(?<=No\.\s)\d*\s*|(?<=issue\s)\d*\s*|(?<=Issue\s)\d*\s*")
        tabliczka = ['no', 'vol', 'article no', 'pages in range', 'publisher name', 'publisher location', 'publisher year']
        results_df = pd.DataFrame(columns=tabliczka)
        details_df = pd.read_csv("details.csv", sep=";",encoding='unicode_escape')
        details_series = details_df["Column1"] + ";" + details_df["Column2"]
        results_df[tabliczka[0]] = details_series.apply(lambda text: regular_expressions(text, tabelka[0]))

        df = pd.read_csv('details_org.csv', usecols=['Column3'], dtype= {'Column3': 'object'},low_memory=False,encoding='unicode_escape',sep=";")

        df_x = pd.DataFrame()
        df_z = pd.DataFrame()
        df_x['val']=results_df[tabliczka[0]]
        df_z['val']=  df.Column3
        df_z['val'] = df_z['val'].fillna('')
        assert_frame_equal(df_x, df_z, check_dtype=False)

    def test_regular_expresions2_vol(self):
        tabelka = []
        tabelka.append("(?<=vol\.\s)\d*|(?<=Vol\.\s)\d*")
        tabliczka = ['no', 'vol', 'article no', 'pages in range', 'publisher name', 'publisher location',
                     'publisher year']
        results_df = pd.DataFrame(columns=tabliczka)
        details_df = pd.read_csv("details.csv", sep=";", encoding='unicode_escape')
        details_series = details_df["Column1"] + ";" + details_df["Column2"]
        results_df[tabliczka[1]] = details_series.apply(lambda text: regular_expressions(text, tabelka[0]))

        df = pd.read_csv('details_org.csv', usecols=['Column4'], dtype={'Column4': 'object'}, low_memory=False,
                         encoding='unicode_escape', sep=";")

        df_x = pd.DataFrame()
        df_z = pd.DataFrame()
        df_x['val'] = results_df[tabliczka[1]]
        df_z['val'] = df.Column4
        df_z['val'] = df_z['val'].fillna('')
        assert_frame_equal(df_x, df_z, check_dtype=False)

    def test_regular_expresions3_article_no(self):
        tabelka = []
        tabelka.append("(?<=nr\sart\.)\s\w*")
        tabliczka = ['no', 'vol', 'article no', 'pages in range', 'publisher name', 'publisher location',
                     'publisher year']
        results_df = pd.DataFrame(columns=tabliczka)
        details_df = pd.read_csv("details.csv", sep=";", encoding='unicode_escape')
        details_series = details_df["Column1"] + ";" + details_df["Column2"]
        results_df[tabliczka[2]] = details_series.apply(lambda text: regular_expressions(text, tabelka[0]))

        df = pd.read_csv('details_org.csv', usecols=['Column5'], dtype={'Column5': 'object'}, low_memory=False,
                         encoding='unicode_escape', sep=";")

        df_x = pd.DataFrame()
        df_z = pd.DataFrame()
        df_x['val'] = results_df[tabliczka[2]]
        df_z['val'] = df.Column5
        df_z['val'] = df_z['val'].fillna('')
        assert_frame_equal(df_x, df_z, check_dtype=False)

    def test_regular_expresions4_pages_in_range(self):
        tabelka = []
        tabelka.append("(?<=\ss\.\s)(?:\d+\-\d+)|(?<=S\.\s)(?:\d+\-\d+)")
        tabliczka = ['no', 'vol', 'article no', 'pages in range', 'publisher name', 'publisher location',
                     'publisher year']
        results_df = pd.DataFrame(columns=tabliczka)
        details_df = pd.read_csv("details.csv", sep=";", encoding='unicode_escape')
        details_series = details_df["Column1"] + ";" + details_df["Column2"]
        results_df[tabliczka[3]] = details_series.apply(lambda text: regular_expressions(text, tabelka[0]))

        df = pd.read_csv('details_org.csv', usecols=['Column6'], dtype={'Column6': 'object'}, low_memory=False,
                         encoding='unicode_escape', sep=";")

        df_x = pd.DataFrame()
        df_z = pd.DataFrame()
        df_x['val'] = results_df[tabliczka[3]]
        df_z['val'] = df.Column6
        df_z['val'] = df_z['val'].fillna('')
        assert_frame_equal(df_x, df_z, check_dtype=False)

    def test_regular_expresions5_publisher_name(self):
        tabelka = []
        tabelka.append("(?<=\:\s)(\s*\D+(?=\,))")
        tabliczka = ['no', 'vol', 'article no', 'pages in range', 'publisher name', 'publisher location',
                     'publisher year']
        results_df = pd.DataFrame(columns=tabliczka)
        details_df = pd.read_csv("details.csv", sep=";", encoding='unicode_escape')
        details_series = details_df["Column1"] + ";" + details_df["Column2"]
        results_df[tabliczka[4]] = details_series.apply(lambda text: regular_expressions(text, tabelka[0]))

        df = pd.read_csv('details_org.csv', usecols=['Column8'], dtype={'Column8': 'object'}, low_memory=False,
                         encoding='unicode_escape', sep=";")

        df_x = pd.DataFrame()
        df_z = pd.DataFrame()
        df_x['val'] = results_df[tabliczka[4]]
        df_z['val'] = df.Column8
        df_z['val'] = df_z['val'].fillna('')
        assert_frame_equal(df_x, df_z, check_dtype=False)

    def test_regular_expresions6_publisher_location(self):
        tabelka = []
        tabelka.append("(?:(\w*\;*)+)")
        tabliczka = ['no', 'vol', 'article no', 'pages in range', 'publisher name', 'publisher location',
                     'publisher year']
        results_df = pd.DataFrame(columns=tabliczka)
        details_df = pd.read_csv("details.csv", sep=";", encoding='unicode_escape')
        details_series = details_df["Column1"] + ";" + details_df["Column2"]
        results_df[tabliczka[5]] = details_series.apply(lambda text: regular_expressions(text, tabelka[0]))

        df = pd.read_csv('details_org.csv', usecols=['Column9'], dtype={'Column9': 'object'}, low_memory=False,
                         encoding='unicode_escape', sep=";")

        df_x = pd.DataFrame()
        df_z = pd.DataFrame()
        df_x['val'] = results_df[tabliczka[5]]
        df_z['val'] = df.Column9
        df_z['val'] = df_z['val'].fillna('')
        assert_frame_equal(df_x, df_z, check_dtype=False)

    def test_regular_expresions7_publisher_year(self):
        tabelka = []
        tabelka.append("(?<=\,\s)(?:\d{4})(?=\;)")
        tabliczka = ['no', 'vol', 'article no', 'pages in range', 'publisher name', 'publisher location',
                     'publisher year']
        results_df = pd.DataFrame(columns=tabliczka)
        details_df = pd.read_csv("details.csv", sep=";", encoding='unicode_escape')
        details_series = details_df["Column1"] + ";" + details_df["Column2"]
        results_df[tabliczka[6]] = details_series.apply(lambda text: regular_expressions(text, tabelka[0]))

        df = pd.read_csv('details_org.csv', usecols=['Column10'], dtype={'Column10': 'object'}, low_memory=False,
                         encoding='unicode_escape', sep=";")

        df_x = pd.DataFrame()
        df_z = pd.DataFrame()
        df_x['val'] = results_df[tabliczka[6]]
        df_z['val'] = df.Column10
        df_z['val'] = df_z['val'].fillna('')
        assert_frame_equal(df_x, df_z, check_dtype=False)

if __name__ =='__main__':
    unittest.main()