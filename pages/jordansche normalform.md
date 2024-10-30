icon:: ↘️
inherit-color-icon-from:: [[logseq-page-color-red]]
template-used:: standard-page
tags:: [[uni]], [[mathematik]]

- $\tilde{\mathbf{A}}=\mathbf{V}^{-1}\mathbf{AV}$
  tags:: formel
  bezeichnung:: transformation auf [[jordansche normalform]]
	- ${}\tilde{\mathbf{A}}$ ... [[jordansche normalform]] der [[matrix]] $\mathbf{A}$
	- $\mathbf{V}$ ... [[transformationsmatrix]]
	- $\mathbf{A}$ ... [[matrix]]
- $\tilde{\mathbf{A}}=\mathbf{T}^{-1} \underbrace{\bar{\mathbf{V}}^{-1} \mathbf{A} \bar{\mathbf{V}}}_{\mathbf{\Lambda}} \mathbf{T} = \mathbf{\Omega} = \begin{pmatrix} {\alpha_{1}}&{\beta_{1}}&{\cdots}&{0}&{0}\\ {-\beta_{1}}&{\alpha_{1}}&{\cdots}&{0}&{0}\\ {\vdots}&{\vdots}&{\ddots}&{\vdots}\\ {0}&{0}&{\cdots}&{\alpha_{r}}&{\beta_{r}}\\ {0}&{0}&{\cdots}&{-\beta_{r}}&{\alpha_{r}}  \end{pmatrix}$
  id:: 672106f0-bdcd-4f36-bc24-36f6986eb183
  tags:: formel
  bezeichnung:: transformation auf [[jordansche normalform]], unter der voraussetzung, dass die [[eigenvektoren]] der [[matrix]] $\mathbf{A}$ [[konjugiert komplex]] sind
	- ${}\tilde{\mathbf{A}}$ ... [[jordansche normalform]] der [[matrix]] $\mathbf{A}$
	- $\mathbf{T}$ ... [[transformationsmatrix]] [link](((671e6fb4-11e3-459b-97b5-51f2c8fb6697)))
	- $\bar{\mathbf{V}}$ ... [[transformationsmatrix]] [link](((6720c624-d622-49e7-8904-bf8803605c50)))
	- $\mathbf{A}$ ... [[matrix]]
	- $\mathbf{\Lambda}$ ... zwischenschritt [[matrix]] für $\tilde{\mathbf{A}}$ [link](((6720fa1a-e78f-495e-98f9-18eb65afbbfe)))
	- $\alpha_i$ ... [[realteil]] des $i$-ten [[eigenwerts]]
	- $\beta_i$ ... [[imaginärteil]] des $i$-ten [[eigenwerts]]
- $\bm{\Lambda}=\bar{\mathbf{V}}^{-1}\mathbf{A}\bar{\mathbf{V}} = \\ \begin{pmatrix}\alpha_1+i\beta_1 & 0 & \cdots & 0 & 0\\ 0 & \alpha_1-i\beta_1 &  & 0 & 0\\ \vdots & \vdots & \ddots & \vdots & \vdots\\ 0 & 0 & \cdots & \alpha_1+i\beta_1 & 0\\ 0 & 0 & \cdots & 0 & \alpha_r-i\beta_r\end{pmatrix}$
  id:: 6720fa1a-e78f-495e-98f9-18eb65afbbfe
  tags:: formel
  bezeichnung:: zwischenstufe der [[matrix]] $\mathbf{A}$ auf [[jordansche normalform]], unter der voraussetzung, dass die [[eigenvektoren]] von  $\mathbf{A}$ [[konjugiert komplex]] sind
	- $\bar{\mathbf{V}}$ ... [[transformationsmatrix]] [link](((671e6a4a-7f50-4907-873e-4ba1e3c4fca5)))
	- $\mathbf{A}$ ... [[matrix]]
	- $\alpha_i$ ... [[realteil]] des $i$-ten [[eigenwerts]]
	- $\beta_i$ ... [[imaginärteil]] des $i$-ten [[eigenwerts]]
- was sind jordan blöcke?
  deck:: Uni::Automatisierungstechnik_Theorie
  tags:: flashcard, wip
	-