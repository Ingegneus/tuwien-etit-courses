tags:: [[templates]], [[uni]]

- standard-page
  template:: standard-page
  template-including-parent:: false
	- icon:: -
	  inherit-color-icon-from:: -
	  template-used:: standard-page
	  tags:: -
	  alias:: -
- uni-subject
  template:: uni-subject
  template-including-parent:: false
  collapsed:: true
	- icon:: -
	  color:: -
	  template-used:: standard-page
	  tags:: [[uni]]
	  alias:: -
	- [📁 folder](file://)
	- ## vorlesungen
	- ## beispiele
	  collapsed:: true
		- ### bsp 1
		  background-color:: green
			- a)
			  background-color:: green
				- formeln
				- ![📚 doc](../assets/documents/)
	- ## flashcards
		- ### index
		  collapsed:: true
			- query-table:: true
			  collapsed:: true
			  #+BEGIN_QUERY
			  {
			  :title [:b "all flashcards"]
			  :query [:find (pull ?block [*])
			  :where
			  [?block :block/content ?blockcontent]
			  [?block :block/page ?page]
			  [?page :block/name ?pagename]
			  [?block :block/path-refs [:block/name "flashcard"]]
			  ( or
			  (property ?block :deck "Uni::Automatisierungstechnik_Theorie")
			  (property ?block :deck "Uni::Mathematik_Theorie")
			  )
			  ( not
			  (?page :page/name "templates-uni")
			  )
			  ]
			  }
			  #+END_QUERY
			- query-table:: true
			  query-properties:: [:block :tags]
			  collapsed:: true
			  #+BEGIN_QUERY
			  {
			  :title [:b "all flashcards defined here"]
			  :query [:find (pull ?block [*])
			  :where
			  [?block :block/content ?blockcontent]
			  [?block :block/page ?page]
			  [?page :block/name ?pagename]
			  [?block :block/path-refs [:block/name "flashcard"]]
			  ( or
			  (property ?block :deck "Uni::Automatisierungstechnik_Theorie")
			  (property ?block :deck "Uni::Mathematik_Theorie")
			  )
			  [?page :page/name "automatisierungstechnik"]
			  ]
			  }
			  #+END_QUERY
- flashcard
  template:: flashcard
  template-including-parent:: false
	- text
	  id:: d15440a1-738b-4891-b9c7-436f5bad96b7
	  deck:: Uni::Wellenausbreitung_Theorie
	  tags:: flashcard
		- .
- beispiel
  template:: beispiel
  template-including-parent:: false
	- Beispiel 1)
	  background-color:: green
		- formeln
		- ![📚 doc](../assets/documents/)
- vocabulary
  template:: vocabulary
  template-including-parent:: false
	- word
	  template-used:: vocabulary
	  meaning:: -
	  tags:: language, vocabulary, english, deutsch, italiano
- formel
  template:: formel
  template-including-parent:: false
  collapsed:: true
	- $-$
	  tags:: formel
	  bezeichnung:: -
		- $-$ ...
- new calc block
  template:: new calc block
  template-including-parent:: false
	- ```python
	  pyodide_js.globals.clear();
	  ```
		- {{evalparent}}
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
	  import io, base64
	  await micropip.install('sympy')
	  import sympy as sp
	  from sympy.utilities.lambdify import lambdify
	  from sympy import latex
	  
	  "resultat: " + f"{var:.4g}" + "unit"
	  ```
		- {{evalparent}}
- calc block
  template:: calc block
  template-including-parent:: false
	- ```python
	  ```
		- {{evalparent}}