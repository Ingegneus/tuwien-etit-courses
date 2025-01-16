public:: true
icon:: 🐍
inherit-color-icon-from:: [[logseq-page-color-green]] 
template-used:: standard-page
tags:: python, uni

- provides some [[python]] utility functions. meant to be used with [[uni]] related tasks
- ```python
  import pyodide_js
  await pyodide_js.loadPackage("micropip")
  import micropip
  await micropip.install('scipy')
  from scipy import *
  from scipy.constants import *
  from numpy import *
  await micropip.install('matplotlib')
  import matplotlib.pyplot as plt
  plt.rcParams['font.family'] = 'serif'
  plt.rcParams['mathtext.fontset'] = 'cm'
  import io, base64, sys
  await micropip.install('sympy')
  import sympy as sp
  from sympy.utilities.lambdify import lambdify
  
  ### sehr selten verwendet, daher deaktiviert ###
  # await micropip.install('latex2mathml')
  # import latex2mathml
  # await micropip.install('ziamath')
  # import ziamath 
  # await micropip.install('schemdraw')
  # import schemdraw
  # import schemdraw.elements as elm
  # schemdraw.use('svg')
  # schemdraw.svgconfig.text = 'path'
  # elm.style(elm.STYLE_IEC)
  
  printer = io.StringIO()
  stdout = sys.stdout
  sys.stdout = printer
  ```
- ```python
  def showPlot():
      buf = io.BytesIO()
      plt.savefig(buf, format = 'png')
      buf.seek(0)
      png = showPngImg(buf.read())
      buf.close()
      plt.clf()
      return png
  ```
- ```python
  def symPrint(expr):
      print(f"latex output: {sp.latex(expr)}")
      sp.pprint(expr,use_unicode=False)
  ```
- ```python
  def resPrint(*args):
      # Check if the number of arguments is a multiple of 3 (name, val, unit)
      if len(args) % 3 != 0:
          raise ValueError("Arguments must be provided in groups of (name, val, unit)")
      outputs = []
      # Process the arguments in chunks of 3
      for i in range(0, len(args), 3):
          name, val, unit = args[i], args[i+1], args[i+2]
          output = f"{name} = {val:.4g}{unit}"
          outputs.append(output)
          print(output)
      print('‾' * (len(max(outputs, key=len))))
  ```
- ```python
  def showSvgImg(buf):
      return 'data:image/svg+xml;base64,' + base64.b64encode(buf).decode('UTF-8')
  
  def showPngImg(buf):
      return 'data:image/png;base64,' + base64.b64encode(buf).decode('UTF-8')
  
  ```