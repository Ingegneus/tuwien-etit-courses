public:: true
icon:: 🦘
inherit-color-icon-from:: [[logseq-page-color-orange]] 
template-used:: standard-page
tags:: [[uni]], [[automatisierungstechnik]], [[Sprungantwort]] 
alias:: sprungfähig

- wann ist ein [[system]] mit der [[Übertragungsfunktion]] $G(s)$ [[sprungfähig]] ? 
  deck:: Uni::Automatisierungstechnik_Theorie
  tags:: flashcard
  id:: 6729c8eb-9d18-43de-8049-66086358715c
	- $G \left(s\right) = \frac{z\left(s\right)}{n\left(s\right)}~,\quad \operatorname*{\mathrm{lim}}_{s\to\infty}G\left(s\right)\ne0\\$  also  $\opn{grad}(z(s)) = \opn{grad}(n(s))$
	  id:: 6729ef23-4d38-4044-b7e9-f4866a30bcc0
	  tags:: formel
	  bezeichnung:: bedingung für die [[sprungfähigkeit]] eines [[systems]]
		- $s$ ... [[laplacebereich]] variable
		- $G\left(s\right)$ ... [[Übertragungsfunktion]]
		- $z\left(s\right)$ ... [zählerpolynom]([[polynom]])
		- $n\left(s\right)$ ... [nennerpolynom]([[polynom]])
	- in Worten ausgedrückt: wenn der Zähler- und Nennergrad von $G(s)$ gleich sind, dann ist das [[system]] [[sprungfähig]]
	- skript
		-