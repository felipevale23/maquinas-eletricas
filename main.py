import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do motor
resistencia_armadura = 0.3  # Ohms
torque = 20  # N.m
tensao_terminal = np.linspace(0, 100, 1000) # V
k = 1.5

# Condições iniciais
velocidade = np.zeros_like(tensao_terminal)
velocidade[0] = 0  # velocidade inicial

corrente_armadura = np.zeros_like(tensao_terminal)
corrente_armadura[0] = 0

tensao_armadura = np.zeros_like(tensao_terminal)
tensao_armadura[0] = 0

# velocidade = (Ea x Ia) / Torque
# Ea = Vt - Ra*Ia = k * velocidade
# Ia = (Vt - Ea) / Ra 
# velocidade = (Vt / k) - (Ra / K**2) * torque

# Solução numérica
for i in range(0, len(tensao_terminal)):
    
    velocidade[i] = (tensao_terminal[i] / k) - (resistencia_armadura / k**2) * torque
    tensao_armadura[i] = k * velocidade[i]
    corrente_armadura[i] = ((tensao_terminal[i] - tensao_armadura[i]) / resistencia_armadura)

# Plot
fig = plt.figure(layout='constrained')
ax1 = fig.add_subplot()
ax1.plot(velocidade, tensao_terminal, color='b', label='Tensão de Terminal')
ax1.plot(velocidade, tensao_armadura, color='r', label='Tensão de Armadura')
ax1.plot(velocidade, corrente_armadura, color='k', label='Corrente de Armadura')

ax1.set_ylabel('Tensão (V)')
ax1.set_xlabel('Velocidade (rad/s)')
ax1.set_title('Operação de um motor CC com torque constante')
ax1.legend()

#ax2 = ax1.twinx() 
#ax2.plot(velocidade, corrente_armadura, color='k', label='Corrente de Armadura')
#ax2.tick_params(axis='y')
#ax2.set_ylabel('Corrente (A)') 
#ax2.legend()

fig.savefig('plot.png')
