import matplotlib.pyplot as plt
import numpy as np
#variant 6

x = np.linspace(-11,11,50)
y = np.linspace(-50,400,20)
y1 = 3*(x**2) + 3*x + 43
y2 = 2*(x**2) + 5*x + 36
y3 = 1*(x**2) + 6*x + 13
y4 = 2*(x**2) + 7*x + 26
x0 = 0*y
y0 = 0*x
plt.xlabel = 'x'
plt.ylabel = 'y'
plt.grid(axis='both')
plt.plot(x,y1, color = 'blue', marker = '+', linestyle = '--', markevery = 1)
plt.plot(x,y2, color = 'yellow', marker = 'X', linestyle = ':', markevery = 3)
plt.plot(x,y3, color = 'black', marker = 'D', linestyle = '-.', markevery = 7)
plt.plot(x,y4, color = 'green', marker = 'o', markevery = 3)

plt.plot(x,y0, color = 'black')
plt.plot(x0,y, color = 'black')
plt.xticks(range(-10,11,2))
plt.yticks(range(0,350,25))


plt.legend(['y1 = 3x^2 + 3x + 43', 
            'y2 = 2x^2 + 5x + 36', 
            'y3 = 1x^2 + 6x + 13',
            'y4 = 2x^2 + 7x + 26'], 
            loc= 'best', edgecolor = 'black')
plt.show()