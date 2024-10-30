icon:: 🔃
color:: "#caffbf"
template-used:: standard-page
tags:: [[uni]], [[matrix]], [[lineare algebra]] 
alias:: invertierbarkeit, invertieren, inverse

- $\text{Rang}(A) = n \iff \det A \ne 0$
  tags:: formel
  bezeichnung:: bedingung für [[invertierbarkeit]]
	- $A$ ... [[matrix]]
	- $n$ ... zeilen/spalten anzahl der [[matrix]] $A$
- $(A|E)\rightarrow(E|A^{-1})\\\left(\begin{matrix}2 & 1 & 3\\ 0 & -1 & 0\\ -1 & 1 & -2\end{matrix}\left|\begin{matrix}1 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & 1\end{matrix}\right.\right)\rightarrow\left(\begin{matrix}1 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & 1\end{matrix}\left|\begin{matrix}2 & 5 & 3\\ 0 & -1 & 0\\ -1 & -3 & -2\end{matrix}\right.\right)$
  tags:: formel
  bezeichnung:: [[invertieren]] einer $n\times n$ [[matrix]] mittels gaußverfahren
	- $A$ ... zu invertierende [[matrix]]
	- $E$ ... [[einheitsmatrix]]
- $\begin{pmatrix}a_{11} & a_{12}\\ a_{21} & a_{22}\end{pmatrix}^{-1}=\frac{1}{\det\left(A\right)}\cdot\begin{pmatrix}a_{22} & -a_{12}\\ -a_{21} & a_{11}\end{pmatrix}=\frac{1}{a_{11}a_{22}-a_{12}a_{21}}\cdot\begin{pmatrix}a_{22} & -a_{12}\\ -a_{21} & a_{11}\end{pmatrix}$
  tags:: formel
  bezeichnung:: [[inverse]] einer $2\times2$ [[matrix]]
	- $A$ ... [[matrix]]
	- $a_{11}, a_{12}, a_{21},a_{22}$ ... elemente [[matrix]] $A$
- $A^{-1}=\frac{\text{adj}A_{i,j}}{\det A}$
  id:: 83774afb-cb88-4c67-b8d6-b4e2313a52d1
  tags:: formel, adjunkte, determinante
  bezeichnung:: [[invertieren]] einer [[matrix]] mittels [[determinante]] (schneller als mit gaußverfahren)
	- $A$ ... [[matrix]]
	- $i$ ... $i$-te zeile der [[matrix]] $A$
	- $j$ ... $j$-te spalte der [[matrix]] $A$