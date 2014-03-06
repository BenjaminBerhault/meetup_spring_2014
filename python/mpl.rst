
Data Visualization with ``matplotlib``
======================================

Monte Lunacek



Objectives
----------

-  Understand the different between ``pylab`` and ``pyplot``.
-  Understand the basic components of a plot.
-  Understand style
-  Give you enough information to use the
   `gallery <http://matplotlib.org/gallery#>`__.
-  Reference for several standard plots.

   -  histogram, density, boxplot (when appropriate)
   -  scatter, line, hexbin
   -  contour, false-color



References
----------

This tutorial based on some of the following excellent content.

-  `J.R. Johansson's
   tutorial <http://nbviewer.ipython.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb>`__
-  `Matplotlib tutorial by Jake
   Vanderplas <http://jakevdp.github.io/mpl_tutorial/>`__
-  `Nicolas P. Rougier's
   tutorial <http://www.loria.fr/~rougier/teaching/matplotlib/>`__
-  `Painless create beautiful
   matplotlib <http://blog.olgabotvinnik.com/post/58941062205/prettyplotlib-painlessly-create-beautiful-matplotlib>`__
-  `Making matplotlib look like
   ggplot <http://messymind.net/2012/07/making-matplotlib-look-like-ggplot/>`__
-  https://github.com/jakevdp/mpld3
-  `Harvard CS109 Data Science
   Class <http://nbviewer.ipython.org/github/cs109/content/blob/master/lec_03_statistical_graphs.ipynb>`__.


Object and Functional Models
----------------------------

**Functional**

-  Emulate ``Matlab``
-  Convension: *implicit state*

   ::

       from pylab import *

**Object-oriented**

-  Not a flat model.
-  ``Figure``, ``Axes``

   ::

       import matplotlib.pyplot as plt

Caution: redundant interface, namespace issues

Enabling plotting
-----------------

**IPython terminal**

::

    ipython --pylab
    ipython --matplotlib

**IPython notebook**

::

    %pylab inline
    %matplotlib inline

    ipython notebook --pylab=inline
    ipython notebook --matplotlib=inline


The funtional ``pylab`` interface
---------------------------------

-  Loads all of ``numpy`` and ``matplotlib`` into the global namesapce.
-  Great for interactive use.


.. code:: python

    #inline to use with notebook (from pylab import *) 
    %pylab inline 

.. parsed-literal::

    Populating the interactive namespace from numpy and matplotlib


.. code:: python

    # make the plots smaller
    rcParams['figure.figsize'] = 8, 4
.. code:: python

    x = linspace(0, 2*pi, 100)
    y = np.sin(x)
    plot(x, y)
    show()


.. image:: mpl_files/mpl_8_0.png


.. code:: python

    hist(randn(1000), alpha=0.5, histtype='stepfilled')
    hist(0.75*randn(1000)+1, alpha=0.5, histtype='stepfilled') #hist?
    show()


.. image:: mpl_files/mpl_9_0.png


.. code:: python

    #hist?
Quick, easy, simple plots.

Object-oriented ``pyplot`` interface
------------------------------------

-  No global variables
-  Separates style from graph
-  Can easily have multiple subplots


.. code:: python

    #restart notebook
    %matplotlib inline
    import matplotlib.pyplot as plt
    import numpy as np
.. code:: python

    import matplotlib as mpl
    mpl.rcParams['figure.figsize'] = 8, 4
.. code:: python

    plot(range(20))

::


    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)

    <ipython-input-3-d0d4e9792ae1> in <module>()
    ----> 1 plot(range(20))
    

    NameError: name 'plot' is not defined


Good, that's the error we want to see.

The ``figures`` and ``axes`` objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, we create a blank figure. Then we add a subpot.

.. code:: python

    x = np.linspace(0, 2*np.pi, 100) #same as before
    y = np.sin(x)
    
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1) # 1 row, 1 col, graphic 1
    ax.plot(x, y)
    fig.show()


.. image:: mpl_files/mpl_18_0.png


Multiple subplots
~~~~~~~~~~~~~~~~~


.. code:: python

    fig = plt.figure()
    
    ax1 = fig.add_subplot(1,2,1) # 1 row, 2 cols, graphic 1
    ax2 = fig.add_subplot(1,2,2) # graphic 2
    
    ax1.plot(x, y)
    
    ax2.hist(np.random.randn(1000), alpha=0.5, histtype='stepfilled')
    ax2.hist(0.75*np.random.randn(1000)+1, alpha=0.5, histtype='stepfilled')
    
    fig.show()


.. image:: mpl_files/mpl_20_0.png


The ``plt.subplots()`` command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    fig, ax = plt.subplots(2,3)
    
    ax[0,0].plot(x, y)
    ax[0,2].hist(np.random.randn(100), alpha=0.5, color="g")
    ax[1,1].scatter(np.random.randn(10), np.random.randn(10), color="r")
    
    fig.show()


.. image:: mpl_files/mpl_22_0.png


plt.plot?

::

    ==========  ========
    character   color
    ==========  ========
    'b'         blue
    'g'         green
    'r'         red
    'c'         cyan
    'm'         magenta
    'y'         yellow
    'k'         black
    'w'         white
    ==========  ========


The ``subplot2grid`` command
----------------------------


.. code:: python

    fig = plt.figure(figsize=(8,6))
    ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
    ax2 = plt.subplot2grid((3,3), (1,0), colspan=2)
    ax3 = plt.subplot2grid((3,3), (1,2), rowspan=2)
    ax4 = plt.subplot2grid((3,3), (2,0))
    ax5 = plt.subplot2grid((3,3), (2,1))
    fig.tight_layout()
    fig.show()


