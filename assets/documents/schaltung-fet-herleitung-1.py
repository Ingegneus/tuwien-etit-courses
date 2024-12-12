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
    elm.Line().left(d.unit*factor).dot().label(r"$S$",loc="left")
    elm.Line().up().dot()
    elm.Line().right(d.unit*factor).label(r"$G$",loc="left")
    
    Cgs = elm.Capacitor().down().label(r"$+$",loc="left").label(r"$-$",loc="right")
    elm.CurrentLabel().at(Cgs).label(r"$v_{gs}$")
    
    elm.Line().right(d.unit*factor)
    Is = celm.SourceI().up()
    elm.CurrentLabelInline('out').at(Is).label(r"$g_m v_1$")
    elm.Line().right(d.unit*factor)
    Rd = elm.Resistor().down().label(r"$r_d$").hold()
    elm.Line().right(d.unit*factor).dot()
    Id = celm.SourceI().down().label(r"$\bar{i}^2_d$").hold()
    
    elm.Line().right(d.unit*factor)
    elm.CurrentLabelInline().label(r"$i_o$")   
    elm.Line().down()
    elm.Line().to(Is.start)
    
saveSchemdraw.saveSchematic(d, __file__)