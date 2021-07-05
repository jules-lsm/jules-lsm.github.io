JULES version 5.2 Release Notes
===============================


The JULES vn5.2 release consists of approximately 52 tickets from 25 authors, including work by many other people.

Full details of the tickets committed for JULES vn5.2 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v5.2+release>`_.

Ticket numbers are indicated below, e.g. #754.

Science changes
---------------

 *  Introduced option for vegetation canopy drag with optional correction for the roughness sublayer - see :nml:mem:`JULES_VEGETATION::l_vegdrag_pft` and :nml:mem:`JULES_VEGETATION::l_rsl_scalar`. (#754)
 *  Soil decomposition added to the code for the ECOSSE soil model (which is not yet ready for use). (#570)
 *  Extension of the screen temperature decoupling diagnostics to screen humidity - only recommended for runs with the UM (atmospheric model). (#508)
 *  Added a new option to the sea albedo calculation to simulate the effect of freezing (sea-ice) below 271 K. (#770)

General/Technical changes
-------------------------

 *  Enabled support for new routines to calculate qsat (the saturated water mixing ratio) which are now the default for standalone JULES. (#685)
 *  Improved interface checking in the surface, fire, FLake and river routing routines. (#678, 728, 729)
 *  The clay ancillary variable can now have multiple layers (note these are the soil biogeochemistry layers, not soil moisture layers). Users should note that an existing run with :nml:mem:`JULES_SOIL_BIOGEOCHEM::l_layeredc` = T that tries to read a single-layered clay variable from a file with :nml:mem:`JULES_SOIL_PROPS::const_z` = F will no longer work; a multi-layered clay field must be provided in this case. All other configurations can be updated. (#687)
 *  Added further IMPLICIT NONE statements and fixed subroutine interface issues. (#737)
 *  Minor modifications to IMOGEN (#430).
 *  Removed the l_flux_bc switch from the UM-coupling argument list and standalone code. (#775)
 *  Improved use of coupled model diagnostic code in standalone runs. (#740)
 *  Diagnostics from INFERNO (interactive fire model) made available to the UM. (#552)
 *  JULES parameters included in the Random Parameter (RP) scheme (for UM runs). (#675)
 *  Rationalised some of the code for the reading and writing of dumps. (#763)
 *  Alignment of JULES and UM urban control and initialisation code. (#319)
 *  Reduced model overhead when running DrHook profiling. (#782)    
 *  Fixed oddities found while investigating the use of CamFort. (#769)
 *  JULES source code fully compliant with the Fortran 2003 standard. (#711)
 *  Corrections to code comments and other minor changes. (#725, 690)
 *  Clarified units of variables in the vegetation code. (#741)
 *  Enable the reading of PFT and soil parameters for CABLE runs via the JULES_PFTPARM_CABLE and JULES_NVEGPARM_CABLE namelists. (#694, 748)
 *  Minor edits to ensure future compatibility of .inc files with the umdp3_fixer used in Rose stem tests. (#762)

Changes to testing
------------------

 *  Rose stem testing working on JASMIN. (#744)
 *  Improved the output of the umdp3 checker task in rose stem. (#764)
 *  Rose stem testing added for IMOGEN and GL7 and GL8 configurations. (#706, 648, 773)
 *  Added an OMP vs no-OMP Rose stem test for the ukv config to the MO XC40 and virtual machine platforms. (#732)
 *  Allowed the option of setting JULES_REMOTE and JULES_REMOTE_HOST when running on the Met Office Cray (meto-xc40-cce). (#755)
 *  Resolved oversubscription problems and rationalised the meto-linux rose stem. (#783)

Bugs fixed
----------

 *  Fix to ensure TRIFFID competition does not try to access non-existent surface types. (#647)
 *  Fixed array/scalar mismatch in arguments to vegcarb. (#682)
 *  Corrected the dimensions given to the frac_prev array in `lotka_eq_jls.F90` (for runs with :nml:mem:`JULES_VEGETATION::l_trif_eq` = T and :nml:mem:`JULES_VEGETATION::l_ht_compete` = T). (#765)
 *  Fix to prevent floating point errors with CABLE. (#694)
 *  Use NINT to guard against imprecision in REAL/INTEGER conversion in routing code. (#726)
 *  Fixed bugs relating to windspeed-dependent unloading of snow from vegetation (UM only) and allowing soil rate modifier diagnostics in standalone runs. (#740)
 *  Correction related to indexing of snow fields in reconfiguration (UM only). (#676)
 *  Fixed certain snow diagnostics (UM stash fields 8,578 to 8,583). (#720)
 *  Correction to logic for canopy parameter updating (UM only). (#746)
 *  Example namelists updated for vn5.1. (#722)
 *  Fix of host specification in `runtime.rc` for site cehwl1. (#731)
 *  Updated the configuration for University of Exeter (`uoe-linux-gfortran.cfg`). (#735)
 *  Fix so rose stem IMOGEN tests work at NCI. (#792)
    
Documentation updates
---------------------
 *  Removed the science configurations section from the documentation. (#736).
 *  Updated the documentation (mainly release notes and hydrological terminology). (#738, 745)
 *  Updated documentation of fcm-make JULES_PLATFORM environment variable. (#739)
 *  Updated hyperlinks to Rose and FCM in the documentation. (#786)

Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.
