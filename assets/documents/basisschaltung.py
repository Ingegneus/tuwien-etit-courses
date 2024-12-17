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
elm.CurrentLabel.defaults['headwidth'] = 0.2
elm.Arrow.defaults['arrowwidth'] = 0.2
elm.style(elm.STYLE_IEC)

hScale = 0.7
vScale = 0.3

with schemdraw.Drawing(show=True) as d:
    d.config(unit=2)
    
    Tr = elm.BjtNpn().up().flip()
    Rbv = elm.Resistor().at(Tr.base).down().label(r"$R_{BV}$")
    Gr = elm.Vss()
    
    elm.Line().at(Tr.emitter).left().dot(open=True)
    Ue = elm.Gap().toy(Gr.start.y).dot(open=True)
    elm.CurrentLabel(top=False).at(Ue).label(r"$U_e$")
    elm.Vss()
    
    Wo = elm.Line().at(Tr.collector).right().dot(open=True)
    Ua = elm.Gap().toy(Gr.start.y).dot(open=True)
    elm.CurrentLabel(top=False).at(Ua).label(r"$U_a$")
    elm.Vss()
    
    Rc= elm.Resistor().at(Wo.center).up().idot().label(r"$R_C$")
    elm.Arrow().up(length=d.unit*0.1).label(r"$U_b$")
      
saveSchemdraw.saveSchematic(d, __file__)