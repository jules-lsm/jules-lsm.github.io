JULES version 5.3 Release Notes
===============================


The JULES vn5.3 release consists of approximately 27 tickets from 17 authors, including work by many other people.

Full details of the tickets committed for JULES vn5.3 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v5.3+release>`_.

Ticket numbers are indicated below, e.g. #742.

Science changes
---------------

 *  Improved initialisation of the surface exchange iteration (:nml:mem:`JULES_SURFACE::cor_mo_iter` = 4). (#742)
 *  Removed canopy radiation options (:nml:mem:`JULES_VEGETATION::can_rad_mod`) 2 and 3. (#791)
 *  Added nitrification, denitrification and leaching to the ECOSSE soil model (which is not yet ready for use). (#781)
 *  Allowed the use of a variable Charnock parameter, provided by a wave model via coupling, instead of a constant value, in runs of the UM (atmosphere-ocean model). See iseasurfalg = 4 or 5 in the jules_sea_seaice namelist. (#797)

General/Technical changes
-------------------------

 *  Coupling of river outflow from river grid to NEMO (ocean) grid via a 1D array. (#624)
 *  Added PBL gustiness parameter to namelist (:nml:mem:`JULES_SURFACE::beta_cnv_bl`). (#742)
 *  Changes required to run the INFERNO fire model interactively in the UM. (#800)
 *  Initial modifications to allow irrigation code to be used in the UM. (#809)
 *  Optimised aspects of the canopy drag scheme. (#795)
 *  Resolved issues identified by OpenMP-related compiler warnings. (#712)
 *  Improved OpenMP coverage. (#723, 815)
 *  Improved performance in UM global ensemble configuration. (#820)
 *  Removed unused code from the surface scheme in standalone JULES. (#753)
 *  Removed idfefs from some of the surf_couple routine argument lists. (#830)
 *  Introduced a framework to move to shared metadata between UM and standalone for ease of converting to and from UM and standalone apps, to assist with configuration management. This introduces the new namelist :nml:lst:`JULES_MODEL_ENVIRONMENT`. (#633)
 *  Ported to NIWA's XC50 platform. (#814)
 *  The meto-linux fcm-make configs have been converted to RHEL7. All Linux rose-stem tasks will run on RHEL7 SPICE nodes. Those using a meto-linux-intel-mpi build outside of rose-stem will need to set `ROSE_LAUNCHER_LIST = mpiexec.hydra` or make an equivalent change to their personal `rose.conf` file, and include the full path to the required MPI-enabled compiler. Refer to the `runtime-linux-intel.rc` file in rose-stem for details. (#835)
 *  Corrected bug in the make_jules_release script. (#796)
 *  Miscellaneous administrative changes. (#807, 839)

Bugs fixed
----------

 *  Corrected a bug in the scalar roughness length diagnostic over sea when using anything other than a fixed roughness length, i.e. anything other than iseasurfalg=0. (#794)
 *  Fixed calls to mask compression routines in UM-only code. (#826)

Changes to testing
------------------

 *  A test of the canopy drag scheme, loobos_vegdrag, based on loobos_gl8 has been added to rose-stem. (#795)
 *  Updated `umdp3_fixer.py` to run on \*.inc files, and included these in the rose stem test. (#776)
 *  Implemented code to align continuation ampersands in column 79 as part of `umdp3_fixer.py`. (#823)
 *  The Met Office rose stem suite now runs all Linux tasks on SPICE, and the metadata checker task is now included in the JASMIN rose stem suite. (#819)
 *  Correction for rose stem on MONSooN. (#852)
    
Documentation updates
---------------------

 *  Updates associated with many of the above changes, and release notes. (#836)

Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.
