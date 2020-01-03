###
#       The code makes scatter plots of seasonal El Nino/La Nina
#       composite anomalies of selected variables and selected models.
#       It requires pre-processed data from the COMPOSITE module for
#       all selected models and variables.
#
#       Contact Information:
#       PI :  Dr. H. Annamalai,
#             International Pacific Research Center,
#             University of Hawaii at Manoa
#             E-mail: hanna@hawaii.edu
#
#       programming :  Jan Hafner,  jhafner@hawaii.edu
#
#    This package is distributed under the LGPLv3 license (see LICENSE.txt)


import numpy as np
import sys
import math
import subprocess
import commands
import time

import os

import datetime

from generate_ncl_plots import generate_ncl_plots
from get_ncl_data import get_ncl_data

'''
       This package is distributed under the LGPLv3 license (see LICENSE.txt)

        input data are as follows:
 
      2-dimensional variables  (fluxes)
     vertical integrals

      PR -precip. kg/m2/sec
         moisture advection  W/m2
         net radiative flux  W/m2
         vertical MSE advection W/m2
         total heat flux (LHF + SHF) W/m2

     Additionally needed on input :
      LON - longitudes [deg.]
      LAT - latitudes [deg.]
      PLEV - pressure levels [mb]

     missing values are flagged by UNDEF which is a large number

'''

now = datetime.datetime.now()
print("===============================================================")
print("      Start of Scatter Plot Module calculations " +  now.strftime("%Y-%m-%d %H:%M"))
print("===============================================================")

undef = float(99999999999.)
undef2 = float(1.1e+20)

###  first prefix for data   + other variables passed to the code 
wkdir =  os.environ["POD_WK_DIR"]

####    reading in the data for scatter plots   from ~/inputdata/obs_data/ENSO_MSE/SCATTER

time.sleep(6.)

###  make the plots  in NCL  
####     default domain plotting   
generate_ncl_plots(os.environ["POD_CODE_DIR"]+ "/SCATTER/NCL/scatter_01.ncl")
generate_ncl_plots(os.environ["POD_CODE_DIR"]+ "/SCATTER/NCL/scatter_02.ncl")
generate_ncl_plots(os.environ["POD_CODE_DIR"]+ "/SCATTER/NCL/scatter_03.ncl")
generate_ncl_plots(os.environ["POD_CODE_DIR"]+ "/SCATTER/NCL/scatter_04.ncl")

###    copy the html files for to create webpages
if os.path.isfile( os.environ["POD_WK_DIR"]+"/MDTF_SCATTER/SCATTER.html" ):
    os.system("rm -f "+os.environ["POD_WK_DIR"]+"/MDTF_SCATTER/SCATTER.html")

os.system("cp "+os.environ["POD_CODE_DIR"]+"/SCATTER/SCATTER.html "+os.environ["POD_WK_DIR"]+"/MDTF_SCATTER/." )
os.system("cp "+os.environ["POD_CODE_DIR"]+"/html/mdtf_diag_banner.png "+os.environ["POD_WK_DIR"]+"/MDTF_SCATTER/." )

###  the end 
now = datetime.datetime.now()
print"   " 
print " ==================================================================="
print "  Scatter  Module Finished    " + now.strftime("%Y-%m-%d %H:%M")
print "  resulting plots are located in : " +os.environ["POD_WK_DIR"],"/MDTF_SCATTER/"
print " ==================================================================="
### 