#===============================================
#RESOLUTION KEYWORDS
#===============================================
oref = 0 #over refine factor - should typically be set to 0
n_ref = 64 #when n_particles > n_ref, octree refines further
zoom = True #False = use the entire grid; True = zoom in on the highest density peak
zoom_box_len = 200 #kpc; so the box will be +/- zoom_box_len from the center
bbox_lim = 1.e5 #kpc - this is the initial bounding box of the grid (+/- bbox_lim)
               #This *must* encompass all of the particles in the
               #simulation. if zoom is set, this is obviated; else, is
               #the simulated boxsize.

#===============================================
#PARALLELIZATION
#===============================================

n_processes = 3 #number of MPI processes to run


#===============================================
#RT INFORMATION
#===============================================
n_photons_initial = 1.e7
n_photons_imaging = 1.e7
n_photons_raytracing_sources = 1.e7
n_photons_raytracing_dust = 1.e7


#===============================================
#DUST INFORMATION
#===============================================
dustdir = '/Users/desika/hyperion-dust-0.1.0/dust_files/' #location of your dust files
dustfile = 'd03_3.1_6.0_A.hdf5'
PAH = True
dusttometals_ratio = 0.4
enforce_energy_range = False #False is the default;  ensures energy conservation


#===============================================
#HYDRO CODE UNITS
#===============================================
unit_mass = 1.e10 #msun/h
unit_length = 1. #kpc/h
unit_age = 1. #Gyr
unit_velocity = 1.e5 #cm/s

#===============================================
#STELLAR SEDS INFO
#===============================================
FORCE_BINNING = True #force SED binning
COSMOFLAG = False  #is this a cosmological simulation?

imf_type = 2 #FSPS imf types; 0 = salpeter, 1 = chabrier; 2 = kroupa; 3 and 4 (vandokkum/dave) not currently supported
pagb = 1 #weight given to post agb stars# 1 is the default



CF_on = False #if set to true, then we enable the Charlot & Fall birthcloud models 
birth_cloud_clearing_age = 0.01 #Gyr - stars with age <
                                #birth_cloud_clearing_age have
                                #charlot&fall birthclouds meaningless
                                #of CF_on  == False

Z_init = 0.02 #force a metallicity increase in the newstar particles.
           #This is useful for idealized galaxies.  The units for this
           #are absolute (so enter 0.02 for solar).  Setting to 0
           #means you use the stellar metallicities as they come in
           #the simulation (more likely appropriate for cosmological
           #runs)

#Idealized Galaxy SED Parameters
disk_stars_age = 8 #Gyr ;meaningless if COSMOFLAG = True; note, if this is <= 7, then these will live in birth clouds
bulge_stars_age = 8 #Gyr ; meaningless if COSMOFLAG = True; note, if this is <= 7, then these will live in birth clouds
disk_stars_metals = 19 #in fsps metallicity units
bulge_stars_metals = 19 #in fsps metallicity units



#bins for binning the stellar ages and metallicities for SED
#assignments in cases of many (where many ==
#>N_METALLICITY_BINS*N_STELLAR_AGE_BINS) stars; this is necessary for
#reduction of memory load; see manual for details.

N_STELLAR_AGE_BINS = 100
N_MASS_BINS = 100  


metallicity_legend= "/Users/desika/fsps/ISOCHRONES/Padova/Padova2007/zlegend_basel.dat"



#===============================================
#IMAGES AND SED
#===============================================

NTHETA = 10


#===============================================
#GRID INFORMATION  
#===============================================
MANUAL_CENTERING = True


#===============================================
#DEBUGGING
#===============================================

SOURCES_IN_CENTER = False
STELLAR_SED_WRITE = True
SUPER_SIMPLE_SED = False #just generate 1 oct of 100 pc on a side,
                         #centered on [0,0,0].  sources are added at
                         #random positions.
SKIP_GRID_READIN = False

CONSTANT_DUST_GRID = False #if set, then we don't create a dust grid by
                          #smoothing, but rather just make it the same
                          #size as the octree with a constant value of
                          #4e-20