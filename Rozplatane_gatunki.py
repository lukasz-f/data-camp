oceny_wszystkie = pd.merge(ratings, movies) #łączy ratings i movies
oceny_wszystkie2 = oceny_wszystkie.tail(200) #wybieramy próbkę 200 ostatnich
s = oceny_wszystkie2['Genre'].str.split('|').apply(pd.Series, 1).stack()
# przypisujemy zmiennej pomocniczej s serię danych powstałą poprzez "rozplątanie" wsyzstkich wierszy zawierających więcej niż jeden gatunek w osobne wiersze
s.index = s.index.droplevel(-1)
# trzeba przesunąć indeks serii w lewo - na numery wpisów/ocen
s.name = "Gatunki"
# nazywamy serię, żeby można było na niej zadziałać .joinem
oceny_wszystkie2 = oceny_wszystkie2.join(s)
del oceny_wszystkie2["Genre"] # to już nie będzie potrzebne

# no i teraz seabornem boxplota :)
plt.figure(figsize=(20,10))
sns.boxplot(x=oceny_wszystkie["Rating"], y=oceny_wszystkie["Gatunki"])
plt.show()