
from dtools.starter1 import *
import tools.lite_grid as lgrid
reload(lgrid)

frame = 57
base = "/anvil/scratch/x-ux454321/p83_turbulence/Enzo/p83e_a04_Ms4.7_Ma1.5_1024"
base = "/anvil/scratch/x-ux454321/p83_turbulence/Enzo/p83e_a03_Ms4.7_Ma1.5_512"
base = "/anvil/scratch/x-ux454321/p83_turbulence/Enzo/p83e_b03_Ms4.7_Ma3_512"
hierarchy = '%s/DD%04d/data%04d.hierarchy'%(base,frame,frame)
field = 'Density'

this_h = lgrid.fake_hierarchy(base,frame)
this_h.parse()
lgrid.proj(this_h,512,'Density',0,'%s/b03_n%04d_proj_Density'%(plot_dir,frame))
