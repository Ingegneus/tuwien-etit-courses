# 1. Übung: Systemanalyse  

Aufgabe 1.1 (Magnetlagerung). Diese Aufgabe soll die Bedeutung von Ruhelagen am Beispiel der eindimensionalen magnetischen Lagerung aus Abbildung 1.1 zeigen. Ein Elektromagnet wird dabei mit einer Spannung $\boldsymbol{v}$ versorgt, welche einen Strom $i$ und damit eine Magnetkraft $f_{m}$ zur Folge hat. Auf das zu lagernde Objekt mit der Masse $m$ wirken die Magnetkraft, die Gewichtskraft und eine äußere Lastkraft $f_{l}$ . Der Luftspalt zwischen Elektromagnet und dem Objekt ist mit $\delta$ bezeichnet und die Geschwindigkeit des Objekts mit $w$ . Ferner ist in Abbildung 1.1 das magnetische Ersatzschaltbild für den magnetischen Fluss $\Phi$ dargestellt. Es besteht aus einer Durchflutungsquelle $\Theta=$ $N i$ , wobei $N$ die Anzahl der Windungen bezeichnet, einer konstanten Eisenreluktanz $\mathcal{R}_{E}=p_{1}$ und einer luftspaltabhängigen Reluktanz $\mathcal{R}_{L}(\delta)=p_{2}\,\delta$ mit den Konstanten $p_{1}$ und $p_{2}$ . Für das elektrische Teilsystem gilt $\begin{array}{r}{\frac{\mathrm{d}}{\mathrm{d}t}\psi=-R i+v}\end{array}$ , wobei $\psi=L_{G}(\delta)i$ den verketteten Fluss und $R$ den elektrischen Widerstand der Spule des Elektromagneten bezeichnen.
- ![img](../assets/test.jpg)  
  Abbildung 1.1.: Prinzipskizze der eindimensionalen Magnetlagerung und magnetisches Ersatzschaltbild.
- Für die Induktivität gilt  
  
  $$
  L_{G}(\delta)=\frac{N^{2}}{\mathcal{R}_{G}(\delta)},
  $$  
  
  wobei $\mathcal{R}_{G}(\delta)$ die Ersatzreluktanz des Magnetkreises gemäß Abbildung 1.1(b) bezeichnet. Für die Magnetkraft gilt  
  
  $$
  f_{m}=\frac{1}{2}\frac{\partial L_{G}(\delta)}{\partial\delta}i^{2}.
  $$
- Das Gesamtmodell der magnetischen Lagerung lautet mit dem Strom $i$ als Ausgangsgröße  
  
  $$
  \begin{array}{l}{{\displaystyle\left[\dot{\hat{\psi}}\right]}}\\ {{\displaystyle\left[\dot{\hat{\delta}}\right]=\dot{\bf x}={\bf f}({\bf x},{\bf u})=\left(\begin{array}{c}{{\displaystyle-\frac{R(p_{1}+p_{2}\delta)}{N^{2}}\psi+v}}\\ {{w}}\\ {{\displaystyle-\frac{1}{2}\frac{p_{2}}{N^{2}m}\psi^{2}+g+\frac{f_{l}}{m}}}\end{array}\right)}}\\ {{\displaystyle\qquad y=h({\bf x},{\bf u})=\frac{\psi}{L_{G}(\delta)}=\frac{p_{1}+p_{2}\delta}{N^{2}}\psi.}}\end{array}
  $$
	- a) Bestimmen Sie die Ruhelage(n) des Systems für konstante Eingangsgrößen $\mathbf{u}_{R}=\left[v_{R}\quad f_{l,R}\right]^{\mathrm{T}}$ .  
	  
	  Im Weiteren wird angenommen, $\delta_{R}\,=\,\delta$ sei eine gewünschte Ruhelage des Systems für $f_{l,R}=0$ . Bestimmen Sie $v_{R}$ so, dass $\delta_{R}=\,\overline{{\delta}}$ eine Ruhelage des Systems darstellt.
	- b) Linearisieren Sie das nichtlineare Zustandsmodell um eine allgemeine Ruhelage $(\mathbf{x}_{R},\mathbf{u}_{R})$ und geben Sie es in der Zustandsraumdarstellung  
	  
	  $$
	  \begin{array}{r}{\Delta\dot{\mathbf{x}}=\mathbf{A}\Delta\mathbf{x}+\mathbf{B}\Delta\mathbf{u}}\\ {\Delta y=\mathbf{c}^{\mathrm{T}}\Delta\mathbf{x}+\mathbf{D}\Delta\mathbf{u}}\end{array}
	  $$  
	  
	  an.
