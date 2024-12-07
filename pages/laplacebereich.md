public:: true
icon:: 🖼
inherit-color-icon-from:: [[logseq-page-color-yellow]] 
template-used:: standard-page
tags:: [[mathematik]], [[uni]], [[Laplace]]
alias:: laplacetransformiert, laplacetransformation, bildbereich, s-bildbereich

- id:: 6724aaef-8410-4c29-8fde-f677528c0937
  tags:: formel
  bezeichnung:: korrespondenz tabelle [[zeitbereich]], [[abtastfolgen]], [[laplacetransformation]], [[z-transformation]]
  | [[zeitbereich]] $f(t)$ | [[abtastfolge]] $\left(f_{k}\right)$ | [[s-bildbereich]] $\hat{f}\left(s\right)$ | [[z-bildbereich]] $f_{z}\left(z\right)$ |
  |---|---|---|---|
  | $\delta(t)$ | $\delta_{k}=\begin{cases} 1 & \text{für} & k=0 \\ 0 & \text{für} & k>0 \end{cases}$ | $1$ | $1$ |
  | $\sigma\left(t\right)$ | $(1^k)$ | $\frac{1}{s}$ | $\frac{z}{z-1}$ |
  | $t$ | $\left(kT_{a}\right)$ | $\frac{1}{s^2}$ | $\frac{T_{a}z}{\left(z-1\right)^{2}}$ |
  | $e^{at}$ | $\left(e^{akT_{a}}\right)$ | $\frac{1}{s-a}$ | $\frac{z}{z-e^{aT_{a}}}$ |
  | $t^{n}e^{at}$ | $\left((k T_{a})^{n}e^{a k T_{a}}\right)$ | $\frac{n!}{\left(s-a\right)^{n+1}}$ | $\frac{\partial^{n}}{\partial a^{n}}\frac{z}{z-e^{a T_{a}}}$ |
  | $\sin\left(bt\right)$ | $\left(\sin\left(bkT_{a}\right)\right)$ | $\frac{b}{s^2+b^2}$ | $\frac{z\sin\left(bT_{a}\right)}{z^2-2z\cos\left(bT_{a}\right)+1}$ |
  | $\cos\left(bt\right)$ | $\left(\cos\left(bkT_{a}\right)\right)$ | $\frac{s}{s^2+b^2}$ | $\frac{z\left(z-\cos\left(bT_{a}\right)\right)}{z^2-2z\cos\left(bT_{a}\right)+1}$ |
  | $e^{at}\sin\left(bt\right)$ | $\left(e_{}^{akT_{a}}\sin\left(bkT_{a}\right)\right)$ | $\frac{b}{\left(s-a\right)^2+b^2}$ | $\frac{ze^{aT_{a}}\sin\left(bT_{a}\right)}{z^2-2ze^{aT_{a}}\cos\left(bT_{a}\right)+e^{2aT_{a}}}$ |
  | $e^{at}\cos\left(bt\right)$ | $e^{akT_a}\cos\left(bkT_{a}\right)$ | $\frac{s-a}{\left(s-a\right)^2+b^2}$ | $\frac{z\left(z-e^{a T_{a}}\cos\left(b T_{a}\right)\right)}{z^{2}-2z e^{a T_{a}}\cos\left(b T_{a}\right)+e^{2a T_{a}}}$ |