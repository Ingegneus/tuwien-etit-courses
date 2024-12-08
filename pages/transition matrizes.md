public:: true
icon:: 🪟
color:: "#9bf6ff"
template-used:: standard-page
tags:: [[uni]], [[automatisierungstechnik]], [[matrix]]
alias:: transitionsmatrix, transitionsmatrizen, transition matrix

- $\mathbf{\Phi}(t) = \exp(\mathbf{A}t) = \left(\sum_{k=0}^{\infty}\mathbf{A}^{k}\frac{t^{k}}{k!}\right)$
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
  tags:: formel, transitionsmatrix
  bezeichnung:: [[transitionsmatrix]] in regulärer [[zustandstransformation]], wenn die transformierte [[Systemmatrix]] sich aufteilen lässt in $\mathbf{D}+\mathbf{N}$
  id:: 671b4e73-5df4-4f5c-b69e-02176e8edb95
	- $\tilde{\Phi}(t)$ ... transformierte [[transitionsmatrix]]
	- $t$ ... zeit
	- $\tilde{\mathbf{A}}$ ... tranformierte [[Systemmatrix]] eines [[linearen]], [[autonomen]] systems ([[jordansche normalform]])
	- $\mathbf{D}$ ... diagonal [[matrix]]
	- $\mathbf{N}$ ... nilpotente [[matrix]]
	- $d_{i}$ ... die diagonalelemente der [[matrix]] $\tilde{\mathbf{A}}$
- $\tilde{\Phi}(t)=e^{\mathbf{\Omega}t} \\ =\begin{pmatrix}{e^{\alpha_1t}\cos(\beta_1t)} & e^{\alpha_1t}\sin(\beta_1t) & \cdots & {0} & 0\\ {-e^{\alpha_1t}\sin(\beta_1t)} & {e^{\alpha_1t}\cos(\beta_1t)} & {\cdots} & {0} & 0\\ {\vdots} & {\vdots} & \ddots & \vdots & \vdots\\ {0} & {0} & {\cdots} & {e^{\alpha_{r}t}\cos(\beta_{r}t)} & e^{\alpha_{r}t}\sin(\beta_{r}t)\\ {0} & {0} & {\cdots} & -e^{\alpha_{r}t}\sin(\beta_{r}t) & {e^{\alpha_{r}t}\cos(\beta_{r}t)}\end{pmatrix}$
  tags:: formel, transitionsmatrix
  bezeichnung:: [[transitionsmatrix]] in regulärer [[zustandstransformation]], wenn die [[eigenwerte]] der [[Systemmatrix]] $\mathbf{A}$ [[konjugiert komplex]] sind
  id:: 67226f1c-9890-463b-9a3d-cbf28270b121
	- $\tilde{\Phi}(t)$ ... transformierte [[transitionsmatrix]]
	- $t$ ... zeit
	- ${\mathbf{\Omega}}$ ... tranformierte [[Systemmatrix]] eines [[linearen]], [[autonomen]] systems wenn die [[eigenwerte]] [[konjugiert komplex]] sind ([[jordansche normalform]]) [link](((672106f0-bdcd-4f36-bc24-36f6986eb183)))
	- $\alpha_{i}$ ... [[realteil]] des $i$-ten [[eigenwerts]] der [[matrix]] ${\mathbf{A}}$
	- $\beta_{i}$ ... [[imaginärteil]] des $i$-ten [[eigenwerts]] der [[matrix]] ${\mathbf{A}}$
- $\mathbf{\Phi}(s) = (s\mathbf{E}-\mathbf{A})^{-1}$
  tags:: formel
  bezeichnung:: [[transitionsmatrix]] im [[laplacebereich]]
  id:: 67234c51-e437-4e1f-a175-2035d14681aa
	- $\mathbf{\Phi}(s)$ ... [[transitionsmatrix]] im $s$-bereich
	- $s$ ... bildvariable
	- $\mathbf{E}$ ... [[einheitsmatrix]]
	- $\mathbf{A}$ ... [[Systemmatrix]]