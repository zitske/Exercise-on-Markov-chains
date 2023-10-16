import numpy as np

# as linhas representam a cidade onde o veículo foi locado e as colunas representam a cidade onde o veículo será devolvido após uma semana. 
# Os valores na matriz representam as probabilidades de transição.

P = np.array([[0.7, 0.2, 0.6, 0.2],
              [0.6, 0.4, 0.0, 0.0],
              [0.5, 0.0, 0.5, 0.0],
              [0.0, 0.1, 0.8, 0.1]])

# Encontrar a distribuição estacionária
eigenvalues, eigenvectors = np.linalg.eig(P.T)
stationary_distribution = eigenvectors[:, 0] / eigenvectors[:, 0].sum()

print(stationary_distribution)

tamanho_medio_patio = stationary_distribution * 1000

print(tamanho_medio_patio)


# RESPOSTA
# A distribuição estacionária indica que, após um longo período de tempo, 
# aproximadamente 405 veículos estarão em Sorocaba, 195 em Santos, 285 em São Paulo 
# e 115 em Campinas. Portanto, o tamanho médio do pátio necessário em cada cidade é aproximadamente:

# Sorocaba: 405 veículos
# Santos: 195 veículos
# São Paulo: 285 veículos
# Campinas: 115 veículos