.. raw:: html

    
    <style>
    
    </style>
    
    <div id="fig1324144129893928944055602"></div>
    <script>
    function mpld3_load_lib(url, callback){
      var s = document.createElement('script');
      s.src = url;
      s.async = true;
      s.onreadystatechange = s.onload = callback;
      s.onerror = function(){console.warn("failed to load library " + url);};
      document.getElementsByTagName("head")[0].appendChild(s);
    }
    
    function create_fig1324144129893928944055602(){
      
      mpld3.draw_figure("fig1324144129893928944055602", {"width": 640.0, "axes": [{"xlim": [0.0, 1.0], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [], "zoomable": true, "images": [], "xdomain": [0.0, 1.0], "ylim": [0.0, 1.0], "paths": [], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"grid": {"gridOn": false}, "position": "bottom", "nticks": 6, "tickvalues": null, "tickformat": null}, {"grid": {"gridOn": false}, "position": "left", "nticks": 6, "tickvalues": null, "tickformat": null}], "lines": [], "markers": [], "id": "132414412985744", "ydomain": [0.0, 1.0], "collections": [], "xscale": "linear", "bbox": [0.051426866319444445, 0.7050925925925926, 0.91740858289930549, 0.25949074074074074]}, {"xlim": [0.0, 1.0], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [], "zoomable": true, "images": [], "xdomain": [0.0, 1.0], "ylim": [0.0, 1.0], "paths": [], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"grid": {"gridOn": false}, "position": "bottom", "nticks": 6, "tickvalues": null, "tickformat": null}, {"grid": {"gridOn": false}, "position": "left", "nticks": 6, "tickvalues": null, "tickformat": null}], "lines": [], "markers": [], "id": "132414412931984", "ydomain": [0.0, 1.0], "collections": [], "xscale": "linear", "bbox": [0.051426866319444445, 0.38009259259259265, 0.5903252495659721, 0.25949074074074063]}, {"xlim": [0.0, 1.0], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [], "zoomable": true, "images": [], "xdomain": [0.0, 1.0], "ylim": [0.0, 1.0], "paths": [], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"grid": {"gridOn": false}, "position": "bottom", "nticks": 6, "tickvalues": null, "tickformat": null}, {"grid": {"gridOn": false}, "position": "left", "nticks": 6, "tickvalues": null, "tickformat": null}], "lines": [], "markers": [], "id": "132414393674064", "ydomain": [0.0, 1.0], "collections": [], "xscale": "linear", "bbox": [0.70559353298611116, 0.055092592592592693, 0.26324191623263882, 0.58449074074074059]}, {"xlim": [0.0, 1.0], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [], "zoomable": true, "images": [], "xdomain": [0.0, 1.0], "ylim": [0.0, 1.0], "paths": [], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"grid": {"gridOn": false}, "position": "bottom", "nticks": 6, "tickvalues": null, "tickformat": null}, {"grid": {"gridOn": false}, "position": "left", "nticks": 6, "tickvalues": null, "tickformat": null}], "lines": [], "markers": [], "id": "132414413062672", "ydomain": [0.0, 1.0], "collections": [], "xscale": "linear", "bbox": [0.051426866319444445, 0.055092592592592693, 0.26324191623263876, 0.25949074074074063]}, {"xlim": [0.0, 1.0], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [], "zoomable": true, "images": [], "xdomain": [0.0, 1.0], "ylim": [0.0, 1.0], "paths": [], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"grid": {"gridOn": false}, "position": "bottom", "nticks": 6, "tickvalues": null, "tickformat": null}, {"grid": {"gridOn": false}, "position": "left", "nticks": 6, "tickvalues": null, "tickformat": null}], "lines": [], "markers": [], "id": "132414413195920", "ydomain": [0.0, 1.0], "collections": [], "xscale": "linear", "bbox": [0.37851019965277771, 0.055092592592592693, 0.26324191623263887, 0.25949074074074063]}], "data": {}, "id": "132414412989392", "toolbar": ["reset", "move"], "height": 480.0});
    }
    
    if(typeof(mpld3) !== "undefined"){
       // already loaded: just create the figure
       create_fig1324144129893928944055602();
    }else if(typeof define === "function" && define.amd){
       // require.js is available: use it to load d3/mpld3
       require.config({paths: {d3: "http://d3js.org/d3.v3.min"}});
       require(["d3"], function(d3){
          window.d3 = d3;
          mpld3_load_lib("http://mpld3.github.io/js/mpld3.v0.1.js", create_fig1324144129893928944055602);
        });
    }else{
        // require.js not available: dynamically load d3 & mpld3
        mpld3_load_lib("http://d3js.org/d3.v3.min.js", function(){
            mpld3_load_lib("http://mpld3.github.io/js/mpld3.v0.1.js", create_fig1324144129893928944055602);})
    }
    </script>


Sharing axis values
~~~~~~~~~~~~~~~~~~~


.. code:: python

    fig, axes = plt.subplots( 3, 1, sharex = True)
    for ax in axes:
        ax.set_axis_bgcolor('0.95')
    fig.show()
    print axes.shape

.. parsed-literal::

    (3,)



.. image:: mpl_files/mpl_27_1.png


.. code:: python

    fig, axes = plt.subplots( 2, 2, sharex = True, sharey = True)
    plt.subplots_adjust( wspace = 0.1, hspace = 0.1)
    fig.show()
    print axes.shape

.. parsed-literal::

    (2, 2)



.. image:: mpl_files/mpl_28_1.png


How about a little ``d3.js`` with ``mpld3``?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

https://github.com/jakevdp/mpld3

.. code:: python

    from mpld3 import enable_notebook
    enable_notebook()
.. code:: python

    fig, ax = plt.subplots(1,2, sharey=True, sharex=True)
    
    print ax.shape
    
    ax[0].plot(x, y, color='green')
    ax[1].scatter(np.random.randn(10), np.random.randn(10), color='red')
    
    fig.show()

.. parsed-literal::

    (2,)



