icon:: 🛜
inherit- color- icon- from:: [[logseq- page- color- purple]]
tags:: uni
alias:: wave propagation, wellenausbreitungs

- ## vorlesungen
	- [[wellen vo temp]]
- ## beispiele
	- Beispiel 1)
	  background-color:: green
		- formeln
			- $\Theta_i = \Theta_r$
			  tags:: formel
			  bezeichnung:: Reflektions gesetz
				- $\Theta_i$ ... einfallswinkel (**i**nbound) $\mathrm{[°]}$
				- $\Theta_r$ ... reflektionswinkel (**r**eflected) $\mathrm{[°]}$
			- $\frac{\sin\left(\Theta_1\right)}{\sin\left(\Theta_2\right)}=\frac{n_1}{n_2}$
			  tags:: formel
			  bezeichnung:: brechungsgesetz/gesetz von snellius
				- $\Theta_i$ ... einfallswinkel (**i**nbound) $\mathrm{[°]}$
				- $\Theta_r$ ... reflektionswinkel (**r**eflected) $\mathrm{[°]}$
				- $n_1$ ... brechungsindex $\mathbf{[-]}$
				- $n_2$ ... brechungsindex $\mathbf{[-]}$
			- $\Theta_{b}=\arctan\left(\frac{n_2}{n_1}\right)$
			  tags:: formel
			  bezeichnung:: brewster winkel $\mathbf{[°]}$
				- $-$ ...
- ## flashcards
	- ### index
		- query-table:: true
		  collapsed:: true
		  #+BEGIN_QUERY
		  {
		  :title [:b "all flashcards"]
		  :query [:find (pull ?block [*])
		  :where
		  [?block :block/content ?blockcontent]
		  [?block :block/page ?page]
		  [?page :block/name ?pagename]
		  [?block :block/path-refs [:block/name "flashcard"]]
		  ( or
		  (property ?block :deck "Uni::Automatisierungstechnik_Theorie")
		  (property ?block :deck "Uni::Mathematik_Theorie")
		  )
		  ( not
		  (?page :page/name "templates-uni")
		  )
		  ]
		  }
		  #+END_QUERY
		- query-table:: true
		  query-properties:: [:block :tags]
		  collapsed:: true
		  #+BEGIN_QUERY
		  {
		  :title [:b "all flashcards defined here"]
		  :query [:find (pull ?block [*])
		  :where
		  [?block :block/content ?blockcontent]
		  [?block :block/page ?page]
		  [?page :block/name ?pagename]
		  [?block :block/path-refs [:block/name "flashcard"]]
		  ( or
		  (property ?block :deck "Uni::Automatisierungstechnik_Theorie")
		  (property ?block :deck "Uni::Mathematik_Theorie")
		  )
		  [?page :page/name "automatisierungstechnik"]
		  ]
		  }
		  #+END_QUERY
