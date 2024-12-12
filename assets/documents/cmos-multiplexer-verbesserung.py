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
    d.config(unit=2.5)
    Opv = elm.Opamp(leads=True)
    elm.Line().at(Opv.out).right(d.unit*hScale).dot(open=True)
    elm.Line().at(Opv.in2).down(d.unit*vScale)
    elm.Vss()
    elm.Line().at(Opv.in1).up(d.unit*vScale*2)
    elm.Switch().right(d.unit*hScale)
    Ro = elm.Resistor().right(d.unit*hScale).label(r"$R_2$")
    elm.Line().toy(Opv.out)
    
    OpvIn = elm.Line().at(Opv.in1).left(d.unit*hScale).dot()
    
    elm.Line().up(d.unit*vScale)
    S2 = elm.Switch().left(d.unit*hScale).reverse().flip()
    R2 = elm.Resistor().left(d.unit*hScale).dot(open=True).label(r"$R_1$")
    
    elm.Line().at(S2.start).up(d.unit*vScale*2)
    S1=elm.Switch().left(d.unit*hScale).reverse().flip()
    R1=elm.Resistor().left(d.unit*hScale).dot(open=True).label(r"$R_1$")
    
    elm.Line().at(OpvIn.end).down(d.unit*vScale)
    S3 = elm.Switch().left(d.unit*hScale).reverse().flip()
    R3 = elm.Resistor().left(d.unit*hScale).dot(open=True).label(r"$R_1$")
    
    elm.Line().at(S3.start).down(d.unit*vScale*2)
    S4=elm.Switch().left(d.unit*hScale).reverse().flip()
    R4=elm.Resistor().left(d.unit*hScale).dot(open=True).label(r"$R_1$")
    
      
saveSchemdraw.saveSchematic(d, __file__)