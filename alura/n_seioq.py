import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


path_notas = f'/home/nd3ll/Documentos/Programação/ALUra/Data_science_analise_e_visualiz_de_dados/aula0/introducao-a-data-science-aula0/aula0/ml-latest-small/ratings.csv'

notas = pd.read_csv(path_notas)
sns.set_theme()

print(sns.boxplot(notas.rating, orient='h'))
plt.show()