- ## formeln
	- $\lambda_{\mathrm{G},m,n} = \frac{1}{\sqrt{\left(\frac{m}{2a} \right)^{2} + \left(\frac{n}{2b} \right)^{2}}}$
	- $\lambda_{\mathrm{H}} = \frac{\lambda}{\sqrt{1 - \left(\frac{\lambda}{\lambda_{\mathrm{G}}} \right)^{2}}}$
	- $v_{\mathrm{P}} = \frac{c}{\sqrt{1 - \left(\frac{\lambda}{\lambda_{\mathrm{G}}} \right)^{2}}}$
	- $v_{\mathrm{G}} = c \sqrt{1 - \left(\frac{\lambda}{\lambda_{\mathrm{G}}} \right)^{2}}$
	- $\kappa^{2} = \left(\frac{m \pi}{a} \right)^{2} + \left(\frac{n \pi}{b} \right)^{2} \equiv \omega^{2} \varepsilon \mu - k_{z}^{2}$
	- $\begin{aligned} P & = \int \opn{Re}\{\vect{T}\} \cdot \opn{d} \vect{F} = \int T_{z} \opn{d}x \opn{d}y = - \frac{1}{2} \int \limits_{0}^{a} \int \limits_{0}^{b} E_{y}H_{x}^{*} \opn{d}x \opn{d}y \\ & = \frac{\omega \vect{k}_{z} \mu}{2} \left(\frac{a A}{\pi} \right)^{2}b \int \limits_{0}^{a} \sin^{2}(\frac{\pi}{a}x) \opn{d}x = \frac{\omega k_{z} \mu}{4}a b \left(\frac{a A}{\pi} \right)^{2} \end{aligned}$
	- $- \opn{d}P = \frac{1}{2}|H_{\mathrm{tang}}|^{2} \mathbb{R}_{\mathrm{M}} \opn{d}F$
	- $\begin{aligned} - \frac{\partial}{\partial z}P(z) & = \frac12 \mathbb{R}_{\mathrm{M}} \left(2 \int_0^{a} \Big[|H_{x}|^2 + |H_{z}|^2 \Big]_{y = 0} \opn{d}x + 2 \int \limits_{0}^{b} \Big[|\underbrace{H_{y}}_0|^2 + |H_{z}|^2 \Big]_{x = 0} \opn{d}y \right) \\ &={\mathbb{R}_{\mathrm{M}}A^{2} \left(\left(\cfrac{k_{z}a}{\pi} \right)^{2} \int \limits_{0}^{a} \sin^{2} \left(\cfrac{\pi}{a}x \right) \mathrm{d}x + \int \limits_{0}^{b} \cfrac{a}{\pi} \cos^{2} \left(\cfrac{\pi}{a}x \right) \mathrm{d}x + \int \limits_{0}^{b} \mathrm{d}y \right)} \\ & = A^{2} \mathbb{R}_{\mathrm{M}} \left(\frac{a}{2} \left(1 + \left(\frac{2a}{\lambda_{\mathrm{H}}} \right)^{2} \right) + b \right) \end{aligned}$
	- $\alpha = \frac{\pi}{\omega \mu} \mathbb{R}_{\mathrm{M}} \frac{\lambda_{\mathrm{H}}}{a^{3} b} \left(\frac{a}{2} \left(1 + \left(\frac{2a}{\lambda_{\mathrm{H}}}\right)^{2} \right) + b \right)$
	- $c = p \frac{\lambda_{\mathrm{H}}}{2}, \quad \text{bzw.} \quad k_{z} = \frac{2 \pi}{\lambda_{\mathrm{H}}} = \frac{p \pi}{c}$
	- $\left(\frac{m \pi}{a} \right)^{2} + \left(\frac{n \pi}{b} \right)^{2} + \left(\frac{p \pi}{c} \right)^{2} = \omega_{m n p}^{2} \varepsilon \mu$
	- $\omega_{m n p} = \pi v \sqrt{\left(\frac{m}{a} \right)^{2} + \left(\frac{n}{b} \right)^{2} + \left(\frac{p}{c} \right)^{2}}$
	- $Q_{0,m n p} = \frac{\omega_{m n p}W}{P}$
	- $Q_{0} = \frac{2 \pi W}{P T} \quad \text{mit} \quad T = \frac{1}{f_{m n p}}$
	- $W = \frac{1}{4} \int_{\mathcal{V}} \left(\varepsilon \vect{E} \cdot \vect{E}^{*} + \mu \vect{H} \cdot \vect{H}^{*} \right) \opn{d}V$
	- $P = \frac{1}{2} \mathbb{R}_{\mathrm{M}} \oint_{\Sigma} \vect{H}_{\mathrm{tang}} \cdot \vect{H}_{\mathrm{tang}}^{*} \opn{d}F$
	- $\lambda_{101} = \frac{2a c}{\sqrt{a^{2} + c^{2}}}$
	- $\omega_{101} = \frac{\pi}{\sqrt{\varepsilon \mu}} \frac{\sqrt{a^{2} + c^{2}}}{a c}$
	- $E_{y} = - 2 \omega \mu \frac{a}{\pi}A \sin \left(\frac{\pi}{a}x \right) \sin \left(\frac{\pi}{c}z \right)$
	- $H_{x} = 2j k_{z} \frac{a}{\pi}A \sin \left(\frac{\pi}{a} x \right) \cos \left(\frac{\pi}{c} z \right)$
	- $H_{z} = - 2j \operatorname{\mathit{A}} \cos{\left(\frac{\pi}{a} x \right)} \sin{\left(\frac{\pi}{c} z \right)}$
	- $W_{e}=W_{m}=A^{2}\mu\frac{a^{2}+c^{2}}{4c^{2}}a b c$
	- $P = A^{2} \mathbb{R}_{\mathrm{M}} \frac{a c \left(a^{2} + c^{2} \right) + 2 b \left(a^{3} + c^{3}\right)}{c^{2}}$
	- $Q_{0} = \frac{\pi \eta}{2 \mathbb{R}_{\mathrm{M}}} \frac{b \sqrt{(a^{2} + c^{2})^{3}}}{a c(a^{2} + c^{2}) + 2b(a^{3} + c^{3})}$
	- $Q_{0} = \frac{\pi \eta \sqrt{2}}{6 \mathbb{R}_{\mathrm{M}}}$
	- ## koaxial leitungen
	- ${\vect{E}} = {E_{r} \vect{e_{r}}}$
	- ${\vect{H}} = {H_{\varphi} \vect{e_{\varphi}}}$
	- $\frac{\partial}{\partial z}U(z) + Z^{\prime}I(z) = 0 ,\qquad \frac{\partial}{\partial z}I(z) + Y^{\prime}U(z) = 0$
	- ${\mathrm{mit}} { \quad Z^{\prime} = R^{\prime} + j \omega L^{\prime} ,\quad} {Y^{\prime} = G^{\prime} + j \omega C^{\prime}}$
	- $\frac{\partial}{\partial z}U(z) - Y^{\prime}Z^{\prime}U(z) = 0 ,\qquad \frac{\partial}{\partial z}I(z) - Y^{\prime}Z^{\prime}I(z) = 0$
	- $U_{v} = Z_{\mathrm{L}}I_{v} ,\qquad U_{r} = - Z_{\mathrm{L}}I_{r}$
	- $Z_{\mathrm{L}} = \sqrt{\frac{Z^{\prime}}{Y^{\prime}}} \qquad \mathrm{bzw.} \qquad Z_{\mathrm{L}} = \sqrt{\frac{R^{\prime} + j \omega L^{\prime}}{G^{\prime} + j \omega C^{\prime}}}$
	- $j k_{z} = \sqrt{Y^{\prime}Z^{\prime}} = \sqrt{(G^{\prime} + j \omega C^{\prime})(R^{\prime} + j \omega L^{\prime})}$
	- $\frac{R^{\prime}}{L^{\prime}} = \frac{G^{\prime}}{C^{\prime}}$
	- $v_{\mathrm{P}} = \frac{\omega}{k} = \frac{\omega}{\opn{Re}\{k_{z}\}} \approx \frac{1}{\sqrt{L^{\prime}C^{\prime}}}$
	- $L = \frac{1}{I} \int_{A} \vect{B} \cdot \vect{n_{A}} \opn{d} \mathcal{A}$
	- $L^{\prime} = \frac{1}{I} \int_{r_{i}}^{r_{a}} \vect{B} \cdot \vect{n_{A}} \opn{d}r = \frac{1}{I} \int_{r_{i}}^{r_{a}}B_{\varphi} \opn{d}r = \frac{\mu}{I} \int_{r_{i}}^{r_{a}}H_{\varphi} \opn{d}r$
	- $H_{\varphi} = \frac{I}{2 \pi r}$
	- $L^{\prime} = \frac{\mu}{I} \int_{r_{i}}^{r_{a}} \frac{I}{2 \pi r} \opn{d}r$
	- $L^{\prime} = \frac{\mu}{2 \pi} \ln \frac{r_{a}}{r_{i}}$
	- $C = \frac{Q}{\int_{\mathcal{C}} \vect{E} \cdot \vect{e_{r}} \opn{d}r}$
	- $\vect{E} = \frac{\tau}{2 \pi \varepsilon} \frac{\vect{e_{r}}}{r}$
	- $C^{\prime} = \frac{\tau}{\int_{\mathcal{C}} \vect{E} \cdot \vect{e}_{r} \opn{d}r} = \frac{\tau}{\int_{r_{i}}^{r_{a}} \frac{\tau}{2 \pi \varepsilon} \frac{\vect{e}_{r}^{\prime}}{r} \cdot \vect{e}_{r}^{\prime} \opn{d}r} = \frac{2 \pi \varepsilon}{\int_{r_{i}}^{r_{a}} \frac{1}{r} \opn{d}r}$
	- $C^{\prime} = \frac{2 \pi \varepsilon}{\ln \frac{r_{a}}{r_{i}}}$
	- $Z_{\mathrm{L,verlustlos}} = \frac{\eta}{2 \pi} \ln \frac{r_{a}}{r_{i}} \qquad \mathrm{mit} \qquad \eta = \sqrt{\frac{\mu}{\varepsilon}}$
	- $\mathbb{R}_{\star} = \sqrt{\frac{\omega \mu_{\mathrm{L}}}{2 \sigma}}$
	- $R^{\prime} = \frac{R_{\mathrm{innen}} + R_{\mathrm{aussen}}}{l} \approx \frac{\frac{\mathbb{R}_{\triangle}l}{2 \pi r_{i}} + \frac{\mathbb{R}_{\triangle}l}{2 \pi r_{a}}}{l} = \frac{\mathbb{R}_{\triangle}}{2 \pi}(\frac{1}{r_{i}} + \frac{1}{r_{a}})$
	- $R^{\prime} = \sqrt{\frac{\omega \mu_{\mathrm{L}}}{2 \sigma}} \frac{1}{2 \pi}(\frac{1}{r_{i}} + \frac{1}{r_{a}})$
	- $G^{\prime} = \omega C^{\prime} \tan \delta_{\varepsilon} = \omega \frac{2 \pi \varepsilon}{\ln \frac{r_{a}}{r_{i}}} \tan \delta_{\varepsilon}$
	- $j k_{z} = \gamma = \alpha + j \beta = \sqrt{(G^{\prime} + j \omega C^{\prime})(R^{\prime} + j \omega L^{\prime})}$
	- $\alpha = \alpha_{R} + \alpha_{C} = (\underbrace{\frac{R^{\prime}}{2 \sqrt{\frac{L^{\prime}}{C^{\prime}}}}}_{(1)} + \underbrace{\underbrace{G^{\prime} \sqrt{\frac{L^{\prime}}{C^{\prime}}}}_{(2)}}_{(3)} \underbrace{1}_{(3)}$
	- $\mathrm{mit} \qquad \quad \mathrm{sinh} \delta_{R} = \frac{R^{\prime}}{\omega L^{\prime}} ,\quad \sinh \delta_{G} = \frac{G^{\prime}}{\omega C^{\prime}}$
	- $\alpha_{R} \approx \frac{R^{\prime}}{2 \sqrt{\frac{L^{\prime}}{C^{\prime}}}} = \frac{\mathbb{R}_{\perp}}{2 \eta r_{a}} \frac{1 + \frac{r_{a}}{r_{i}}}{\ln \frac{r_{a}}{r_{i}}}$
	- $Z_{\mathrm{L,min. Dampfung}} = \frac{\eta_{0}}{2 \pi \sqrt{\varepsilon_{r}}} \ln \frac{r_{a}}{r_{i}} = \frac{77 \Omega}{\sqrt{\varepsilon_{r}}}$
	- $U_{\mathrm{max}} = E_{\mathrm{max}} r_{i} \ln \frac{r_{a}}{r_{i}} = E_{\mathrm{max}} r_{a} \frac{\ln \frac{r_{a}}{r_{i}}}{\frac{r_{a}}{r_{i}}}$
	- $Z_{\mathrm{L,max.Spannungsfest}} = \frac{60 \Omega}{\sqrt{\varepsilon_{r}}}$
	- $P_{\mathrm{max}} = \frac{U_{\mathrm{max}}^{2}}{2Z_{\mathrm{L}}} = \frac{\pi E_{\mathrm{max}}^{2}r_{i}^{2}}{\eta} \ln \frac{r_{a}}{r_{i}} = \frac{\pi E_{\mathrm{max}}^{2}r_{a}^{2}}{\eta} \frac{\ln \frac{r_{a}}{r_{i}}}{(\frac{r_{a}}{r_{i}})^{2}}$
	- $Z_{\mathrm{L,max. Leistung}} = \frac{30 \Omega}{\sqrt{\varepsilon_{r}}}$
	- $p_{v}(z) = - \frac{\opn{d}P}{\opn{d}z} = - \frac{\opn{d}}{\opn{d}z}P_{0}e^{ - 2 \alpha z} = 2 \alpha P_{0}e^{ - 2 \alpha z} = 2 \alpha P(z)$
	- $\mathrm{mit} \qquad \alpha = \alpha_{R} + \alpha_{G}$
	- ## diel wellenleiter
	- ${\xi = k_{x1}d}$
	- ${\eta = k_{x2}d}$
	- ${ - \xi \cot \xi = \eta}$
	- $\xi^{2} + \eta^{2} = \omega^{2} \mu_{0}d^{2}(\varepsilon_{1} - \varepsilon_{2}) = V^{2} \quad \Rightarrow \quad V = \frac{2 \pi d}{\lambda_{0}} \sqrt{n_{1}^{2} - n_{2}^{2}}$
	- $k_{x1,m} = \frac{(2m - 1) \pi}{2d},\quad m = 1,2,\dots.$
	- $\omega_{c,m} = \frac{(2m - 1) \pi}{2d \sqrt{\varepsilon_{0} \mu_{0}(\varepsilon_{r1} - \varepsilon_{r2})}}$
	- ## streifen leit
	- $Z_{\mathrm{L},0} \approx \sqrt{\frac{\mu_{0}}{\varepsilon_{0}}} \frac{1}{2 \pi} \ln \left(\frac{8h}{w} + \frac{w}{4h} \right)$
	- $Z_{\mathrm{L}} = \frac{Z_{\mathrm{L},0}}{\sqrt{\varepsilon_{\mathrm{eff}}}}$
	- $\lambda = \frac{\lambda_{0}}{\sqrt{\varepsilon_{\mathrm{eff}}}}$
	- $\varepsilon_{\mathrm{eff}} = 1 + q(\varepsilon_{r} - 1)$
	- $f_{c,\mathrm{TEM}} = \frac{c}{4h \sqrt{\varepsilon_{r} - 1}}$
	- $h_{\mathrm{max}} = \frac{\lambda_{0}}{4 \sqrt{\varepsilon_{r} - 1}}$
	- $f_{c,\mathrm{QTEM}} = \frac{c}{(2w + 0,8h) \sqrt{\varepsilon_{r}}}$
	- $\alpha \equiv \alpha_{\mathrm{L}} \parallel \alpha_{\mathrm{D}}$
	- ${ - \cfrac{\partial}{\partial \varepsilon}P(z) = |H_{x v}|^{2} \mathbb{R} w,}$
	- ${\mathbb{R} = \sqrt{\frac{\omega \mu}{\nu \mu}},}$
	- ${\mathrm{c.}} $
	- ${\mathrm{c.}} $
	- ${\mathrm{c.}} { = \cfrac{1}{2P(z)} \sqrt{\cfrac{\omega \mu}{\rho}}w|H_{z v}|^{2} = \sqrt{\cfrac{\omega \mu}{\rho}} \cfrac{1}{h}]}$
	- $P = \int \vect{P} \cdot \opn{d} \vect{F} = \int T_{w,z} \opn{d}x \opn{d}y = \frac{1}{2} \int E_{y}I I_{x}^{*} \opn{d}x \opn{d}y = \frac{1}{2 \eta}|E_{y0}|^{2} \mathrmw$
	- $Z_{\mathrm{W}} = \eta \frac{h}{w}.$
	- $\alpha_{\mathrm{L}} = \sqrt{\frac{\omega \mu}{2 \sigma}} \frac{1}{Z_{\mathrm{L}}w}.$
	- $\alpha_{\mathrm{L}}^{\prime} = \alpha_{\mathrm{L}} \left(1 + \frac{2}{\pi} \arctan$
	- $left(1,4 \frac{\Delta}{d_{1}}$
	- $right) \right)$
	- $\alpha_{\mathrm{D}} = k_{\mathrm{E}} \frac{S}{2},\quad \frac{\varepsilon^{\prime}}{\varepsilon^{\prime \prime}} = \tan \Theta = s$
	- $\alpha_{\mathrm{D}} = \frac{\pi}{\lambda} \tan \Theta$
	- $\alpha_{\mathrm{D}} = \frac{\pi}{\lambda} \tan \Theta \left(\frac{\varepsilon_{r}}{\varepsilon_{\mathrm{eff}}} \frac{\varepsilon_{\mathrm{eff}} - 1}{\varepsilon_{r} - 1} \right)$
	- ## wellen und hindernisse
	- $\Gamma_{\mathrm{rauh}} = \Gamma_{\mathrm{glatt}} \exp \left[ - 2 \left(k \sigma \cos \Theta_{\mathrm{e}} \right)^{2} \right]$
	- $E/E_{0} = 1/2 - \exp \left( - j \pi/4 \right) \left[C \left(v \right) + j S \left(v \right) \right]/\sqrt{2}$
	- $C \left(v \right) = \int^{v} \cos \left(\pi t^{2}/2 \right)d t \qquad S \left(v \right) = \int^{v} \sin \left(\pi t^{2}/2 \right)d t$
	- $v = h \sqrt{2/\lambda \left(1/d_{s} + 1/d_{e} \right)}$
	- ## Antennen
	- $\vect{\mathbf{A}} \left(\vect{r} \right) = \mu \int \frac{\vect{\mathbf{S}}_{e} \left(\vect{r}^{\prime} \right)e^{ - j k \left|\vect{r} - \vect{r}^{\prime} \right|}}{4 \pi \left|\vect{r} - \vect{r}^{\prime} \right|} d V^{\prime}$
	- ${V}^{\prime}$
	- $\vect{\mathbf{A}} \left(\vect{r} \right) = \mu \frac{e^{ - j k r}}{4 \pi r} \int \vect{\mathbf{S}}_{e} \left(\vect{r}^{\prime} \right) e^{ + j k r^{\prime} \cos \vartheta}d V^{\prime} = \mu \frac{e^{ - j k r}}{4 \pi r} \vect{\mathbf{N}} \left(\vartheta \right)$
	- ${|\tilde{r} - \tilde{r}^{\prime}|} = {\sqrt{r^{2} + r^{\prime2} - 2r r^{\prime} \cos \tilde{\vartheta}}}$
	- ${ - } { \sqrt{\left(r - r^{\prime} \cos \vartheta \right)^{2} + r^{\prime2} \sin^{2} \vartheta}}$
	- $ = {(r - r^{\prime} \cos \vartheta) \left[1 + \frac{1}{2} \frac{r^{\prime}}{\left(r - r^{\prime} \cos \vartheta \right)^{2}} + \cdots \right]}$
	- $\Delta \alpha = k \Delta r = \frac{2 \pi}{\lambda} \frac{r^{\prime}^{2} \sin^{2} \vartheta}{2 \left(r - r^{\prime} \cos \vartheta \right)}$
	- $\Delta \alpha_{m a x} = \frac{\pi}{\lambda} \frac{r^{\prime2}}{r}$
	- $\frac{\pi}{2} = \frac{\pi}{\lambda} \frac{D^{2}}{r_{R}}$
	- $r_{R} = \frac{2D^{2}}{\lambda} \left( + \lambda \right)$
	- $\frac{\left|\mathbf{E}_{\mathrm{Co}} \left(\vartheta,\varphi \right) \right|}{\left|\mathbf{E}_{\mathrm{Co}} \left(\vartheta_{m a x},\varphi_{m a x} \right) \right|} = \frac{\left|\mathbf{H}_{\mathrm{X}} \left(\vartheta,\varphi \right) \right|}{\left|\mathbf{H}_{\mathrm{X}} \left(\vartheta_{m a x},\varphi_{m a x} \right) \right|} = f \left(\vartheta,\varphi \right)$
	- $\vartheta_{m a x} = \pi/2 \mathrm{und}$
	- $\varphi_{m a x} = \mathrm{beliebig}$
	- $\frac{\mathbf{E}_{\vartheta}}{\mathbf{E}_{\vartheta} \left(\pi/2 \right)} = \frac{\mathbf{H}_{\varphi}}{\mathbf{H}_{\varphi} \left(\pi/2 \right)} = f \left(\vartheta,\varphi \right) = \sin \vartheta$
	- $\phi = r^{2}R e \left\{\vect{\Gamma} \right\} \cdot \vect{e}_{r}$
	- $\vect{\mathbb{\Gamma}} = \frac{1}{2} \vect{\mathbb{\mathbf{H}}} \times \vect{\mathbb{\Pi}}^{\star}$
	- $\frac{1}{2} \underset{f}{\int} \left(\vect{\mathbf{E}} \times \vect{\mathbf{H}}^{\star} \right) \cdot \vect{e_{r}} d f$
	- $P_{r} = \frac{1}{2}R e \left\{\underset{f}{\int} \left(\vect{\mathbf{E}} \times \vect{\mathbf{H}}^{\star} \right) \cdot \vect{e}_{r}^{\phantom{\prime}} d f \right\}$
	- $\mathit{d f} = r^{2} \sin \vartheta d \vartheta d \varphi = r^{2}d \Omega$
	- $P_{r} = \int_{4 \pi}R e \left\{\vect{\mathbf{T}} \right\}r^{2} \cdot \vect{e}_{r} d \Omega = \int_{4 \pi} \phi d \Omega = \phi_{m a x} \int_{4 \pi} \frac{\phi}{\phi_{m a x}} d \Omega$
	- $f \left(\vartheta,\varphi \right) = \frac{\left|\mathrm{E}_{\mathrm{Co}} \left(\vartheta,\varphi \right) \right|}{\left|\mathrm{E}_{\mathrm{Co}} \left(\vartheta_{m a x},\varphi_{m a x} \right) \right|}$
	- $\frac{\phi}{\phi_{m a x}} = \left|f \left(\vartheta,\varphi \right) \right|^{2}$
	- $P_{r} = \phi_{m a x} \int \left|f \left(\vartheta,\varphi \right) \right|^{2}d \Omega = \phi_{m a x} \Omega_{\ddot{a}}$
	- $\Omega_{\ddot{a}} = \int_{0} \int_{0} \left|f \left(\vartheta,\varphi \right) \right|^{2} \sin \vartheta d \vartheta d \varphi$
	- ${D = \cfrac{4 \pi}{\Omega_{\dot{a}}} = \cfrac{4 \pi}{2 \pi} = \cfrac{4 \pi}{2 \pi}}$
	- ${\int_{0}d \varphi \int_{0}^{\pi}|f(\vartheta,\varphi)|^{2} \sin \vartheta d \vartheta}$
	- $\frac{P_{\mathrm{L_{HD}}}}{P_{\mathrm{L_{DUT}}}} = \frac{P_{\mathrm{r_{HD}}}}{P_{\mathrm{r_{DUT}}}}e_{\mathrm{DUT}} = \cdot \cdot \cdot \cdot \cdot$
	- $|\mathbf{E}_{\vartheta_{H D}}| = \frac{\eta \left|\mathbf{I} \right|s}{2 \lambda r} \sin \vartheta.$
	- $P_{\mathrm{r_{_{HD}}}} = \frac{\pi \eta}{3} \left(\frac{s^{2}}{\lambda^{2}} \right) \left|\mathbf{I} \right|^{2}$
	- $|\mathbb{E}_{\vartheta_{H D}}| = \sqrt{\frac{3 \eta}{4 \pi}} \sqrt{P_{r,H D}} \frac{\sin \vartheta}{r}$
	- $P_{\mathrm{r_{_{HD}}}} = \frac{4 \pi r^{2}}{3 \eta} \left|\mathbf{E}_{\vartheta_{H D}} \right|^{2} \frac{1}{\sin^{2} \vartheta}$
	- $\frac{\left|\mathbf{E}_{\vartheta_{H D}} \right|}{\left|\mathbf{E}_{\vartheta_{\mathrm{HD}}} \right|_{m a x}} = f_{H D} \left(\vartheta \right) = \sin \vartheta$
	- $P_{\mathrm{r_{HD}}} = \frac{4 \pi r^{2}}{3 \eta} \left|\mathbf{E}_{\vartheta,H D} \right|_{m a x}^{2}$
	- $\mathbb{E}_{\vartheta} = \frac{j \eta \mathbf{I}}{2 \pi r} e^{ - j k r} \mathbb{F} \left(\vartheta,\varphi \right)$
	- $\mathbf{H}_{\varphi}^{\star} = - j \frac{\mathbf{I}^{\star}}{2 \pi r} e^{ + j k r} \mathbf{F}^{\star} \left(\vartheta,\varphi \right)$
	- $P_{\mathrm{rpcr}} - \frac{1}{2}R e \left\{\oint \left(\dot{\mathbf{E}} \times \dot{\mathbf{H}}^{\star} \right) \cdot e_{r}^{\star} d f \right\} - \frac{1}{2} \int_{0}^{2 \pi} \int_{0}^{\pi} \eta \frac{|\mathbf{I}|^{2}}{4 \pi^{2}r^{2}} \left|\mathbf{F} \left(\vartheta,\varphi \right) \right|^{2}r^{2} \sin \vartheta d \vartheta d \varphi = 0.$
	- $ = \eta \frac{\left|\mathbf{I} \right|^{2}}{8 \pi^{2}} \underset{0}{\overset{2 \pi}{\int}} \underset{0}{\overset{\pi}{\int}} \left|\mathbf{F} \left(\vartheta,\varphi \right) \right|^{2} \sin \vartheta d \vartheta d \varphi$
	- $\left|\mathbf{E}_{\vartheta} \right|_{m a x} = \frac{\eta \left|\mathbf{I} \right|}{2 \pi r} \left|\mathbf{F} \left(\vartheta_{m a x},\varphi_{m a x} \right) \right|$
	- $\frac{\left|\mathbf{E}_{\vartheta} \right|}{\left|\mathbf{E}_{\vartheta} \right|_{m a x}} = \frac{\left|\mathbf{F} \left(\vartheta,\varphi \right) \right|}{\left|\mathbf{F} \left(\vartheta_{m a x},\varphi_{m a x} \right) \right|} = \left|f \left(\vartheta,\varphi \right) \right|$
	- $\left|\mathbf{F} \left(\vartheta,\varphi \right) \right| = \left|f \left(\vartheta,\varphi \right) \right|\left|\mathbf{F} \left(\vartheta_{m a x},\varphi_{m a x} \right) \right| = \left|f \left(\vartheta,\varphi \right) \right|\frac{2 \pi r}{\eta \left|\mathbf{I} \right|} \left|\mathbf{E}_{\vartheta} \right|_{m a x}$
	- $2 \pi \pi$
	- $P_{_ \mathrm{{PUT}}} = \frac{r^{2}}{2 \eta} \left|\mathbf{E}_{\vartheta} \right|_{m a x}^{2} \underbrace{\int}_{\cdot} \int_{\cdot} \left|f \left(\vartheta,\varphi \right) \right|^{2} \sin \vartheta d \vartheta d \varphi$
	- $\frac{P_{\mathrm{rmD}}}{P_{\mathrm{rDUT}}} = \frac{\frac{4 \pi r^{2}}{3 \eta}}{\frac{r^{2}}{2 \eta}} \frac{\left|\mathbf{E}_{\vartheta_{H D}} \right|_{m a x}^{2}}{\left|\mathbf{E}_{\vartheta} \right|_{m a x}^{2}} \int_{0}^{2 \pi} \int_{0}^{\pi} \left|f \left(\vartheta,\varphi \right) \right|^{2} \sin \vartheta d \vartheta d \varphi$
	- $G_{R E F} = \frac{P_{\mathrm{L_{REF}}}}{P_{\mathrm{L_{DUT}}}} \cdot \frac{\left|\mathbf{E}_{\vartheta_{D U T}} \right|_{m a x}^{2}}{\left|\mathbf{E}_{\vartheta_{R E F}} \right|_{m a x}^{2}}$
	- $G_{\mathrm{HD}} = \frac{P_{\mathrm{L}_{\mathrm{HID}}}}{P_{\mathrm{L}_{\mathrm{DUT}}}} \cdot \frac{|E_{\vartheta_{\mathrm{DUT}}}|_{\mathrm{max}}^{2}}{|E_{\vartheta_{\mathrm{HD}}}|_{\mathrm{max}}^{2}} = e_{\mathrm{DUT}} \frac{P_{\mathrm{r}_{\mathrm{HID}}}}{P_{\mathrm{r}_{\mathrm{DUT}}}} \cdot \frac{|E_{\vartheta_{\mathrm{DUT}}}|_{\mathrm{max}}^{2}}{|E_{\vartheta_{\mathrm{HD}}}|_{\mathrm{max}}^{2}}$
	- $G_{H D} = \frac{8 \pi/\mathbf{3}}{2 \pi \pi}$
	- ${\underset{0}{\int} \int_{0}|f(\vartheta,\varphi)|^{2} \mathrm{sin} \vartheta d \vartheta d \varphi}$
	- $G_{H D} = \frac{8 \pi/3}{\Omega_{\ddot{a}}} = \frac{2}{3} G_{I S O}$
	- $T_{E} \left(r \right) = G \frac{P_{S}}{4 \pi r^{2}}$
	- $|\mathbf{E}_{E}| = \frac{A}{\lambda r}E_{0}$
	- $T_{E} \left(r \right) = \frac{\left|\mathbf{E}_{E} \right|^{2}}{2 \eta} = \left(\frac{A}{\lambda r} \right)^{2} \frac{E_{0}^{2}}{2 \eta}$
	- $P_{S} = \frac{E_{0}^{2}}{2 \eta} A$
	- $G = 4 \pi r^{2} \frac{T_{E} \left(r \right)}{P_{S}} = 4 \pi \frac{A}{\lambda^{2}}$
	- $G_{I S O} = \frac{4 \pi}{\lambda^{2}}A w$
	- $P_{E} = A \bar{T}_{E}$
	- $G_{\mathrm{DUT/ISO}} = \frac{\mathit{E I R P}}{P_{\mathrm{L_{\mathrm{DUT}}}}} \cdot \frac{\left|E_{\vartheta_{\mathrm{DUT}}} \right|_{\mathrm{max}}^{2}}{\left|E_{\vartheta_{\mathrm{ISO}}} \right|_{\mathrm{max}}^{2}}$
	- $\mathit{E I R P} = P_{L}G_{I S O}$
	- $\mathit{\mathit{\Delta}} \mathit{\mathit{\Delta}} \mathit{\mathit{\Delta}} \mathit{\mathit{\Delta}} \mathit{\mathit{\Delta}} \mathit{\mathit{\Delta}} \mathit{\mathit{\Delta}} \mathit{\mathit{\Delta}} \mathit{\mathit{\Delta}} \mathit{\mathit{\Delta}} \mathit{\mathit{\Delta}} \mathit{\mathit{\Delta}} \mathit{\mathit{\Delta}} \mathit{\mathit{\Delta}} \mathit{\mathit{\Delta}} \mathit{\mathit{\Delta}} \mathit{\mathit{\Delta}} \mathit{\mathit{\Delta}} \mathit{\mathit{\Delta}} \mathit{\mathit{\Delta}} \mathit{\mathit{\Delta}} \mathit{\mathit{\Delta}} \mathit{\mathit{\Delta}}}$
	- $l = \frac{\pi D}{\cos \psi}$
	- $s = l \sin \psi = \pi D \tan \psi$
	- ${k_{\mathrm{wendel}}l - k_{0}s = 2 \pi \nu \qquad \nu = 1,2,3,\dots.}$
	- $k_{\mathrm{wendel}} = \frac{\omega}{v}$
	- $\omega \left(\frac{l}{v} - \frac{s}{c_{0}} \right) = 2 \pi \nu \qquad \nu = 1,2,3,\dots.$
	- $\omega = 2 \pi \frac{c_{0}}{\lambda_{0}} \quad \mathrm{u}n d \quad l \approx \pi D \approx \lambda_{0}$
	- $l = \left(\lambda_{0} + s \right) \frac{v}{c_{0}}$
	- $\frac{3}{4} \lambda_{0}<\lambda<\frac{4}{3} \lambda_{0}$
	- $\mathbf{P} = \frac{1}{2} \left|\mathbf{I} \right|^{2} \mathbf{Z}_{A}$
	- $\vect{\mathbf{\Gamma}} \vect{\mathbf{\Gamma}} = \frac{1}{2} \vect{\mathbf{\Gamma}} \vect{\mathbf{\Sigma}} \vect{\mathbf{\Sigma}} \vect{\mathbf{\Sigma}} \vect{\mathbf{\Sigma}} \vect{\mathbf{\Sigma}} \vect{\mathbf{\Sigma}}$
	- $\mathbf{\Gamma}^{r} \mathbf{\Gamma}_{r} = \frac{1}{2} \mathbf{\Gamma} \mathbf{\Gamma} \mathbf{\Gamma} \mathbf{\Gamma} \mathbf{\Gamma} \mathbf{\Gamma} \mathbf{\Gamma} \mathbf{\Gamma} \mathbf{\Gamma}$
	- $\mathbf{\Pi}_{\vartheta} = - \frac{1}{2} \mathbf{\Pi}_{\vartheta} \mathbf{\Pi}_{\varphi}^{\star} \approx0$
	- $\underline{{r}}_{ - } \underline{{\Gamma}}_{\varphi} \overline{{\overline{{\mathbf{\Sigma}}}}}_{ - } \mathbf{\Lambda}_{\mathbf{\Lambda}}$
	- $\left|\overline{{\Pi}}_{\varphi} \right| = \left|\underline{{\pm}}_{\vartheta} \right|/\eta$
	- $P_{r} = \frac{1}{2} \mathop{\int}_{\varphi = 0}^{2 \pi} \mathop{\int}_{\vartheta = 0}^{\pi} \frac{\left|\mathbf{E}_{\vartheta} \right|^{2}}{\eta} r^{2} \sin \vartheta d \vartheta d \varphi$
	- $P_{r} = \frac{1}{3} \pi \eta \left(\frac{s^{2}}{\lambda^{2}} \right) \left|\mathbf{I} \right|^{2}$
	- $R_{A} = \frac{2}{3} \pi \eta \left(\frac{s^{2}}{\lambda^{2}} \right)$
	- $m = \frac{1 + |\rho|}{1 - |\rho|} = \frac{|U_{m a x}|}{|U_{m i n}|}$
	- $\mathbf{Z}(z) = \frac{\mathbf{U}(z)}{\mathbf{I}(z)}$
	- $Q = \frac{\omega}{2R_{A}} \left(\frac{\partial X_{A}}{\partial \omega} \right) \bigg|_{\omega = \omega_{0}} \qquad \mathrm{ mit } \qquad \mathbf{Z}_{A} = R_{A} + j X_{A}$
	- $\Delta \omega = \frac{\omega_{0}}{Q}$
	- $Q = \frac{\omega}{2G_{A}} \left(\frac{\partial B_{A}}{\partial \omega} \right) \bigg|_{\omega = \omega_{0}} \qquad \mathrm{mit} \qquad \mathbf{Y}_{A} = G_{A} + j B_{A}$
	- $\mathcal{r} = \mathcal{r}_{\mathsf{0}} \exp \left(\mathit{a} \psi \right)$
	- $\frac{P_{S1}}{P_{E2}} = \frac{P_{S2}}{P_{E1}}$
	- $G \left(\vartheta,\varphi \right) = \frac{P_{\mathrm{L_{REF}}}}{P_{\mathrm{L_{DUT}}}} \cdot \frac{\left|E_{\vartheta_{\mathrm{DUT}}} \left(\vartheta,\varphi \right) \right|^{2}}{\left|E_{\vartheta_{\mathrm{REF}}} \left(\vartheta,\varphi \right) \right|^{2}} = $
	- $M E G = \int G \left(\vartheta,\varphi \right) P \left(\vartheta,\varphi \right)d \Omega$
	- $\mathbf{4} \boldsymbol{\pi}$
	- $\Delta \omega = \frac{\omega_{0}}{Q}$
	- $Q = \frac{\omega}{2G_{A}} \left(\frac{\partial B_{A}}{\partial \omega} \right) \bigg|_{\omega = \omega_{0}} \qquad \mathrm{mit} \qquad \mathbf{Y}_{A} = G_{A} + j B_{A}$
	- $\mathcal{r} = \mathcal{r}_{\mathsf{0}} \exp \left(\mathit{a} \psi \right)$
	- $\frac{P_{S1}}{P_{E2}} = \frac{P_{S2}}{P_{E1}}$
	- $G \left(\vartheta,\varphi \right) = \frac{P_{\mathrm{L_{REF}}}}{P_{\mathrm{L_{DUT}}}} \cdot \frac{\left|E_{\vartheta_{\mathrm{DUT}}} \left(\vartheta,\varphi \right) \right|^{2}}{\left|E_{\vartheta_{\mathrm{REF}}} \left(\vartheta,\varphi \right) \right|^{2}} =$
	- $M E G = \int G \left(\vartheta,\varphi \right) P \left(\vartheta,\varphi \right)d \Omega$
	- $\mathbf{4} \boldsymbol{\pi}$
	- ## wellen im freien raum
	- $r \doteq \sqrt{\frac{d \lambda}{4}}$
	- $T_{e,I S O} = \frac{P_{s}}{4 \pi d^{2}}$
	- $T_{e} = \frac{P_{s}G_{s}}{4 \pi d^{2}}$
	- $P_{e} = \textstyle \int_{e} \boldsymbol{A}_{e}$
	- $P_{e} = T_{e}A_{e} = \frac{P_{s} \mathit{G}_{s}}{4 \pi \mathit{d}^{2}}A_{e}$
	- $A = \frac{\lambda^{2}}{4 \pi}G_{i s o}$
	- $P_{e} = \frac{P_{s}G_{s}}{4 \pi d^{2}} \frac{\lambda^{2}}{4 \pi}G_{e} = P_{s} \left(\frac{\lambda}{4 \pi d} \right)^{2} G_{s}G_{e}$
	- $P_{e} = P_{s} \left(\frac{1}{\lambda d} \right)^{2}A_{s}A_{e}$
	- $L \big|_{\mathrm{dB}} = 10 \mathrm{log} \frac{P_{s}}{P_{e}}$
	- $P_{e} \left|_{\mathrm{dBW}} = P_{s} \right|_{\mathrm{dBW}} + G_{s} \right.\right|_{\mathrm{dB}} - L_{I S O} \right|_{\mathrm{dB}} + G_{e} \left.\right|_{\mathrm{dB}}$
	- $L_{I S O} = - 20 \log \left(\frac{\lambda}{4 \pi d} \right)$
	- $L_{s} = 10 \left.\log \frac{P_{s}}{P_{n}} = 10 \cdot \log \frac{P_{s}}{P_{e,\mathrm{min}}} \frac{P_{e,\mathrm{min}}}{P_{n}} = L \right|_{\mathrm{dB}} + S N R_{\mathrm{min}} \left|_{\mathrm{dB}}$
	- $T_{i} = \frac{P_{s}G_{s}}{4 \pi d^{2}}$
	- $P_{e} = T_{e}A_{e} = \frac{T_{i} \sigma}{4 \pi d^{2}}A_{e} = \frac{P_{s}G_{s} \sigma}{\left(4 \pi d^{2} \right)^{2}} \frac{\lambda^{2}}{4 \pi}G_{e}$
	- $\frac{P_{e}}{P_{s}} = \sigma G_{s}^{2} \bigg(\frac{\lambda}{4 \pi} \bigg)^{2} \frac{1}{4 \pi d^{4}}$
	- $\sigma = A G = A \frac{4 \pi}{\lambda^{2}}A = 4 \pi \frac{A^{2}}{\lambda^{2}}$
	- ## Mehrwegausbreitung
	- $\tau_{1} = d_{1}/c,\qquad \mathrm{und} \qquad \tau_{2} = d_{2}/c$
	- $\mathbf{h}(\tau) = \mathbf{A}_{1} \delta \left(\tau - \tau_{1} \right) + \mathbf{A}_{2} \delta \left(\tau - \tau_{2} \right)$
	- $\mathbf{H} \left(j \omega \right) = \int \mathbf{h}(\tau)e^{ - j \omega \tau} \left.d \tau = \mathbf{A}_{1} \left.e^{ - j \omega \tau_{1}} + \mathbf{A}_{2} \left.e^{ - j \omega \tau_{2}} \right.$
	- $\left|\mathbf{H} \left(j \omega \right) \right| = \sqrt{A_{1}^{2} + A_{2}^{2} + 2 \lambda_{1}A_{2} \cos \left(\omega \cdot \Delta \tau \right)} \qquad \mathrm{mit} \qquad \Delta \tau = \tau_{2} - \tau_{1}$
	- $\Delta f_{N o t c h} = \frac{1}{\Delta \tau}$
	- $\mathbf{H} \left(j \omega \right) = \left|\mathbf{H} \left(j \omega \right) \right|e^{j \phi_{H} \left(j \omega \right)}$
	- $\tau_{G r} = - \frac{d \phi_{H}}{d \omega}$
	- $\vect{\mathbf{E}} \left(\vect{r} \right) = \vect{\mathbf{E}}_{1} \left.e^{ - j \vect{k}_{1} \vect{r}} + \vect{\mathbf{E}}_{2} \left.e^{ - j \vect{k}_{2} \vect{r}} \right.$
	- ${\varepsilon^{I}(l)} { = E_{0} \cdot \mathrm{ev}(\varepsilon_{i}(l - E||l_{0} - l|l_{0})}$
	- ${\varepsilon^{\prime}(l)} { = l_{0} \cdot \mathrm{ev}(\varepsilon_{i}^{\prime}) k_{i}^{\prime}|l_{0}^{\prime}}$
	- ${\varepsilon_{0} \cdot \mathrm{ev}(\varepsilon_{i}^{\prime}) \cdot \mathrm{ev}(\varepsilon_{i}^{\prime}) \cdot \mathrm{ev}(\varepsilon_{i}^{\prime}) \cdot \mathrm{ev}(\varepsilon_{i}^{\prime}) \cdot \mathrm{ev}(\varepsilon_{i}^{\prime}|l_{0}^{\prime})}$
	- ${\varepsilon_{0} \cdot \mathrm{ev}(\varepsilon_{i}^{\prime}|l_{0}^{\prime}|l_{0}^{\prime}|l_{0}^{\prime}|l_{0}^{\prime}|l_{0}^{\prime}|l_{0}^{\prime}|l_{0}^{\prime}|l_{0}^{\prime}|l_{0}^{\prime}|l_{0}^{\prime}|l_{0}^{\prime}|l_{0}^{\prime}|l_{0}^{\prime}|l_{0}^{\prime}|l_{0}^{\prime}|l_{0}^{\prime}|l_{0}^{\prime}|l_{0}^{\prime}|l_{0}^{\prime}|l_{0}^{\prime}|l_{0}^{\prime}|l_{0}}^{\prime}|l_{0}^{\prime}|l_{0}|l_{0}^{\prime}|l_{0}} \right)}$
	- ${|l_{0}^{\prime}|l_{0}|l_{0}^{\prime}|l_{0}|l_{0}} \right).}$
	- $\Delta f_{D} = - \frac{v}{\lambda} \cos \left(\gamma \right) = - f \cdot \frac{v}{c} \mathrm{cos} \left(\gamma \right)$
	- $p(E) = \frac{1}{\sigma \sqrt{2 \cdot \pi}} \cdot e^{ - \frac{E^{2}}{2 \cdot \sigma^{2}}}$
	- $\mathrm{Varianz}{: = \overline{{E^{2}}} - \left(\overline{{E}} \right)^{2}}$
	- $\mathrm{Varianz} = \overline{{E^{2}}} = \int E^{2} \cdot p(E)d E = \sigma^{2}$
	- $\sigma^{2} = \overline{{R e(\mathbb{\mathbf{\mathcal{L}}})^{2}}} = P_{m}$
	- $p(a) = \frac{a}{\sigma^{2}} \cdot \exp \left[ - \frac{a^{2}}{2 \sigma^{2}} \right]$
	- ${\mathrm{Mittelwert}} { \overline{{a}} = \sigma \sqrt{\frac{\pi}{2}}}$
	- ${\mathrm{Mittelwert}} { \frac{a^{2}}{a^{2}} = 2 \sigma^{2}}$
	- ${\mathrm{Varianz}} { \overline{{a^{2}}} - \left(\overline{{a}} \right)^{2} = 2 \sigma^{2} - \sigma^{2} \frac{\pi}{2} = 0.429 \sigma^{2}}$
	- ${\mathrm{Medianwert}} {a_{50} = \sigma \sqrt{2 \cdot l n2} = 1.18 \sigma}$
	- $p(a) = \frac{a}{\sigma^{2}} \cdot \exp \left[ - \frac{a^{2} + A^{2}}{2 \sigma^{2}} \right]\cdot I_{0} \left(\frac{a A}{\sigma^{2}} \right)$
	- $\mathrm{quadrat. Mittelwert} \quad \overline{{a^{2}}} = 2 \sigma^{2} + A^{2}$
	- $\frac{P_{e}}{P_{r}} = G_{s} \cdot G_{e} \left(\frac{\lambda}{4 \pi d_{0}} \right)^{2} \left(\frac{d_{0}}{d} \right)^{n}$
	- $p(F) = \frac{1}{\sigma_{F} \sqrt{2 \cdot \pi}} \cdot \exp \left[ - \frac{(F - M)^{2}}{2 \cdot \sigma_{F}^{2}} \right]