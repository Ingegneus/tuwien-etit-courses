import schemdraw
import schemdraw.elements as elm
from schemdraw.segments import *

class SourceV(elm.Source):
    ''' EU Voltage source '''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.segments.append(Segment([(0, 0), 
                                      (1, 0)]))    # line through
        
class SourceI(elm.Source):
    ''' EU Current source '''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.segments.append(Segment([(0.5, -0.5), 
                                      (0.5, 0.5)]))    # line cross