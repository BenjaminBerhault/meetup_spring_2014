# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Plot util

# <codecell>

%%writefile smash.py


try:
	from IPython.core.getipython import get_ipython
	from matplotlib.figure import Figure
except ImportError:
	raise ImportError('This feature requires IPython 1.0+ and Matplotlib')
    
def print_fig(fig):
	for ax in fig.axes:
		for s in ['bottom', 'left', 'top', 'right']:
			ax.spines[s].set_linewidth(0.7)
			ax.spines[s].set_color('grey')  

		for s in ['top','right']:
			ax.spines[s].set_visible(False)
	        
		ax.patch.set_facecolor('1.0')
		ax.grid(False)

		ax.tick_params(direction='out', 
		               length=10, 
		               width=1., 
		               colors='grey',
		               bottom='on',
		               top='off', 
		               left='on', 
		               right='off',
		               pad=12
		               )
		
		if ax.legend_ is not None:
			ax.legend_.get_frame().set_linewidth(0)
			ax.legend_.get_frame().set_alpha(0.5)

ip = get_ipython()
formatter = ip.display_formatter.formatters['text/html']
formatter.for_type(Figure, print_fig)

# <codecell>

import os

directory = os.path.join(os.environ['HOME'],'.matplotlib')

if not os.path.exists(directory):
    os.makedirs(directory)
    print 'creating', directory
else:
    print directory, 'exists'

# <codecell>

filename = os.path.join(directory,'matplotlibrc')
print filename

# <codecell>

with open(filename,'w') as outfile:
    outfile.write('''
patch.linewidth: 0.5
patch.facecolor: 348ABD
patch.facecolor: white

patch.edgecolor: EEEEEE
patch.antialiased: True

font.size: 10.0

axes.facecolor: white
axes.edgecolor: white
axes.linewidth: 1
axes.grid: True
axes.titlesize: x-large
axes.labelsize: large
axes.labelcolor: 555555
axes.axisbelow: True       # grid/ticks are below elements (eg lines, text)

axes.color_cycle: E24A33, 348ABD, 988ED5, 777777, FBC15E, 8EBA42, FFB5B8
                   # E24A33 : red
                   # 348ABD : blue
                   # 988ED5 : purple
                   # 777777 : gray
                   # FBC15E : yellow
                   # 8EBA42 : green
                   # FFB5B8 : pink

xtick.color: 555555
xtick.direction: out

ytick.color: 555555
ytick.direction: out

grid.color: white
grid.linestyle: -    # solid line

figure.facecolor: white
figure.edgecolor: 0.50

legend.scatterpoints: 1
legend.frameon: True''')

# <codecell>


