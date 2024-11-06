icon:: 🗿
inherit-color-icon-from:: [[logseq-page-color-green]]
tags:: [[uni]], [[automatisierungstechnik]] 
alias:: BIBO-stabil, BIBO-Stabilität, BIBO stabil

- steht für <u>B</u>ounded <u>I</u>nput <u>B</u>ounded <u>O</u>utput
- wann ist ein [[system]] [[BIBO-stabil]]? 
  deck:: Uni::Automatisierungstechnik_Theorie
  tags:: flashcard, grundlagen
	- $\int_{0}^{\infty}|g(t)|\opn{d}t<\infty$
	  tags:: formel
	  bezeichnung:: Bedingung für [[BIBO-Stabilität]], wenn ein [[lineares]], [[zeitinvariantes]] [[Eingrößensystem]] dieser Form vorliegt [link](((6729bee5-385f-4bbf-ac7d-5f099188180c))) (entspricht absoluter integrabilität)
		- $g(t)$ ... [[impulsantwort]] [link](((672a3592-c9ec-4f08-a779-e8d980b3a932)))
		- $t$ ... zeit
	- $\opn{Re}(s_i)=\alpha_i<0~, \quad s_i = \alpha_i + i\omega_i$
	  tags:: formel
	  bezeichnung:: Bedingung für [[BIBO-Stabilität]], wenn ein [[lineares]], [[zeitinvariantes]] [[Eingrößensystem]] dieser Form vorliegt [link](((6729bee5-385f-4bbf-ac7d-5f099188180c)))
	  id:: 672a2989-ea9a-4046-b0d5-aeb334016b0e
		- $s_i$ ... [[pole]] der zugehörigen [[Übertragungsfunktion]] $G(s)$ [link](((67254498-19a4-47c4-a559-8bad13c5ebe3)))
		- $\alpha_i$ ... realteil des [[pols]] $s_i$
		- $\omega_i$ ... imaginärteil des [[pols]] $s_i$