JULES version 6.3 Release Notes
===============================


The JULES vn6.3 release consists of approximately 28 tickets from 14 authors, including work by many other people.

Full details of the tickets committed for JULES vn6.3 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v6.3+(Feb-22)>`_.

Ticket numbers are indicated below, e.g. #1142.


Science changes
---------------

 *  Restructured the parameterisation of thermal acclimation of photosynthesis to permit a wider range of configurations - see :nml:mem:`JULES_VEGETATION::photo_acclim_model`. (#1142)
 *  Updated soil N limitation in layered CN model (only applies when :nml:mem:`JULES_SOIL_BIOGEOCHEM::l_layeredc` = TRUE). (#1213)


General/Technical changes
-------------------------

 *  Improved nitrogen leaching for vertically-resolved soil biogeochemistry. (#1219)
 *  Allowed the use of daily files for input and output (via time templating for input files). (#1215)
 *  Further developments towards the RED vegetation model. (#1182)
 *  Refactored IMOGEN in preparation for adding netcdf reading and variable resolution. (#1214)
 *  Added functionality for the first phase of a standalone Rivers executable. This uses JULES I/O and is still under development; it currently is not scientifically correct as a result of a timestamp issue and does not include dumping capability. (#1084)
 *  Namelists `jules_urban2t_param` and `jules_urban_switches` amalgamated into :nml:lst:`JULES_URBAN`, which is also now consistent with the module name. (#1077)
 *  Updated metadata for bedrock and layered soil carbon. (#1234)
 *  Framework for a shared metadata solution introduced initially with namelist items from `jules_surface` and `jules_vegetation` currently shared with LFRic. (#1195)
    More information on sharing JULES metadata can be found here: `SharingJULESmetadata <https://code.metoffice.gov.uk/trac/jules/wiki/SharingJULESmetadata>`_
 *  Minor adjustment to how FLake variables are dealt with during initialisation. (#1169)
 *  Modularised and refactored subroutine vgrav. (#1199)
 *  Rivers variables bundled in a new TYPE. (#1176)
 *  Modularised further UM-only files. (#1221)
 *  Removed the soil carbon variable cs from the UM, in prepration for the introduction of layered soil carbon. (#1210)
 *  Removed snowmelt_ij from fluxes_mod. (#1167)
 *  Tidied code to remove compiler warnings. (#1245)
 *  Revised the implementation of defining the veg/soil parameters to be passed to CABLE as a single TYPE, following them being read in through namelists. We also implement a working variables TYPE to hold variables at the top-level so that they may be passed between pathways (i.e explicit, implicit); as well as between time steps (at least until they are elevated to prognostics level). (#1223)
 *  Added a further restriction on the type of processor used for rose stem testing on JASMIN. (#1222)
 *  Updated list of module leaders. (#1240)

    
Bugs fixed
----------

 *  Fixes to FLake surface exchange and decoupling FLake from the soil column. (#1094)
 *  Added missing metadata for PFT parameter `dust_veg` (only used in the UM). (#1206)
 *  Corrected the definitions of the surface longwave radiation diagnostics. (#1220)
 *  Fixed a bug that prevented files from being closed when running with MPI. (#1241)
 *  Ensured that soileccose types are set up correctly. (#1229)
 *  Ensured Python3 is in path on both MONSooN and JASMIN systems. (#1216, 1231)

    
Documentation updates
---------------------

 *  Updates associated with many of the above changes, and release notes. (#1243)

Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.