.. raw:: html

    
    <style>
    
    </style>
    
    <div id="fig1324144131150242021881580"></div>
    <script>
    function mpld3_load_lib(url, callback){
      var s = document.createElement('script');
      s.src = url;
      s.async = true;
      s.onreadystatechange = s.onload = callback;
      s.onerror = function(){console.warn("failed to load library " + url);};
      document.getElementsByTagName("head")[0].appendChild(s);
    }
    
    function create_fig1324144131150242021881580(){
      
      mpld3.draw_figure("fig1324144131150242021881580", {"width": 640.0, "axes": [{"xlim": [-2.0, 7.0], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [], "zoomable": true, "images": [], "xdomain": [-2.0, 7.0], "ylim": [-1.5, 1.5], "paths": [], "sharey": ["132414409872080"], "sharex": ["132414409872080"], "axesbgalpha": null, "axes": [{"grid": {"gridOn": false}, "position": "bottom", "nticks": 10, "tickvalues": null, "tickformat": null}, {"grid": {"gridOn": false}, "position": "left", "nticks": 7, "tickvalues": null, "tickformat": null}], "lines": [{"color": "#008000", "yindex": 1, "coordinates": "data", "dasharray": "10,0", "zorder": 2, "alpha": 1, "xindex": 0, "linewidth": 1.0, "data": "data01", "id": "132414394075344"}], "markers": [], "id": "132414413100880", "ydomain": [-1.5, 1.5], "collections": [], "xscale": "linear", "bbox": [0.125, 0.099999999999999978, 0.35227272727272724, 0.80000000000000004]}, {"xlim": [-2.0, 7.0], "yscale": "linear", "axesbg": "#FFFFFF", "texts": [], "zoomable": true, "images": [], "xdomain": [-2.0, 7.0], "ylim": [-1.5, 1.5], "paths": [], "sharey": ["132414413100880"], "sharex": ["132414413100880"], "axesbgalpha": null, "axes": [{"grid": {"gridOn": false}, "position": "bottom", "nticks": 10, "tickvalues": null, "tickformat": null}, {"grid": {"gridOn": false}, "position": "left", "nticks": 7, "tickvalues": null, "tickformat": ""}], "lines": [], "markers": [], "id": "132414409872080", "ydomain": [-1.5, 1.5], "collections": [{"paths": [[[[0.0, -0.5], [0.13260155, -0.5], [0.25978993539242673, -0.44731684579412084], [0.3535533905932738, -0.3535533905932738], [0.44731684579412084, -0.25978993539242673], [0.5, -0.13260155], [0.5, 0.0], [0.5, 0.13260155], [0.44731684579412084, 0.25978993539242673], [0.3535533905932738, 0.3535533905932738], [0.25978993539242673, 0.44731684579412084], [0.13260155, 0.5], [0.0, 0.5], [-0.13260155, 0.5], [-0.25978993539242673, 0.44731684579412084], [-0.3535533905932738, 0.3535533905932738], [-0.44731684579412084, 0.25978993539242673], [-0.5, 0.13260155], [-0.5, 0.0], [-0.5, -0.13260155], [-0.44731684579412084, -0.25978993539242673], [-0.3535533905932738, -0.3535533905932738], [-0.25978993539242673, -0.44731684579412084], [-0.13260155, -0.5], [0.0, -0.5]], ["M", "C", "C", "C", "C", "C", "C", "C", "C", "Z"]]], "edgecolors": ["#FF0000"], "edgewidths": [1.0], "offsets": "data02", "yindex": 1, "id": "132414393883984", "pathtransforms": [[4.969039949999533, 0.0, 0.0, 4.969039949999533, 0.0, 0.0]], "pathcoordinates": "display", "offsetcoordinates": "data", "zorder": 1, "xindex": 0, "alphas": [null], "facecolors": ["#FF0000"]}], "xscale": "linear", "bbox": [0.54772727272727262, 0.099999999999999978, 0.35227272727272729, 0.80000000000000004]}], "data": {"data02": [[-0.20550261855314667, 0.9458039613313609], [-0.9101847311761952, -0.10522597883106194], [-0.8716043626684341, 1.1654690446022378], [1.083120603437884, 1.2970989974845384], [-0.7246627324526638, -0.36634959731512146], [-0.5652108270999734, 1.0462898144160877], [0.9775321155594898, -0.3387240447605498], [-0.6289532294329799, 0.658760702075893], [-1.1013118767852932, 0.20596891036036072], [-0.5323764515488499, -0.18695097315258277]], "data01": [[0.0, 0.0], [0.06346651825433926, 0.0634239196565645], [0.12693303650867852, 0.12659245357374926], [0.1903995547630178, 0.18925124436041021], [0.25386607301735703, 0.2511479871810792], [0.3173325912716963, 0.31203344569848707], [0.3807991095260356, 0.3716624556603276], [0.4442656277803748, 0.42979491208917164], [0.5077321460347141, 0.4861967361004687], [0.5711986642890533, 0.5406408174555976], [0.6346651825433925, 0.5929079290546404], [0.6981317007977318, 0.6427876096865393], [0.7615982190520711, 0.690079011482112], [0.8250647373064104, 0.7345917086575333], [0.8885312555607496, 0.7761464642917568], [0.9519977738150889, 0.8145759520503357], [1.0154642920694281, 0.8497254299495144], [1.0789308103237674, 0.8814533634475821], [1.1423973285781066, 0.9096319953545183], [1.2058638468324459, 0.9341478602651068], [1.269330365086785, 0.9549022414440739], [1.3327968833411243, 0.9718115683235417], [1.3962634015954636, 0.984807753012208], [1.4597299198498028, 0.9938384644612541], [1.5231964381041423, 0.998867339183008], [1.5866629563584815, 0.9998741276738751], [1.6501294746128208, 0.9968547759519424], [1.71359599286716, 0.9898214418809327], [1.7770625111214993, 0.9788024462147787], [1.8405290293758385, 0.963842158559942], [1.9039955476301778, 0.9450008187146685], [1.967462065884517, 0.9223542941045814], [2.0309285841388562, 0.8959937742913359], [2.0943951023931957, 0.8660254037844386], [2.1578616206475347, 0.8325698546347714], [2.221328138901874, 0.795761840530832], [2.284794657156213, 0.7557495743542584], [2.3482611754105527, 0.7126941713788628], [2.4117276936648917, 0.6667690005162916], [2.475194211919231, 0.6181589862206051], [2.53866073017357, 0.5670598638627709], [2.6021272484279097, 0.5136773915734063], [2.6655937666822487, 0.4582265217274105], [2.729060284936588, 0.4009305354066136], [2.792526803190927, 0.3420201433256689], [2.8559933214452666, 0.2817325568414296], [2.9194598396996057, 0.2203105327865408], [2.982926357953945, 0.15800139597334986], [3.0463928762082846, 0.09505604330418244], [3.1098593944626236, 0.031727933498067656], [3.173325912716963, -0.03172793349806785], [3.236792430971302, -0.09505604330418263], [3.3002589492256416, -0.15800139597335008], [3.3637254674799806, -0.22031053278654059], [3.42719198573432, -0.28173255684142984], [3.490658503988659, -0.34202014332566866], [3.5541250222429985, -0.40093053540661383], [3.6175915404973376, -0.4582265217274103], [3.681058058751677, -0.5136773915734064], [3.744524577006016, -0.5670598638627706], [3.8079910952603555, -0.6181589862206053], [3.8714576135146945, -0.6667690005162915], [3.934924131769034, -0.7126941713788628], [3.998390650023373, -0.7557495743542582], [4.0618571682777125, -0.7957618405308321], [4.1253236865320515, -0.8325698546347713], [4.188790204786391, -0.8660254037844388], [4.25225672304073, -0.895993774291336], [4.3157232412950695, -0.9223542941045814], [4.3791897595494085, -0.9450008187146683], [4.442656277803748, -0.9638421585599422], [4.506122796058087, -0.9788024462147787], [4.569589314312426, -0.9898214418809327], [4.6330558325667655, -0.9968547759519423], [4.696522350821105, -0.9998741276738751], [4.759988869075444, -0.998867339183008], [4.823455387329783, -0.9938384644612541], [4.886921905584122, -0.9848077530122081], [4.950388423838462, -0.9718115683235417], [5.013854942092801, -0.9549022414440739], [5.07732146034714, -0.9341478602651068], [5.14078797860148, -0.9096319953545182], [5.204254496855819, -0.881453363447582], [5.267721015110158, -0.8497254299495144], [5.331187533364497, -0.814575952050336], [5.394654051618837, -0.7761464642917566], [5.458120569873176, -0.7345917086575331], [5.521587088127515, -0.690079011482112], [5.585053606381854, -0.6427876096865396], [5.648520124636194, -0.5929079290546402], [5.711986642890533, -0.5406408174555974], [5.775453161144872, -0.48619673610046876], [5.838919679399211, -0.4297949120891719], [5.902386197653551, -0.37166245566032724], [5.96585271590789, -0.31203344569848707], [6.029319234162229, -0.25114798718107934], [6.092785752416569, -0.18925124436040974], [6.156252270670908, -0.12659245357374904], [6.219718788925247, -0.06342391965656452], [6.283185307179586, -2.4492935982947064e-16]]}, "id": "132414413115024", "toolbar": ["reset", "move"], "height": 320.0});
    }
    
    if(typeof(mpld3) !== "undefined"){
       // already loaded: just create the figure
       create_fig1324144131150242021881580();
    }else if(typeof define === "function" && define.amd){
       // require.js is available: use it to load d3/mpld3
       require.config({paths: {d3: "http://d3js.org/d3.v3.min"}});
       require(["d3"], function(d3){
          window.d3 = d3;
          mpld3_load_lib("http://mpld3.github.io/js/mpld3.v0.1.js", create_fig1324144131150242021881580);
        });
    }else{
        // require.js not available: dynamically load d3 & mpld3
        mpld3_load_lib("http://d3js.org/d3.v3.min.js", function(){
            mpld3_load_lib("http://mpld3.github.io/js/mpld3.v0.1.js", create_fig1324144131150242021881580);})
    }
    </script>


