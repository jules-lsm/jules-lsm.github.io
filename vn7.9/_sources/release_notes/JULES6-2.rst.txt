JULES version 6.2 Release Notes
===============================


The JULES vn6.2 release consists of approximately 23 tickets from 15 authors, including work by many other people.

Full details of the tickets committed for JULES vn6.2 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v6.2+(Oct-21)>`_.

Ticket numbers are indicated below, e.g. #470.


Science changes
---------------

 *  Added the ability to label and trace a subset of the soil carbon in the RothC layered model - see :nml:mem:`JULES_SOIL_BIOGEOCHEM::l_label_frac_cs`. (#470)
 *  Replaced original logical for corrections to coastal tiling with a 3 way switch (:nml:mem:`JULES_TEMP_FIXES::ctile_orog_fix`). The latest improved fix combines the previous fix over sea with the original behaviour over land. (This is mainly relevant for runs with the Unified Model.) (#1184)

General/Technical changes
-------------------------

 *  Improvements and bug fixes for river grid and flow directions. (#1170)
 *  Selected output variables are now available on the river grid. (#1163)
 *  Technical work coupling the RED vegetation model to JULES. This is early in a staged process and RED is not yet available for general use. (#1034)
 *  Only check for duplicate lat-lon coordinates if those are set using constant values. (#1164)
 *  Variables related to fluxes and atmospheric chemistry bundled into TYPEs. (#1104, 1159)
 *  Removed momentum calculations for LFRic as those are now done in bespoke LFRic code. (#1144)
 *  Further work towards enabling interoperability between the JULES and CABLE land surface models - this step dealing with CABLE prognostic variables (see :nml:lst:`CABLE_PROGS`). (#1131)
 *  Removed most compiler warnings flagged by UM builds. (#1187)
 *  Ported the JULES codebase to the Met Office's EX1A system. (#1193)
 *  Updated Python scripts to be Python 3 compatible. (#1091)
 *  Preparing the JULES vn6.2 release. (#1204)

    
Bugs fixed
----------

 *  Bug fix to correct an array addressing issue in snow albedo calculations with :nml:mem:`JULES_RADIATION::l_embedded_snow` = TRUE. (#1064)
 *  Deallocating a few more arrays in ancil_info. (#1190)
 *  Fix to ensure that in coupled NWP models lake ice temperatures (where lakes are defined as sea points) evolve correctly - this is fixed by setting :nml:mem:`JULES_TEMP_FIXES::l_fix_lake_ice_temperatures` = TRUE. (#1161)
 *  Prevent error in internal write of ctile_orog_fix (potentially many characters long) into a 3 character buffer. (#1205)
 *  Fix arguments to subroutine next_time. (#1209)

    
Documentation updates
---------------------

 *  Updates associated with many of the above changes, and release notes. (#1156, 1186, 1192, 1198)

Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.

