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
	  collapsed:: true
		- ### index
			- {{query (and [[flashcard]] (page [[]]))}}
			  query-table:: true
			  query-properties:: [:block :tags]
			  query-sort-by:: block
			  query-sort-desc:: false
- flashcard
  template:: flashcard
  template-including-parent:: false
  collapsed:: true
	- text
	  id:: d15440a1-738b-4891-b9c7-436f5bad96b7
	  deck:: Uni::Automatisierungstechnik_Theorie
	  tags:: flashcard
		- .
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