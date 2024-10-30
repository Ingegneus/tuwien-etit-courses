icon:: 🔳
color:: "#fdffb6"
template-used:: standard-page
tags:: [[lineare algebra]] 
alias:: matrix, matrizen

- wenn die dimension angegeben wird, dann werden zuerst die zeilen, dann die spalten angegeben. also eine $3 \times 2$ matrix schaut so aus
  $\begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \\ a_{31} & a_{32} \end{pmatrix}$
- die indizes sind auch immer zuerst die zeile, dann die spalte
- $\begin{pmatrix}a_{11} & a_{12}\\ a_{21} & a_{22}\end{pmatrix}^{-1}=\frac{1}{\det\left(A\right)}\cdot\begin{pmatrix}a_{22} & -a_{12}\\ -a_{21} & a_{11}\end{pmatrix}=\frac{1}{a_{11}a_{22}-a_{12}a_{21}}\cdot\begin{pmatrix}a_{22} & -a_{12}\\ -a_{21} & a_{11}\end{pmatrix}$
  tags:: formel
  bezeichnung:: invertieren/inverse einer $2\times2$ [[matrix]]
	- $A$ ... [[matrix]]
	- $a_{11}, a_{12}, a_{21},a_{22}$ ... elemente [[matrix]] $A$
- $(A|E)\rightarrow(E|A^{-1})\\\left(\begin{matrix}2 & 1 & 3\\ 0 & -1 & 0\\ -1 & 1 & -2\end{matrix}\left|\begin{matrix}1 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & 1\end{matrix}\right.\right)\rightarrow\left(\begin{matrix}1 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & 1\end{matrix}\left|\begin{matrix}2 & 5 & 3\\ 0 & -1 & 0\\ -1 & -3 & -2\end{matrix}\right.\right)$
  tags:: formel
  bezeichnung:: invertieren einer $n\times n$ [[matrix]] mittels gaußverfahren
	- $A$ ... zu invertierende [[matrix]]
	- $E$ ... [[einheitsmatrix]]
- $A^{-1}=\frac{\text{adj}A_{i,j}}{\det A}$
  id:: 83774afb-cb88-4c67-b8d6-b4e2313a52d1
  tags:: formel, adjunkte, determinante
  bezeichnung:: invertieren einer [[matrix]] mittels [[determinante]] (schneller als mit gaußverfahren)
	- $A$ ... [[matrix]]
	- $i$ ... $i$-te zeile der [[matrix]] $A$
	- $j$ ... $j$-te spalte der [[matrix]] $A$