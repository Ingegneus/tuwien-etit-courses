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
    d.config(unit=2.5)
    Opv = elm.Opamp(leads=True).flip()
    Ued = elm.Gap().at(Opv.in2).to(Opv.in1)
    elm.CurrentLabel(top=False, length=d.unit*.3).at(Ued).label('$U_{ed}$')

    R2 = elm.Resistor().down().at(Opv.out).idot().dot().label('$R_2$')
    elm.CurrentLabelInline(direction='in').at(R2).label('$i$')
    R1 = elm.Resistor().down().dot().label('${R_1}$')
    Gr = elm.Vss()
    elm.Wire('-|').at(R2.end).to(Opv.in1)   
    
    elm.Line().left(d.unit*0.5).at(Opv.in2)
    Ue = celm.EUSourceV().down(d.unit*2).reverse().label('$U_e$')
    elm.CurrentLabel(top=False).at(Ue).reverse()
    elm.Wire('|-').to(R1.end)
    
    Out1 = elm.Line().at(R2.start).right(d.unit*0.5).dot(open=True)
    Out2 = elm.Line().at(R1.end).right(d.unit*0.5).dot(open=True)
    Ua = elm.Gap().at(Out1.end).to(Out2.end)
    elm.CurrentLabel(length=d.unit*1.5).at(Ua).label('$U_a$')

saveSchemdraw.saveSchematic(d, __file__)