import pandas as pd
import io ##pega uma string e transforma em um arquivo para o pandas ler, sem precisar criar um arquivo físico no disco
dados = '''concelho,ano,ganho_medio_mensal_euro
Guimarães,2023,1247
Braga,2023,1321
Famalicão,2023,1198
Vizela,2023,1156
Fafe,2023,1089
Porto,2023,1463
Lisboa,2023,1687
Coimbra,2023,1225'''

df = pd.read_csv(io.StringIO(dados))
print(df)
print("\n--- ESTATÍSTICAS ---")
print(df['ganho_medio_mensal_euro'].describe())

import matplotlib.pyplot as plt
##grafico de barras
plt.bar(df['concelho'], df['ganho_medio_mensal_euro'], color='red')
plt.xlabel('Concelho')
plt.ylabel('Ganho Médio Mensal (Euro)')
plt.title('Renda Média Mensal por Concelho')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('renda_mensal_concelhos.png', dpi=300, bbox_inches='tight') ##salvar o gráfico como imagem em alta qualidade
plt.show() ##continua mostrando o gráfico na tela
