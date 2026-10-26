'''
Importe as bibliotecas pandas, seaborn, matplotlib.pyplot e o módulo scipy.stats.
Carregue os dados com a função sns.load_dataset(’titanic’).
'''

import seaborn as sns
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import time
pd.options.display.float_format = '{:.2f}'.format

df = sns.load_dataset("titanic")
print("Dataset carregado.")
'''
Visualize as primeiras linhas do DataFrame através de .head() e verifique os tipos de
dados e a presença de valores nulos com os métodos .info() e .isnull().sum().
'''
print("================================")
print(df.head())
print("================================")
print(df.info())
print("================================")
print(df.isnull().sum())

'''
Para preparar os dados numéricos, filtre as variáveis quantitativas (age, fare, sibsp,
parch) e trate os valores ausentes de age substituindo-os pela mediana (método fillna).
'''
df_copy = df.copy()
df_numeros = ['age', 'fare', 'sibsp', 'parch']

df_copy['age'] = df_copy['age'].fillna(df_copy['age'].median())

'''
Calcule a matriz de Correlação de Pearson entre as variáveis numéricas selecionadas
utilizando o método corr(method=’pearson’) da biblioteca Pandas.
'''

corr = df_copy[df_numeros].corr(method='pearson')
print("================================")
print("Correlação de Pearson: ")
print(corr)

'''
Plote um mapa de calor (heatmap) da matriz de correlação com a biblioteca Seaborn,
exibindo os valores numéricos dos coeficientes nas células (annot=True) e utilizando a
paleta coolwarm.
'''
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Heatmap - Pearson - Titanic')
plt.show()


'''
Identifique o par de atributos numéricos com maior correlação linear (em módulo). Em
seguida, utilize a função pearsonr de scipy.stats para calcular o coeficiente r e o
respectivo p-valor.
'''
print("================================")
print("Pearson [parch - sibsp]")
pearsonr = stats.pearsonr(df_copy['sibsp'].dropna(), df_copy['parch'].dropna())
print("r = ", pearsonr[0])
print("p-value = ", pearsonr[1])

'''
Plote um gráfico de dispersão com reta de regressão linear para esse par selecionado
utilizando sns.regplot(). Interprete a relação quanto à sua direção, força e significância
estatística (α = 0,05).
'''
print("================================")
plt.figure(figsize=(8, 6))
sns.regplot(x='sibsp', y='parch', data=df_copy, line_kws={'color':'red'})
plt.title('Gráfico de Dispersão com reta de Regressão Linear- SibSp vs Parch')
plt.xlabel('SibSp')
plt.ylabel('Parch')
plt.legend([f"r = {pearsonr[0]:.2f}, p-valor = {pearsonr[1]:.4f}"])
plt.show()

print("================================")
print("Interpretação da relação: ")
print("A relação entre SibSp e Parch é positiva, \
indicando que, conforme o número de irmãos/cônjuges a bordo aumenta, \
o número de pais/filhos a bordo também tende a aumentar. \
O coeficiente r = {:.2f} sugere uma correlação moderada entre as duas variáveis. \
O p-valor = {:.4f} indica que a relação é estatisticamente significativa ao nível de significância α = 0,05.".format(pearsonr[0], pearsonr[1]))

'''
Para a análise de variáveis qualitativas, construa uma tabela de contingência (frequências
observadas) entre as colunas sex (sexo) e survived (sobrevivência) utilizando a função
pd.crosstab()
'''
print("================================")

df_contingencia = pd.crosstab(df_copy['sex'], df_copy['survived'])
print(df_contingencia.to_string())

'''
Aplique o Teste Qui-Quadrado de Independência sobre a tabela de contingência
com a função chi2_contingency de scipy.stats. Obtenha e exiba a estatística χ2, o
p-valor, os graus de liberdade e a matriz de frequências esperadas
'''
print("================================")
qui_quadrado = stats.chi2_contingency(df_contingencia)
x_quadrado, p_valor, graus_liberdade, frequencias_esperadas = qui_quadrado
print("χ2 = ", x_quadrado)
print("p-valor = ", p_valor)
print("Graus de liberdade = ", graus_liberdade)
print("Frequências esperadas = \n", frequencias_esperadas)

'''
Formule formalmente as hipóteses H0 (independência) e H1 (associação). Considerando
o nível de significância de 5% (α = 0,05) e o p-valor obtido no item anterior, apresente
sua conclusão: a taxa de sobrevivência dependeu do sexo do passageiro? Justifique.
'''
print("================================")
#h0: A taxa de sobrevivência é independente do sexo do passageiro.
#h1: A taxa de sobrevivência depende do sexo do passageiro.
print("H0: Taxa e sexo independentes.")
print("H1: Taxa e sexo dependentes.")
print("p-valor foi 1.1973570627755645e-58. Por ser muito menor que 0.05, a hipótese nula da independência é rejeitada. \
    Logo, é possível concluir que a taxa de sobrevivência depende do sexo do passageiro.")
# Pode-se comentar também sobre a possível razão para essa dependência,
# como o fato de que mulheres e crianças foram priorizadas durante os resgates.
