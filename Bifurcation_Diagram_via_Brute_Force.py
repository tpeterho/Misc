import numpy as np
import matplotlib.pyplot as plt

#def x_dot(u,x):
#    return np.exp(-x**2 / (u**2)) - (u * np.sin(x * u)) / (x**2 + np.cos(u * x)**2)

def x_dot(u,x):
    return x*(1-x)-u*(2*x)/(1+2*x)

u_stable_ij = []
x_stable_ij = []
u_unstable_ij = []
x_unstable_ij = []
u_stable_ji = []
x_stable_ji = []
u_unstable_ji = []
x_unstable_ji = []

error = 1e-1
step_size = 1e-2
epsilon = 1e-4

i_min = -20
i_max = 20
j_min = -20
j_max = 20

j = j_min
while j <= j_max:
    i = i_min
    while i <= i_max:
        if abs(x_dot(i,j)) < error:
            if ((x_dot(i,j+epsilon) > 0) and (x_dot(i,j-epsilon) < 0)):
                u_unstable_ij.append(i)
                x_unstable_ij.append(j)
                u_unstable_ji.append(j)
                x_unstable_ji.append(i)
                break
            elif ((x_dot(i,j+epsilon) < 0) and (x_dot(i,j-epsilon) > 0)):
                u_stable_ij.append(i)
                x_stable_ij.append(j)
                u_stable_ji.append(j)
                x_stable_ji.append(i)
                break
        i += step_size
    j += step_size

plt.figure(figsize=(10,10))
plt.title('Bifurcation Diagram',size=20)

plt.xlabel('$\mu$',size=20)
plt.ylabel('$x$',size=20)
plt.xlim(i_min,i_max)
plt.ylim(j_min,j_max)

plt.axhline(y=0,color='k',lw=0.5)
plt.axvline(x=0,color='k',lw=0.5)
                  
plt.plot(u_unstable_ij,x_unstable_ij,'.',color='r',ms=3,label='unstable')
plt.plot(u_stable_ij,x_stable_ij,'.',color='k',ms=3,label='stable')
plt.plot(np.negative(u_unstable_ji),np.negative(x_unstable_ji),'.',color='r',ms=3)
plt.plot(u_stable_ji,x_stable_ji,'.',color='k',ms=3)

plt.grid(True)
plt.legend(fontsize=10,markerscale=4,title='Stability',title_fontsize=10,edgecolor='inherit')

