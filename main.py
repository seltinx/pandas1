import numpy as np
import pandas as pd
import xlrd
import openpyxl

#Zadanie 1

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
# print(df)


#Zadanie 2
#•	tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
# print(df[df['Liczba'] > 1000])

#•	tylko rekordy gdzie nadane imię jest takie jak Twoje
# print(df[df['Imie'] == 'SZYMON'])

# •	sumę wszystkich urodzonych dzieci w całym danym okresie,
#print(df[(df['Rok'] == 2000)]['Liczba'].sum())  # <---- Nie jestem piewien czy to jest prawidłowe

#•	sumę dzieci urodzonych w latach 2000-2005
# print(df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)]['Liczba'].sum())

#•	sumę urodzonych chłopców i dziewczynek
# print(df[(df['Plec'] == 'M')]['Liczba'].sum() & df[(df['Plec'] == 'K')]['Liczba'].sum())

#•	najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),
# print(df.groupby(['Rok', 'Plec'])['Imie'].max())

#•	najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,
# print(df.groupby(['Rok', 'Plec'])['Imie'].max())


#Zadanie 3

df1 = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
# print(df1)

#•	listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame)
# print(df1['Sprzedawca'].unique())

#•	5 najwyższych wartości zamówień
# print(df1.sort_values('Utarg', ascending=False).head(5))

#•	ilość zamówień złożonych przez każdego sprzedawcę
# print(df1.groupby(['Sprzedawca'])['Utarg'].sum())

#•	sumę zamówień dla każdego kraju
# print(df1.groupby(['Kraj'])['idZamowienia'].count())

# •	sumę zamówień dla roku 2005, dla sprzedawców z Polski
# print(df1.loc[(df1['Kraj']) == 'Polska']) <-- dalej próbowałem ale chaos się dział w błedach

#•	średnią kwotę zamówienia w 2004 roku,
# print(round(df1.loc[(pd.DatetimeIndex(df1['Data zamowienia']).year == 2004)]['Utarg'].mean()))
#
# zapis2004 = df1.loc[((pd.DatetimeIndex(df1['Data zamowienia']).year == 2004))]
#
# zapis2004.to_csv('zamowienia_2004.csv', index=False)