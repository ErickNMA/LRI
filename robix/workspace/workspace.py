import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mc
import scienceplots

# Configurações de plot:
plt.style.use([
    'grid',
    'retro'
])
plt.rcParams['lines.linewidth'] = 3
plt.rcParams['font.size'] = 20
plt.rcParams['figure.figsize'] = (12, 8)

lim_j1 = [-74.3, 64.3]
lim_j2 = [-61.6, 73]
lim_j3 = [-92.6, 46.9]

ppg = 0.5 #pontos por grau

joints = [
    np.radians(np.linspace(lim_j1[0], lim_j1[1], int((lim_j1[1]-lim_j1[0])*ppg))),
    np.radians(np.linspace(lim_j2[0], lim_j2[1], int((lim_j2[1]-lim_j2[0])*ppg))),
    np.radians(np.linspace(lim_j3[0], lim_j3[1], int((lim_j3[1]-lim_j3[0])*ppg)))
]

points = []

for j1 in joints[0]:
    for j2 in joints[1]:
        for j3 in joints[2]:
            x = ((79*np.cos(j1))+((2*np.cos(j1-j2))*((52*np.cos(j3))+(5*np.sin(j3))))+(76*np.cos(j1-j2))+(30*np.sin(j1-j2)))
            y = ((-79*np.sin(j1))-((2*np.sin(j1-j2))*((52*np.cos(j3))+(5*np.sin(j3))))-(76*np.sin(j1-j2))+(30*np.cos(j1-j2)))
            z = (137+(104*np.sin(j3))-(10*np.cos(j3)))
            points.append([x, y, z])

points = np.array(points)

#Vista lateral:
plt.figure('Espaço de Trabalho: Vista Lateral')
plt.scatter(points[:, 0], points[:, 2], color='C1')
plt.arrow(x=0, y=0, dx=48, dy=0, linewidth=2, color='red', head_length=4.8,head_width=3.2)
plt.arrow(x=0, y=0, dx=0, dy=32, linewidth=2, color='blue', head_length=3.2,head_width=4.8)
plt.xlabel('X [mm]')
plt.ylabel('Z [mm]')
plt.xlim(-300, 300)
plt.ylim(-5, 250)
plt.savefig('vista_lateral.eps', dpi=600, transparent=True, bbox_inches='tight')
plt.show()

#Vista Superior:
plt.figure('Espaço de Trabalho: Vista Superior')
plt.scatter(points[:, 0], points[:, 1], color='C2')
plt.arrow(x=0, y=0, dx=32, dy=0, linewidth=2, color='red', head_length=3.2,head_width=4.8)
plt.arrow(x=0, y=0, dx=0, dy=48, linewidth=2, color='green', head_length=4.8,head_width=3.2)
plt.xlabel('X [mm]')
plt.ylabel('Y [mm]')
plt.xlim(-300, 300)
plt.ylim(-300, 300)
plt.savefig('vista_superior.eps', dpi=600, transparent=True, bbox_inches='tight')
plt.show()

#Parnorâmica:
ccmp1 = mc.LinearSegmentedColormap.from_list('custom', ['C4', 'C5', 'C6'])
ax = plt.figure('Espaço de Trabalho Tridimensional').add_subplot(projection='3d')
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=points[:, 2], cmap=ccmp1, antialiased=False)
ax.set_xlabel('X [mm]')
ax.set_ylabel('Y [mm]')
ax.set_zlabel('Z [mm]')
ax.set_xticks([0], [''])
ax.set_yticks([0], [''])
ax.set_zticks([0], [''])
ax.set_xlim(-300, 300)
ax.set_ylim(-300, 300)
ax.set_zlim(0, 250)
ax.view_init(elev=30, azim=0, roll=0)
plt.savefig('perspectiva.eps', dpi=600, transparent=True, bbox_inches='tight')
plt.show()