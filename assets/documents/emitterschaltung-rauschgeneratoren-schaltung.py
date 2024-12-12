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

factor = 0.7

with schemdraw.Drawing(show=True) as d:
    d.config(unit=2.5)
    Us = celm.SourceV().up()
    elm.CurrentLabel(reverse=True).at(Us).label(r"$\bar{v}^2_s$")
    Rs = elm.Resistor().right(d.unit*factor).label(r"$R_s$")
    Rb = elm.Resistor().right(d.unit*factor).label(r"$R_b$")
    Ub = celm.SourceV().right(d.unit*factor).label(r"$\bar{v}^2_b$")
    Ib = celm.SourceI().down().label(r"$\bar{i}^2_b$").hold()
    elm.Line().right(d.unit*factor)
    Rpi= elm.Resistor().down().label(r"$r_\pi$").hold()
    elm.Line().right(d.unit*factor)
    Cpi = elm.Capacitor().down().label(r"$+$",loc="right").label(r"$-$",loc="left").label(r"$c_\pi$")
    elm.CurrentLabel().at(Cpi).label(r"$v_1$")
    
    elm.Line().right()
    
    I1 = celm.SourceI().up()
    elm.CurrentLabelInline(direction="out").at(I1).label(r"$g_m v_1$", loc="bottom")
    elm.Line().right(d.unit*factor)
    Ro = elm.Resistor().down().label(r"$r_o$").hold()
    elm.Line().right(d.unit*factor)
    Ic = celm.SourceI().down().label(r"$\bar{i}^2_c$").hold()
    elm.Line().right(d.unit*factor)
    Ro = elm.Resistor().down().label(r"$R_L$").hold()
    elm.Line().right(d.unit*factor)
    Il = celm.SourceI().down().label(r"$\bar{i}^2_L$").hold()
    elm.Line().right(d.unit*factor)
    Rl = elm.Resistor().down().label(r"$r_c$")
    
    elm.Line().to(Us.start)    
    
saveSchemdraw.saveSchematic(d, __file__)