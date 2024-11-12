icon:: 🌊
inherit-color-icon-from:: [[logseq-page-color-lightblue]] 
template-used:: standard-page
tags:: [[wellenausbreitung]], [[uni]]
alias:: surface waves, oberflächenwelle

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
- $Z_{\mathrm{W}}= \cfrac{E_{x}}{H_{y}}$
- $Z_{\mathrm{W2}}= \cfrac{k_{z}}{\omega \delta_{2}}= \cfrac{k_{\mathrm{E2}} \left(1-j \cfrac{1}{2s_{1}} \cfrac{\varepsilon_{2}}{\varepsilon_{1}} \right)}{\omega \varepsilon_{2}(1-j s_{2})} \approx \eta_{\mathrm{E2}} \left(1+j \cfrac{s_{2}}{2} \right)$
- $Z_{\mathrm{W1}}= \cfrac{k_{z}}{\omega \delta_{1}}$
- $\begin{aligned} I_{z}&= \int \limits_{\Sigma} \vect{S}_{1} \cdot \opn{d} \vect{F}= \sigma_{1} \int \limits_{x=0}^{\infty} \int \limits_{y=0}^{b}E_{z1} \opn{d}x \opn{d}y  \\ & =  \sigma_{1} A_{1} b e^{-j k_{z}z} \int \limits_{x=0}^{\infty}e^{j k_{x1}x} \mathrm{d}x  \\ &=j \cfrac{\sigma_{1}A_{1}b}{k_{x1}}e^{-j k_{z}z} \end{aligned}$
- $T_{x0}= \cfrac{1}{2} \Big(-E_{z0}H_{y0}^{*} \Big)=- \cfrac{1}{2} \cfrac{\omega \delta_{1}^{*}}{k_{x1}^{*}}|A_{1}|^{2}$
- $\opn{d}P=T_{x0}~b \opn{d}z$
- $T_{x0}~b \opn{d}z= \cfrac{1}{2}|I_{z}|^{2} \opn{d}Z \quad \Rightarrow \quad \opn{d}Z=- \cfrac{\omega \delta_{1}^{*}k_{x1}^{2}}{\sigma_{1}^{2}} \cfrac{\opn{d}z}{b}$
- $\mathrm{d}Z \approx \eta_{1} \cfrac{\mathrm{d}z}{b}$
- $\mathrm{d}Z= \mathrm{d} \mathbb{R}+j \mathrm{d} \mathbb{X}, \quad \mathrm{d} \mathbb{R}= \cfrac{\mathrm{d}z}{b} \mathbb{R}_{1}, \quad \mathrm{d} \mathbb{X}= \cfrac{\mathrm{d}z}{b} \mathbb{X}_{1}$
- $\mathrm{d}P_{\mathrm{W}}=T_{\mathrm{W}}b \opn{d}z= \cfrac{1}{2}|I_{z}|^{2} \opn{d} \mathbb{R}$
- $I_{z}=-b H_{y1}(0)$
- $\mathrm{d}P_{\mathrm{w}}= \cfrac{1}{2}|H_{y1}(0)|^{2}b \mathbb{R}_{1} \opn{d}z \quad \text{bzw.} \quad \cfrac{\mathrm{d}P_{\mathrm{W}}}{\mathrm{d}z}= \cfrac{1}{2}|H_{y1}(0)|^{2}b \mathbb{R}_{1}$
- $p= \cfrac{1}{b} \cfrac{\mathrm{d}P_{\mathrm{W}}}{\mathrm{d}z}= \cfrac{1}{2}|H_{\mathrm{tang}}(0)|^{2} \mathbb{R}_1$
- $\mathbb{R}_{1}= \cfrac{1}{\sigma_{1}d_{1}}= \mathbb{R}_{\mathbb{\square}} \quad \text{(lies: R square)}$
- $R= \cfrac{l}{\sigma A}$
- $R= \int \mathrm{d}R= \int \limits_{0}^{l} \cfrac{\mathbb{R}_{\square}}{b} \mathrm{d}z= \cfrac{1}{\sigma_{1}d_{1}} \cfrac{l}{b} \propto \sqrt{\omega}$
- $R= \cfrac{l}{2 \pi a} \sqrt{\cfrac{\omega \mu}{2 \sigma_{1}}}, \quad X= \cfrac{l}{2 \pi a} \sqrt{\cfrac{\omega \mu}{2 \sigma_{1}}}$
- $\cfrac{R}{R_{0}}= \cfrac{X}{X_{0}}= \cfrac{a}{2} \sqrt{\cfrac{\omega \mu \sigma_{1}}{2}}= \cfrac{a}{2d_{1}} \propto \sqrt{\omega} \gg1$