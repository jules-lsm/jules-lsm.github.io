JULES version 7.0 Release Notes
===============================

The JULES vn7.0 release consists of approximately 31 tickets from 20 authors, including work by many other people.

Full details of the tickets committed for JULES vn7.0 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+Jun-2022>`_.

Ticket numbers are indicated below, e.g. #911.


Science changes
---------------

 *  New functionality for modelling bioenergy crops - see :nml:mem:`JULES_VEGETATION::l_trif_biocrop` and :nml:mem:`JULES_VEGETATION::l_ag_expand`. (#911)
 *  Implemented a socio-economic factor in the fire ignition and suppression parameterisation in INFERNO, based on a Human Development Index (HDI). (#1284)
 *  A new logical switch :nml:mem:`JULES_SURFACE::l_mo_buoyancy_calc` enables an interactive buoyancy in the calculation of the surface transfer coefficients. (#1242)


General/Technical changes
-------------------------

 *  Surface type IDs fully extended to JULES to allow extra surface configuration checks to take place. A routine to check compatible science options is now accessible to all parent models, allowing cross-namelist checking to take place once all the namelists have been read, removing the dependency on order. (#1249)
 *  Upgraded FLake driver to version 1.10 to include a bug fix from the FLake community and keep our copy of FLake aligned with the community code base. (#1227)
 *  JULES now passes sea ice surface heat flux (surf_ht_flux_sice), sea ice top melt (sice_melt) and sea ice sublimation (ei_sice) from JULES to LFRic as part of the fluxes structure. These variables, and a few others, are no longer weighted by sea ice fraction before being passed out of JULES. The weighting by sea ice fraction should be done in the parent models. (#1259)
 *  Made stencil used in buddy_sea option work for unstructured meshes, rather than assuming i+1, j+1 indexing will work. (#1286)
 *  Tidied soil code so that arguments follow UMDP3 order, and corrected some argument INTENTs. (#843)
 *  Streamlined standalone code dealing with input of ancillary fields. (#1256)
 *  In preparation for including layered soil carbon in the UM, the soil respiration returned to the UM now has an extra dimension which can potentially be used to represent layers. (#1236)
 *  Migration of :nml:lst:`JULES_NVEGPARM` and :nml:lst:`JULES_SURFACE_TYPES` used in LFRic to shared metadata held in jules-shared. Checking of :nml:lst:`JULES_NVEGPARM` moved to a new shared routine and added to UM. (#1272)
 *  Passing CABLE vars (TYPEs) from top level through to and into surf_couple layer. (#1226)
 *  Updated the module load of the make_jules_release script. (#1263)

    
Bugs fixed
----------

 *  Fix for precision issue whereby infiltration of rainfall into snowpack could become larger than the incident rainfall, resulting in negative large-scale rain. (#1092)
 *  Bug fix for persistent small snow amounts - see :nml:mem:`JULES_TEMP_FIXES::l_fix_snow_frac`. (#1279)
 *  Correction to the chlorophyll dependence of the oceanic albedo in the scheme of Jin et al. (2011). (#1260)
 *  Bug fix to allow calculation of the lw_net diagnostic. (#1270)
 *  Fixes to UM routines identified by the NAG compiler. (#1276)
 *  Corrected namelist reading to ensure that FLake can be run with urban2t and MORUSES schemes in standalone JULES. (#1277)
 *  Fixed bug that prevented finalisation of initial output files. (#1281)
 *  Introduced namelist variable :nml:mem:`JULES_RIVERS_PROPS::coordinate_file` to fix bug preventing use of file-name templating with river ancillaries. (#1287)
 *  Prevent faults caused by attempting to read an absent dummy argument. (#1292)
 *  Fixed benign OMP bug in snowpack_mod. (#1304)


Changes to testing
------------------

 *  Added rose stem test for the FLake lake model. (#1277)
 *  Altered the eraint rose stem apps to better represent river routing. (#1299)
 *  Increased resources requested for build in Met Office XC40 rose stem. (#1291)
 *  Changes to module load, mpiexec usage, and memory requested for rose stem for the Met Office EXZ platform. (#1296, 1302, 1305, 1309)


Documentation updates
---------------------

 *  Updates associated with many of the above changes and to module leaders file, and release notes. (#1275, 1300)

Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.

