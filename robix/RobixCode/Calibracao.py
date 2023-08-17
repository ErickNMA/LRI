#%%
import matplotlib.pyplot as plt
import numpy as np

theta1Off = 81
theta1Cmd = np.array([1400, 721, -660, -1400])
theta1Ang = np.array([64.3, 28.4, -36.2, -74.3])

theta2Off = -175
theta2Cmd = np.array([1400, 575, -960, -1400])
theta2Ang = np.array([73, 36.2, -39.4, -61.6])

theta3Off = 461
theta3Cmd = np.array([1400, 931, -90, -1400])
theta3Ang = np.array([46.9, 21.8, -27.8, -92.6])

polinomio1 = np.polyfit(theta1Ang, theta1Cmd, 1)
polinomio2 = np.polyfit(theta2Ang, theta2Cmd, 1)
polinomio3 = np.polyfit(theta3Ang, theta3Cmd, 1)

fig, ax = plt.subplots(1, 1, constrained_layout=True)
ax.set_title("Relação entre ângulos das juntas e o valor enviado", fontsize=14)
ax.plot(theta1Ang, theta1Cmd, label='Theta 1', linewidth=2)
ax.plot(theta2Ang, theta2Cmd, label='Theta 2', linewidth=2)
ax.plot(theta3Ang, theta3Cmd, label='Theta 3', linewidth=2)
ax.set_xlabel("Ângulo das juntas(°)", fontsize=12)
ax.set_ylabel("Valor enviado pelo terminal", fontsize=12)
ax.set_xlim(-100, 75)
ax.set_ylim(-1500, 1500)
ax.scatter(theta1Ang, theta1Cmd, s=40)
ax.scatter(theta2Ang, theta2Cmd, s=40)
ax.scatter(theta3Ang, theta3Cmd, s=40)
ax.grid()
ax.legend(fontsize=12)
plt.show()

X = [0, 0, 0]

theta1 = polinomio1[0]*X[0] + polinomio1[1]
theta2 = polinomio2[0]*X[1] + polinomio2[1]
theta3 = polinomio3[0]*X[2] + polinomio3[1]

print(theta1)
print(theta2)
print(theta3)