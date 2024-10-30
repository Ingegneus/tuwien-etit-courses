public:: true
icon:: 🪟
color:: "#9bf6ff"
template-used:: standard-page
tags:: [[uni]], [[automatisierungstechnik]]

- $\mathbf{\Phi}(t) = \exp(\mathbf{A}t) = \left(\sum_{k=0}^{\infty}\mathbf{A}^{k}\frac{t^{k}}{k!}\right)$
  id:: 6717bedf-9586-4607-a3d4-5211a81e6421
  tags:: formel, transitionsmatrix
  bezeichnung:: definition der [[transitionsmatrix]]
	- $\Phi(t)$ ... [[transitionsmatrix]]
	- $t$ ... zeit
	- $\mathbf{A}$ ... [[Systemmatrix]] eines [[linearen]], [[autonomen]] systems
- $\tilde{\Phi}(t)=e^{\tilde{\mathbf{A}}t}=\begin{pmatrix}e^{a_1t} & 0 & \cdots & 0\\ 0 & e^{a_2t} &  & 0\\ \vdots & \vdots & \ddots & \vdots\\ 0 & 0 & \cdots & e^{a_{n}t}\end{pmatrix}$
  tags:: formel, transitionsmatrix
  bezeichnung:: [[transitionsmatrix]] in regulärer [[zustandstransformation]]
	- $\tilde{\Phi}(t)$ ... transformierte [[transitionsmatrix]]
	- $t$ ... zeit
	- $\tilde{\mathbf{A}}$ ... tranformierte [[Systemmatrix]] eines [[linearen]], [[autonomen]] systems ([[diagonalform]])
	- $a
	- $a_{i}$ ... die diagonalelemente der [[matrix]] $\tilde{\mathbf{A}}$
- $\tilde{\Phi}(t)=e^{\tilde{\mathbf{A}}t}=e^{\mathbf{D}+\mathbf{N}}=e^{\mathbf{D}t}e^{\mathbf{N}t}=\begin{pmatrix}e^{d_1t} & 0 & \cdots & 0\\ 0 & e^{d_2t} &  & 0\\ \vdots & \vdots & \ddots & \vdots\\ 0 & 0 & \cdots & e^{d_{n}t}\end{pmatrix}e^{\mathbf{N}t}$
  id:: 671b4e73-5df4-4f5c-b69e-02176e8edb95
  tags:: formel, transitionsmatrix
  bezeichnung:: [[transitionsmatrix]] in regulärer [[zustandstransformation]]
	- $\tilde{\Phi}(t)$ ... transformierte [[transitionsmatrix]]
	- $t$ ... zeit
	- $\tilde{\mathbf{A}}$ ... tranformierte [[Systemmatrix]] eines [[linearen]], [[autonomen]] systems ([[jordansche normalform]])
	- $d_{i}$ ... die diagonalelemente der [[matrix]] $\tilde{\mathbf{A}}$