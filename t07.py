import numpy as np
from numpy.testing import assert_allclose

P = np.array([[0.7, 0.2, 0.6, 0.2],
              [0.6, 0.4, 0.0, 0.0],
              [0.5, 0.0, 0.5, 0.0],
              [0.0, 0.1, 0.8, 0.1]])

# Número total de veículos
total_veiculos = 1000

# Estimativa inicial da distribuição
distribution = np.array([total_veiculos, 0, 0, 0])

# Parâmetro de tolerância para considerar a distribuição estacionária
tolerance = 1e-6

while True:
    new_distribution = np.dot(distribution, P)
    
    # Verificar se a nova distribuição é idêntica à anterior
    if np.all(np.isclose(new_distribution, distribution, rtol=tolerance)):
        break

    distribution = new_distribution

# Normalizar a distribuição estacionária para que a soma seja igual ao número total de veículos
stationary_distribution = distribution / distribution.sum() * total_veiculos

print(stationary_distribution)
