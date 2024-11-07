icon:: 📉
inherit-color-icon-from:: [[logseq-page-color-red]]
tags:: [[uni]], [[schaltungstechnik]], [[automatisierungstechnik]], [[signale uns systeme 1]] 
alias:: Übertragungsfunktion

- $G(s) = \frac{Y\left(s\right)}{X\left(s\right)}$
  tags:: formel
  bezeichnung:: allgemeine [[Übertragungsfunktion]] im [[s-bildbereich]]
	- $s$ ... bildvariable
	- $G(s)$ ... [[Übertragungsfunktion]]
	- $Y(s)$ ... [[eingangsgröße]] im [[bildbereich]] (oft auch als $\hat{y}$ dargestellt)
	- $X(s)$ ... [[eingangsgröße]] im [[bildbereich]] (oft auch als $\hat{x}$ oder $\hat{u}$ dargestellt)
- $G(s) = \frac{z\left(s\right)}{n\left(s\right)}$
  tags:: formel
  bezeichnung:: allgemeine [[Übertragungsfunktion]] im [[s-bildbereich]]
  id:: 672a3290-b9d3-4434-9d7c-133715e031d8
	- $s$ ... bildvariable
	- $G(s)$ ... [[Übertragungsfunktion]]
	- $z(s)$ ... [zählerpolynom]([[polynom]]) im [[bildbereich]]
	- $n(s)$ ... [nennerpolynom]([[polynom]]) im [[bildbereich]]
- ((672a3290-b9d3-4434-9d7c-133715e031d8)) $= \mathbf{C} \mathbf{\Phi}(s) \mathbf{B} +\mathbf{D}$
  id:: 67254498-19a4-47c4-a559-8bad13c5ebe3
  tags:: formel
  bezeichnung:: [[Übertragungsfunktion]] eines systems im $s$-[bereich]([[laplacetransformiert]])
	- $\mathbf{C}$ ... [[Ausgangsmatrix]]
	- $\mathbf{\Phi}(s)$ ... [[transitionsmatrix]]
	- $\mathbf{B}$ ... [[Eingangsmatrix]]
	- $\mathbf{D}$ ... [[Durchgriffsmatrix]]
- wenn bei ((67254498-19a4-47c4-a559-8bad13c5ebe3)), $~\mathbf{D} = 0$, dann ist immer $\opn{grad}(z(s)) < \opn{grad}(n(s))$ [[realisierbarkeit]]? 
  tags:: formel, wip
  bezeichnung:: eigenschaft einer [[Übertragungsfunktion]].
	- $\mathbf{D}$ ... [[Durchgriffsmatrix]]
	- $n(s)$ ... [Nennerpolynom]([[polynom]])
	- $z(s)$ ... [Zählerpolynom]([[polynom]])