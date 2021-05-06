import matplotlib.pyplot as plt
import numpy as np


x = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
     'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
y = [2, 3, 27, 42, 30, 11, 12, 32, 14, 21, 10, 12]
z = [20 , 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]

plt.title('Vendas por mês')
plt.xlabel('Mês')
plt.ylabel('Volume de Vendas')
plt.plot(x, y)
plt.plot(x, z)
plt.show()
