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

factor=0.7

with schemdraw.Drawing(show=True) as d:
    d.config(unit=2.5)
    Vs = celm.SourceV().right(d.unit*factor).label(r"$\bar{v}^2_b$")
    Rb = elm.Resistor().down().label(r"$r_\pi$")
    elm.Line().left(d.unit*factor).dot()
    elm.Line().up().dot().label(r"$E$", loc="left").label(r"$B$", loc="right")
    
    elm.Line().at(Vs.end).right(d.unit*factor)
    C = elm.Capacitor().down().label(r"$C_\pi$").label(r"$+$", loc="right").label(r"$-$", loc="left")
    elm.CurrentLabel().at(C).label(r"$v_1$")
    elm.Line().left(d.unit*factor)
    
    elm.Line().at(C.end).right(d.unit*factor)
    
    Is = celm.SourceI().up()
    elm.CurrentLabelInline('out').at(Is).label(r"$g_m v_1$")
    
    elm.Line().right(d.unit*factor)
    Ro = elm.Resistor().down().label(r"$r_o$").hold()
    elm.Line().right(d.unit*factor).dot()
    Ic = celm.SourceI().down().label(r"$\bar{i}^2_c$").label(r"$C$", loc="right").hold()
    
    elm.Line().right(d.unit*factor)
    elm.CurrentLabelInline().label(r"$i_o$")
    elm.Line().down()
    elm.Line().left(d.unit*factor)
    elm.Line().left(d.unit*factor)
    elm.Line().left(d.unit*factor)
    
saveSchemdraw.saveSchematic(d, __file__)