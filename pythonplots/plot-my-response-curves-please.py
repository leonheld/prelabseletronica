"""
stuff I used: MikTeX (all text is rendered with LaTeX). Also, you gotta manually save the figure bc of backend bug in matplotlib.
"""
import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
freq = [0, 10, 20, 50, 100, 200, 500, 1000, 5000, 10000]
integrador_com_perdas_phase = list()
integrador_com_perdas_mag = list()

for i in range(len(freq)):
    integrador_com_perdas_mag.append(20 * math.log10( 10 * 1 /(math.sqrt(math.pow((2 * math.pi), 2) * math.pow(freq[i], 2) * math.pow(6.8E-9, 2) * math.pow(100E3, 2) + 1))))
    integrador_com_perdas_phase.append(math.degrees(math.pi - math.atan((2.0 * math.pi * freq[i] * 100E3 * 6.8E-9))))

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = [
    r'\usepackage{amsmath}',
    r'\usepackage{amssymb}']
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Computer Modern'
plt.figure(0)

plt.plot(freq, integrador_com_perdas_phase, linestyle='--', marker='o', color='b', lw=2)
#plt.plot(freq, integrador_com_perdas_expr, linestyle='--', marker='x', color='r', lw=2)
plt.xscale('log')

plt.xlabel('Frequência $f$ [Hz]', fontsize = 14)
#plt.ylabel('Ganho $\mathfrak{G}(j\omega)$ [dB]', fontsize = 14)
plt.ylabel('Fase $\phi(f)$ [Graus]', fontsize = 14)

for xy in zip(freq, integrador_com_perdas_phase):
    plt.annotate('(%s, %s)' % xy, xy = xy, textcoords = 'data') 

plt.suptitle('Integrador com perdas', fontsize = 20)

manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())

plt.savefig("intperdasfase.pdf", dpi = 100)

plt.show()
