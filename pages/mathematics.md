icon:: ➗
inherit-color-icon-from:: [[logseq-page-color-blue]] 
template-used:: standard-page
tags:: [[uni]]
alias:: mathematik, math

- $x=\frac{a}{b}$ dann ist $|x|=|\frac{a}{b}|=\frac{|a|}{|b|}$
  tags:: formel, mathematik
  bezeichnung:: betragsrechnung von brüchen
- ## flashcards
	- wie erfolgt die erweiterung/ergänzung auf ein vollständiges quadrat?
	  id:: 67235854-9c4c-44d4-8fd0-b81872bedc7b
	  deck:: Uni::Mathematik_Theorie
	  tags:: flashcard
		- #### Vorgangsweise mit Beispiel: 
		  gegeben: $ax^2+bx+c$
			- $a\left(x^2+\frac{b}{a}x\right)+c$
			  logseq.order-list-type:: number
			- $a\left(x^2+\frac{b}{a}x+\left(\frac{b}{2a}\right)^2-\left(\frac{b}{2a}\right)^2\right)+c$
			  logseq.order-list-type:: number
			- $a\left(x+\frac{b}{a}\right)^2-\left(\frac{b}{2a}\right)^2+c$
			  logseq.order-list-type:: number
			  background-color:: yellow
		- gegeben $2x^2+4x+10$
			- $2\left(x^2+2x\right)+10$
			  logseq.order-list-type:: number
			- $2\left(x^2+2x+4-4\right)+10$
			  logseq.order-list-type:: number
			- $2\left(x+2\right)^2-8+10$
			  logseq.order-list-type:: number
			- $2\left(x+2\right)^2+2$
			  logseq.order-list-type:: number
			  background-color:: yellow
	- wie wird eine [[taylorreihe]] entwickelt?
	  id:: 6713c995-9c83-45db-8427-7ad83d4e50cb
	  deck:: Uni::Mathematik_Theorie
	  tags:: flashcard
		- $\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^{n}$
		  tags:: formel, tylorreihe
		  bezeichnung:: taylorreihe erster erdnung, allgemeine form
			- $f^{\left(n\right)}$ ... die funktion die entwickelt werden soll abgeleitet nach der $n$-ten ordnung
			- $a$ ... stelle in dessen umgebung entwickelt werden soll
		- ${\mathbf{f}(\mathbf{x}_{0}+\Delta\mathbf{x})=\mathbf{f}(\mathbf{x}_{0})+\frac{\partial}{\partial\mathbf{x}}\mathbf{f}(\mathbf{x}_{0})\Delta\mathbf{x}+\mathbf{r}(\mathbf{x}_{0},\Delta\mathbf{x})}$
		  tags:: formel, taylorreihe
		  bezeichnung:: [[taylorreihe]] zweiter erdnung, allgemeine form
			- $\mathbf{x}_0$ ... stelle um die entwickelt wird
			  id:: 6710e826-3066-47c5-9fe6-69a1b1b0ba21
			- $\Delta\mathbf{x}$ ... kleine auslenkung von der entwicklungsstelle
			  id:: 6710e8dc-6b9b-4548-a7ab-ac28c8e04d30
			- $\mathbf{f}\left(\mathbf{x}_{0}\right)$ ... funktion an der stelle $\mathbf{x}_{0}$
			- $\frac{\partial}{\partial\mathbf{x}}\mathbf{f}(\mathbf{x}_{0})$ ... [[totales differential]] der funktion
			  id:: 6711120b-361a-4ab7-a2b5-ac2b1817ba34
		-