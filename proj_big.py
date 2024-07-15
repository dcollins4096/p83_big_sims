
from dtools.starter1 import *
import tools.lite_grid as lgrid
reload(lgrid)

frame = 14
hierarchy = '/scratch1/00369/tg456484/Paper83/Enzo/p83e_a05_Ms4.7_Ma1.5_2048/DD%04d/data%04d.hierarchy'%(frame,frame)
field = 'Density'

this_h = lgrid.lg(hierarchy)
this_h.parse()