- Aufgabe 1.2 (Ruhelagen und Linearisierung). Im Folgendem soll die Berechnung der Ruhelagen und die Linearisierung für verschiedene Systemklassen behandelt werden.
	- a) Das mathematische Modell einer Kugel (Radius $R>0$ , Masse $m>0$ ), die in einer Flüssigkeit mit dem spezifischen Gewicht $\rho$ schwimmt (siehe Abbildung 1.2) ist durch  
	  
	  $$
	  \begin{array}{r l}&{\mathbf{f}(\mathbf{x},u)=\left[g-\displaystyle\frac{F}{m}-\frac{\rho g\pi h^{2}}{3m}(3R-h)\right]}\\ &{h(\mathbf{x},u)=h}\end{array}
	  $$  
	  
	  gegeben. Dabei bezeichnet ${\bf x}=\left[h\:\:\:\:w\right]^{\mathrm{T}}$ den Zustand, $u=F$ den Eingang und $y=h$ den Ausgang sowie $g$ die Gravitationskonstante.  
	  
	  ![](images/c6fdf98b373f065b821347887bfbfbf861a21f2aef213ad894b9e0c86f772bc9.jpg)  
	  Abbildung 1.2.: Schwimmende Kugel.  
	  
	  Bestimmen Sie jenen Wert der Kraft $F_{R}$ , bei dem die Eintauchtiefe der Kugel in der Ruhe hR = R3 beträgt und bringen Sie das mathematische Modell durch Linearisierung um diese Ruhelage in die Form (1.5).
	- b) Gegeben ist das elektrische System nach Abbildung 1.3. Die darin verwendete Induktivität ist eine Funktion des Stroms $L=L(i_{L})$ und die Kapazität ist von der Spannung $u_{C}$ abhängig, d. h. $C=C(u_{C})$ . Der Operationsverstärker wird ideal angenommen und ein unbelasteter Ausgang $u_{C}$ vorausgesetzt, d. h. es fließt kein Strom aus den Klemmen.  
	  
	  ![](images/43ad0f05b70f91c012af0fb51ebf00f78de8769e23b5026c4c7f84905128721e.jpg)  
	  Abbildung 1.3.: Elektrisches Netzwerk.  
	  
	  Das mathematische Modell ergibt sich mit dem Zustand $\mathbf{x}=\left[u_{C}\quad i_{L}\right]^{\mathrm{T}}$ zu  
	  
	  $$
	  \begin{array}{r l}&{\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},\mathbf{u})=\left[\begin{array}{l}{\displaystyle\frac{\left(2u_{1}-u_{C}-u_{s}-2R_{1}i_{L}\right)}{\left(C(u_{C})+u_{C}\frac{\mathrm{d}(C(u_{C}))}{\mathrm{d}u_{C}}\right)R_{3}}}\\ {\displaystyle\frac{u_{1}-R_{1}i_{L}}{L(i_{L})+i_{L}\frac{\mathrm{d}(L(i_{L}))}{\mathrm{d}i_{L}}}}\end{array}\right]}\\ &{y=h(\mathbf{x},\mathbf{u})=u_{C}.}\end{array}
	  $$  
	  
	  Im Folgenden gilt  
	  
	  $$
	  \begin{array}{l}{{\displaystyle{\cal L}(i_{L})={\cal L}_{0}+{\cal L}_{1}i_{L}^{2}}}\\ {{\displaystyle C(u_{C})=C_{0}+C_{1}\left(1-e^{-\displaystyle\frac{u_{C}}{u_{C0}}}\right)}}\end{array}
	  $$  
	  
	  mit den konstanten, positiven Parametern $L_{0}$ , $L_{1}$ , $C_{0}$ , $C_{1}$ und $u_{C0}$ . Berechnen Sie alle Ruhelagen des Systems für $u_{s}=0$ und $u_{1}=\mathrm{konst}$ .
- Aufgabe 1.3 (Linearität und Zeitinvarianz). Überprüfen Sie die folgenden dynamischen Systeme auf Linearität bzw. Zeitinvarianz.
- a)  
  
  $$
  5\ddot{y}-\frac{1}{10}\dot{y}y=7.5t u
  $$
- b)  
  
  $$
  \frac{1}{2}y^{(3)}-10\ddot{y}-\frac{y}{1+t}=\int_{0}^{t}\sqrt{2}u(\tau)\mathrm{d}\tau+\frac{1}{3}\dot{u}
  $$
- c)  
  
  $$
  \cos\left({\frac{4}{5}}\pi\right){\ddot{y}}+3y={\frac{7}{10}}u
  $$