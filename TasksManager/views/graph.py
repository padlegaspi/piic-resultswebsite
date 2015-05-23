from matplotlib import pylab
from pylab import *

import PIL
import PIL.Image
import StringIO

from django.http import HttpResponse
from django.template import RequestContext, loader

def graph():
        x = [1,2,3,4,5,6]
        y = [5,2,6,8,2,7]
        plot(x,y, linewidth=2)

        xlabel('x axis')
        ylabel('y axis')
        title('sample graph')
        grid(True)
#       pylab.show()

        buffer = StringIO.StringIO()
        canvas = pylab.get_current_fig_manager().canvas
        canvas.draw()
        graphIMG = PIL.Image.fromstring("RGB",canvas.get_width_height(), canvas.tostring_rgb())
        graphIMG.save(buffer,"PNG")
        pylab.close()

        return HttpResponse(buffer.getvalue(), mimetpye="image/png")
