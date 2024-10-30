icon:: 🟪
color:: "#bdb2ff"
template-used:: standard-page
tags:: [[uni]], [[linear algebra]] 
alias:: [[determinanten]]

- $\det\left(A\right)=\left\vert A\right\vert=\left\vert\begin{pmatrix}a_{11} & a_{12}\\ a_{21} & a_{22}\end{pmatrix}\right\vert=a_{11}a_{22}-a_{12}a_{21}$
  tags:: formel
  bezeichnung:: berechnung der [[derterminanten]] einer $2\times2$ [[matrix]]
	- $A$ ... [[matrix]]
	- $a_{ij}$ ... elemente der [[matrix]]
- $\begin{array}{ll}\det\left(A\right)=\left\vert A\right\vert=\left\vert\begin{pmatrix}a_{11} & a_{12} & a_{13}\\ a_{21} & a_{22} & a_{23}\\ a_{31} & a_{32} & a_{33}\end{pmatrix}\right\vert= & a_{11}a_{22}a_{33}+a_{12}a_{23}a_{31}+a_{13}a_{21}a_{32}-\\  & -a_{113}a_{22}a_{31}-a_{11}a_{23}a_{32}-a_{12}a_{21}a_{33}\end{array}$
  tags:: formel
  bezeichnung:: berechnung der [[derterminanten]] einer $3\times3$ [[matrix]] (regel von [[Sarrus]])
  id:: 671678e8-ee03-4007-b265-9bc44d9e4b10
	- $A$ ... [[matrix]]
	- $a_{ij}$ ... elemente der [[matrix]] $A$
	- visualiesierung
	  collapsed:: true
		- ![img](../assets/regel-sarrus.webp){:width 400}
- ${\text{det}}A=\sum_{i=1}^{n}(-1)^{i+j}\cdot a_{i j}\cdot{\text{det}}A_{i j} \quad (j\text{-te Spalte})\\ {\text{det}}A=\sum_{i=1}^{n}(-1)^{i+j}\cdot a_{i j}\cdot{\text{det}}A_{i j} \quad (i\text{-te Zeile})$
  tags:: formel
  bezeichnung:: berechnung einer der [[determinanten]] einer $n\times n$ [[matrix]] mit dem [[Laplace]]schen Entwicklungssatz. es muss entschieden werden ob nach zeile oder spalte entwickelt wird.
	- $A$ ... [[matrix]]
	- $i$ ... laufindex der zeilen
	- $j$ ... laufindex der spalten
	- $a_{ij}$ ... elemente der [[matrix]] $A$
	- $A_{ij}$ ... $\left(n-1\right)\times\left(n-1\right)$ [untermatrix]([[matrix]]) von $A$, die durch Streichen der $i$-ten Zeile und $j$-ten Spalte entsteht
- $M_{i,j}=\det\begin{pmatrix}{a_{1,1}} & {\cdots} & {}a_{1,j-1} & {a_{1,j+1}} & {\cdots} & {a_{i,n}}\\ {\vdots} & {\ddots} & {\vdots} & {\vdots} & \ddots & {\vdots}\\ {a_{i-1,1}} & {\cdots} & {a_{i-i,j-1}} & {a_{i-i,j+1}} & {\cdots} & a_{i-i,n}\\ {a_{i+1,1}} & {\cdots} & {a_{i+1,j-1}} & {a_{i+i,j+1}} & {\cdots} & a_{i+1,n}\\ {\vdots} & {\ddots} & {\vdots} & {\vdots} & \ddots & \vdots\\ {a_{n,1}} & {\cdots} & {a_{n,j-1}} & {a_{n,j+1}} & {\cdots} & a_{n,n}\end{pmatrix}$
  tags:: formel
  bezeichnung:: minoren/unter[[determinanten]] der [[matrix]] $A$ (einfach gesagt, die [[determinante]] wenn man die $i$-te zeile und $j$-te spalte streicht)
  id:: 67214d42-a47c-4a89-b298-2d1675c2f281
	- $M_{i,j}$ ... minoren/unter[[determinanten]] der [[matrix]] $A$
	- $i$ ... $i$-te zeile der [[matrix]] $A$
	- $j$ ... $j$-te spalte der [[matrix]] $A$