#!/usr/bin/env python3
import pyten as ptn
import sys,os
pp=os.path.dirname(os.path.abspath(__file__))
pp = os.path.dirname(pp)
sys.path.append(pp)          #used this, be careful
from src import helpers, utils, DMRG 
print(pp)
par=helpers.params()

par.Lx = int(float(sys.argv[1]))
par.Ly = int(float(sys.argv[2]))   #number of sites along y-direction
par.Nphi = float(sys.argv[3])
par.U = float(sys.argv[4])
par.N = int(float(sys.argv[5]))
par.S = float(sys.argv[6])
par.pbc = bool(float(sys.argv[7]))
par.g = float(sys.argv[8])
par.x0 = int(float(sys.argv[9])); par.y0 = int(float(sys.argv[10]))
par.chis = [100, 100, 200, 200, 400, 400, 400, 800, 800, 800, 800, 1600, 1600, 1600, 2000, 2000, 2000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 6000, 6000, 6000, 6000, 6000, 6000]
lat=DMRG.FHH_Ham_SU2(par.Ly, par.Lx, par.Nphi, 1.0, par.pbc)  
par.lat = DMRG.add_pin_SU2(lat, par.g, par.x0, par.y0, par)
par.pin = True

#tar_loc = "/project/th-scratch/m/Mert.Kurttutan/QH-FM-01/Lx" + str(par.Lx) + "_Ly" + str(par.Ly) + "/"
#tar_loc = "/project/th-scratch/m/Mert.Kurttutan/QH-FM-02/Lx" + str(par.Lx) + "_Ly" + str(par.Ly) + "/"
tar_loc = "/project/th-scratch/m/Mert.Kurttutan/QH-FM-03/Lx" + str(par.Lx) + "_Ly" + str(par.Ly) + "/"
#tar_loc="../temp/"
#tar_loc= pp+"/temp_trial/"

if __name__ == "__main__":            #make sure it runs only when it is executed
    DMRG.run_dmrg_FHH_SU2_conv2(par, tar_loc, tar_loc, True)
    
