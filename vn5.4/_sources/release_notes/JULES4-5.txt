JULES version 4.5 Release Notes
===============================


The JULES vn4.5 release consists of 31 tickets from 19 authors across 35 commits.

Full details of the tickets committed for JULES vn4.5 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v4.5+release>`_.

Science changes
---------------

 * UKCA dry deposition working with 13 surface tiles
 * Check litter flux carbon balance
 * Allow litter carbon fluxes from variable numbers of PFTs
 * Improved seasonal cycle of soil respiration: switch l_soil_resp_lev2 alters how soil temperature and moisture are used for respiration calculation.
 * Added parameters to trait physiology for nitrogen in wood and roots - see :nml:mem:`JULES_PFTPARM::nr_io`, :nml:mem:`JULES_PFTPARM::nsw_io` and :nml:mem:`JULES_PFTPARM::hw_sw_io`.
 * INFERNO model of fire emissions and burnt area - see :nml:mem:`JULES_VEGETATION::l_inferno`
 * Option to represent crops using triffid - see :nml:mem:`JULES_VEGETATION::l_trif_crop`
 * Remove MORUSES hard-wired roof coupling
 * Add diagnostic for canopy FAPAR (Fraction of Absorbed Photosynthetically Active Radiation).
 * JULES-CN: enabled nitrogen limitation of NPP - see :nml:mem:`JULES_VEGETATION::l_nitrogen`
 * Added the FLake lake model into JULES (for UM use)

Technical changes
-----------------

 * Variable renaming to support soil tiling
 * Add JASMIN as a supported system for rose-stem jobs
 * Fix Cray compiler warnings
 * Protect print statements from the TRIP river routing code with PrintStatus

Bugs fixed
----------

 * Fix ozone diagnostics in JULES

Documentation updates
---------------------
Coding standards, and documentation can be viewed on the 'github page <http://jules-lsm.github.io/>_'.

 * Update to coding standards to reflect and protect variable name changes
 * Represent crops using TRIFFID
 * JULES-CN
 * Nitrogen trait physiology
 * Check litter C flux carbon balance
 * kgC and kgN in netCDF units metadata
 * adding nfita to hydrology namelist
 * add FAPAR diagnostic
