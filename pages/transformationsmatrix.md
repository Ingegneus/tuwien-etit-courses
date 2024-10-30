public:: true
icon:: 💱
inherit-color-icon-from:: [[logseq-page-color-pink]]
template-used:: standard-page
tags:: [[uni]], [[mathematik]]

- $\mathbf{V}=\begin{pmatrix}\mathbf{v}_1 & \mathbf{v}_2 & \cdots & \mathbf{v}_{n}\end{pmatrix}$
  tags:: formel
  bezeichnung:: die [[transformationsmatrix]] bei der berechnung der [[transformationsmatrix]] $\mathbf{V}$ der [[matrix]] $\mathbf{A}$ in die [[jordansche normalform]]
	- $\bar{\mathbf{V}}$ ... [[transformationsmatrix]]
	- $\mathbf{v}_{i}$ ... [[eigenvektoren]] in spalten form der [[matrix]] $\mathbf{A}$
	- $\mathbf{V}=\underbrace{\begin{pmatrix}\mathbf{v}_1 & \mathbf{v}_1^{*} & \cdots & \mathbf{v}_{n} & \mathbf{v}_{n}^{*}\end{pmatrix}}_{\bar{\mathbf{V}}}\mathbf{T}\\=\begin{pmatrix}\underbrace{\frac12\left(\mathbf{v}_1+\mathbf{v}_1^{*}\right)}_{\text{Re}(\mathbf{v}_1)} & \underbrace{\frac{i}{2}\left(\mathbf{v}_1^{*}-\mathbf{v}_1\right)}_{\text{Im}(\mathbf{v}_1)} & \cdots & \underbrace{\frac12\left(\mathbf{v}_{r}+\mathbf{v}_{r}^{*}\right)}_{\text{Re}(\mathbf{v}_{r})} & \underbrace{\frac{i}{2}\left(\mathbf{v}_{r}^{*}-\mathbf{v}_{r}\right)}_{\text{Im}(\mathbf{v}_{r})}\end{pmatrix}$
	  id:: 671e6a4a-7f50-4907-873e-4ba1e3c4fca5
	  tags:: formel
	  bezeichnung:: [[transformationsmatrix]] für die ähnlichkeitstransformation der [[matrix]] $\mathbf{A}$ auf die [[jordansche normalform]], wenn die [[eigenvektoren]] [[konjugiert komplex]] sind
	  collapsed:: true
		- $\mathbf{V}$ ... [[transformationsmatrix]]
		- $\bar{\mathbf{V}}$ ... eine [[transformationsmatrix]] [link](((6720c624-d622-49e7-8904-bf8803605c50)))
		- $\mathbf{T}$ ... eine [[transformationsmatrix]] [link](((671e6fb4-11e3-459b-97b5-51f2c8fb6697)))
-
- $\mathbf{T}=\frac12\begin{pmatrix}1 & -i & \cdots & 0 & 0\\ 1 & i & \cdots & 0 & 0\\ \vdots & \vdots & \ddots & \vdots & \vdots\\ 0 & 0 & \cdots & 1 & -i\\ 0 & 0 & \cdots & 1 & i\end{pmatrix}~,\\ \mathbf{T^{-1}}=\frac12\begin{pmatrix}1 & 1 & \cdots & 0 & 0\\ i & -i & \cdots & 0 & 0\\ \vdots & \vdots & \ddots & \vdots & \vdots\\ 0 & 0 & \cdots & 1 & 1\\ 0 & 0 & \cdots & i & -i\end{pmatrix}$
  tags:: formel
  bezeichnung:: eine [[transformationsmatrix]]
  id:: 671e6fb4-11e3-459b-97b5-51f2c8fb6697
  collapsed:: true
	- $\mathbf{T}$ ... eine [[matrix]]
	- $i$ ... imaginäre einheit
- $\bar{\mathbf{V}}=\begin{pmatrix}\mathbf{v}_1 & \mathbf{v}_1^{*} & \cdots & \mathbf{v}_{n} & \mathbf{v}_{n}^{*}\end{pmatrix}$
  id:: 6720c624-d622-49e7-8904-bf8803605c50
  tags:: formel
  bezeichnung:: eine [[transformationsmatrix]] die als zwischenschritt bei der berechnung der endgültigen [[transformationsmatrix]] $\mathbf{V}$ der [[matrix]] $\mathbf{A}$ in die [[jordansche normalform]] dient
  collapsed:: true
	- $\mathbf{v}_{i}$ ... [[eigenvektoren]] in spalten form der [[matrix]] $\mathbf{A}$
	- $\mathbf{v}_{i}^{*}$ ... [[konjugiert komplexe]] [[eigenvektoren]] in spalten form der [[matrix]] $\mathbf{A}$