icon:: ⚡
inherit-color-icon-from:: [[logseq-page-color-yellow]] 
template-used:: standard-page
tags:: [[uni]]
alias:: et1

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
- $\varepsilon = \varepsilon_r \cdot \varepsilon_0$
  tags:: formel
  bezeichnung:: [[permittivität]] in materie
	- $\varepsilon_r$ ... relative [[permittivität]] $\mathbf{[-]}$
	- ((6734c4a0-0bc0-452c-a33f-bcf1d8de32da))