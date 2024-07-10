JULES version 5.7 Release Notes
===============================


The JULES vn5.7 release consists of approximately 34 tickets from 16 authors, including work by many other people.

Full details of the tickets committed for JULES vn5.7 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v5.7+(Feb-20)>`_.

Ticket numbers are indicated below, e.g. #548.

Science changes
---------------

 *  Soil tiling made available - see :nml:mem:`JULES_SOIL::l_tile_soil`. Each land gridbox can be modelled using a single soil column or with a separate soil column for each surface tile. (#548)
 *  Enabled the simulation of multiple crops in a growing season, and therefore crop rotations - see :nml:mem:`JULES_VEGETATION::l_croprotate`. (#821)
 *  Added thermal adaptation and acclimation of leaf-level photosynthesis - see :nml:mem:`JULES_VEGETATION::photo_acclim_model`. (#863)
 *  Remaining source/sink terms for inorganic nitrogen included with the ECOSSE soil model (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 3). (#788)


General/Technical changes
-------------------------

 *  New functionality added to allow for a new vegetation biogeochemical model. Introduced more extensive use of modules to control the read and write of variable states, and FORTRAN type objects to control data flows. This code is not yet suitable for general use. (#888)
 *  Technical work for the implementation of the Robust Ecosystem Demography (RED) dynamic vegetation model. (#902)
 *  Moved allocation statements into the modules that hold the variables (and out of the monolithic allocate_jules_arays.F90). (#978)
 *  Improved processing of the values read from namelist :nml:lst:`JULES_OVERBANK`. (#987)
 *  Added a KIND type to the declarations of REAL variables. (#958, 996, 997)
 *  Removed some redundant operations from the science code. (#1001)
 *  Removed redundant arguments for copydiag_3d (affects UM runs only). (#954)
 *  Added STASH code controls for a new scale-dependent gust diagnostic in the UM. (#984)
 *  Trivial change to USE statements relating to a UM change to atm_fields_mod. (#1003)
 *  Further work on CABLE front end, adding namelists :nml:lst:`CABLE_PROGS` and :nml:lst:`CABLE_SURFACE_TYPES`. (#940)
 *  Tidied to remove compiler warnings related to um_parvars (decomposition) and unused variables (NAG compiler), and to make JULES compliant with changes to UM debug compiler flags. (#963, 966, 1002)
 *  Added some missing platforms to the metadata for fcm-make (so those are available in rose edit). (#976)
 *  Fixed the make_jules_release script to push latest documentation onto the master on GitHub. (#957)
 *  The example namelists (difficult to maintain) and benchmarking suite (obselete) have been removed. (#928, 969)

    
Bugs fixed
----------

 *  Bug fixes for the RothC-based soil biogeochemistry model (:nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 2) with :nml:mem:`JULES_SOIL_BIOGEOCHEM::l_layeredc` = TRUE and :nml:mem:`JULES_VEGETATION::l_nitrogen` = TRUE. (#681)
 *  Prevented race condition in leaf_mod. (#1009)


Changes to testing
------------------

 *  Added NAG compiler to Met Office linux test suite. (#955)
 *  Fixed JULES rose stem build jobs on the VM. (#956)
 *  Updated NIWA rose-stem configuration for Maui HPC. (#965)
 *  Changed the path to data and libraries for rose stem testing on JASMIN. The default is the new jules group-workspace, and an environment variable JASMIN_JULES_BASE_DIR can be exported and picked up by rose stem. (#967)

Documentation updates
---------------------

 *  Improved description of :nml:mem:`JULES_RADIATION::l_embedded_snow`. (#916)
 *  Assorted clarifications in documentation and comments. (#980)
 *  Basic infrastructure provided to support future JULES Documentation Papers. (#968)
 *  Updates associated with many of the above changes, and release notes. (#995)

Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.
