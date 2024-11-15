icon:: 🛜
inherit-color-icon-from:: [[logseq-page-color-purple]]
tags:: uni
alias:: wave propagation, wellenausbreitungs

- ## vorlesungen
	- ![📚 WA-Skriptum-17.Auflage.pdf](file://C:\Users\Matteo\Documents\Uni\Wellenausbreitung\WA-Skriptum-17.Auflage.pdf)
	- [[wellen vo temp]]
- ## beispiele
	- Übergang von Vakuum nach Glas
	  background-color:: green
		- Variante 1) Eine zirkular polarisierte Welle mit einem Querschnitt von $A = \mathrm{3~mm^2}$ und einer Leistung von $P = \mathrm{10~mW}$ wird unter dem Brewster-Winkel auf eine Grenzﬂäche zwischen Vakuum ($n_1 = \mathrm{1}$) und Glas ($n_2 = \mathrm{1.6}$) eingestrahlt.
		  background-color:: green
		  ![img](../assets/Documents/WA_vakuum_glas_bsp1.webp){:width 400}
			- a) Berechnen Sie Einfallswinkel $\Theta_e$, Reﬂexionswinkel $\Theta_r$ und Austrittswinkel $\Theta_t$ und zeichnen Sie diese in die Skizze ein!
			  background-color:: green
				- formeln
				  collapsed:: true
					- $\Theta_i = \Theta_r$
					  tags:: formel
					  bezeichnung:: Reflektions gesetz
						- $\Theta_i$ ... einfallswinkel (***i***nbound) $\mathrm{[°]}$
						- $\Theta_r$ ... reflektionswinkel (***r***eflected) $\mathrm{[°]}$
					- ((6734720f-e42f-46c0-a512-3075ea423042))
					- $\Theta_{b}=\arctan\left(\frac{n_2}{n_1}\right)$
					  tags:: formel
					  bezeichnung:: [[brewster winkel]]
						- $\Theta_b$ ... Brewster winkel $\mathrm{[°]}$
						- $n_1$ ... brechungsindex $\mathrm{[-]}$
						- $n_2$ ... brechungsindex $\mathrm{[-]}$
			- b) Berechnen Sie die Querschnitsfläche $A$ des transmittierten Strahls
			  background-color:: green
				- formeln
					- ((6734720b-5c51-4f95-ac33-ed541e99c1ca))
			- c) Berechnen Sie die TE und TM-Anteile ($E$ und $H$) der reﬂektierten und der transmittierten Welle!
			  background-color:: green
				- formeln
					- ((6735b379-5292-4604-baef-85a4c9a6fc3f))
					- ((6735b379-80fa-4b2a-be2d-af5089fe1fa8))
					- ((6735b379-8ba8-4a90-b5e2-8b5b38036526))
					- ((6735b379-1a1f-417e-8323-7fe94bd9e2cf))
					- $n=\frac{k_2}{k_1}=\sqrt{\frac{\varepsilon_2}{\varepsilon_1}}=\frac{n_2}{n_1}$
					  tags:: formel
					  bezeichnung:: relativer brechnungsindex
					  collapsed:: true
						- $n$ ... relativer brechnungsindex $\mathrm{\left[ - \right]}$
						- $k_1$ ... wellenzahl $\mathrm{\left[ \frac{rad}{m} \right]}$
						- $k_2$ ... wellenzahl $\mathrm{\left[ \frac{rad}{m} \right]}$
						- $\varepsilon_1$ ... relative permittivität $\mathrm{\left[ - \right]}$
						- $\varepsilon_2$ ... relative permittivität $\mathrm{\left[ - \right]}$
						- $n_1$ ... brechnungsindex $\mathrm{\left[ - \right]}$
						- $n_2$ ... brechnungsindex $\mathrm{\left[ - \right]}$
					- $\Gamma_{TM} = 0$
					  tags:: formel
					  bezeichnung:: reflektionsfaktor wenn einfallswinkel = [[brewster winkel]] [FS](((6735b379-a4a2-48f4-800f-7b9292b7a3a1)))
						- $\Gamma_{TM}$ ... reflektionsfaktor $\mathrm{\left[ - \right]}$
					- $P=\frac{E_0^2A}{2\eta}$
					  tags:: formel, wip
					  bezeichnung:: abgestrahlte leistung einer [[antenne]]
						- $P$ ... Strahlleistung $\mathrm{\left[ W \right]}$
						- $E$ ...
						- $A$ ...
						- $\eta$ ... wellenwiderstand $\mathrm{\left[ \Omega \right]}$
						- skript
						  collapsed:: true
							- ((6737138c-9739-4333-8d9b-11a498e0f337))
					- $\eta H = E$
					  tags:: formel, wip
					  bezeichnung:: abgeleitet von hier [link](((6735b379-187a-4654-8126-efd8a322477b)))
						- $\eta$ ... wellenwiderstand $\mathrm{\left[ \Omega \right]}$
						- $H$ ... magnetsiche feldstärke $\mathrm{\left[ \frac{A}{m} \right]}$
						- $E$ ... elektrische feldstärke $\mathrm{\left[ \frac{V}{s} \right]}$
					- $\eta=\sqrt{\frac{\mu}{\varepsilon}}$
					  tags:: formel
					  bezeichnung:: wellenwiderstand
						- $\eta$ ... wellenwiderstand $\mathrm{\left[ \Omega \right]}$
						- $\mu$ ... permeabilität des mediums $\mathrm{\left[ \frac{A}{s} \right]}$
						- $\varepsilon$ ... permettivität des mediums $\mathrm{\left[ \frac{V}{m} \right]}$
			- d) Berechnen Sie die Elliptizität der reﬂektierten und der transmittierten Welle in $\mathrm{dB}$!
			  background-color:: green
				- formeln
			- [📚 2024-11-12 16h29m.xopp](../assets/documents/2024-11-12 16h29m.xopp)
			- ![📚 2024-11-12 16h29m_annotated.pdf](../assets/documents/2024-11-12 16h29m_annotated.pdf)
		- Variante 2) Ein Lichtstrahl der Sonne (unpolarisiert, aber TM, TE gleich stark) fällt zu später Stunde ($\Theta_e = 75°$) auf einen See ($n2 = 1.33$). An der glatten Wasseroberﬂäche wird er reﬂektiert. Zwei Fotografen fotograﬁeren diese Landschaft. Der zweite verwendet ein ideales Polarisationsﬁlter um die Reﬂexion der Sonne im Wasser zu unterdrücken.
		  background-color:: green
		  ![img](../assets/documents/WA_vakuum_glas_bsp2.webp){:width 400}
			- a) Wie groß ist die (gesamte) reﬂektierte Lichtleistung im Verhältnis zur eingestrahlten (in $\mathrm{dB}$)? Zeichnen Sie alle verwendeten Winkel ein.
			  background-color:: green
			- b) Wie gut kann das ideal eingesetzte Polarisationsﬁlter des zweiten Fotografen die Reﬂexion im Vergleich zum ersten Fotografen unterdrücken (in $\mathrm{dB}$)?
			  background-color:: green
	- Stehende Welle im verlustbehafteten Medium
	  background-color:: green
		- Eine sich im verlustbehafteten Medium (z.B.: trockener Erdboden) ausbreitende ebene Welle mit $f = \mathrm{20~MHz}$ wird von einer auf die Ausbreitungsrichtung senkrecht stehenden metallischen Wand mit unendlicher Leitfähigkeit reﬂektiert (siehe Abbildung). Die Amplitude der einfallenden Welle bei $z = 0$ beträgt $\mathrm{5~V/m}$.
		  background-color:: green
		  Hinweis: $\varepsilon_0 = \mathrm{8,854· 10^{−12}~As/Vm}$, $µ0 = \mathrm{4π · 10^{−7}~Vs/Am}$.
		  ![img](../assets/documents/WA_stehende_welle_wand_bsp1.webp){:width 400}
			- a) Wie groß ist die Phasengeschwindigkeit $v_P$?
			  background-color:: green
			- b) Setzten Sie die einfallende Welle an ($E_e$ und $H_e$) und berechnen Sie die Wellenzahl $k_e$. Wie groß ist die Dämpfung in $\mathrm{dB/m}$
			  background-color:: green
			- c) Berechnen Sie die komplexe Amplitude und den zeitlichen Verlauf der einfallenden Welle am Ort der metallischen Wand $z_0 = \mathrm{8~m}$!
			  background-color:: green
			- d) Finden Sie einen Ansatz für die reﬂektierte Welle ($E_r$ und $H_r$)! Wie muss der zeitliche Verlauf der reﬂektierten Welle aussehen, damit die Randbedingungen erfüllt sind?
			  background-color:: green
			- e) Berechnen Sie die Hüllkurve des Gesamtfeldes
			  background-color:: green
- ## flashcards
	- ### index
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
	- wofür stehen TM, TE und TEM? 
	  deck:: Uni::Wellenausbreitung_Theorie
	  tags:: flashcard
	  id:: 6736247d-67c9-4c4e-ba0e-2d9d5c1a369d
		- TM
			- ***T***ransversal ***M***agnetische Welle
			- $H_z=0$ also der magnetische feldstärke vektor ist komplett transversal ($90°$) zur ausbreitungsrichtung (hier $z$)
		- TE
			- ***T***ransversal ***E***lektrische Welle
			- $E_z=0$ also der elektrische feldstärke vektor ist komplett transversal ($90°$) zur ausbreitungsrichtung (hier $z$)
		- TEM
			- ***T***ransversal ***E***lektrische ***M***agnetische Welle
			- $H_z = E_z = 0$ also der magnetische und elektrische feldstärke vektor ist komplett transversal ($90°$) zur ausbreitungsrichtung (hier $z$)