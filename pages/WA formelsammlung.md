public:: true
icon:: 📚
inherit-color-icon-from:: [[logseq-page-color-purple]] 
template-used:: standard-page
tags:: [[wellenausbreitung]], formeln
alias:: cheat sheet

- ![📚 Formelsammlung_7.Auflage.pdf](.\assets\uni-unterlagen\Wellenausbreitung\Formelsammlung_7.Auflage.pdf)
- ## [[maxwell]]
  collapsed:: true
	- [S. 1](((677f9cf8-f37e-4b35-8c07-3ff96a2323f1)))
	- $\vect{\nabla} \cdot \vect{S} = \opn{lim}_{\mathcal{V} \to0} \frac{1}{V} \oint_{\Sigma} \vect{S} \cdot \d  \vect{F} = - \frac{\partial}{\partial t} \rho$
	- $\vect{\nabla} \cdot( \vect{\nabla} \times \vect{H}) \equiv0$
	- $\vect{\nabla} \times \vect{H} = \vect{S} + \frac{\partial}{\partial t} \vect{D}$
	- $\vect{\nabla} \cdot \vect{S} = - \frac{\partial}{\partial t}( \vect{\nabla} \cdot \vect{D}) = - \frac{\partial}{\partial t} \rho$
	- $\vect{\nabla} \cdot \vect{S} + \frac{\partial}{\partial t} \rho = 0$
	- ((674d7759-514d-4a2f-86fd-5eefd6ce3560))
	- ((674d7759-9266-4b79-976c-cf24786054dc))
	- ((674d7759-5865-4965-ba0b-734256ee8c82))
	- ((674d7759-9dd7-4dae-9bfd-fab05a74ed26))
	- $\int_{\Sigma} \vect{D} \cdot \d  \vect{F} = \int_{\tau} \rho \d V$
	  id:: 674d7759-90de-4016-b2c3-c6ff31f602cd
	- $\int_{\Sigma} \vect{B} \cdot \d  \vect{F} = 0$
	  id:: 674d7759-c6ee-43ea-b699-6c73aca1240d
	- $\oint \vect{E} \cdot \d  \vect{l} =  - \frac{\partial}{\partial t} \int_{\Sigma} \vect{B} \cdot \d  \vect{F}$
	  id:: 674d7759-0a77-4eca-b8f6-dece037a378a
	- $\oint \vect{H} \cdot \d  \vect{l} =  \int_{\Sigma} \vect{S} \cdot \d  \vect{F} + \frac{\partial}{\partial t} \int_{\Sigma} \vect{D} \cdot \d  \vect{F}$
	  id:: 674d7759-852f-457f-b1c5-6a68ea277918
	- $\vect{F} = q \left( \vect{E} + \vect{v} \times \vect{B} \right)$
	- $\vect{S} = \sigma \vect{E}$
	- $\vect{S} = \rho \vect{v}$
	- $\vect{D} = \varepsilon \vect{E} = \varepsilon_{r} \varepsilon_{0} \vect{E}$
	- $\vect{B} = \mu \vect{H} = \mu_{r} \mu_{0} \vect{H}$
	- $\frac{\partial}{\partial t} \rho( \vect{r},t) + \frac{\sigma}{\varepsilon} \rho( \vect{r},t) = 0$
	- $\rho( \vect{r},t) = \rho_{0}( \vect{r})e^{ - \frac{\sigma}{\varepsilon}t}$
	- $\tau_{\d } = \frac{\varepsilon}{\sigma}$
	- $\vect{\nabla} \cdot \vect{E} = 0$
	- $\vect{E}(x,y,z,t) = \vect{E}( \vect{r},t) = \opn{Re} \{\vect{E}( \vect{r})e^{j \omega t} \} = \frac{1}{2} \left( \vect{E}( \vect{r})e^{j \omega t} + \vect{E^{*}}( \vect{r})e^{ - j \omega t} \right)$
	- $\vect{\nabla} \times \vect{H} = \vect{S} + j \omega \vect{D} = \sigma \vect{E} + j \omega \varepsilon \vect{E} = j \omega \delta \vect{E}$
	- $\delta = \varepsilon + \frac{\sigma}{j \omega} = \varepsilon - j \frac{\sigma}{\omega}$
	  id:: 67646b82-d9c1-4b67-aa1d-70d30b6541ec
	- $\tan \theta = \frac{\varepsilon''}{\varepsilon'} = \frac{\sigma}{\omega \varepsilon}$
	  id:: 673e3379-c5b6-4af8-a61a-20daa9718476
	  collapsed:: true
		- $\tan \theta$ ...  verlustwinkel
		- $\varepsilon''$ ... [[imaginärteil]] von ((673e3379-64cb-4d50-98c9-668f6b9fd3fd)) $\iu{ \frac{As}{Vm} }$
		- $\varepsilon'$ ... [[realteil]]  von ((673e3379-64cb-4d50-98c9-668f6b9fd3fd)) $\iu{ \frac{As}{Vm} }$
		- $\sigma$ ... elektrische leitfähigkeit $\iu{ \frac{S}{m} }$
		- $\varepsilon$ ... absolute [[permittivität]] $\iu{ \frac{As}{Vm} }$
		- $\omega$ ... [[kreisfrequenz]] $\iu{ \frac{rad}{s} }$
	- $\vect{\nabla} \cdot \vect{E} = 0$
	- $\vect{\nabla} \cdot \vect{H} = 0$
	- $\vect{\nabla} \times \vect{E} = - j \omega \mu \vect{H}$
	- $\vect{\nabla} \times \vect{H} = j \omega \delta \vect{E}$
	- $\vect{P}(t) = \vect{E}(t) \times \vect{H}(t)$
	- $\vect{\nabla}\cdot\vect{P}(t)=-\sigma\underbrace{{E}(t)\cdot{E}(t)}_{\vect{E^2}(t)}-\frac{\partial}{\partial t}\left(\frac{\varepsilon}{2} \underbrace{{E}(t)\cdot{E}(t)}_{\vect{E^2}(t)}+\frac{\mu}{2} \underbrace{\vect{H}(t)\cdot\vect{H}(t)}_{\vect{H^2}(t)}\right)$
	- $w_{\opn{e}}(t) = \frac{\varepsilon}{2} \vect{E^2}(t)$
	- $w_{\opn{m}}(t) = \frac{\mu}{2} \vect{H}^{2}(t)$
	- $\int_{\mathcal{V}} \vect{\nabla} \cdot \vect{P}(t) \d V = \oint_{\Sigma} \vect{P}(t) \cdot \d  \vect{F}$
	- $- \frac{\partial}{\partial t} \int_{\mathcal{V}} \left(w_{\opn{e}}(t) + w_{\opn{m}}(t) \right) \d V = \oint_{\Sigma} \vect{P}(t) \cdot \d  \vect{F} + \int_{\mathcal{V}}p_{\opn{v}}(t) \d V$
	- $\vect{E}( \vect{r},t) = \frac{1}{2} \left( \vect{E}( \vect{r}) \mathit{e}^{j \omega t} + \vect{E}^{*}( \vect{r}) \mathit{e}^{ - j \omega t} \right)$
	- $\vect{E}(t) \cdot \vect{E}(t) = \frac{1}{4} \left( \vect{E}( \vect{r}) \cdot \vect{E}( \vect{r})e^{2j \omega t} + 2 \vect{E}( \vect{r}) \cdot \vect{E}^{*}( \vect{r}) + \vect{E}^{*}( \vect{r}) \cdot \vect{E}^{*}( \vect{r})e^{ - 2j \omega t} \right)$
	- $\overrightarrow{E}(t) \cdot \overrightarrow{E}(t) = \frac{1}{2}| \overrightarrow{E}(t)|^{2}$
	- $\overline{{w_{\mathrm{e}}(t)}} = w_{\mathrm{e}} = \frac{\varepsilon}{4}| \vect{E}(t)|^{2}$
	- $\overline{{w_{\mathrm{m}}(t)}} = w_{\mathrm{m}} = \frac{\mu}{4}| \vect{H}(t)|^{2}$
	- $\overline{{p_{\mathrm{v}}(t)}} = p_{\mathrm{v}} = \frac{\sigma}{2}| \vect{E}(t)|^{2}$
	- $\vect{T} = \frac{1}{2} \vect{E} \times \vect{H}^{*} = \vect{T}_{\opn{w}} + j \vect{T}_{\opn{b}}$
	- ${{\oint \vect{E} \cdot \d  \vect{l}' = }} { E_{t1} \Delta l + E_{n1} \Delta x + E_{n2} \Delta x - E_{t2} \Delta l - E_{n2} \Delta x - E_{n1} \Delta x}$
	- $= { (E_{t1} - E_{t2}) \Delta l - 0E_{n1} + 0E_{n2} = - \frac{\partial}{\partial t} \int_{F} \vect{B} \cdot \d  \vect{F} = 0}$
	- $E_{t1} = E_{t2}$
	- $H_{t1} = H_{t2}$
	- $\int \vect{D} \cdot \d  \vect{F} = (D_{n1} - D_{n2}) \Delta F = \rho_{\opn{S}} \Delta F$
	- $D_{n1} - D_{n2} = \rho_{\opn{S}} \quad \to \quad \varepsilon_{1}E_{n1} - \varepsilon_{2}E_{n2} = \rho_{\opn{S}}$
	- $B_{n1} = B_{n2} \to \mu_{1} H_{n1} = \mu_{2}H_{n2}$
	- $\vect{n} \cdot \vect{D}_{1} = \rho_{\opn{S}}$
	- $\vect{n} \cdot \vect{B}_{1} = 0$
	- $\vect{n} \times \vect{E}_{1} = \vect{0}$
	- $\vect{n} \times \vect{H}_{1} = \vect{K}$
	- $\vect{n} \cdot( \vect{D}_{1} - \vect{D}_{2}) = \rho_{8}$
	- $\vect{n} \cdot( \vect{B}_{1} - \vect{B}_{2}) = 0$
	- $\vect{n} \times( \vect{E}_{1} - \vect{E}_{2}) = \vect{0}$
	- $\vect{n} \times( \vect{H}_{1} - \vect{H}_{2}) = \vect{K}$
	- $\nabla^{2} \vect{E} - \mu \varepsilon \pdiff{t} \vect{E} - \mu \sigma \frac{\partial}{\partial t} \vect{E} = 0$
	  tags:: formel, wip
	  bezeichnung:: wellengleichung (telegrafengleichung) mit verlusten
	  id:: 67646b82-91a5-483a-9d35-9669db690b89
		- $\nabla^2$ ... [[laplace operator]]
		- $\vect{E}$ ... elektrischer feldstärke vektor der momentanwerte $\iu{ \frac{V}{m} }$
		- $\mu$ ... magnetische permeabilität $\iu{ \frac{Vs}{Am} }$
		- $\varepsilon$ ... elektrische permittivität $\iu{ \frac{As}{Vm} }$
		- $\sigma$ ... elektrische leitfähigkeit $\iu{ \frac{S}{m} }$
		- $t$ ... zeit
		- $\cfrac{\partial}{\partial t}, \cfrac{\partial^2}{\partial t^2}$ ... partielle ableitung 1./2. ordnung nach der zeit
	- $\nabla^{2} \vect{E} + ( \omega^{2} \mu \varepsilon - j \omega \mu \sigma) \vect{E} = 0$
	- $\nabla^{2} \vect{E} + \omega^{2} \mu \delta \vect{E} = 0$
	- $\nabla^{2} = \pdiff{x} + \pdiff{y} + \pdiff{z}$
	  id:: 67646b82-b5eb-4e3f-abc8-275303abed5c
	- $k = \omega \sqrt{\mu \delta}$
	  tags:: formel, wip
	  bezeichnung:: wellenzahl
		- $\omega$ ... [[kreisfrequenz]] $\iu{ \frac{rad}{s} }$
		- $\delta$ ... [[komplexe]] [[dielektrizitätskonstante]] $\iu{ \frac{As}{Vm} }$
	- $\Psi(x,y,z) = X(x)Y(y)Z(z)$
	- $\frac{1}{X(x)} \pdiff{x}X(x) + \frac{1}{Y(y)} \pdiff{y}Y(y) + \frac{1}{Z(z)} \pdiff{z}Z(z) + \underbrace{k^{2}}_{\text{const.}} = 0$
	- $\frac{1}{X(x)} \pdiff{x}X(x) = - k_{x}^{2}$
	- $k_{x}^{2} + k_{y}^{2} + k_{z}^{2} = k^{2} = \omega^{2} \mu \delta$
	  tags:: formel, wip
	  bezeichnung:: separationsbedingung
	  id:: 674d7759-0e35-482f-8086-9026be01cd14
		- $\delta$ ... [[komplexe]] [[dielektrizitätskonstante]] $\iu{ \frac{As}{Vm} }$
		  id:: 67646b82-819c-4927-9c2f-03c15802ec4f
	- $\pdiff{x}X(x) + k_{x}^{2}X(x) = 0$
	- $\pdif{y}H_{z} - \pdif{z}H_{y} = j \omega \delta E_{x} \\ \pdif{z}H_{x} - \pdif{x}H_{z} = j \omega \delta E_{y} \\ \pdif{x}H_{y} - \pdif{y}H_{x} = j \omega \delta E_{z} \\ \pdif{y}E_{z} - \pdif{z}E_{y} = - j \omega \mu H_{x} \\ \pdif{z}E_{x} - \pdif{x}E_{z} = - j \omega \mu H_{y} \\ \pdif{x}E_{y} - \pdif{y}E_{x} = - j \omega \mu H_{z}$
	  tags:: formel, wip
	  bezeichnung:: komponentenweise darstellung der [[maxwellschen]] rotorgleichungen in [[kartesischer]] form. vorraussetzung: [[harmonische]] Vorgänge und Quellenfreiheit anschreiben
		- $-$ ...
	- ((6750988d-c460-4ec0-8652-1b15a9976b66))
	  id:: 674d7759-2ef6-4ef6-9620-b611b833d779
- ## [[homogene ebene wellen]]
  collapsed:: true
	- [S. 5](((677f9d41-15df-4c22-be17-7538e60becb7)))
	- $+ \cfrac{\partial}{\partial z}e_{y} = \mu \cfrac{\partial}{\partial t}h_{x}$
	- $- \cfrac{\partial}{\partial z}e_{x} = \mu \cfrac{\partial}{\partial t}h_{y}$
	- $0 = \mu \cfrac{\partial}{\partial t}h_{z}$
	- $- \cfrac{\partial}{\partial z}h_{y} = \varepsilon \cfrac{\partial}{\partial t}e_{x}$
	- $+ \cfrac{\partial}{\partial z}h_{x} = \varepsilon \cfrac{\partial}{\partial t}e_{y}$
	- $0 = \varepsilon \cfrac{\partial}{\partial t}e_{z}$
	- $\cfrac{\partial^2}{\partial z^2}e_{x} - \mu \varepsilon \cfrac{\partial^2}{\partial t^2}e_{x} = 0$
	  id:: 67646b82-c128-49c7-b8b1-18a53926ceca
	  tags:: formel
	  bezeichnung:: eindimensionale homogene Wellengleichung in karthesischen koordinaten
		- $z$ ... raumkoordinate $\iu{ m }$
		- $\cfrac{\partial^2}{\partial z^2}$ ... partielle ableitung 2. ordnung nach der $z$ koordinate
		- $e_x$ ... momentan wert des elektrischen feldes in $x$ richtung $\iu{ \frac{V}{m} }$
		- $\mu$ ... magnetische permeabilität $\iu{ \frac{Vs}{Am} }$
		- $\varepsilon$ ... elektrische permittivität $\iu{ \frac{As}{Vm} }$
		- $t$ ... zeit
		- $\cfrac{\partial^2}{\partial t^2}$ ... partielle ableitung 2. ordnung nach der zeit
	- $e_{x}\left(z,t\right) = \underbrace{c_1f_1\left(z - vt\right)}_{ = e_{x}^{ + }\left(z,t\right)} + \underbrace{c_2f_2\left(z + vt\right)}_{ = e_{x}^{ - }\left(z,t\right)}$
	  id:: 6745a3c5-baa9-4655-ac6f-92348bdacfc0
	  tags:: formel
	  bezeichnung:: allgemeiner lösungsansatz der eindimensionalen [[hew]]
	  collapsed:: true
		- $e_x(z,t)$ ... momentanwert des [[elektrischen feldes]] in $x$-richtung $\iu{ \frac{V}{m} }$
		- $e_x^{+}(z,t)$ ... momentanwert des [[elektrischen feldes]] in $x$-richtung der hinlaufenden welle $\iu{ \frac{V}{m} }$
		- $e_x^{-}(z,t)$ ... momentanwert des [[elektrischen feldes]] in $x$-richtung der rücklaufenden welle $\iu{ \frac{V}{m} }$
		- $z$ ... $z$-koordinate, hier ist es die ausbreitungsrichtung $\iu{ m }$
		- $t$ ... zeit $\iu{ s }$
		- $c_1 , c_2$ ... beliebige komplexe constante
		- $f_1(z-vt) , f_2(z-vt)$ ... beliebige 2 mal stetig differenzierbare funktion
		- skript
			- ((6745f002-178c-48da-aada-e68861acbbc2))
	- $v_p = \cfrac{1}{\sqrt{\varepsilon \mu}} = \cfrac{\omega}{k}$
	  tags:: formel
	  bezeichnung:: phasengeschwindigkeit
	  id:: 673e3379-4b5b-475a-91a4-08da8e21eb58
		- $v_p$ ... phasengeschwindigkeit $\iu{ \frac{m}{s} }$
		- $\varepsilon$ ... absolute [[permittivität]] $\iu{ \frac{As}{Vm} }$
		- $\mu$ ... absolute [[permeabilität]] $\iu{ \frac{Vs}{Am} }$
		- $\omega$ ... [[kreisfrequenz]] der welle $\iu{ \frac{rad}{s} }$
		- $k$ ... [[wellenzahl]] $\iu{ \frac{rad}{m} }$
	- ((673c4eb2-5827-434c-a323-0ff29f347504))
	  id:: 67646b82-6d7d-47d2-bb9e-0000d5f455c2
	- ((673b66c9-9d1e-40e9-9289-92ee3f902303))
	- $h_{x}^{ + } = - \cfrac{e_{y}^{ + }}{\eta}$
	- $\cfrac{e_{x}^{ + }}{h_{y}^{ + }} = - \cfrac{e_{y}^{ + }}{h_{x}^{ + }} = \eta$
	- $\vect{E} \perp \vect{H} \perp \vect{i}_{z}$
	- $\cfrac{e_{x}^{ - }}{h_{y}^{ - }} = - \cfrac{e_{y}^{ - }}{h_{x}^{ - }} = - \eta$
	- $w_{\opn{e}}\left(t\right) = \cfrac{\varepsilon}{2}\left(e_{x}^2 + e_{y}^2\right)$
	- $w_{\opn{m}}\left(t\right) = \cfrac{\mu}{2}\left(h_{x}^2 + h_{y}^2\right)$
	- $w_{\opn{m}}\left(t\right) = \cfrac{\mu}{2} \cfrac{1}{\eta^2}\left(e_{x}^2 + e_{y}^2\right) = w_{\opn{e}}\left(t\right)$
	- ${p_{x}^{+}\equiv0}$
	- ${p_{y}^{ + } \equiv 0}$
	- ${p_{z}^{+}=e_{x}^{+}h_{y}^{+}}-{e_{y}^{+}h_{x}^{+}}$
	- ${p_{z}^{+}=-\cfrac{1}{\eta}\left(e_{r}^{+^2}+e_{y}^{+^2}\right)}$
	- $\overline{\vect{P}\left(t\right)}=\overline{\vect{E}\times \vect{H}}=\cfrac{1}{\eta}\left(\overline{{e_{x}^{+}}^2+{e_{y}^{+}}^2}\right)\vect{i}_{z}=\cfrac{1}{2\eta}\left(\overline{E_{x0}^2+E_{y0}^2}\right)\vect{i}_{z}$
	  id:: 6735b379-9fad-4f67-bd6e-6a9603401496
	- $e_{x}\left(z,t\right) = \operatorname{Re} \{E_{x}\left(z\right)e^{j \omega t} \} = E_0 \cos \left(k\left(vt - z\right) \right) = E_0 \cos \left( \omega t - kz \right)$
	- ((67403e6c-c82c-4ada-a67e-ba11b41ebcc8))
	  id:: 67404a07-268a-4632-b86f-c136cdfaf0eb
	- $\lambda = \cfrac{2 \pi}{k} = \cfrac{2 \pi}{\omega \sqrt{\varepsilon \mu}}$
	- ${\vect{E}_1 = \vect{E}_{x} = \left(E_1 \vect{i}_{x} + 0 \vect{i}_{y} \right)e^{ - jkz}} \\ {\vect{E}_2 = \vect{E}_{y} = \left(0 \vect{i}_{x} + E_2 \vect{i}_{y} \right)e^{ - jkz}}$
	  id:: 673e3379-9e8e-4059-b99e-e764c678fa51
	  tags:: formel, wip
	  bezeichnung:: allgemeine form einer polarisierten welle (elliptische polarisation) Effektivwert (?)
	  collapsed:: true
		- $-$ ...
		- skript
			- ((67459414-cc15-4ce4-be2d-77b9db927f8b))
	- ${e_{ x}\left(z,t\right) = E_1 \cos\left( ω t - kz \right)} \\ {e_{y}\left(z,t\right) = E_2 \cos \left( \omega t - kz + \psi \right)}$
	  id:: 673e3379-54d5-49f8-b0db-18b82bf799c4
	  tags:: formel, wip
	  bezeichnung:: allgemeine form des momentanwertes einer polarisierten welle (elliptische polarisation)
		- skript
			- ((674594a5-fb6a-4ebb-89dd-80b6f7e96ed2))
	- ${e_{x}\left(0,t\right) = E_1 \cos{\left( \omega t\right)}}$
	- ${e_{y}\left(0,t\right) = E_2 \cos{\left( \omega t + \psi\right)}}$
	- $e_{x}\left(0,t\right) = E \cos{\left( \omega t\right)}$
	- ${e_{y}\left(0,t\right) = E \cos{\left( \omega t \mp \cfrac{\pi}{2}\right)} = \pm E \sin{\left( \omega t\right)}}$
	- ${e_{x}\left(z,0\right)} = {E \cos \left( - kz \right) = E \cos\left(kz\right)}$
	- ${e_{y}\left(z,0\right)} = {E \cos \left( - kz \pm \cfrac{\pi}{2} \right) = \pm E \sin \left(kz \right)}$
	- $\vect{E} =E_{y0}e^{ - jkz} \vect{i}_y$
	  id:: 673e3379-7ae8-425b-bf90-a176d50f983b
	  tags:: formel
	  bezeichnung:: ansatz der elektrischen komponente einer $\mathrm{TEM}$ welle
		- $\vect{E}$ ... elektrischer feldstärke vektor $\iu{ \frac{V}{m} }$
		- $E_{y0}$ ... amplitude des elektrischen feldes in $y$ richtung $\iu{ \frac{V}{m} }$
		- $k_z$ ...  wellenzahl in $z$ richtung $\iu{ \frac{rad}{m} }$
		- $\vect{i}_y$ ... einheitsvektor in $y$ richtung $\iu{ - }$
	- $\eta \vect{H} = - E_{y0}e^{ - jkz} \vect{i}_{x}$
	  id:: 6735b379-187a-4654-8126-efd8a322477b
	  tags:: formel
	  bezeichnung:: ansatz der magnetischen komponente einer $\mathrm{TEM}$ welle
		- $\eta$ ... mediumswiderstand $\iu{ \Omega }$
		- $\vect{H}$ ... magnetischer feldstärke vektor $\iu{ \frac{A}{m} }$
		- $E_{y0}$ ... amplitude des elektrischen feldes in $y$ richtung $\iu{ \frac{V}{m} }$
		- $k_z$ ...  wellenzahl in $z$ richtung $\iu{ \frac{rad}{m} }$
		- $\vect{i}_x$ ... einheitsvektor in $x$ richtung $\iu{ - }$
	- $\begin{aligned} P&=\int\vect{P}\cdot\d \vect{F}=\cfrac12\opn{Re} \left\{\int(\vect{E}\times\vect{H^{*}})\cdot\d \vect{F} \right\} \\ &= \cfrac{1}{2} \opn{Re} \left\{\int(E_{x}H_{y}^{*} - E_{y}H_{x}^{*}) \d F \right\} \\ &= \cfrac{w d}{2} \opn{Re} \{ - E_{y0}e^{ - j k z}( - \cfrac{E_{y0}}{\eta}e^{ + j k z}) \} = \cfrac{E_{y0}^{2}}{2 \eta}w d \end{aligned}$
	- $P = \cfrac{|U|^{2}}{2Z_{\opn{PV}}}$
	  id:: 6735b379-6bbc-4df6-9bbd-9f29e63108cf
	- $U = \int_{ - d}^{0}E_{y} \d y = E_{y0}~d$
	- $P = \cfrac{|E_{y0}|^{2}d^{2}}{2Z_{\opn{PV}}}$
	  id:: 6735b379-fdec-41d2-9e92-0a885348c026
	  tags:: formel
	  bezeichnung:: transportierte leistung in der parallelplattenleitung
		- $E_{y0}$ ... elektrisches Feld in $y$-Richtung (normal zur Platte/Grenzfläche) $\iu{ \frac{V}{m} }$
		- $d$ ... abstand zwischen den platten der parallelplattenleitung $\iu{ m }$
		- $Z_{PV}$ ... Leitungswellenwiderstand (?). Widerstand der über leistung und spannung berechnet wird. entspricht dem [[wellenwiderstand]] $Z_L$ bzw $\eta$ $\iu{ \Omega }$
	- $\vect{\nabla}\times\vec{E}=-j\omega\mu\vect{H}$
	- $\vect{\nabla}\times\vect{H}=\sigma\vec{E}+j\omega\varepsilon\vect{E}$
	- ((67459ac7-d3b4-47bf-9ac5-0379a5e2e1e8))
	  id:: 673e3379-64cb-4d50-98c9-668f6b9fd3fd
	- ((673e3379-65ec-4bba-988b-f6a5d8499e68))
	  id:: 6745a2d1-96eb-4141-93fd-4c8e10df8d94
	- $\eta^{2} = \cfrac{\mu}{\delta} = \cfrac{\mu}{\varepsilon} \cfrac{1}{1 - j s}$
	- $\eta = \mathbb{R} + j \mathbb{X} = \eta_{\opn{E}} \cfrac{1}{\sqrt{1 - j s}}$
	- ((674496c6-ef08-4cfe-8444-ef86aadf0f47))
	  id:: 6740c68b-e124-4f93-b1f1-9c8be879951c
	- ((673e3379-c0da-481e-b625-bd67e865a008))
	- $\mathbb{R} = \eta_{\opn{E}} \sqrt{\cfrac{\sqrt{1 + s^{2}} + 1}{2(1 + s^{2})}} \qquad \mathbb{X} = \eta_{\opn{E}} \sqrt{\cfrac{\sqrt{1 + s^{2}} - 1}{2(1 + s^{2})}}$
	-
	- $\alpha = k_{\opn{E}} \sqrt{\cfrac{\sqrt{1 + s^{2}} - 1}{2}} \qquad \beta = k_{\opn{E}} \sqrt{\cfrac{\sqrt{1 + s^{2}} + 1}{2}}$
	- $\eta\approx\eta_{\mathrm{E}}\left(1+j\frac{s}{2}\right)\qquad j k_{z}\approx k_{\mathrm{E}}\left(\frac{s}{2}+j\right)$
	- $\eta \approx \eta_{\opn{E}} \cfrac{1 + j}{\sqrt{2s}} \qquad j k_{z} \approx k_{\opn{E}} \sqrt{\cfrac{s}{2}}\left(1 + j\right)$
	- $d = \cfrac{1}{\alpha} \approx \cfrac{1}{k_{\mathrm{E}}} \sqrt{\cfrac{2}{s}} = \sqrt{\cfrac{2}{\omega \mu \sigma}}$
	  id:: 674d7759-c315-4a22-a755-be7a35c4b441
	  tags:: formel
	  bezeichnung:: eindringtiefe
	  collapsed:: true
		- $\alpha$ ... [[realteil]] der [[komplexen]] [[wellenzahl]] $\iu{ \frac{rad}{m} }$
		- $k_\mathrm{E}$ ...
		- $s$ ... bandbreite $\iu{ - }$
		- $\omega$ ... [[kreisfrequenz]] $\iu{ \frac{rad}{s} }$
		- $\mu$ ...
		- $\sigma$ ... elektrische leitfähigkeit $\iu{ \frac{S}{m} }$
- ## Reﬂexion an glatten Grenzflächen, die [[parallelplattenleitung]]
  collapsed:: true
	- [S. 8](((677f9d68-fcb5-4a5b-a2fd-8a396f1f8d0a)))
	- $\frac{\sin \Theta_{1}}{\sin \Theta_{2}} =  \sqrt{\frac{\varepsilon_{2}}{\varepsilon_{1}}} =  \frac{n_{2}}{n_{1}}$
	  tags:: formel
	  bezeichnung:: brechungsgesetz/gesetz von snellius
	  id:: 6734720f-e42f-46c0-a512-3075ea423042
	  collapsed:: true
		- $\Theta_1$ ... winkel in medium 1 (eintritt) $\mathrm{[°]}$
		- $\Theta_2$ ... winkel in medium 2 (transmission) $\mathrm{[°]}$
		- $\varepsilon_1$ ... absolute [[permittivität]] $\iu{\frac{As}{Vm}}$
		- $n_1$ ... [[brechungsindex]] $\mathrm{[-]}$
		- $n_2$ ... [[brechungsindex]] $\mathrm{[-]}$
	- $\Gamma_{\mathrm{TM}} =  \displaystyle \frac{\sqrt{\varepsilon_{2}} \cos \Theta_{1} -  \sqrt{\varepsilon_{1}} \cos \Theta_{2}}{\sqrt{\varepsilon_{2}} \cos \Theta_{1} +  \sqrt{\varepsilon_{1}} \cos \Theta_{2}} =  \displaystyle \frac{n^{2} \cos \Theta_{1} -  \sqrt{n^{2} -  \sin^{2} \Theta_{1}}}{n^{2} \cos \Theta_{1} +  \sqrt{n^{2} -  \sin^{2} \Theta_{1}}}$
	  id:: 6735b379-5292-4604-baef-85a4c9a6fc3f
	  tags:: formel, wip
	  bezeichnung:: reflektionsfaktor der transversal polarisierten magnetischen welle (fresnel formel TM fall)
	  collapsed:: true
		- $\Gamma_{\mathrm{TM}}$ ... reflexionsfaktor der TM Welle $\iu{ - }$
		- $\varepsilon_i$ ... relative [[permittivität]] $\iu{ - }$
		- $\Theta_1$ ... eintrittswinkel $\iu{ ° }$
		- $\Theta_2$ ... transmissionswinkel $\iu{ ° }$
		- $n$ ... relativer [[brechnungsindex]] [link](((67360de7-70f6-457a-b7e1-e13b553b5d80))) $\iu{ - }$
	- ${T_{\mathrm{TM}}} = {\displaystyle \frac{2 \sqrt{\varepsilon_{1}} \cos \Theta_{1}}{\sqrt{\varepsilon_{2}} \cos \Theta_{1} +  \sqrt{\varepsilon_{1}} \cos \Theta_{2}} =  \displaystyle \frac{2n \cos \Theta_{1}}{n^{2} \cos \Theta_{1} +  \sqrt{n^{2} -  \sin^{2} \Theta_{1}}}}$
	  id:: 6735b379-80fa-4b2a-be2d-af5089fe1fa8
	  tags:: formel, wip
	  bezeichnung:: transmissionsfaktor der transversal polarisierten magnetischen welle (fresnel formel TM fall)
	  collapsed:: true
		- $T_{\mathrm{TE}}$ ... transmissionsfaktor der TE Welle $\iu{ - }$
		- $\varepsilon_i$ ... relative [[permittivität]] $\iu{ - }$
		- $\Theta_1$ ... eintrittswinkel $\iu{ ° }$
		- $\Theta_2$ ... transmissionswinkel $\iu{ ° }$
		- $n$ ... relativer [[brechnungsindex]] [link](((67360de7-70f6-457a-b7e1-e13b553b5d80))) $\iu{ - }$
	- $\Gamma_{\mathrm{TE}} = \frac{\sqrt{\varepsilon_{1}} \cos \Theta_{1} - \sqrt{\varepsilon_{2}} \cos \Theta_{2}}{\sqrt{\varepsilon_{1}} \cos \Theta_{1} + \sqrt{\varepsilon_{2}} \cos \Theta_{2}} = \frac{\cos \Theta_{1} - \sqrt{n^{2} - \sin^{2} \Theta_{1}}}{\cos \Theta_{1} + \sqrt{n^{2} - \sin^{2} \Theta_{1}}}$
	  id:: 6735b379-8ba8-4a90-b5e2-8b5b38036526
	  tags:: formel, wip
	  bezeichnung:: reflektionsfaktor der transversal polarisierten elektrischen welle (fresnel formel TE fall)
	  collapsed:: true
		- $\Gamma_{\mathrm{TE}}$ ... reflexionsfaktor der TE Welle $\iu{ - }$
		- $\varepsilon_i$ ... relative [[permittivität]] $\iu{ - }$
		- $\Theta_1$ ... eintrittswinkel $\iu{ ° }$
		- $\Theta_2$ ... transmissionswinkel $\iu{ ° }$
		- $n$ ... relativer [[brechnungsindex]] [link](((67360de7-70f6-457a-b7e1-e13b553b5d80))) $\iu{ - }$
	- $T_{\mathrm{TE}} = \frac{2 \sqrt{\varepsilon_{1}} \cos \Theta_{1}}{\sqrt{\varepsilon_{1}} \cos \Theta_{1} + \sqrt{\varepsilon_{2}} \cos \Theta_{2}} = \frac{2 \cos \Theta_{1}}{\cos \Theta_{1} + \sqrt{n^{2} - \sin^{2} \Theta_{1}}}$
	  id:: 6735b379-1a1f-417e-8323-7fe94bd9e2cf
	  tags:: formel
	  bezeichnung:: transmissionsfaktor der transversal polarisierten magnetischen welle (fresnel formel TE fall)
	  collapsed:: true
		- $T_{\mathrm{TE}}$ ... transmissionsfaktor der TE Welle $\iu{ - }$
		- $\varepsilon_i$ ... relative [[permittivität]] $\iu{ - }$
		- $\Theta_1$ ... eintrittswinkel $\iu{ ° }$
		- $\Theta_2$ ... transmissionswinkel $\iu{ ° }$
		- $n$ ... relativer [[brechnungsindex]] [link](((67360de7-70f6-457a-b7e1-e13b553b5d80))) $\iu{ - }$
	- $\Gamma_{\mathrm{TM}} = 0 \quad \Leftarrow \quad \tan \Theta_{\mathrm{B}} =$ ((67360de7-70f6-457a-b7e1-e13b553b5d80))
	  id:: 6735b379-a4a2-48f4-800f-7b9292b7a3a1
	- $\frac{2 \pi}{\lambda_1}z_{0m} \cos \Theta_{m}=m \pi \quad \Rightarrow \quad d=-z_{0m}= \frac{\lambda_1m}{2 \cos \Theta_{m}}= \frac{m}{2f \sqrt{\mu_1 \varepsilon_1} \cos \Theta_{m}}$
	- $\lambda_{x}= \frac{\lambda_{1}}{\sin \Theta_{m}}$
	- $\lambda_{\mathrm{H},m}= \frac{\lambda_{0}}{\sin \Theta_{m}}$
	- $d=m \frac{\lambda_{0}}{2}$
	- $f_{\mathrm{G},m}= \frac{m \mathit{c}}{2d}$
	  id:: 67646b82-d905-4edd-915a-d4c002f45a0b
	  tags:: formel
	  bezeichnung:: [[grenzfrequenz]] einer bestimmten mode
		- $f_{\mathrm{G},m}$ ... [[grenzfrequenz]] $\iu{ Hz }$
		- $m$ ... entspricht der mode $\iu{ - }$
		- $c$ ... lichtgeschwindigkeit im medium $\iu{ \frac{m}{s} }$
		- $d$ ... abstand zwischen den platten/hohlleitergröße $\iu{ m }$
		- skript
		  collapsed:: true
			- ((67814da4-970e-4339-a254-52ccde167cb4))
	- $\lambda_{\mathrm{G},m}= \frac{c}{f_{\mathrm{G},m}}= \frac{2d}{m}$
	- $\lambda_{\mathrm{H},m}= \frac{\lambda_{0}}{\sqrt{1-( \frac{m \lambda_{0}}{2d})^{2}}}$
	- $\lambda_{\mathrm{H},m}= \frac{\lambda_{0}}{\sqrt{1-( \frac{\lambda_{0}}{\lambda_{\mathrm{G},m}})^{2}}}$
	- $\sin \Theta_{m}= \frac{\lambda_{0}}{\lambda_{\mathrm{H},m}}= \sqrt{1-( \frac{m \lambda_{0}}{2d})^{2}}$
- ## Die [[oberflächenwelle]]
  collapsed:: true
	- [S. 9](((677f9d88-87bb-4a8d-9a0f-3e5744c782e1)))
	- ${s_{1}= \cfrac{\sigma_{1}}{\omega \varepsilon_{1}} \gg1}$
	- ${s_{2}= \cfrac{\sigma_{2}}{\omega \varepsilon_{2}} \ll1}$
	- $k_{\mathrm{E2}}= \omega \sqrt{\varepsilon_{2} \mu_{0}}$
	- $k_{z} \approx k_{\mathrm{E2}} \Big(1-j \cfrac{1}{2s_{1}} \cfrac{\varepsilon_{2}}{\varepsilon_{1}} \Big)$
	- $\alpha \approx k_{\mathrm{E2}} \frac{1}{2s_{1}} \frac{\varepsilon_{2}}{\varepsilon_{1}}=k_{\mathrm{E2}} \Big( \frac{\mathbb{R}_{1}}{\mathbb{R}_{2}} \Big)^{2}= \frac{\beta}{2} \frac{1}{s_{1}} \frac{\varepsilon_{2}}{\varepsilon_{1}}$
	- $\beta \approx k_{\mathrm{E2}}= \omega \sqrt{\varepsilon_{2} \mu_{0}}$
	- $k_{x1} \approx \sqrt{\frac{\omega \mu_{0} \sigma_{1}}{2}}(-1+j)$
	- $k_{x2} \approx \omega \varepsilon_{2} \sqrt{\frac{\omega \mu_{0}}{2 \sigma_{1}}}(1-j)= \omega \varepsilon_{2} \eta_{1}$
	- $\cfrac{k_{x2}}{k_{x1}} \approx- \cfrac{\omega \varepsilon_{2}}{\sigma_{1}}$
	- $E_{x1}=k_{\mathrm{E2}}d_{1} \cfrac{1- \cfrac{j \varepsilon_{2}}{2s_{1} \varepsilon_{1}}}{-1+j}A_{1}e^{ j k_{x1}x}e^{-j k_{z}z}$
	- $E_{x1}=-E_{z1} \sqrt{\cfrac{\omega \varepsilon_{2}}{2 \sigma_{1}}}(1+j)$
	- $E_{x2}=- \cfrac{1}{1-j}E_{z2} \Big( \sqrt{\cfrac{2 \sigma_{1}}{\omega \varepsilon_{2}}}-j \sqrt{\cfrac{\omega \varepsilon_{2}}{2 \sigma_{1}}} \Big)$
	- $Z_{\mathrm{W}} = \cfrac{E_{x}}{H_{y}} = -\cfrac{E_{y}}{H_{x}}$
	  id:: 67646b82-eb39-40e9-8c9c-8e081117f756
	  tags:: formel, wip
	  bezeichnung:: Feldwellenwiderstand ($Z_{\mathrm{W,TE}}$)
		- $E_x$ ...
		- $H_y$ ...
	- $Z_{\mathrm{W2}}= \cfrac{k_{z}}{\omega \delta_{2}}= \cfrac{k_{\mathrm{E2}} \left(1-j \cfrac{1}{2s_{1}} \cfrac{\varepsilon_{2}}{\varepsilon_{1}} \right)}{\omega \varepsilon_{2}(1-j s_{2})} \approx \eta_{\mathrm{E2}} \left(1+j \cfrac{s_{2}}{2} \right)$
	- $Z_{\mathrm{W1}}= \cfrac{k_{z}}{\omega \delta_{1}}$
	- $\begin{aligned} I_{z}&= \int \limits_{\Sigma} \vect{S}_{1} \cdot \d  \vect{F}= \sigma_{1} \int \limits_{x=0}^{\infty} \int \limits_{y=0}^{b}E_{z1} \d x \d y  \\ & =  \sigma_{1} A_{1} b e^{-j k_{z}z} \int \limits_{x=0}^{\infty}e^{j k_{x1}x} \mathrm{d}x  \\ &=j \cfrac{\sigma_{1}A_{1}b}{k_{x1}}e^{-j k_{z}z} \end{aligned}$
	- $T_{x0}= \cfrac{1}{2} \Big(-E_{z0}H_{y0}^{*} \Big)=- \cfrac{1}{2} \cfrac{\omega \delta_{1}^{*}}{k_{x1}^{*}}|A_{1}|^{2}$
	- $\d P=T_{x0}~b \d z$
	- $T_{x0}~b \d z= \cfrac{1}{2}|I_{z}|^{2} \d Z \quad \Rightarrow \quad \d Z=- \cfrac{\omega \delta_{1}^{*}k_{x1}^{2}}{\sigma_{1}^{2}} \cfrac{\d z}{b}$
	- $\mathrm{d}Z \approx \eta_{1} \cfrac{\mathrm{d}z}{b}$
	- $\mathrm{d}Z= \mathrm{d} \mathbb{R}+j \mathrm{d} \mathbb{X}, \quad \mathrm{d} \mathbb{R}= \cfrac{\mathrm{d}z}{b} \mathbb{R}_{1}, \quad \mathrm{d} \mathbb{X}= \cfrac{\mathrm{d}z}{b} \mathbb{X}_{1}$
	- $\mathrm{d}P_{\mathrm{W}}=T_{\mathrm{W}}b \d z= \cfrac{1}{2}|I_{z}|^{2} \d  \mathbb{R}$
	- $I_{z}=-b H_{y1}(0)$
	- $\mathrm{d}P_{\mathrm{w}}= \cfrac{1}{2}|H_{y1}(0)|^{2}b \mathbb{R}_{1} \d z \quad \text{bzw.} \quad \cfrac{\mathrm{d}P_{\mathrm{W}}}{\mathrm{d}z}= \cfrac{1}{2}|H_{y1}(0)|^{2}b \mathbb{R}_{1}$
	- $p= \cfrac{1}{b} \cfrac{\mathrm{d}P_{\mathrm{W}}}{\mathrm{d}z}= \cfrac{1}{2}|H_{\mathrm{tang}}(0)|^{2} \mathbb{R}_1$
	- $\mathbb{R}_{1}= \cfrac{1}{\sigma_{1}d_{1}}= \mathbb{R}_{\square} \quad \text{(lies: R square)}$
	- $R= \cfrac{l}{\sigma A}$
	- $R= \int \mathrm{d}R= \int \limits_{0}^{l} \cfrac{\mathbb{R}_{\square}}{b} \d z= \cfrac{1}{\sigma_{1}d_{1}} \cfrac{l}{b} \propto \sqrt{\omega}$
	  id:: 674d7759-2399-4628-94f1-400ee5be7c0e
	  tags:: formel
	  bezeichnung:: gesamtwiderstand eines leiterstreifens aufgrund des skin effekts
	  collapsed:: true
		- $R$ ... gesamter ohmscher widerstand $\iu{\Omega}$
		- $l$ ... länge des streifens $\iu{m}$
		- $\mathbb{R}_{\square}$ ... oberflächenwiderstand $\iu{\Omega}$
		- $b$ ... breite des streifens $\iu{m}$
		- $z$ ... ausbreitungsrichtung
		- $\sigma_1$ ... elektrische leitfähigkeit $\iu{\frac{S}{m}}$
		- $d_1$ ... eindringtiefe $\iu{m}$
		- $\omega$ ... [[kreisfrequenz]] $\iu{\frac{rad}{s}}$
	- $R= \cfrac{l}{2 \pi a} \sqrt{\cfrac{\omega \mu}{2 \sigma_{1}}}, \quad X= \cfrac{l}{2 \pi a} \sqrt{\cfrac{\omega \mu}{2 \sigma_{1}}}$
	- $\cfrac{R}{R_{0}}= \cfrac{X}{X_{0}}= \cfrac{a}{2} \sqrt{\cfrac{\omega \mu \sigma_{1}}{2}}= \cfrac{a}{2d_{1}} \propto \sqrt{\omega} \gg1$
- ## Resonatoren
  collapsed:: true
	- [S. 11](((677f9d9c-d39d-4951-8678-363a04793cb4)))
	- $\lambda_{\mathrm{G},m,n} = \frac{1}{\sqrt{\left(\frac{m}{2a} \right)^{2} + \left(\frac{n}{2b} \right)^{2}}}$
	  tags:: formel
	  bezeichnung:: [grenzwellenlänge]([[wellenlänge]]) des $\mathrm{TE}_{mn}$ oder $\mathrm{TM}_{mn}$ modus
		- $\lambda_{\mathrm{G},m,n}$ ... [grenzwellenlänge]([[wellenlänge]]) $\iu{ m }$
		- $m$ ... modenindex $\iu{ - }$
		- $n$ ... modenindex $\iu{ - }$
		- $a$ ... breite des [[hohlraumleiters]] $\iu{ m }$
		- $b$ ... höhe des [[hohlraumleiters]] $\iu{ m }$
	- $\lambda_{\mathrm{H}} = \frac{\lambda}{\sqrt{1 - \left(\frac{\lambda}{\lambda_{\mathrm{G}}} \right)^{2}}}$
	- $v_{\mathrm{P}} = \frac{c}{\sqrt{1 - \left(\frac{\lambda}{\lambda_{\mathrm{G}}} \right)^{2}}}$
	- $v_{\mathrm{G}} = c \sqrt{1 - \left(\frac{\lambda}{\lambda_{\mathrm{G}}} \right)^{2}}$
	- $\kappa^{2} = \left(\frac{m \pi}{a} \right)^{2} + \left(\frac{n \pi}{b} \right)^{2} \equiv \omega^{2} \varepsilon \mu - k_{z}^{2}$
	  id:: 67646b82-a752-4db8-b782-284ff6dc6db8
	- $\begin{aligned} P & = \int \opn{Re}\{\vect{T}\} \cdot \d  \vect{F} = \int T_{z} \d x \d y = - \frac{1}{2} \int \limits_{0}^{a} \int \limits_{0}^{b} E_{y}H_{x}^{*} \d x \d y \\ & = \frac{\omega \vect{k}_{z} \mu}{2} \left(\frac{a A}{\pi} \right)^{2}b \int \limits_{0}^{a} \sin^{2}(\frac{\pi}{a}x) \d x = \frac{\omega k_{z} \mu}{4}a b \left(\frac{a A}{\pi} \right)^{2} \end{aligned}$
	- $- \d P = \frac{1}{2}|H_{\mathrm{tang}}|^{2} \mathbb{R}_{\mathrm{M}} \d F$
	- $\begin{aligned} - \pdif{z}P(z) & = \frac12 \mathbb{R}_{\mathrm{M}} \left(2 \int_0^{a} \Big[|H_{x}|^2 + |H_{z}|^2 \Big]_{y = 0} \d x + 2 \int \limits_{0}^{b} \Big[|\underbrace{H_{y}}_0|^2 + |H_{z}|^2 \Big]_{x = 0} \d y \right) \\ &={\mathbb{R}_{\mathrm{M}}A^{2} \left(\left(\cfrac{k_{z}a}{\pi} \right)^{2} \int \limits_{0}^{a} \sin^{2} \left(\cfrac{\pi}{a}x \right) \mathrm{d}x + \int \limits_{0}^{b} \cfrac{a}{\pi} \cos^{2} \left(\cfrac{\pi}{a}x \right) \mathrm{d}x + \int \limits_{0}^{b} \mathrm{d}y \right)} \\ & = A^{2} \mathbb{R}_{\mathrm{M}} \left(\frac{a}{2} \left(1 + \left(\frac{2a}{\lambda_{\mathrm{H}}} \right)^{2} \right) + b \right) \end{aligned}$
	- $\alpha = \frac{\pi}{\omega \mu} \mathbb{R}_{\mathrm{M}} \frac{\lambda_{\mathrm{H}}}{a^{3} b} \left(\frac{a}{2} \left(1 + \left(\frac{2a}{\lambda_{\mathrm{H}}}\right)^{2} \right) + b \right)$
	- $c = p \frac{\lambda_{\mathrm{H}}}{2}, \quad \text{bzw.} \quad k_{z} = \frac{2 \pi}{\lambda_{\mathrm{H}}} = \frac{p \pi}{c}$
	  id:: 6745a3c5-8db7-45c1-93bd-26e16b795df2
	- $\left(\frac{m \pi}{a} \right)^{2} + \left(\frac{n \pi}{b} \right)^{2} + \left(\frac{p \pi}{c} \right)^{2} = \omega_{m n p}^{2} \varepsilon \mu$
	  tags:: formel, wip
	  bezeichnung:: separationsbedingung
	  id:: 67646b82-9985-4e5d-ad63-f1a604ea0334
		- $m,n,p$ ... modenindizes $\iu{ - }$
		- $a,b,c$ ... abmessungen des resonators $\iu{ m }$
		-
	- $\omega_{m n p} = \pi v \sqrt{\left(\frac{m}{a} \right)^{2} + \left(\frac{n}{b} \right)^{2} + \left(\frac{p}{c} \right)^{2}}$
	  id:: 6745a3c5-c443-4fb4-bbea-b455958f827a
	  tags:: formel
	  bezeichnung:: resonanz [[kreisfrequenz]] für $\mathrm{TE}_{mnp}$ und $\mathrm{TM}_{mnp}$ schwingungen in einem [[hohlraumleiter]]
		- $\omega_{mnp}$ ... resonanz [[kreisfrequenz]] $\iu{ Hz }$
		- $v$ ... phasengeschwindigkeit $\iu{ \frac{m}{s} }$
		- $m$ ... modenindex $\iu{ - }$
		- $n$ ... modenindex $\iu{ - }$
		- $p$ ... modenindex $\iu{ - }$
		- $a$ ... breite des [[hohlraumleiters]] $\iu{ m }$
		- $b$ ... höhe des [[hohlraumleiters]] $\iu{ m }$
		- $c$ ... länge des [[hohlraumleiters]] . muss diese bedingung erfüllen [link](((6745a3c5-8db7-45c1-93bd-26e16b795df2))) $\iu{ m }$
		- skript
			- ((674b6434-58f7-44a3-b43b-601434f2dbaf))
	- $Q_{0,m n p} = \frac{\omega_{m n p}W}{P}$
	  tags:: formel
	  bezeichnung:: unbelastete [[güte]] (innere [[güte]])
		- $-$ ...
	- $Q_{0} = \frac{2 \pi W}{P T} \quad \text{mit} \quad T = \frac{1}{f_{m n p}}$
	- $W = \frac{1}{4} \int_{\mathcal{V}} \left(\varepsilon \vect{E} \cdot \vect{E}^{*} + \mu \vect{H} \cdot \vect{H}^{*} \right) \d V$
	- $P = \frac{1}{2} \mathbb{R}_{\mathrm{M}} \oint_{\Sigma} \vect{H}_{\mathrm{tang}} \cdot \vect{H}_{\mathrm{tang}}^{*} \d F$
	- $\lambda_{101} = \frac{2a c}{\sqrt{a^{2} + c^{2}}}$
	- $\omega_{101} = \frac{\pi}{\sqrt{\varepsilon \mu}} \frac{\sqrt{a^{2} + c^{2}}}{a c}$
	- $E_{y} = - 2 \omega \mu \frac{a}{\pi}A \sin \left(\frac{\pi}{a}x \right) \sin \left(\frac{\pi}{c}z \right)$
	- $H_{x} = 2j k_{z} \frac{a}{\pi}A \sin \left(\frac{\pi}{a} x \right) \cos \left(\frac{\pi}{c} z \right)$
	- $H_{z} = - 2j \operatorname{\mathit{A}} \cos{\left(\frac{\pi}{a} x \right)} \sin{\left(\frac{\pi}{c} z \right)}$
	- $W_{e}=W_{m}=A^{2}\mu\frac{a^{2}+c^{2}}{4c^{2}}a b c$
	- $P = A^{2} \mathbb{R}_{\mathrm{M}} \frac{a c \left(a^{2} + c^{2} \right) + 2 b \left(a^{3} + c^{3}\right)}{c^{2}}$
	- $Q_{0} = \frac{\pi \eta}{2 \mathbb{R}_{\mathrm{M}}} \frac{b \sqrt{(a^{2} + c^{2})^{3}}}{a c(a^{2} + c^{2}) + 2b(a^{3} + c^{3})}$
	  id:: 6745a3c5-66f7-450b-94fe-f6068dde589d
	  tags:: formel
	  bezeichnung:: unbelastete [[güte]] der $\mathrm{TE}_{101}$
		- $\eta$ ... [[wellenwiderstand]] $\iu{ \Omega }$
		- $\mathbb{R}_\mathrm{M}$ ... oberflächenwiderstand $\iu{ \Omega }$
		- $a$ ... breite des [[hohlraumleiters]] $\iu{ m }$
		- $b$ ... höhe des [[hohlraumleiters]] $\iu{ m }$
		- $c$ ... länge des [[hohlraumleiters]] $\iu{ m }$
	- $Q_{0} = \frac{\pi \eta \sqrt{2}}{6 \mathbb{R}_{\mathrm{M}}}$
	  tags:: formel
	  bezeichnung:: unbelastete [[güte]] der $\mathrm{TE}_{101}$ wenn $a=b=c$
		- $\eta$ ... [[wellenwiderstand]] $\iu{ \Omega }$
		- $\mathbb{R}_\mathrm{M}$ ... oberflächenwiderstand $\iu{ \Omega }$
- ## [[koaxialleitungen]]
  collapsed:: true
	- [S. 13](((677f9db4-66d0-4a27-9319-1ee51e246d94)))
	- ${\vect{E}} = {E_{r} \vect{e_{r}}}$
	- ${\vect{H}} = {H_{\varphi} \vect{e_{\varphi}}}$
	- $\pdif{z}U(z) + Z'I(z) = 0 ,\qquad \pdif{z}I(z) + Y'U(z) = 0$
	- ${\mathrm{mit}} { \quad Z' = R' + j \omega L' ,\quad} {Y' = G' + j \omega C'}$
	- $\pdif{z}U(z) - Y'Z'U(z) = 0 ,\qquad \pdif{z}I(z) - Y'Z'I(z) = 0$
	- $U_{v} = Z_{\mathrm{L}}I_{v} ,\qquad U_{r} = - Z_{\mathrm{L}}I_{r}$
	- $Z_{\mathrm{L}} = \sqrt{\frac{Z'}{Y'}} \quad \text{bzw.} \quad Z_{\mathrm{L}} = \sqrt{\frac{R' + j \omega L'}{G' + j \omega C'}}$
	  id:: 674d7759-d37d-42be-8941-e48d01b3fc05
	- $Z_{\mathrm{L,verlustlos}} = \sqrt{\frac{L'}{C'}} \quad \text{wenn} \quad R' = G' = 0 \quad \text{in}$ ((674d7759-d37d-42be-8941-e48d01b3fc05))
	  tags:: formel, wip
	  bezeichnung:: -
	  id:: 674de501-a2a9-4e7a-8a81-892354262c7e
		- $-$ ...
	- $j k_{z} = \sqrt{Y'Z'} = \sqrt{(G' + j \omega C')(R' + j \omega L')}$
	- $\frac{R'}{L'} = \frac{G'}{C'}$
	- $v_{\mathrm{P}} = \frac{\omega}{k} = \frac{\omega}{\opn{Re}\{k_{z}\}} \approx \frac{1}{\sqrt{L'C'}}$
	- $L = \frac{1}{I} \int_{A} \vect{B} \cdot \vect{n_{A}} \d  \mathcal{A}$
	- $L' = \frac{1}{I} \int_{r_{i}}^{r_{a}} \vect{B} \cdot \vect{n_{A}} \d r = \frac{1}{I} \int_{r_{i}}^{r_{a}}B_{\varphi} \d r = \frac{\mu}{I} \int_{r_{i}}^{r_{a}}H_{\varphi} \d r$
	- $H_{\varphi} = \frac{I}{2 \pi r}$
	- $L' = \frac{\mu}{I} \int_{r_{i}}^{r_{a}} \frac{I}{2 \pi r} \d r$
	- $L' = \frac{\mu}{2 \pi} \ln \frac{r_{a}}{r_{i}}$
	- $C = \frac{Q}{\int_{\mathcal{C}} \vect{E} \cdot \vect{e_{r}} \d r}$
	- $\vect{E} = \frac{\tau}{2 \pi \varepsilon} \frac{\vect{e_{r}}}{r}$
	- $C' = \frac{\tau}{\int_{\mathcal{C}} \vect{E} \cdot \vect{e}_{r} \d r} = \frac{\tau}{\int_{r_{i}}^{r_{a}} \frac{\tau}{2 \pi \varepsilon} \frac{\vect{e}_{r}'}{r} \cdot \vect{e}_{r}' \d r} = \frac{2 \pi \varepsilon}{\int_{r_{i}}^{r_{a}} \frac{1}{r} \d r}$
	- $C' = \frac{2 \pi \varepsilon}{\ln \frac{r_{a}}{r_{i}}}$
	- $Z_{\mathrm{L,verlustlos}} = \frac{\eta}{2 \pi} \ln \frac{r_{a}}{r_{i}} \quad \text{mit} \quad \eta = \sqrt{\frac{\mu}{\varepsilon}}$
	  id:: 6745a3c5-c563-4874-8d5b-50fee6812aea
	- $\mathbb{R}_\square = \sqrt{\frac{\omega \mu_{\mathrm{L}}}{2 \sigma}}$
	- $R' = \frac{R_{\mathrm{innen}} + R_{\mathrm{aussen}}}{l} \approx \frac{\frac{\mathbb{R}_{\triangle}l}{2 \pi r_{i}} + \frac{\mathbb{R}_{\triangle}l}{2 \pi r_{a}}}{l} = \frac{\mathbb{R}_{\triangle}}{2 \pi}(\frac{1}{r_{i}} + \frac{1}{r_{a}})$
	- $R'=\sqrt{\frac{\omega\mu_{\mathrm{L}}}{2\sigma}}\frac{1}{2\pi}\left(\frac{1}{r_{i}}+\frac{1}{r_{a}}\right)$
	  id:: 674d7759-1d40-46b8-9d39-cbf868cd298e
	  tags:: formel, wip
	  bezeichnung:: widerstandsbelag
		- $\mu_L$ ... [[magnetische permeabilität]] des leiters $\iu{\frac{Vs}{Am}}$
	- $G' = \omega C' \tan \delta_{\varepsilon} = \omega \frac{2 \pi \varepsilon}{\ln \frac{r_{a}}{r_{i}}} \tan \delta_{\varepsilon}$
	  id:: 674d7759-056e-4bac-998e-f2bccdc83035
	  tags:: formel
	  bezeichnung:: leitwert belag einer [[koaxialleitung]]
		- $\omega$ ... [[kreisfrequenz]] $\iu{\frac{rad}{s}}$
		- $C'$ ... kapazitätsbelag $\iu{\frac{F}{m}}$
		- $\delta_\varepsilon$ ... eﬀektive Verlustwinkel des Dielektrikums unter Berücksichtigung eventueller 
		  Lufträume. oft auch als $\theta_\varepsilon$ bekannt. $\iu{\degree}$
		- $\varepsilon$ ... absolute [[permittivität]] des dielektrikums $\iu{\frac{As}{Vm}}$
		- $r_a$ ... radius des außenleiters $\iu{m}$
		- $r_i$ ... radius des innenleiters $\iu{m}$
		- skript
			- ((67500928-2cd7-4736-974a-ac900c32e971))
	- $j k_{z} = \gamma = \alpha + j \beta = \sqrt{(G' + j \omega C')(R' + j \omega L')}$
	- $\alpha = \alpha_{R} + \alpha_{G} = \Bigg( \underbrace{ \frac{R'}{2\sqrt{\frac{L'}{C'}}}}_{(1) \mathrlap{~~ \approx \alpha_R}} + \underbrace{\frac{G' \sqrt{\frac{L'}{C'}}}{2}}_{(2) \mathrlap{~~ \approx \alpha_G}} \Bigg) \underbrace{\frac{1}{\cosh \frac{\theta_R - \theta_G}{2}}}_{(3) \mathrlap{ ~~\approx 1}} \\ \text{mit} \quad \sinh \theta_{R} = \frac{R'}{\omega L'} ~, \quad \sinh \theta_{G} = \frac{G'}{\omega C'}$
	  id:: 674d7759-bd4b-46b8-ad6c-6eba0f844dff
	  tags:: formel, wip
	  bezeichnung:: dämpfung
		- $\alpha$ ... gesamte dämpfung
		- $\alpha_R$ ... ohmsche verluste
		- $\alpha_C$ ... dielektrische verluste
		- $R'$ ... widerstandsbelag $\iu{\frac{\Omega}{m}}$
		- $L'$ ... induktivitätsbelag $\iu{\frac{H}{m}}$
		- $C'$ ... kapazitätsbelag $\iu{\frac{F}{m}}$
		- $G'$ ... leitwertsbelag $\iu{\frac{S}{m}}$
		- $\theta_R$ ... induktiver verlustfaktor
		- $\theta_G$ ... kapazitiver verlustfaktor
	- $\alpha_{R} \approx \frac{R'}{2 \sqrt{\frac{L'}{C'}}} = \frac{\mathbb{R}_{\perp}}{2 \eta r_{a}} \frac{1 + \frac{r_{a}}{r_{i}}}{\ln \frac{r_{a}}{r_{i}}}$
	  tags:: formel, wip
	  bezeichnung:: ohmsche verluste einer [[koaxialleitung]] [link](((674d7759-bd4b-46b8-ad6c-6eba0f844dff)))
	  id:: 674d7759-4a7e-4220-b396-27bd49ccaa45
		- $-$ ...
	- $Z_{\mathrm{L,min. Dampfung}} = \frac{\eta_{0}}{2 \pi \sqrt{\varepsilon_{r}}} \ln \frac{r_{a}}{r_{i}} = \frac{77 \Omega}{\sqrt{\varepsilon_{r}}}$
	- $U_{\mathrm{max}} = E_{\mathrm{max}} r_{i} \ln \frac{r_{a}}{r_{i}} = E_{\mathrm{max}} r_{a} \frac{\ln \frac{r_{a}}{r_{i}}}{\frac{r_{a}}{r_{i}}}$
	- $Z_{\mathrm{L,max.Spannungsfest}} = \frac{60 \Omega}{\sqrt{\varepsilon_{r}}}$
	- $P_{\mathrm{max}} = \frac{U_{\mathrm{max}}^{2}}{2Z_{\mathrm{L}}} = \frac{\pi E_{\mathrm{max}}^{2}r_{i}^{2}}{\eta} \ln \frac{r_{a}}{r_{i}} = \frac{\pi E_{\mathrm{max}}^{2}r_{a}^{2}}{\eta} \frac{\ln \frac{r_{a}}{r_{i}}}{(\frac{r_{a}}{r_{i}})^{2}}$
	- $Z_{\mathrm{L,max. Leistung}} = \frac{30 \Omega}{\sqrt{\varepsilon_{r}}}$
	- $p_{v}(z) = - \frac{\d P}{\d z} = - \frac{\d }{\d z}P_{0}e^{ - 2 \alpha z} = 2 \alpha P_{0}e^{ - 2 \alpha z} = 2 \alpha P(z)$
	- $\mathrm{mit} \qquad \alpha = \alpha_{R} + \alpha_{G}$
- ## [[dielektrische wellenleiter]]
  collapsed:: true
	- [S. 15](((677f9dca-32a1-4dec-b900-f8422e84750a)))
	- ${\xi = k_{x1}d}$
	- ${\eta = k_{x2}d}$
	- ${ - \xi \cot \xi = \eta}$
	- $\xi^{2} + \eta^{2} = \omega^{2} \mu_{0}d^{2}(\varepsilon_{1} - \varepsilon_{2}) = V^{2} \quad \Rightarrow \quad V = \frac{2 \pi d}{\lambda_{0}} \sqrt{n_{1}^{2} - n_{2}^{2}}$
	- $k_{x1,m} = \frac{(2m - 1) \pi}{2d},\quad m = 1,2,\dots.$
	- $\omega_{c,m} = \frac{(2m - 1) \pi}{2d \sqrt{\varepsilon_{0} \mu_{0}(\varepsilon_{r1} - \varepsilon_{r2})}}$
	  id:: 674d7759-f065-41be-aa7b-2bb81097b152
	  tags:: formel
	  bezeichnung:: grenz [[kreisfrequenz]] eines [[dielektrischen wellenleiters]]
		- $\omega_{c,m}$ ... grenz [[kreisfrequenz]] $\iu{\frac{rad}{s}}$
		- $m$ ... index der untersuchten mode $\iu{-}$
		- $d$ ... dicke der dielektrischen schicht $\iu{m}$
		- ((67403e6e-6727-48b1-a844-64fcf2c30521))
		- ((67403e6f-2a7f-4aec-8c79-829be01340e3))
		- $\varepsilon_{r1}, \varepsilon_{r2}$ ... relative [[permittivität]] $\iu{-}$
- ## [[streifenleitungen]]
  collapsed:: true
	- [S. 16](((677f9ddb-619a-431e-ad3e-32d1c258411b)))
	- $Z_{\mathrm{L},0} \approx \sqrt{\frac{\mu_{0}}{\varepsilon_{0}}} \frac{1}{2 \pi} \ln \left(\frac{8h}{w} + \frac{w}{4h} \right)$
	- $Z_{\mathrm{L}} = \frac{Z_{\mathrm{L},0}}{\sqrt{\varepsilon_{\mathrm{eff}}}}$
	  id:: 67646b82-d0e0-4846-b3a4-95047ec3ffab
	- $\lambda = \frac{\lambda_{0}}{\sqrt{\varepsilon_{\mathrm{eff}}}}$
	- $\varepsilon_{\mathrm{eff}} = 1 + q(\varepsilon_{r} - 1)$
	  id:: 67646b82-7d16-4f2c-8ee2-9a3d830a3bc4
	  tags:: formel
	  bezeichnung:: effektive [[permittivität]]
		- $\varepsilon_{\mathrm{eff}}$ ... effektive [[permittivität]] $\iu{ - }$
		- $q$ ... füllfaktor $\iu{ - }$
		- $\varepsilon_r$ ... relative [[permittivität]] $\iu{ - }$
	- $f_{c,\mathrm{TEM}} = \frac{c}{4h \sqrt{\varepsilon_{r} - 1}}$
	- $h_{\mathrm{max}} = \frac{\lambda_{0}}{4 \sqrt{\varepsilon_{r} - 1}}$
	- $f_{c,\mathrm{QTEM}} = \frac{c}{(2w + 0,8h) \sqrt{\varepsilon_{r}}}$
	- $\alpha = \alpha_{\mathrm{L}} + \alpha_{\mathrm{D}}$
	- $\begin{aligned} - \cfrac{\partial}{\partial z}P(z) = & |H_{x 0}|^{2} \mathbb{R} w~, \\ \mathbb{R} =  & \sqrt{\frac{\omega \mu}{\nu \mu}}~, \\ \alpha_L = & \cfrac{1}{2P(z)} \sqrt{\cfrac{\omega \mu}{\rho}}w|H_{z 0}|^{2} = \sqrt{\cfrac{\omega \mu}{2 \sigma}} \cfrac{1}{\eta h}\end{aligned}$ 
	  id:: 67646b82-5793-44f2-bf08-2157166a28aa
	  [link](((67646b82-fd98-4993-91b2-db2db6267fd3)))
	- $P = \int \vect{P} \cdot \d  \vect{F} = \int T_{w,z} \d x \d y = \frac{1}{2} \int E_{y} H_{x}^{*} \d x \d y = \frac{1}{2 \eta}|E_{y0}|^{2} hw$
	  id:: 67646b82-afb7-461b-b7c5-33308e3f9af8
	- ((677f880d-96b0-404f-aba0-4f8d87e354a1))
	  id:: 677f8df3-6685-4052-a48a-f893c12cfc77
	- $\alpha_{\mathrm{L}} = \sqrt{\frac{\omega \mu}{2 \sigma}} \frac{1}{Z_{\mathrm{L}}w}$
	  id:: 67646b82-fd98-4993-91b2-db2db6267fd3
	- $\alpha_{\mathrm{L}}' = \alpha_{\mathrm{L}} \left(1 + \frac{2}{\pi} \arctan \left(1,4 \frac{\Delta}{d_{1}} \right) \right)$
	- $\alpha_{\mathrm{D}} = k_{\mathrm{E}} \frac{S}{2},\quad \frac{\varepsilon'}{\varepsilon''} = \tan \Theta = s$
	- $\alpha_{\mathrm{D}} = \frac{\pi}{\lambda} \tan \Theta$
	- $\alpha_{\mathrm{D}} = \frac{\pi}{\lambda} \tan \Theta \left(\frac{\varepsilon_{r}}{\varepsilon_{\mathrm{eff}}} \frac{\varepsilon_{\mathrm{eff}} - 1}{\varepsilon_{r} - 1} \right)$
- ## Wellen und Hindernisse
  collapsed:: true
	- [S. 17](((677f9dee-cbfa-428f-8158-c5169aa0c07e)))
	- $\Gamma_{\mathrm{rauh}} = \Gamma_{\mathrm{glatt}} \exp \left[ - 2 \left(k \sigma \cos \Theta_{\mathrm{e}} \right)^{2} \right]$
	- $E/E_{0} = 1/2 - \exp \left( - j \pi/4 \right) \left[C \left(v \right) + j S \left(v \right) \right]/\sqrt{2}$
	- $C \left(v \right) = \int^{v} \cos \left(\pi t^{2}/2 \right)d t \qquad S \left(v \right) = \int^{v} \sin \left(\pi t^{2}/2 \right)d t$
	- $v = h \sqrt{2/\lambda \left(1/d_{s} + 1/d_{e} \right)}$
- ## [[antennen]]
	- [S. 18](((677f9e00-c940-4779-8c23-449b4e9ba2e2)))
	- $\vect{\mathbf{A}} \left(\vect{r} \right) = \mu \int \frac{\vect{\mathbf{S}}_{e} \left(\vect{r}' \right)e^{ - j k \left|\vect{r} - \vect{r}' \right|}}{4 \pi \left|\vect{r} - \vect{r}' \right|} d V'$
	- ${V}'$
	- $\vect{\mathbf{A}} \left(\vect{r} \right) = \mu \frac{e^{ - j k r}}{4 \pi r} \int \vect{\mathbf{S}}_{e} \left(\vect{r}' \right) e^{ + j k r' \cos \vartheta}d V' = \mu \frac{e^{ - j k r}}{4 \pi r} \vect{\mathbf{N}} \left(\vartheta \right)$
	- $\begin{aligned}|\tilde{r} - \tilde{r}'| = & {\sqrt{r^{2} + r'^{2} - 2r r' \cos \vartheta}} \\ = & \sqrt{\left(r - r' \cos \vartheta \right)^{2} + r'^{2} \sin^{2} \vartheta} \\ = & {(r - r' \cos \vartheta) \left[1 + \frac{1}{2} \frac{r'^2 \sin^2 \vartheta}{\left(r - r' \cos \vartheta \right)^{2}} + \cdots \right]}\end{aligned}$
	- $\Delta \alpha = k \Delta r = \frac{2 \pi}{\lambda} \frac{r'^{2} \sin^2 \vartheta}{2 \left(r - r' \cos \vartheta \right)}$
	- $\Delta \alpha_{m a x} = \frac{\pi}{\lambda} \frac{r'^{2}}{r}$
	- $\frac{\pi}{2} = \frac{\pi}{\lambda} \frac{D^{2}}{r_{R}}$
	- $r_{R} = \frac{2D^{2}}{\lambda} \left( + \lambda \right)$
	- $\frac{\left|\mathbf{E}_{\mathrm{Co}} \left(\vartheta,\varphi \right) \right|}{\left|\mathbf{E}_{\mathrm{Co}} \left(\vartheta_{m a x},\varphi_{m a x} \right) \right|} = \frac{\left|\mathbf{H}_{\mathrm{X}} \left(\vartheta,\varphi \right) \right|}{\left|\mathbf{H}_{\mathrm{X}} \left(\vartheta_{m a x},\varphi_{m a x} \right) \right|} = f \left(\vartheta,\varphi \right)$
	- $\vartheta_{m a x} = \pi/2 \mathrm{und}$
	- $\varphi_{m a x} = \mathrm{beliebig}$
	- $\frac{\mathbf{E}_{\vartheta}}{\mathbf{E}_{\vartheta} \left(\pi/2 \right)} = \frac{\mathbf{H}_{\varphi}}{\mathbf{H}_{\varphi} \left(\pi/2 \right)} = f \left(\vartheta,\varphi \right) = \sin \vartheta$
	- $\phi = r^{2}R e \left\{\vect{\Gamma} \right\} \cdot \vect{e}_{r}$
	- $\vect{\mathbb{\Gamma}} = \frac{1}{2} \vect{\mathbb{\mathbf{H}}} \times \vect{\mathbb{\Pi}}^{\star}$
	- $\frac{1}{2} \underset{f}{\int} \left(\vect{\mathbf{E}} \times \vect{\mathbf{H}}^{\star} \right) \cdot \vect{e_{r}} d f$
	- $P_{r} = \frac{1}{2}R e \left\{\underset{f}{\int} \left(\vect{\mathbf{E}} \times \vect{\mathbf{H}}^{\star} \right) \cdot \vect{e}_{r}^{\phantom{'}} d f \right\}$
	- $\mathit{d f} = r^{2} \sin \vartheta d \vartheta d \varphi = r^{2}d \Omega$
	- $P_{r} = \int_{4 \pi}R e \left\{\vect{\mathbf{T}} \right\}r^{2} \cdot \vect{e}_{r} d \Omega = \int_{4 \pi} \phi d \Omega = \phi_{m a x} \int_{4 \pi} \frac{\phi}{\phi_{m a x}} d \Omega$
	- $f \left(\vartheta,\varphi \right) = \frac{\left|\mathrm{E}_{\mathrm{Co}} \left(\vartheta,\varphi \right) \right|}{\left|\mathrm{E}_{\mathrm{Co}} \left(\vartheta_{m a x},\varphi_{m a x} \right) \right|}$
	- $\frac{\phi}{\phi_{m a x}} = \left|f \left(\vartheta,\varphi \right) \right|^{2}$
	- $P_{r} = \phi_{m a x} \int \left|f \left(\vartheta,\varphi \right) \right|^{2}d \Omega = \phi_{m a x} \Omega_{ä}$
	- $\Omega_{ä} = \int\limits_{0}^{2\pi} \int\limits_{0}^{\pi} \left|f \left(\vartheta,\varphi \right) \right|^{2} \sin (\vartheta) \d \vartheta \d  \varphi$
	  id:: 678780ff-0ccf-4de6-9d47-a917d9ea7907
	  tags:: formel
	  bezeichnung:: äquivalenter raumwinkel
	  collapsed:: true
		- $\Omega_{ä}$ ... äquivalenter raumwinkel $\iu{ sr }$
		- $\varphi$ ... azimut/längen winkel [link](((6787811c-b191-47c2-bfb0-165bf5a84e4e))) $\iu{°}$
		- $\vartheta$ ... höhen/breiten winkel [link](((6787811c-b191-47c2-bfb0-165bf5a84e4e))) $\iu{°}$
		- $f(\vartheta,\varphi)$ ... richtcharakteristik
	- ${D=\cfrac{4\pi}{\Omega_{ä}}=\frac{4\pi}{\int\limits_0^{2\pi}\opn d \varphi\int\limits_0^{\pi}|f(\vartheta,\varphi)|^2 \sin (\vartheta) \opn d \vartheta \opn d \varphi}}$
	  tags:: formel
	  bezeichnung:: direktivität einer antenne
	  id:: 678780ff-213f-4ae3-b6b5-da29521bc3ab
	  collapsed:: true
		- $\Omega_{ä}$ ... äquivalenter raumwinkel $\iu{ sr }$
		- $\varphi$ ... azimut/längen winkel [link](((6787811c-b191-47c2-bfb0-165bf5a84e4e))) $\iu{°}$
		- $\vartheta$ ... höhen/breiten winkel [link](((6787811c-b191-47c2-bfb0-165bf5a84e4e))) $\iu{°}$
		- $f(\vartheta,\varphi)$ ... richtcharakteristik
	- ${\int_{0}d \varphi \int_{0}^{\pi}|f(\vartheta,\varphi)|^{2} \sin \vartheta d \vartheta}$
	- $\frac{P_{\mathrm{L_{HD}}}}{P_{\mathrm{L_{DUT}}}} = \frac{P_{\mathrm{r_{HD}}}}{P_{\mathrm{r_{DUT}}}}e_{\mathrm{DUT}} = \cdot \cdot \cdot \cdot \cdot$
	- $|\mathbf{E}_{\vartheta_{H D}}| = \frac{\eta \left|\mathbf{I} \right|s}{2 \lambda r} \sin \vartheta.$
	- $P_{\mathrm{r_{_{HD}}}} = \frac{\pi \eta}{3} \left(\frac{s^{2}}{\lambda^{2}} \right) \left|\mathbf{I} \right|^{2}$
	- $|\mathbf{E}_{\vartheta_{H D}}| = \sqrt{\frac{3 \eta}{4 \pi}} \sqrt{P_{r,H D}} \frac{\sin \vartheta}{r}$
	- $P_{\mathrm{r_{_{HD}}}} = \frac{4 \pi r^{2}}{3 \eta} \left|\mathbf{E}_{\vartheta_{H D}} \right|^{2} \frac{1}{\sin^{2} \vartheta}$
	  id:: 678780ff-6f02-40df-af15-e74da9988f12
	  tags:: formel, wip
	  bezeichnung:: empfangene leistung eines hertz'schen dipols
		- $r$ ... radius/entfernung von HD zum messpunkt $\iu{W}$
		- $\eta$ ... wellenwiderstand des ausbreitungsmediums $\iu{\Omega}$
		- $\mathbf{E}_{{\vartheta}_{HD}}$ ... feldstärke(?)
		- $\vartheta$ ... elevationswinkel $\iu{°}$
	- $\frac{\left|\mathbf{E}_{\vartheta_{H D}} \right|}{\left|\mathbf{E}_{\vartheta_{\mathrm{HD}}} \right|_{m a x}} = f_{H D} \left(\vartheta \right) = \sin \vartheta$
	- $P_{\mathrm{r_{HD}}} = \frac{4 \pi r^{2}}{3 \eta} \left|\mathbf{E}_{\vartheta,H D} \right|_{m a x}^{2}$
	- $\mathbb{E}_{\vartheta} = \frac{j \eta \mathbf{I}}{2 \pi r} e^{ - j k r} \mathbb{F} \left(\vartheta,\varphi \right)$
	- $\mathbf{H}_{\varphi}^{\star} = - j \frac{\mathbf{I}^{\star}}{2 \pi r} e^{ + j k r} \mathbf{F}^{\star} \left(\vartheta,\varphi \right)$
	- $P_{\mathrm{rpcr}} - \frac{1}{2}R e \left\{\oint \left(\dot{\mathbf{E}} \times \dot{\mathbf{H}}^{\star} \right) \cdot e_{r}^{\star} d f \right\} - \frac{1}{2} \int_{0}^{2 \pi} \int_{0}^{\pi} \eta \frac{|\mathbf{I}|^{2}}{4 \pi^{2}r^{2}} \left|\mathbf{F} \left(\vartheta,\varphi \right) \right|^{2}r^{2} \sin \vartheta d \vartheta d \varphi = 0.$
	- $= \eta \frac{\left|\mathbf{I} \right|^{2}}{8 \pi^{2}} \underset{0}{\overset{2 \pi}{\int}} \underset{0}{\overset{\pi}{\int}} \left|\mathbf{F} \left(\vartheta,\varphi \right) \right|^{2} \sin \vartheta d \vartheta d \varphi$
	- $\left|\mathbf{E}_{\vartheta} \right|_{m a x} = \frac{\eta \left|\mathbf{I} \right|}{2 \pi r} \left|\mathbf{F} \left(\vartheta_{m a x},\varphi_{m a x} \right) \right|$
	- $\frac{\left|\mathbf{E}_{\vartheta} \right|}{\left|\mathbf{E}_{\vartheta} \right|_{m a x}} = \frac{\left|\mathbf{F} \left(\vartheta,\varphi \right) \right|}{\left|\mathbf{F} \left(\vartheta_{m a x},\varphi_{m a x} \right) \right|} = \left|f \left(\vartheta,\varphi \right) \right|$
	- $\left|\mathbf{F} \left(\vartheta,\varphi \right) \right| = \left|f \left(\vartheta,\varphi \right) \right|\left|\mathbf{F} \left(\vartheta_{m a x},\varphi_{m a x} \right) \right| = \left|f \left(\vartheta,\varphi \right) \right|\frac{2 \pi r}{\eta \left|\mathbf{I} \right|} \left|\mathbf{E}_{\vartheta} \right|_{m a x}$
	- $2 \pi \pi$
	- $P_{\mathrm{{r_{DUT}}}} = \frac{r^{2}}{2 \eta} \left|\mathbf{E}_{\vartheta} \right|_{m a x}^{2} \int\limits_0^{2\pi} \int\limits_0^{\pi} \left|f \left(\vartheta,\varphi \right) \right|^{2} \sin \vartheta d \vartheta d \varphi$
	- $\frac{P_{\mathrm{rmD}}}{P_{\mathrm{rDUT}}} = \frac{\frac{4 \pi r^{2}}{3 \eta}}{\frac{r^{2}}{2 \eta}} \frac{\left|\mathbf{E}_{\vartheta_{H D}} \right|_{m a x}^{2}}{\left|\mathbf{E}_{\vartheta} \right|_{m a x}^{2}} \int\limits_{0}^{2 \pi} \int\limits_{0}^{\pi} \left|f \left(\vartheta,\varphi \right) \right|^{2} \sin \vartheta d \vartheta d \varphi$
	- $G_{R E F} = \frac{P_{\mathrm{L_{REF}}}}{P_{\mathrm{L_{DUT}}}} \cdot \frac{\left|\mathbf{E}_{\vartheta_{D U T}} \right|_{m a x}^{2}}{\left|\mathbf{E}_{\vartheta_{R E F}} \right|_{m a x}^{2}}$
	- $G_{H D} = e_{DUT}\frac{8 \pi/3}{{\int\limits_0^{2\pi} \int\limits_0^{\pi} |f(\vartheta,\varphi)|^{2} \sin \vartheta \d  \vartheta \d  \varphi}}$
	  tags:: formel
	  bezeichnung:: gewinn eines hertz'schen dipols gegenüber des isotropen strahlers
		- $e_{DUT}$ ... strahlungseffizienz $\iu{-}$
	- $G_{\mathrm{HD}} = \frac{P_{\mathrm{L}_{\mathrm{HD}}}}{P_{\mathrm{L}_{\mathrm{DUT}}}} \cdot \frac{|E_{\vartheta_{\mathrm{DUT}}}|_{\mathrm{max}}^{2}}{|E_{\vartheta_{\mathrm{HD}}}|_{\mathrm{max}}^{2}} = e_{\mathrm{DUT}} \frac{P_{\mathrm{r}_{\mathrm{HID}}}}{P_{\mathrm{r}_{\mathrm{DUT}}}} \cdot \frac{|E_{\vartheta_{\mathrm{DUT}}}|_{\mathrm{max}}^{2}}{|E_{\vartheta_{\mathrm{HD}}}|_{\mathrm{max}}^{2}}$
	  tags:: formel
	  bezeichnung:: -
		- $P_{L_{HD}}$ ... sendeleistung eines hertz'schen dipols $\iu{W}$
	- $G_{H D} = \frac{8 \pi/3}{{\int\limits_0^{2\pi} \int\limits_0^{\pi} |f(\vartheta,\varphi)|^{2} \sin \vartheta \d  \vartheta \d  \varphi}}$
	- $G_{H D} = \frac{8 \pi/3}{\Omega_{ä}} = \frac{2}{3} G_{I S O}$
	  id:: 678949c8-3f57-4289-8d02-6e339ae100a8
	  tags:: formel
	  bezeichnung:: gewinn des hertz'schen dipols gegenüber des isotropen strahlers
		- $G_{HD}$ ... gewinn gegenüber des <u>H</u>ertz'schen <u>D</u>ipols $\iu{-}$
		- $\Omega_{ä}$ ... äquivalenter raumwinkel $\iu{ sr }$
		- $G_{ISO}$ ... gewinn gegenüber des <u>ISO</u>tropstrahlers $\iu{-}$
	- $T_{E} \left(r \right) = G \frac{P_{S}}{4 \pi r^{2}}$
	- $|\mathbf{E}_{E}| = \frac{A}{\lambda r}E_{0}$
	- $T_{E} \left(r \right) = \frac{\left|\mathbf{E}_{E} \right|^{2}}{2 \eta} = \left(\frac{A}{\lambda r} \right)^{2} \frac{E_{0}^{2}}{2 \eta}$
	- $P_{S} = \frac{E_{0}^{2}}{2 \eta} A$
	  tags:: formel, wip
	  bezeichnung:: abgestrahlte leistung einer [[antenne]]
	  id:: 6735b379-9a02-48b3-997c-2ecd856cb257
		- $P_S$ ... Strahlleistung $\iu{ W }$
		- $E_0$ ... elektrische feldstärke $\iu{ \frac{V}{m} }$
		- $A$ ... fläche der antennen apertur $\iu{ m^2 }$
		- $\eta$ ... [[wellenwiderstand]] $\iu{ \Omega }$
		- skript
			- ((6737138c-9739-4333-8d9b-11a498e0f337))
	- $G = 4 \pi r^{2} \frac{T_{E} \left(r \right)}{P_{S}} = 4 \pi \frac{A}{\lambda^{2}}$
	- $G_{I S O} = \frac{4 \pi}{\lambda^{2}}A w$
	- $P_{E} = A \bar{T}_{E}$
	- $G_{\mathrm{DUT/ISO}} = \frac{\mathit{E I R P}}{P_{\mathrm{L_{\mathrm{DUT}}}}} \cdot \frac{\left|E_{\vartheta_{\mathrm{DUT}}} \right|_{\mathrm{max}}^{2}}{\left|E_{\vartheta_{\mathrm{ISO}}} \right|_{\mathrm{max}}^{2}}$
	- $\mathit{E I R P} = P_{L}G_{I S O}$
	- $L=ns$
	- $l = \frac{\pi D}{\cos \psi}$
	- $s = l \sin \psi = \pi D \tan \psi$
	- ${k_{\mathrm{wendel}}l - k_{0}s = 2 \pi \nu \qquad \nu = 1,2,3,\dots.}$
	- $k_{\mathrm{wendel}} = \frac{\omega}{v}$
	- $\omega \left(\frac{l}{v} - \frac{s}{c_{0}} \right) = 2 \pi \nu \qquad \nu = 1,2,3,\dots.$
	- $\omega = 2 \pi \frac{c_{0}}{\lambda_{0}} \quad \mathrm{u}n d \quad l \approx \pi D \approx \lambda_{0}$
	- $l = \left(\lambda_{0} + s \right) \frac{v}{c_{0}}$
	- $\frac{3}{4} \lambda_{0}<\lambda<\frac{4}{3} \lambda_{0}$
	- $\mathbf{P} = \frac{1}{2} \left|\mathbf{I} \right|^{2} \mathbf{Z}_{A}$
	- $\vect{\mathbf{T}} = \frac{1}{2} \vect{\mathbf{E}} \times \vect{\mathbf{H}}^{\star}$
	- $\mathbf{T}_{r}=\frac{1}{2} \mathbf{E}_{\vartheta}\mathbf{H}_{\varphi}^{\star}$
	- $\mathbf{T}_{\vartheta}=-\frac{1}{2}\mathbf{E}_{r}\mathbf{H}_{\varphi}^{\phantom{\varphi}\star}\approx0$
	- $\mathbf{T}_{\varphi}\equiv0$
	- $|\mathbf{H}_{\varphi}|=\left|\mathbf{E}_{\vartheta}\right|/\eta$
	- $P_{r} = \frac{1}{2} \int \limits_{\varphi = 0}^{2 \pi} \int \limits_{\vartheta = 0}^{\pi} \frac{\left|\mathbf{E}_{\vartheta} \right|^{2}}{\eta} r^{2} \sin \vartheta \opn d \vartheta \opn d \varphi$
	- $\mathbf{E}_{\vartheta}=j\eta~\frac{\mathbf{I}s}{2\lambda}~\frac{e^{-j k r}}{r}~\sin\vartheta$
	- $P_{r} = \frac{1}{3} \pi \eta \left(\frac{s^{2}}{\lambda^{2}} \right) \left|\mathbf{I} \right|^{2}$
	- $R_{A} = \frac{2}{3} \pi \eta \left(\frac{s^{2}}{\lambda^{2}} \right)$
	- $m = \frac{1 + |\rho|}{1 - |\rho|} = \frac{|U_{m a x}|}{|U_{m i n}|}$
	- $\mathbf{Z}(z) = \frac{\mathbf{U}(z)}{\mathbf{I}(z)}$
	- $Q = \frac{\omega}{2R_{A}} \left(\frac{\partial X_{A}}{\partial \omega} \right) \bigg|_{\omega = \omega_{0}} \qquad \mathrm{ mit } \qquad \mathbf{Z}_{A} = R_{A} + j X_{A}$
	- $\Delta \omega = \frac{\omega_{0}}{Q}$
	- $Q = \frac{\omega}{2G_{A}} \left(\frac{\partial B_{A}}{\partial \omega} \right) \bigg|_{\omega = \omega_{0}} \qquad \mathrm{mit} \qquad \mathbf{Y}_{A} = G_{A} + j B_{A}$
	- $\mathcal{r} = \mathcal{r}_{\mathsf{0}} \exp \left(\mathit{a} \psi \right)$
	- $\frac{P_{S1}}{P_{E2}} = \frac{P_{S2}}{P_{E1}}$
	- $G \left(\vartheta,\varphi \right) = \frac{P_{\mathrm{L_{REF}}}}{P_{\mathrm{L_{DUT}}}} \cdot \frac{\left|E_{\vartheta_{\mathrm{DUT}}} \left(\vartheta,\varphi \right) \right|^{2}}{\left|E_{\vartheta_{\mathrm{REF}}} \left(\vartheta,\varphi \right) \right|^{2}} =$
	- $M E G = \int G \left(\vartheta,\varphi \right) P \left(\vartheta,\varphi \right)d \Omega$
	- $\mathbf{4} \boldsymbol{\pi}$
	- $\Delta \omega = \frac{\omega_{0}}{Q}$
	- $Q = \frac{\omega}{2G_{A}} \left(\frac{\partial B_{A}}{\partial \omega} \right) \bigg|_{\omega = \omega_{0}} \qquad \mathrm{mit} \qquad \mathbf{Y}_{A} = G_{A} + j B_{A}$
	- $\mathcal{r} = \mathcal{r}_{\mathsf{0}} \exp \left(\mathit{a} \psi \right)$
	- $\frac{P_{S1}}{P_{E2}} = \frac{P_{S2}}{P_{E1}}$
	- $\begin{aligned}G\left(\vartheta,\varphi\right)= & \frac{P_{\mathrm{L_{REF}}}}{P_{\mathrm{L_{DUT}}}} \cdot \frac{\left|E_{\vartheta_{\mathrm{DUT}}} \left(\vartheta,\varphi\right)\right|^{2}} {\left|E_{\vartheta_{\mathrm{REF}}} \left(\vartheta,\varphi\right)\right|^{2}} = \\ =& \frac{P_{\mathrm{L_{REF}}}}{P_{\mathrm{L_{DUT}}}} \frac{\left|E_{\vartheta_{\mathrm{DUT}}}\right|_{\mathrm{max}}^{2}}{\left|E_{\vartheta_{\mathrm{REF}}}\right|_{\mathrm{max}}^{2}}\frac{\left|f_{\mathrm{DUT}}\left(\vartheta,\varphi\right)\right|^{2}}{\left|f_{\mathrm{REF}}\left(\vartheta,\varphi\right)\right|^{2}}= \\ = & G_{\mathrm{REF}}\cdot\frac{\left|f_{\mathrm{DUT}}\left(\vartheta,\varphi\right)\right|^{2}}{\left|f_{\mathrm{REF}}\left(\vartheta,\varphi\right)\right|^{2}} \end{aligned}$
	- $M E G = \int G \left(\vartheta,\varphi \right) P \left(\vartheta,\varphi \right)d \Omega$
	- $\mathbf{4} \boldsymbol{\pi}$
- ## wellen im freien raum
	- [S. 23](((677f9e16-d327-4592-a537-5690a7082038)))
	- $r \doteq \sqrt{\frac{d \lambda}{4}}$
	- $T_{e,I S O} = \frac{P_{s}}{4 \pi d^{2}}$
	- $T_{e} = \frac{P_{s}G_{s}}{4 \pi d^{2}}$
	- $P_{e} = \textstyle \int_{e} \boldsymbol{A}_{e}$
	- $P_{e} = T_{e}A_{e} = \frac{P_{s} \mathit{G}_{s}}{4 \pi \mathit{d}^{2}}A_{e}$
	- $A = \frac{\lambda^{2}}{4 \pi}G_{i s o}$
	- $P_{e} = \frac{P_{s}G_{s}}{4 \pi d^{2}} \frac{\lambda^{2}}{4 \pi}G_{e} = P_{s} \left(\frac{\lambda}{4 \pi d} \right)^{2} G_{s}G_{e}$
	- $P_{e} = P_{s} \left(\frac{1}{\lambda d} \right)^{2}A_{s}A_{e}$
	- $L \big|_{\mathrm{dB}} = 10 \mathrm{log} \frac{P_{s}}{P_{e}}$
	- $P_{e} \big|_{\mathrm{dBW}} = P_{s} \big|_{\mathrm{dBW}} + G_{s} \big|_{\mathrm{dB}} - L_{I S O} \big|_{\mathrm{dB}} + G_{e} \big|_{\mathrm{dB}}$
	- $L_{I S O} = - 20 \log \left(\frac{\lambda}{4 \pi d} \right)$
	- $L_{s} = 10 \log \frac{P_{s}}{P_{n}} = 10 \cdot \log \frac{P_{s}}{P_{e,\mathrm{min}}} \frac{P_{e,\mathrm{min}}}{P_{n}} = L \big|_{\mathrm{dB}} + S N R_{\mathrm{min}} \big|_{\mathrm{dB}}$
	- $T_{i} = \frac{P_{s}G_{s}}{4 \pi d^{2}}$
	- $P_{e} = T_{e}A_{e} = \frac{T_{i} \sigma}{4 \pi d^{2}}A_{e} = \frac{P_{s}G_{s} \sigma}{\left(4 \pi d^{2} \right)^{2}} \frac{\lambda^{2}}{4 \pi}G_{e}$
	- $\frac{P_{e}}{P_{s}} = \sigma G_{s}^{2} \bigg(\frac{\lambda}{4 \pi} \bigg)^{2} \frac{1}{4 \pi d^{4}}$
	- $\sigma = A G = A \frac{4 \pi}{\lambda^{2}}A = 4 \pi \frac{A^{2}}{\lambda^{2}}$
- ## [[mehrwegausbreitung]]
	- [S. 24](((677f9e30-fbb1-4656-af18-4d0e59104263)))
	- $\tau_{1} = d_{1}/c,\qquad \mathrm{und} \qquad \tau_{2} = d_{2}/c$
	- $\mathbf{h}(\tau) = \mathbf{A}_{1} \delta \left(\tau - \tau_{1} \right) + \mathbf{A}_{2} \delta \left(\tau - \tau_{2} \right)$
	- $\mathbf{H} \left(j \omega \right) = \int_0^\infty \mathbf{h}(\tau) e^{-j \omega \tau} \d  \tau = \mathbf{A}_{1} e^{-j \omega \tau_{1}} + \mathbf{A}_{2} e^{-j\omega\tau_{2}}$
	- $\left|\mathbf{H} \left(j \omega \right) \right| = \sqrt{A_{1}^{2} + A_{2}^{2} + 2 \lambda_{1}A_{2} \cos \left(\omega \cdot \Delta \tau \right)} \qquad \mathrm{mit} \qquad \Delta \tau = \tau_{2} - \tau_{1}$
	- $\Delta f_{N o t c h} = \frac{1}{\Delta \tau}$
	- $\mathbf{H} \left(j \omega \right) = \left|\mathbf{H} \left(j \omega \right) \right|e^{j \phi_{H} \left(j \omega \right)}$
	- $\tau_{G r} = - \frac{d \phi_{H}}{d \omega}$
	- $\vect{\mathbf{E}} \left(\vect{r} \right) = \vect{\mathbf{E}}_{1} e^{ - j \vect{k}_{1} \vect{r}} + \vect{\mathbf{E}}_{2} e^{ - j \vect{k}_{2} \vect{r}}$
	- $\vect{\mathcal{E}}(t)=\vect{E}_{0}\cdot\cos{(\omega t-k d)}$
	- $\begin{aligned} \vect{\mathcal{E}}\left(t\right) = & \vect{E}_{0} \cdot \cos \left( \omega t-k \left[d_{0} + v t\right] \right) \\ = & \vect{E}_{0}\cdot\cos\left(t\left[\omega-k v\right]-k d_{0}\right)\\ = & \vect{E}_{0}\cdot\cos\left(t\left[2\pi f-\frac{2\pi}{\lambda}v\right]-k d_{0}\right) \\ = & \vect{E}_{0}\cdot\cos\left(2\pi t\left[f-\frac{v}{\lambda}\right]-k d_{0}\right)\end{aligned}$
	- $\Delta f_{D}=-\frac{v}{\lambda}=-f\cdot\frac{v}{c}$
	- $\Delta f_{D} = - \frac{v}{\lambda} \cos \left(\gamma \right) = - f \cdot \frac{v}{c} \mathrm{cos} \left(\gamma \right)$
	- $p(E) = \frac{1}{\sigma \sqrt{2 \cdot \pi}} \cdot e^{ - \frac{E^{2}}{2 \cdot \sigma^{2}}}$
	- $\mathrm{Varianz}{: = \overline{{E^{2}}} - \left(\overline{{E}} \right)^{2}}$
	- $\mathrm{Varianz} = \overline{{E^{2}}} = \int E^{2} \cdot p(E)d E = \sigma^{2}$
	- $\sigma^{2} = \overline{{R e(\mathbb{\mathbf{\mathcal{L}}})^{2}}} = P_{m}$
	- $p(a) = \frac{a}{\sigma^{2}} \cdot \exp \left[ - \frac{a^{2}}{2 \sigma^{2}} \right]$
	- ${\mathrm{Mittelwert}} { \overline{{a}} = \sigma \sqrt{\frac{\pi}{2}}}$
	- ${\text{Mittelwert }} { \frac{a^{2}}{a^{2}} = 2 \sigma^{2}}$
	- ${\text{Varianz }} { \overline{{a^{2}}} - \left(\overline{{a}} \right)^{2} = 2 \sigma^{2} - \sigma^{2} \frac{\pi}{2} = 0.429 \sigma^{2}}$
	- ${\text{Medianwert }} {a_{50} = \sigma \sqrt{2 \cdot l n2} = 1.18 \sigma}$
	- $p(a) = \frac{a}{\sigma^{2}} \cdot \exp \left[ - \frac{a^{2} + A^{2}}{2 \sigma^{2}} \right]\cdot I_{0} \left(\frac{a A}{\sigma^{2}} \right)$
	- $\mathrm{quadrat. Mittelwert} \quad \overline{{a^{2}}} = 2 \sigma^{2} + A^{2}$
	- $\frac{P_{e}}{P_{r}} = G_{s} \cdot G_{e} \left(\frac{\lambda}{4 \pi d_{0}} \right)^{2} \left(\frac{d_{0}}{d} \right)^{n}$
	- $p(F) = \frac{1}{\sigma_{F} \sqrt{2 \cdot \pi}} \cdot \exp \left[ - \frac{(F - M)^{2}}{2 \cdot \sigma_{F}^{2}} \right]$