JULES version 4.8 Release Notes
===============================


The JULES vn4.8 release consists of approximately 77 tickets from 26 authors, including work by many other people.

Full details of the tickets committed for JULES vn4.8 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v4.8+release>`_.

Ticket numbers are indicated below, e.g. #400.

Science changes
---------------

 * Changes to calculate transpiration on tiles and as a gridbox mean. A resistance factor based on stomatal resistance excluding soil is calculated and then multiplied by evapotranspiration. This affects the diagnostics 'et_stom' and 'et_stom_gb'. (#400)
 * Addition of interactive fire/vegetation, selected using :nml:mem:`JULES_VEGETATION::l_trif_fire`. Fire disturbance modifies vegetation dynamics and can be modelled by the INFERNO fire model or prescribed via an ancillary file. This is a preliminary version that will be developed further.  (#456)
 * Added option to allow downward longwave and net shortwave radiation to be used to force the model (see :ref:`list-of-jules-forcing-variables`). JULES now stops if too many or incorrect radiation variablse are provided (rather than carrying on if a valid combination was found). (#409)
 * Added an option for the treatment of graupel in input to snow scheme (primarily for the UM; see :nml:mem:`JULES_SNOW::graupel_options`). (#414)
 * Looping required for soil tiling functionality added in a disabled state (nsoilt still hard-coded to 1). (#379)
 * Added the ability for hydrol_jls.F90 to work with tiled runoff once soil tiling is enabled in a later change. (#341)


General/Technical changes
-------------------------

 * Refactoring of albpft_jls.F90 to be more efficient.
 * Improved code to calculate litter, landuse change and harvest fluxes.
 * New namelist :nml:lst:`JULES_SOIL_BIOGEOCHEM`. The soil and vegetation components of TRIFFID have been separated.
 * :nml:mem:`JULES_INITIAL::total_snow` defaults to .FALSE.
 * :nml:mem:`JULES_OUTPUT::dump_period` controls the frequency with which dumps are written.
 * River routining changes: user initialised surface and sub-surface storage and flows for RFM river routing. See :ref:`list-of-initial-condition-variables`. Two options for standalone river routing: 'rfm' or 'trip' in namelist :nml:lst:`JULES_RIVERS`. New remapping utilities provide efficient translation between land points and river points vectors.
 * New and added diagnostics for UKESM, CMIP6 'NDVI_land'. See :ref:`output_variables_section`.
 * Improved error checking and error messages.
 * Print statement improvements.
 * Urban namelists prefixed with 'jules'.
 * Tidy up unused variables and an unused dummy argument in the FLake code.
 * General code developments and improvements to meet the coding standards.
 * A minor change to communication routines' API.
 * OpenMP developments.
 * Rationalisation of UM ancil routines, part 1 (#346)
 * Removed redundant code from the soil ancillary reading code. (#450)
 * Rose stem configurations for JASMIN, NIWA, CEH, Exeter Uni, remote JASMIN and MetO XCS computer. Ensure that the same tests are run at all sites. cylc7 compatable
 * New or improved rose stem tests.
 * Improvements to create-rose-app and suite_report.py



Bugs fixed
----------

 * Bug in the argument list to irrig_dmd, where the surface-tiled irrigated fraction was passed instead of the gridbox mean. (#389)
 * Various fixes related to argument INTENTs (snow #396; soil respiration #392, h_blend_orog #452, surface flux code #412).
 * Bug fixes for INFERNO fire model (soil carbon #415, incorrect rainfall #390, minor fixes #371).
 * Bug fix in TRIFFID so soil nitrogen with l_trif_crop does not depend on processor configuration (#372)
 * Bug fix for soil inorganic N in UM runs (#395)
 * Bug fix in hydrology for when :nml:mem:`JULES_HYDROLOGY::l_wetland_unfrozen` = .TRUE. (#473)
 * Initialisation of TRIFFID diagnostics (#313, #474, #479)
 * Minor update to correct standalone river routing grid definition for non-regular grids (e.g. UKV variable resolution). (#410)
 * Bug fix in the calculation of NPP in TRIFFID with N limitation. (#308)
 * Fixed error in frequency of calls to phenology in long standalone runs. (#421)
 * Bugs fixed so IMOGEN will restart more accurately from a dump. (#420)
 * Bug fixes and improvements for layered soil CN model (#394, #407)
 * Bug fix for albpft_jls.F90 (#458)
 * Bug fix to allow compilation without netCDF (#464)
 * Bug fixes for metadata and upgrade macro (#404, #459, #490)
   
Documentation updates
---------------------
Coding standards, and documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.

