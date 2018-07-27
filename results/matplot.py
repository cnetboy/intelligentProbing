import sys
sys.path.insert(0, '/home/efcastillo/ryu/ryu/app/intelligentProbing/tools/')
from bytes_to import *
import matplotlib.pyplot as plt
from os import scandir, getcwd
import os.path as path
import numpy as np
from numpy import *
import csv

#current position getcwd()

x = []
y = []
z = []

csv_file = 'speed_' + sys.argv[1] + '.csv'
csv_plot = 'speed_' + sys.argv[1] + '.png'

if not path.exists(csv_file):
        print("The file does not exist")
        sys.exit()

with open(csv_file,'r') as csvfile:
    plots = csv.DictReader(csvfile)
    for row in plots:
        x.append(int(row["Row"]))
        y.append(Bytes_to(int(row["TX"])))
        z.append(Bytes_to(int(row["RX"])))

plt.style.use('ggplot')
plt.subplot(2, 1, 1)
plt.plot(x,y, 'r', label='Controller-Switch')
#plt.plot(x,z, 'b', label='Loaded from file!')
plt.xlabel('Time (S)',fontsize=9)
plt.ylabel('Control channel load (kbps)',fontsize=9)
#plt.title('Interesting Graph\nCheck it out')
plt.legend()
#plt.show()

"""
xcoords = [1, 3.5, 4.5]
colors = ['r','k','b']

for xc,c in zip(xcoords,colors):
    plt.axvline(x=xc, label='line at x = {}'.format(xc), c=c)
"""

plt.subplot(2, 1, 2)
plt.plot(x,z, 'b', label='Switch-Controller')
plt.xlabel('Time (S)',fontsize=9)
plt.ylabel('Control channel load (kbps)', fontsize=9)
#plt.title('Interesting Graph\nCheck it out')
plt.legend()

plt.tight_layout()
#plt.savefig(csv_plot, dpi=300)

#plt.fill_between(x, z, color='c', alpha=0.2, linewidth=0,)
#plt.axvspan(270, 600, ymin=0.0, ymax=0.6, alpha=0.5, color='red')

# shaded area
sixty = [50<x<200 for x in x]
ninety = [250<x<400 for x in x]
plt.fill_between(x,0,z,where=sixty,color='g',alpha=0.15)
plt.fill_between(x,0,z,where=ninety,color='g',alpha=0.15)


# Annotate plot with integral results
#xy -> where the arrow points
#xytext -> where the annotation text is located
style = dict(size=10, color='gray')
plt.annotate('Text', xy=(200, 1000), xytext=(250, 500),
            arrowprops=dict(facecolor='black', shrink=0.05))


#plt.text(200, 450, "Independence Day", ha='center', **style)
#plt.savefig(csv_plot, dpi=300)
plt.show()