Matplotlib Style
----------------

Who doesn't like feel and `colors <http://colorbrewer2.org/>`__ of
`ggplot <http://ggplot2.org/>`__?



How do we make matplotlib look like this?

Useful exercise (even if you don't appreciate this). References:

-  `Painless create beautiful
   matplotlib <http://blog.olgabotvinnik.com/post/58941062205/prettyplotlib-painlessly-create-beautiful-matplotlib>`__
-  `Making matplotlib look like
   ggplot <http://messymind.net/2012/07/making-matplotlib-look-like-ggplot/>`__


The ``scatter`` plot
~~~~~~~~~~~~~~~~~~~~


.. code:: python

    %matplotlib inline
    import os
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib as mpl
.. code:: python

    cars = pd.read_csv(os.path.join('data','cars.csv'))
    cars.head()



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>type</th>
          <th>mpg</th>
          <th>cyl</th>
          <th>disp</th>
          <th>hp</th>
          <th>drat</th>
          <th>wt</th>
          <th>qsec</th>
          <th>vs</th>
          <th>am</th>
          <th>gear</th>
          <th>carb</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>         MazdaRX4</td>
          <td> 21.0</td>
          <td> 6</td>
          <td> 160</td>
          <td> 110</td>
          <td> 3.90</td>
          <td> 2.620</td>
          <td> 16.46</td>
          <td> 0</td>
          <td> 1</td>
          <td> 4</td>
          <td> 4</td>
        </tr>
        <tr>
          <th>1</th>
          <td>      MazdaRX4Wag</td>
          <td> 21.0</td>
          <td> 6</td>
          <td> 160</td>
          <td> 110</td>
          <td> 3.90</td>
          <td> 2.875</td>
          <td> 17.02</td>
          <td> 0</td>
          <td> 1</td>
          <td> 4</td>
          <td> 4</td>
        </tr>
        <tr>
          <th>2</th>
          <td>        Datsun710</td>
          <td> 22.8</td>
          <td> 4</td>
          <td> 108</td>
          <td>  93</td>
          <td> 3.85</td>
          <td> 2.320</td>
          <td> 18.61</td>
          <td> 1</td>
          <td> 1</td>
          <td> 4</td>
          <td> 1</td>
        </tr>
        <tr>
          <th>3</th>
          <td>     Hornet4Drive</td>
          <td> 21.4</td>
          <td> 6</td>
          <td> 258</td>
          <td> 110</td>
          <td> 3.08</td>
          <td> 3.215</td>
          <td> 19.44</td>
          <td> 1</td>
          <td> 0</td>
          <td> 3</td>
          <td> 1</td>
        </tr>
        <tr>
          <th>4</th>
          <td> HornetSportabout</td>
          <td> 18.7</td>
          <td> 8</td>
          <td> 360</td>
          <td> 175</td>
          <td> 3.15</td>
          <td> 3.440</td>
          <td> 17.02</td>
          <td> 0</td>
          <td> 0</td>
          <td> 3</td>
          <td> 2</td>
        </tr>
      </tbody>
    </table>
    <p>5 rows × 12 columns</p>
    </div>



.. code:: python

    fig, ax = plt.subplots(figsize=(6,4))
    ax.scatter(cars['wt'], cars['mpg'])
    fig.show()


.. image:: mpl_files/mpl_37_0.png


Changing style
~~~~~~~~~~~~~~

Check out `color brewer <http://colorbrewer2.org/>`__ and `brewer2mpl
wiki <https://github.com/jiffyclub/brewer2mpl/wiki>`__

.. code:: python

    import brewer2mpl
    
    color = brewer2mpl.get_map('Set2', 'qualitative', 3).mpl_colors
.. code:: python

    fig, ax = plt.subplots(figsize=(6,5))
    for i, cyl in enumerate([4,6,8]):
        df = cars[cars['cyl'] == cyl]
        ax = plt.scatter(df['wt'], df['mpg'], s=100, alpha=0.95, edgecolor='none', c=color[i])
    fig.show()


.. image:: mpl_files/mpl_40_0.png


The beauty of ``objects``
~~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    def base_figure():
        fig, ax = plt.subplots(figsize=(6,5))
        for index, cyl in enumerate([4,6,8]):
            df = cars[cars['cyl'] == cyl]
            ax.scatter(df['wt'], df['mpg'], c=color[index], s=100, alpha=0.75, edgecolor='none')
        return fig, ax
.. code:: python

    fig, ax = base_figure()
    
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')  
    
    fig.show()


.. image:: mpl_files/mpl_43_0.png


.. code:: python

    def remove_ticks(ax):
        ax.xaxis.set_ticks_position('none')
        ax.yaxis.set_ticks_position('none')
        
    def remove_splines(ax, spl):
        for s in spl:
            ax.spines[s].set_visible(False)  
    
    def modify_splines(ax, lwd, col):    
        for s in ['bottom', 'left','top','right']:
            ax.spines[s].set_linewidth(lwd)
            ax.spines[s].set_color(col)    
               
.. code:: python

    fig, ax = base_figure()
    
    remove_ticks(ax)
    modify_splines(ax, lwd=0.75, col='0.8')
    remove_splines(ax, ['top','right'])
    
    ax.patch.set_facecolor('0.93')
    ax.grid(True, 'major', color='0.98', linestyle='-', linewidth=1.0)
    ax.set_axisbelow(True)   
    
    fig.show()


.. image:: mpl_files/mpl_45_0.png


Define custom transformations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    def ggplot(ax):
        
        remove_ticks(ax)
        modify_splines(ax, lwd=0.75, col='0.8')
        remove_splines(ax, ['top','right'])
        
        ax.patch.set_facecolor('0.93')
        ax.grid(True, 'major', color='0.98', linestyle='-', linewidth=1.0)
        ax.set_axisbelow(True)   
.. code:: python

    fig, ax = base_figure()
    ggplot(ax)
    fig.show()


.. image:: mpl_files/mpl_48_0.png


Legends
~~~~~~~


.. code:: python

    def base_figure():
        
        fig, ax = plt.subplots(figsize=(6,5))
        for index, cyl in enumerate([4,6,8]):
            df = cars[cars['cyl'] == cyl]
            ax.scatter(df['wt'], 
                       df['mpg'], 
                       c=color[index], 
                       s=100, 
                       alpha=0.75, 
                       edgecolor='none',
                       label='{0} cyl'.format(cyl))  # adding a label
        
        return fig, ax
    
    fig, ax = base_figure()
    
    ax.legend(loc='best')
    
    ggplot(ax)
    
    fig.show()


.. image:: mpl_files/mpl_50_0.png


.. code:: python

    def nice_legend(ax):
        if ax.legend_ is not None:
            ax.legend_.get_frame().set_linewidth(0)
            ax.legend_.get_frame().set_alpha(0.5)
.. code:: python

    fig, ax = base_figure()
    
    ax.legend(loc='best', scatterpoints=1) # for a single point
    
    ggplot(ax)
    nice_legend(ax)
    
    fig.show()        


.. image:: mpl_files/mpl_52_0.png


Changing your default style
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can add *some* custom styles in your ``~/.matplotlib/matplotlibrc``
file.

.. code:: python

    fig, ax = base_figure()
    fig.show()


.. image:: mpl_files/mpl_54_0.png


Setting the ``mpl.rcParams``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


The default figue size.

.. code:: python

    mpl.rcParams['figure.figsize'] = 8, 4
Change the axes background color, turn on grid lines, change the color.

.. code:: python

    mpl.rcParams['axes.facecolor'] = '0.93'
    mpl.rcParams['axes.grid'] = True
    mpl.rcParams['grid.linestyle'] = '-'
    mpl.rcParams['grid.linewidth'] = 1
    mpl.rcParams['grid.color'] = '1.0' 
    mpl.rcParams['axes.axisbelow'] = True
    mpl.rcParams['axes.linewidth'] = 0.5
    mpl.rcParams['axes.edgecolor'] = '0.7' #can't remove some
    mpl.rcParams['xtick.major.size'] = 0.0
    mpl.rcParams['ytick.major.size'] = 0.0
Modify the legend.

.. code:: python

    mpl.rcParams['legend.fancybox'] = True
    mpl.rcParams['legend.scatterpoints'] = 1
    mpl.rcParams['legend.frameon'] = False
.. code:: python

    fig, ax = base_figure()
    ax.legend(loc='best')
    fig.show()


.. image:: mpl_files/mpl_62_0.png


And many more options....

.. code:: python

    mpl.rcParams.keys()[:10]



.. parsed-literal::

    ['agg.path.chunksize',
     'animation.avconv_args',
     'animation.avconv_path',
     'animation.bitrate',
     'animation.codec',
     'animation.convert_args',
     'animation.convert_path',
     'animation.ffmpeg_args',
     'animation.ffmpeg_path',
     'animation.frame_format']



Let's save that for later...

.. code:: python

    import json
    
    with open('mplrc.json','w') as output:
        output.write(json.dumps(mpl.rcParams))
Tricks with ``itertools`` and ``functools``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    fig, ax = plt.subplots(figsize=(6,5))
    
    for index, cyl in enumerate([4,6,8]):
        df = cars[cars['cyl'] == cyl]
        ax.scatter(df['wt'], 
                   df['mpg'], 
                   c=color[index], 
                   s=100, 
                   alpha=0.75, 
                   edgecolor='none',
                   label='{0} cyl'.format(cyl))  # adding a label
        
    ax.legend(loc='best')
    fig.show()


.. image:: mpl_files/mpl_68_0.png


.. code:: python

    import itertools
    from functools import partial
.. code:: python

    color_iter = itertools.cycle(color)
    partial_scatter = partial(plt.scatter, s=100, alpha=0.75, edgecolor='none')
.. code:: python

    fig, ax = plt.subplots(figsize=(6,5))
    for cyl in [4,6,8]:
        df = cars[cars['cyl'] == cyl]
        
        ax = partial_scatter(df['wt'], df['mpg'], c=next(color_iter), label='{0} cyl'.format(cyl))
    
    fig.show()


.. image:: mpl_files/mpl_71_0.png


How about as a ``d3`` svg?
~~~~~~~~~~~~~~~~~~~~~~~~~~

https://github.com/jakevdp/mpld3

.. code:: python

    from mpld3 import enable_notebook
    enable_notebook()
    
    fig, ax = base_figure()
    #ax.legend(loc='best')  # Note quite yet
    fig.show()


.. raw:: html

    
    <style>
    
    </style>
    
    <div id="fig1308744280999844569860445"></div>
    <script>
    function mpld3_load_lib(url, callback){
      var s = document.createElement('script');
      s.src = url;
      s.async = true;
      s.onreadystatechange = s.onload = callback;
      s.onerror = function(){console.warn("failed to load library " + url);};
      document.getElementsByTagName("head")[0].appendChild(s);
    }
    
    function create_fig1308744280999844569860445(){
      
      mpld3.draw_figure("fig1308744280999844569860445", {"width": 480.0, "axes": [{"xlim": [1.0, 6.0], "yscale": "linear", "axesbg": "#EDEDED", "texts": [], "zoomable": true, "images": [], "xdomain": [1.0, 6.0], "ylim": [5.0, 40.0], "paths": [], "sharey": [], "sharex": [], "axesbgalpha": null, "axes": [{"grid": {"color": "#FFFFFF", "alpha": 1.0, "dasharray": "10,0", "gridOn": true}, "position": "bottom", "nticks": 6, "tickvalues": null, "tickformat": null}, {"grid": {"color": "#FFFFFF", "alpha": 1.0, "dasharray": "10,0", "gridOn": true}, "position": "left", "nticks": 8, "tickvalues": null, "tickformat": null}], "lines": [], "markers": [], "id": "130874425644112", "ydomain": [5.0, 40.0], "collections": [{"paths": [[[[0.0, -0.5], [0.13260155, -0.5], [0.25978993539242673, -0.44731684579412084], [0.3535533905932738, -0.3535533905932738], [0.44731684579412084, -0.25978993539242673], [0.5, -0.13260155], [0.5, 0.0], [0.5, 0.13260155], [0.44731684579412084, 0.25978993539242673], [0.3535533905932738, 0.3535533905932738], [0.25978993539242673, 0.44731684579412084], [0.13260155, 0.5], [0.0, 0.5], [-0.13260155, 0.5], [-0.25978993539242673, 0.44731684579412084], [-0.3535533905932738, 0.3535533905932738], [-0.44731684579412084, 0.25978993539242673], [-0.5, 0.13260155], [-0.5, 0.0], [-0.5, -0.13260155], [-0.44731684579412084, -0.25978993539242673], [-0.3535533905932738, -0.3535533905932738], [-0.25978993539242673, -0.44731684579412084], [-0.13260155, -0.5], [0.0, -0.5]], ["M", "C", "C", "C", "C", "C", "C", "C", "C", "Z"]]], "edgecolors": [], "edgewidths": [1.0], "offsets": "data01", "yindex": 1, "id": "130874419617744", "pathtransforms": [[11.11111111111111, 0.0, 0.0, 11.11111111111111, 0.0, 0.0]], "pathcoordinates": "display", "offsetcoordinates": "data", "zorder": 1, "xindex": 0, "alphas": [0.75], "facecolors": ["#66C2A5"]}, {"paths": [[[[0.0, -0.5], [0.13260155, -0.5], [0.25978993539242673, -0.44731684579412084], [0.3535533905932738, -0.3535533905932738], [0.44731684579412084, -0.25978993539242673], [0.5, -0.13260155], [0.5, 0.0], [0.5, 0.13260155], [0.44731684579412084, 0.25978993539242673], [0.3535533905932738, 0.3535533905932738], [0.25978993539242673, 0.44731684579412084], [0.13260155, 0.5], [0.0, 0.5], [-0.13260155, 0.5], [-0.25978993539242673, 0.44731684579412084], [-0.3535533905932738, 0.3535533905932738], [-0.44731684579412084, 0.25978993539242673], [-0.5, 0.13260155], [-0.5, 0.0], [-0.5, -0.13260155], [-0.44731684579412084, -0.25978993539242673], [-0.3535533905932738, -0.3535533905932738], [-0.25978993539242673, -0.44731684579412084], [-0.13260155, -0.5], [0.0, -0.5]], ["M", "C", "C", "C", "C", "C", "C", "C", "C", "Z"]]], "edgecolors": [], "edgewidths": [1.0], "offsets": "data02", "yindex": 1, "id": "130874425633936", "pathtransforms": [[11.11111111111111, 0.0, 0.0, 11.11111111111111, 0.0, 0.0]], "pathcoordinates": "display", "offsetcoordinates": "data", "zorder": 1, "xindex": 0, "alphas": [0.75], "facecolors": ["#FC8D62"]}, {"paths": [[[[0.0, -0.5], [0.13260155, -0.5], [0.25978993539242673, -0.44731684579412084], [0.3535533905932738, -0.3535533905932738], [0.44731684579412084, -0.25978993539242673], [0.5, -0.13260155], [0.5, 0.0], [0.5, 0.13260155], [0.44731684579412084, 0.25978993539242673], [0.3535533905932738, 0.3535533905932738], [0.25978993539242673, 0.44731684579412084], [0.13260155, 0.5], [0.0, 0.5], [-0.13260155, 0.5], [-0.25978993539242673, 0.44731684579412084], [-0.3535533905932738, 0.3535533905932738], [-0.44731684579412084, 0.25978993539242673], [-0.5, 0.13260155], [-0.5, 0.0], [-0.5, -0.13260155], [-0.44731684579412084, -0.25978993539242673], [-0.3535533905932738, -0.3535533905932738], [-0.25978993539242673, -0.44731684579412084], [-0.13260155, -0.5], [0.0, -0.5]], ["M", "C", "C", "C", "C", "C", "C", "C", "C", "Z"]]], "edgecolors": [], "edgewidths": [1.0], "offsets": "data03", "yindex": 1, "id": "130874423595984", "pathtransforms": [[11.11111111111111, 0.0, 0.0, 11.11111111111111, 0.0, 0.0]], "pathcoordinates": "display", "offsetcoordinates": "data", "zorder": 1, "xindex": 0, "alphas": [0.75], "facecolors": ["#8DA0CB"]}], "xscale": "linear", "bbox": [0.125, 0.099999999999999978, 0.77500000000000002, 0.80000000000000004]}], "data": {"data02": [[2.62, 21.0], [2.875, 21.0], [3.215, 21.4], [3.46, 18.1], [3.44, 19.2], [3.44, 17.8], [2.77, 19.7]], "data03": [[3.44, 18.7], [3.57, 14.3], [4.07, 16.4], [3.73, 17.3], [3.78, 15.2], [5.25, 10.4], [5.4239999999999995, 10.4], [5.345, 14.7], [3.52, 15.5], [3.435, 15.2], [3.84, 13.3], [3.845, 19.2], [3.17, 15.8], [3.57, 15.0]], "data01": [[2.32, 22.8], [3.19, 24.4], [3.15, 22.8], [2.2, 32.4], [1.615, 30.4], [1.835, 33.9], [2.465, 21.5], [1.935, 27.3], [2.14, 26.0], [1.5130000000000001, 30.4], [2.78, 21.4]]}, "id": "130874428099984", "toolbar": ["reset", "move"], "height": 400.0});
    }
    
    if(typeof(mpld3) !== "undefined"){
       // already loaded: just create the figure
       create_fig1308744280999844569860445();
    }else if(typeof define === "function" && define.amd){
       // require.js is available: use it to load d3/mpld3
       require.config({paths: {d3: "http://d3js.org/d3.v3.min"}});
       require(["d3"], function(d3){
          window.d3 = d3;
          mpld3_load_lib("http://mpld3.github.io/js/mpld3.v0.1.js", create_fig1308744280999844569860445);
        });
    }else{
        // require.js not available: dynamically load d3 & mpld3
        mpld3_load_lib("http://d3js.org/d3.v3.min.js", function(){
            mpld3_load_lib("http://mpld3.github.io/js/mpld3.v0.1.js", create_fig1308744280999844569860445);})
    }
    </script>


Examples
--------


.. code:: python

    %matplotlib inline
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib as mpl
A little style from the previous session.

.. code:: python

    import json
    import brewer2mpl
    
    data = json.loads(open('mplrc.json','r').read())
    for x in data.keys():
        try:
            mpl.rcParams[x] = data[x]
        except ValueError:
            pass
            
    colors = brewer2mpl.get_map('Set1', 'qualitative', 8).mpl_colors
    mpl.rcParams['axes.color_cycle'] = colors
The ``line`` graph
~~~~~~~~~~~~~~~~~~

plt.plot?

.. code:: python

    fig, ax = plt.subplots()
    ax.plot(np.random.randn(200).cumsum())
    fig.show()


.. image:: mpl_files/mpl_79_0.png


.. code:: python

    fig, ax = plt.subplots()
    for i in range(8):
        ax.plot(np.random.randn(200).cumsum())
    fig.show()


.. image:: mpl_files/mpl_80_0.png


Histogram
~~~~~~~~~

?plt.hist

.. code:: python

    mu = 100
    sigma = 15
    x = mu + sigma * np.random.randn(300)
    
    fig, ax = plt.subplots()
    ax.hist(x, alpha=0.5, bins=20)
    fig.show()


.. image:: mpl_files/mpl_82_0.png


.. code:: python

    fig, ax = plt.subplots()
    for i in range(3):
        x = 20.0*np.random.randn() + sigma*np.random.randn(300)
        ax.hist(x, normed=1, alpha=0.5, histtype='stepfilled', bins=20)
    fig.show()


.. image:: mpl_files/mpl_83_0.png


Kernel Density Estimates
~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    from sklearn.neighbors.kde import KernelDensity
.. code:: python

    fig, ax = plt.subplots()
    for i in range(3):
        
        data = 20.0*np.random.randn() + sigma*np.random.randn(100)
        x = np.linspace(data.min(), data.max(), 100)
    
        # For sklearn
        data = data.reshape(-1, 1)
        x = x.reshape(-1, 1)
        
        kde = KernelDensity().fit(data)  # you can adjust the 'bandwidth' parameter
        density = np.exp(kde.score_samples(x))
        ax.plot(x, density)
    
    fig.show()


.. image:: mpl_files/mpl_86_0.png


``Scipy.stats``
~~~~~~~~~~~~~~~


.. code:: python

    from scipy import stats
    
    fig, ax = plt.subplots()
    for i in range(3):
        
        x = 20.0*np.random.randn() + sigma*np.random.randn(300)
        xd = np.linspace(min(x)-10, max(x)+10, 100)
        density = stats.kde.gaussian_kde(x)
        ax.plot(xd, density(xd))
        
    fig.show()


.. image:: mpl_files/mpl_88_0.png


``fill_between``
~~~~~~~~~~~~~~~~


.. code:: python

    import itertools
    colors = itertools.cycle(mpl.rcParams['axes.color_cycle'])
    
    fig, ax = plt.subplots()
    for i in range(4):
        
        x = 20.0*np.random.randn() + sigma*np.random.randn(300)
        xd = np.linspace(min(x)-10, max(x)+10, 100)
        density = stats.kde.gaussian_kde(x)
        
        ax.fill_between(xd, 0, density(xd), alpha=0.25, color=next(colors), linewidth=2)
        
    fig.show()


.. image:: mpl_files/mpl_90_0.png


Combined ``hist`` and ``kde``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    fig, ax = plt.subplots()
    for i in range(2):
        
        x = 20.0*np.random.randn() + sigma*np.random.randn(300)
        xd = np.linspace(min(x)-10, max(x)+10, 100)
        density = stats.kde.gaussian_kde(x)
        c = next(colors)
        
        ax.hist(x, normed=1, alpha=0.25, color=c, histtype='stepfilled')
        ax.plot(xd, density(xd), alpha=0.75, color=c, linewidth=2)
        
    fig.show()


.. image:: mpl_files/mpl_92_0.png


Bar charts
~~~~~~~~~~

Adapted from `Harvard
CS109 <http://nbviewer.ipython.org/github/cs109/content/blob/master/lec_03_statistical_graphs.ipynb>`__.

.. code:: python

    years = [2004, 2005, 2006, 2007, 2008]
    heights = [501, 607, 709, 650, 532]
    box_colors = mpl.rcParams['axes.color_cycle']  
    
    fig, ax = plt.subplots()
    
    ax.bar(np.array(years)-0.4, heights, color=box_colors, alpha=0.75)
    
    ax.set_xlim(2003.5, 2008.5)
    ax.set_ylim(0,800)
    
    for x, y in zip(years, heights):
        plt.annotate('{0}'.format(y), (x, y + 20), ha='center')
    
    fig.show()


.. image:: mpl_files/mpl_94_0.png


The ``box`` plot
~~~~~~~~~~~~~~~~


.. code:: python

    fig, ax = plt.subplots()
    
    d1 = 20.0*np.random.randn() + sigma*np.random.randn(300)
    d2 = 20.0*np.random.randn() + sigma*np.random.randn(300)
    
    data = [d1, d2]
    bp = ax.boxplot(data, widths=0.65)
    
    fig.show()


.. image:: mpl_files/mpl_96_0.png


Error bars
~~~~~~~~~~


.. code:: python

    x = np.linspace(0, 10, 50)
    xerr = np.random.normal(np.sin(x), 0.4)
    y = np.sin(x)
    
    fig, ax = plt.subplots()
    
    ax.plot(x, y)
    ax.errorbar(x, y, xerr, fmt='.k')
    
    fig.show()


.. image:: mpl_files/mpl_98_0.png


.. code:: python

    fig, ax = plt.subplots()
    
    ax.plot(x, y)
    ad = abs(y-xerr)
    ax.fill_between(x, y - ad, y + ad, color='0.5', alpha=0.2)
    
    fig.show()


.. image:: mpl_files/mpl_99_0.png


.. code:: python

    from sklearn.datasets import make_blobs
    
    X, _ = make_blobs(n_samples=20000, centers=2, random_state=37, cluster_std=4)
    x = X[:,0]
    y = X[:,1]
    
    fig, ax = plt.subplots()
    
    ax.plot(x,y, 'o', alpha=0.02)
    
    fig.show()


.. image:: mpl_files/mpl_100_0.png


.. code:: python

    fig, ax = plt.subplots(figsize=(6,5))
    
    ax.hexbin(x, y, gridsize=20)
    
    fig.show()


.. image:: mpl_files/mpl_101_0.png


.. code:: python

    blues=plt.get_cmap('Blues')
    
    fig, ax = plt.subplots()
    
    tmp = ax.hexbin(x, y, gridsize=40, cmap=blues)
    fig.colorbar(tmp, ax=ax)
    fig.show()


.. image:: mpl_files/mpl_102_0.png


Contour
~~~~~~~


Create a simple surface.

.. code:: python

    x = np.linspace(-1, 1, 50)
    y = np.linspace(-2, 2, 50)
    
    X, Y = np.meshgrid(x, y)
    z = X*X + Y*Y + X*Y
Default countour.

.. code:: python

    fig, ax = plt.subplots()
    
    ax.contour(x, y, z, 20)
    
    fig.show()


.. image:: mpl_files/mpl_107_0.png


.. code:: python

    fig, ax = plt.subplots()
    
    con = ax.contourf(x, y, z, 20)
    
    fig.colorbar(con, ax=ax)
    fig.show()


.. image:: mpl_files/mpl_108_0.png


.. code:: python

    fig, ax = plt.subplots()
    
    tmp = ax.contour(x, y, z, 20, cmap=blues, alpha=0.9)
    con = ax.contourf(x, y, z, 20, cmap=blues, alpha=1.)
    
    fig.colorbar(con, ax=ax)
    fig.show()


.. image:: mpl_files/mpl_109_0.png


False-color
~~~~~~~~~~~


.. code:: python

    fig, ax = plt.subplots()
    
    im = ax.imshow(z, cmap=blues, interpolation='nearest', origin='lower')
    ax.grid(False)
    #tmp = ax.contour(z, 20)
    
    fig.colorbar(im, ax=ax)
    fig.show()


.. image:: mpl_files/mpl_111_0.png

