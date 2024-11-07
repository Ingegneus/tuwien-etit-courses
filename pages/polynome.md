icon:: 📈
inherit-color-icon-from:: [[logseq-page-color-pink]]
template-used:: standard-page
tags:: [[mathematik]], [[uni]]
alias:: polynom, polynoms

- $-\frac{p}{2}\pm\sqrt{\left(\frac{p}{2}\right)^2-q}$
  tags:: formel
  bezeichnung:: wenn der koeffizeint der quadratischen potenz $1$ ist, kann man die kleine lösungsformel anwenden
  alias:: quadratische lösungsformel, quadratic formula
	- $p, q$ ... koeffizienten des quadratischen [[polynoms]]
- $\frac{-b\pm\sqrt{b^2-4ac}}{2a}$
  tags:: formel
  bezeichnung:: große lösungsformel, quadratische lösungsformel, quadratic formula
	- $a, b, c$ ... koeffizienten des quadratischen [[polynoms]]
- polynomdivision [link](https://www.mathebibel.de/polynomdivision)
  deck:: Uni::Automatisierungstechnik_Theorie
  tags:: flashcard, wip
  id:: 67290be5-009a-4d75-afb2-6a0484a92450
  collapsed:: true
	- ### Berechne $\\(2 x^3 + 4 x^2 − 2 x − 4) : (x − 1) =~? \\$ mithilfe einer Polynomdivision.
		- #### $x^3$-Term
			- Division
				- $(\bggreen{2x^3} + 4x^2 - 2x - 4) : (\bggreen{x}-1) = \bggreen{2x^2}$
				- _Beschreibung_
					- Wie oft passt $x$ in $2 x^3$ ?
					- $\frac{2x^3}{x}=2x^2$
			- Multiplikation
				- $\begin{alignedat}{1} &\hspace{1em}(2x^3 + 4x^2 - 2x - 4) : \bggreen{(x-1)} = \bggreen{2x^2} \\ & \bggreen{-(2x^3 - 2x^2)} \end{alignedat}$
				- _Beschreibung_
					- Wir multiplizieren $2 x^2$ mit $(x − 1)$ .
					- $2 x^2 \cdot (x − 1) = 2 x^3 − 2 x^2$
				- Das Ergebnis schreiben wir mit einem negativen Vorzeichen in die 2. Zeile.
			- Subtraktion
				- $\begin{alignedat}{2} &\hspace{0.8em}(\bggreen{2x^3 + 4x^2 - 2x - 4}) : (x-1)= 2x^2\\&\hspace{0.8em}(2x^3 + 4x^2 - 2x - 4) : (x-1)= 2x^2 \\ &\bggreen{-(2x^3 - 2x^2)} \\ &\hspace{3.9em} \bggreen{6x^2- 2x - 4} \end{alignedat}$
				- _Beschreibung_
					- Das Ergebnis der vorherigen Multiplikation ziehen wir von der ursprünglichen Gleichung ab.
					- $2 x^3 + 4 x^2 − 2 x − 4 − 2 x^3 − 2 x^2 \\= 6 x^2 − 2 x − 4$
				- Das Ergebnis schreiben wir in die 3. Zeile.
		- #### $x^2$ \-Term
			- Division
				- $\begin{alignedat}{4} &(2x^3 + &&4x^2 - 2x - 4) : (\bggreen{x}-1) = 2x^2 + \bggreen{6x} \\ &\hspace{-1.2em}-(2x^3 - &&2x^2) \\ & && \bggreen{6x^2}- 2x - 4 \end{alignedat}$
				- _Beschreibung_
					- Wie oft passt $x$ in $6 x^2$ ?
					- $\frac{6x^2}{x}=6x$
			- Multiplikation
				- $\begin{alignedat}{3} & (2x^3 + && 4x^2 - 2x - 4) : \bggreen{(x-1)} = 2x^2 + \bggreen{6x} \\ -&(2x^3 - &&2x^2) \\ & && 6x^2 - 2x - 4 \\ & && \hspace{-1.2em} \bggreen{- (6x^2-6x)} \end{alignedat}$
				- _Beschreibung_
					- Wir multiplizieren $6 x$ mit $(x − 1)$ .
					- $6 x \cdot (x − 1) = 6 x^2 − 6 x$
				- Das Ergebnis schreiben wir mit einem negativen Vorzeichen in die 4. Zeile.
			- Subtraktion
				- $\begin{alignedat}{1} & (2x^3 + 4x^2 - 2x - 4) : (x - 1) = 2x^2 + 6x \\ -&(2x^3 - 2x^2) \\ & \hspace{3.1em} \bggreen{6x^2 - 2x - 4} \\ & \hspace{1.9em} \bggreen{-(6x^2-6x)} \\ & \hspace{5.7em} \bggreen{4x - 4} \end{alignedat}$
				- _Beschreibung_
					- Das Ergebnis der vorherigen Multiplikation ziehen wir vom Restterm ab.
					- $6 x^2 − 2 x − 4 − (6 x^2 − 6 x) \\= 6 x^2 − 2 x − 4 − 6 x^2 + 6 x \\= 4 x − 4$
			- Das Ergebnis schreiben wir in die 5. Zeile.
		- #### $x$-Term
			- Division
				- $\begin{alignedat}{4} & (2x^3 + &&4x^2 - &&2x - &&4) : (\bggreen{x}-1) = 2x^2 + 6x + \bggreen{4} \\ -&(2x^3 - &&2x^2) \\ &  &&6x^2 - &&2x - &&4 \\ & &&\hnsp-(6x^2-&&6x) \\ &  &&&& \bggreen{4x} - &&4 \end{alignedat}$
				- _Beschreibung_
					- Wie oft passt x in 4 x ?
					- 4 x x = 4
				- Multiplikation
					- $\begin{alignedat}{4} & (2x^3 + &&4x^2 - &&2x - 4) : \bggreen{(x-1)} = 2x^2 + 6x + \bggreen{4} \\ -&(2x^3 - &&2x^2) \\ & && 6x^2 - &&2x - 4 \\ & &&\hnsp-(6x^2-&&6x) \\ & &&  &&4x - 4 \\ & && &&\bggreen{-(4x-4)} \end{alignedat}$
					- _Beschreibung_
						- Wir multiplizieren 4 mit $(x − 1)$ .
						- $4 \cdot (x − 1) = 4 x − 4$
					- Das Ergebnis schreiben wir mit einem negativen Vorzeichen in die 6. Zeile.
				- Subtraktion
					- $\begin{alignedat}{4} &( 2x^3 + && 4x^2 - && 2x -  4) : (x - 1) = 2x^2 + 6x + 4 \\ - & (2x^3 - && 2x^2 ) &&&&\\  &&&  6x^2 - && 2x - 4 &&\\ &&& \hnsp-(6x^2 - && 6x) &&\\ &&&&& \bggreen{4x - 4} &&\\ &&&&& \hspace{-2em}\bggreen{ -( -4x - 4)}&& \\ &&&&&&& \hspace{-11.7em}\bggreen{0} \end{alignedat}$
					- _Beschreibung_
						- Das Ergebnis der vorherigen Multiplikation ziehen wir vom Restterm ab.
						- $4 x − 4 − (4 x − 4) = 4 x − 4 − 4 x + 4 = 0$
					- Das Ergebnis schreiben wir in die 7. Zeile.
		- Da kein Rest übrig geblieben ist, ist die Polynomdivision beendet.
		- Falls wir richtig gerechnet haben, gilt:
		- $(2 x^2 + 6 x + 4) \cdot (x − 1) = 2 x^3 + 4 x^2 − 2 x − 4$
- horner schema [link](https://www.mathebibel.de/horner-schema)
  deck:: Uni::Automatisierungstechnik_Theorie
  tags:: flashcard
  id:: 6729bef4-6c12-40e9-bca8-0b1527ebce40
  collapsed:: true
	- ### Berechne $\\(2x^3 + 4x^2 - 2x - 4) : (x - 1) =  ?\\$ mit hilfe des Horner-Schemas.
		- #### Tabelle aufstellen
		  logseq.order-list-type:: number
			- $(\bggreen{2}x^3 + \bggreen{4}x^2 - \bggreen{2}x - \bggreen{4}) : (x \bgred{- 1}) = ?$
			- Wir übertragen die Polynomkoeffizienten – beginnend mit dem 
			  Koeffizienten der höchsten Potenz – in die 1. Zeile einer Tabelle mit 
			  drei Zeilen, wobei wir die 1. Spalte sowie die 2. und 3. Zeile zunächst 
			  frei lassen:
			- $\begin{array}{c|c|c|c|c} & \bggreen{2} & \bggreen{4} & \bggreen{-2} & \bggreen{-4} \\ \hline \phantom{x_1 = 1} && & & \\ \hline & & & & \end{array}$
			- In der 1. Spalte auf Höhe der 2. Zeile schreiben wir die Zahl, die in 
			  der Klammer hinter dem Geteiltzeichen steht, wobei wir das Vorzeichen 
			  umdrehen und  davor schreiben.
			- $\begin{array}{c|c|c|c|c} & 2 & 4 & -2 & -4 \\ \hline x_1 = \bgred{1} & & & & \\ \hline & & & & \end{array}$
		- #### Horner-Schema anwenden
		  logseq.order-list-type:: number
			- Übertrag
				- Zunächst übertragen wir den 1. Koeffizienten der 1. Zeile in die 3. Zeile.
				- $\begin{array}{c|c|c|c|c} & \bgblue{2} & 4 & -2 & -4 \\ \hline x_1 = 1 & & & & \\ \hline & \bgblue{2} & & & \end{array}$
			- Multiplikation
				- Wir multiplizieren die Zahl, die in der 1. Spalte steht, mit dem 
				  Koeffizienten, den wir gerade in die 3. Zeile geschrieben haben:
				- $1 \cdot 2 = 2$
				- Das Ergebnis schreiben wir in das Feld unterhalb des 2. Koeffizienten der 1. Zeile:
				- $\begin{array}{c|c|c|c|c} & 2 & 4 & -2 & -4 \\ \hline x_1 = \bggreen{1} && \bggreen{2} & & \\ \hline & \bggreen{2} & & & \end{array}$
			- Addition
				- Wir addieren das Ergebnis der Multiplikation mit der Zahl darüber
				- $4 + 2 = 6$
				- und schreiben das Ergebnis darunter:
				- $\begin{array}{c|c|c|c|c} & 2 & \bggreen{4} & -2 & -4 \\ \hline x_1 = 1 && \bggreen{2} & & \\ \hline & 2 & \bgblue{6} & & \end{array}$
				- Jetzt wiederholen wir den Multiplikationsschritt und den Additionsschritt bis zum Ende der Tabelle:
					- Multiplikation: $1 \cdot 6 = 6$
						- $\begin{array}{c|c|c|c|c} & 2 & 4 & -2 & -4 \\ \hline x_1 = \bggreen{1} && 2 & \bggreen{6} & \\ \hline & 2 & \bggreen{6} & & \end{array}$
					- Addition: $-2 + 6 = 4$
						- $\begin{array}{c|c|c|c|c} & 2 & 4 & \bggreen{-2} & -4 \\ \hline x_1 = 1 && 2 & \bggreen{6} & \\ \hline & 2 & 6 & \bgblue{4} & \end{array}$
					- Multiplikation: $1 \cdot 4 = 4$
						- $\begin{array}{c|c|c|c|c} & 2 & 4 & -2 & -4 \\ \hline x_1 = \bggreen{1} && 2 & 6 & \bggreen{4} \\ \hline & 2 & 6 & \bggreen{4} & \end{array}$
					- Addition: $-4 + 4 = 0$
						- $\begin{array}{c|c|c|c|c} & 2 & 4 & -2 & \bggreen{-4} \\ \hline x_1 = 1 && 2 & 6 & \bggreen{4} \\ \hline & 2 & 6 & 4 & \bgblue{0} \end{array}$
		- #### Ergebnis aufschreiben
		  logseq.order-list-type:: number
			- Das Ergebnis des Horner-Schemas (entspricht dem Ergebnis der [Polynomdivision]((67290be5-009a-4d75-afb2-6a0484a92450))) können wir in der 3. Zeile ablesen:
			- $\begin{array}{c|c|c|c|c} & 2 & 4 & -2 & -4 \\ \hline x_1 = 1 && 2 & 6 & 4 \\ \hline & \bgblue{2} & \bgblue{6} & \bgblue{4} & \bgblue{0} \end{array}$
			- Dabei ist die letzte Zahl der Rest der Division. In diesem Fall ist der 
			  Rest gleich Null und kann entsprechend weggelassen werden:
			- $\begin{alignedat}{1} (2x^3 + 4x^2 - 2x - 4):(x-1) &= \bgblue{2}x^2 + \bgblue{6}x + \bgblue{4} + \frac{\bgblue{0}}{x-1} \\ &= 2x^2 + 6x + 4 \end{alignedat}$
			-