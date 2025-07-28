import numpy as np 
import matplotlib.pyplot as plt
import random as rd

theta = np.linspace(0, 2*np.pi, 100)

r = np.sqrt(1.0)

x1 = r*np.cos(theta)
x2 = r*np.sin(theta)

fig, ax = plt.subplots(1)

ax.plot(x1, x2)
ax.set_aspect(1)
ax.fill_between(x1, x2, alpha=0.2)

plt.xlim(-1.00, 1.00)
plt.ylim(-1.00, 1.00)

plt.savefig("cir.png", bbox_inches='tight')

print("Método monte carlo...")
pontos_dentro = 0

for i in range(1,10001):
    x = rd.uniform(-1, 1)
    y = rd.uniform(-1, 1)
    if(x*x + y*y <= 1):
        plt.scatter(x,y, s=3, c="blue")
        pontos_dentro += 1
    else:
        plt.scatter(x,y, s=3, c="red")

pi = 4 * pontos_dentro / i

plt.savefig("cir2.png", bbox_inches='tight')

print(f"Valor de PI: {pi}")