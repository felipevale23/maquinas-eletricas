import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do motor
potencia = 1000
tensao_terminal = 100 # V
resistencia_armadura = 0.3  # Ohms
corrente_armadura = potencia / tensao_terminal  # Ohms
tensao_armadura = tensao_terminal -  corrente_armadura * resistencia_armadura

resistencia_campo = np.linspace(0.1, 1, 1000)
k = 1.5

# Condições iniciais
velocidade = np.zeros_like(resistencia_campo)
velocidade[0] = 0  # velocidade inicial

corrente_campo = np.zeros_like(resistencia_campo)
corrente_campo[0] = 0


# velocidade = (Ea x Ia) / Torque
# Ea = Vt - Ra*Ia = k * velocidade
# Ia = (Vt - Ea) / Ra 
# velocidade = (Vt / k) - (Ra / K**2) * torque

# Solução numérica
for i in range(0, len(resistencia_campo)):
    
    corrente_campo[i] = tensao_terminal / resistencia_campo[i]
    
    velocidade[i] = ((tensao_terminal / k*corrente_campo[i]) - np.sqrt(((tensao_terminal / k*corrente_campo[i])**2)-4*((resistencia_armadura / (k*corrente_campo[i])**2)) * corrente_armadura * tensao_armadura))/2
    

# Plot
fig = plt.figure(layout='constrained')
ax1 = fig.add_subplot()
ax1.plot(velocidade, corrente_campo, color='b', label='Tensão de Terminal')

ax1.set_ylabel('Velocidade (Rad/s)')
ax1.set_xlabel('Corrente de Campo(A)')
ax1.set_title('Operação de um motor CC com potência constante')
ax1.legend()

#ax2 = ax1.twinx() 
#ax2.plot(velocidade, corrente_armadura, color='k', label='Corrente de Armadura')
#ax2.tick_params(axis='y')
#ax2.set_ylabel('Corrente (A)') 
#ax2.legend()

fig.savefig('plot.png')
