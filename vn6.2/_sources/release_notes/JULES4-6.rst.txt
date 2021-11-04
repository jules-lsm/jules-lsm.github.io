JULES version 4.6 Release Notes
===============================


The JULES vn4.6 release consists of 43 tickets from 22 authors across 52 commits.

Full details of the tickets committed for JULES vn4.6 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v4.6+release>`_.

Science changes
---------------

 * Multiple ice tiles in a gridbox to simulate snowpacks at different elevations - see :nml:mem:`JULES_SURFACE::l_elev_land_ice`
 * Modifications to snowpack physics to better represent deep, compact firn/snow on ice sheets - description at :nml:mem:`JULES_SURFACE::l_elev_land_ice`
 * Option to link whole-plant maintenance respiration to soil moisture stress - see :nml:mem:`JULES_VEGETATION::l_scale_resp_pm`
 * Read clay content of soil for soil carbon decomposition model from ancillary file - see :nml:lst:`JULES_SOIL_PROPS`
 * Improved climate downscaling physics for ice elevation tiles
 * Calculate FAO Penman-Monteith evapotranspiration for reference crop - see diagnostic fao_et0
 * Diagnostic form drag for sea ice (UM only)
 * Calculation of new sea ice variables required for CMIP6
 * Implement a canopy clumping factor - see :nml:mem:`JULES_PFTPARM::can_struct_a_io`
 * Allow for non-istropic scattering in plant canopies - see :nml:mem:`JULES_RADIATION::l_niso_direct`
 * Increased flexibility to represent soil moisture stress on vegetation - see :nml:mem:`JULES_PFTPARM::fsmc_mod_io` and :nml:mem:`JULES_PFTPARM::fsmc_p0_io`
 * Improved parameterisation of crop leaf senescence
 * New crop harvest diagnostics
 * Lake model FLake beneath multi-layer snow (UM only)

Technical changes
-----------------

 * JULES-C-1p1 Regression Tests
 * Remove the UM_FLAKE CPP macro
 * Move sorp and n_inorg_turnover to namelist to enable user input.
 * VM rose stem bug fixed.
 * Add support for rose-stem on MONSooN
 * Move some of the hard-wired crop parameters to :nml:lst:`JULES_CROPPARM`
 * Remove UM descent.h include file and put values into JULES module descent.F90
 * Fix race conditions and improve OpenMP DEFAULTs
 * Modularise and header refactor science/snow

Bugs fixed
----------

 * Fixed GC3 tstar_sice bug
 * Corrected canopy nitrogen profiles - see :nml:mem:`JULES_VEGETATION::l_leaf_n_resp_fix`. This increases plant maintenance respiration.
 * Reduced stem respiration with trait-based physiology
 * Reinstated missing veg parms, for trait initialisation.
 * Soil respiration bug resolved
 * Corrected mistake in merging of crop PFT changes
 * Fixed N diagnostic to avoid runtime crashes
 * Fixed calculation of dust deposition exchange coefficient
 * Fixed wetland emission of methane with TRIFFID on
 * Fixed aerodynamic resistance diagnostic (UM diagnostic)

Documentation updates
---------------------
Coding standards, and documentation can be viewed on the 'github page <http://jules-lsm.github.io/>_'.

