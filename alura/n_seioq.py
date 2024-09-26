import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


path_notas = f'/home/nd3ll/Documentos/Programação/ALUra/Data_science_analise_e_visualiz_de_dados/aula0/introducao-a-data-science-aula0/aula0/ml-latest-small/ratings.csv'

path_filmes = f'/home/nd3ll/Documentos/Programação/ALUra/Data_science_analise_e_visualiz_de_dados/aula0/introducao-a-data-science-aula0/aula0/ml-latest-small/movies.csv'

notas = pd.read_csv(path_notas)
sns.set_theme()

filmes = pd.read_csv(path_filmes)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# print(sns.boxplot(notas.rating, orient='h'))
# plt.show()

#Fazendo relações no dataframe
#Quero as notas do filme Toy Story


notas_toy = notas.query('movieId==1').rating.mean()
# print(notas_toy)

print(filmes)

notas_jumanji = notas.query('movieId==2').rating.mean()
# for x in filmes['movieId']:
#     print(notas.query(f'movieId=={x}').rating.mean())

medias_por_filme = notas.groupby(['movieId']).mean()['rating']

# medias_por_filme.plot(kind='hist')
print(medias_por_filme.describe())
# sns.boxplot(medias_por_filme, orient='h')

#sns.distplot(medias_por_filme, bins=10)
#
# plt.show()
lista_de_filmes = filmes.title.unique().tolist()