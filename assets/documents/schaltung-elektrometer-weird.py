###### set Computer Modern as font ######
import matplotlib
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['mathtext.fontset'] = 'cm'
import schemdraw
import schemdraw.elements as elm

###### custom elements import ######
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
custom_code_path = os.path.abspath(os.path.join(current_dir, '..', 'storages'))
sys.path.append(custom_code_path)
from customPyCode import *
from customPyCode import customSchemdrawElements as celm

###### style settings ######
schemdraw.config(lblofst=0.2, bgcolor='white', lw=1.5)
elm.CurrentLabelInline.defaults['headwidth'] = 0.2
elm.style(elm.STYLE_IEC)

with schemdraw.Drawing(background='white', show=False) as d:
    d.config(unit=2)
    Opv = elm.Opamp(leads=True,).flip()
    elm.Line().at(Opv.in2).up()
    R1 = elm.Resistor().left().label(r"$R_1$")
    elm.Vss()
    R2 = elm.Resistor().at(R1.start).right().label(r"$R_2$")
    elm.Wire('-|').to(Opv.out)
    Out = elm.Line().right(d.unit*0.5).dot(open=True).label(r"$u_a(t)$", loc="right")
    Ue = celm.EUSourceV().at(Opv.in1).down().label(r"$u_e(t)$")
    elm.Vss()
    
    elm.Arrow().at(Opv.vs).up(d.unit*.3).label(r'$10\mathrm{V}$', loc='bottom')
    elm.Arrow().at(Opv.vd).down(d.unit*.3).label(r'$-10\mathrm{V}$', loc='bottom')

saveSchemdraw.saveSchematic(d, __file__)