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

with schemdraw.Drawing(show=True) as d:
    d.config(unit=2.5)
    elm.Vss()
    Ue = celm.SourceV().up()
    elm.CurrentLabel().at(Ue).label(r"$u_e$")
    Rs = elm.Resistor().right().label(r"$R_s$")
    Tr = elm.Bjt().label(r"$T$")
    elm.Line().at(Tr.emitter).down().toy(Ue.start)
    elm.Vss()
    
    Ua = elm.Line().at(Tr.collector).right().dot(open=True).label(r"$u_a$",loc="right")
    Rl = elm.Resistor().at(Tr.collector).up().label(r"$R_L$")
    elm.Arrow().up(d.unit*0.1).label(r"$+$",loc="right")
    
saveSchemdraw.saveSchematic(d, __file__)