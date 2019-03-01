JULES version 4.9 Release Notes
===============================


The JULES vn4.9 release consists of approximately 60 tickets from 19 authors, including work by many other people.

Full details of the tickets committed for JULES vn4.9 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v4.9+release>`_.

Ticket numbers are indicated below, e.g. #262.

Science changes
---------------

 * New parameter :nml:mem:`JULES_HYDROLOGY::s_pdm` represents the minimum soil wetness below which there is no saturation excess surface runoff from the PDM model. s_pdm can be made slope-dependent using :nml:mem:`JULES_HYDROLOGY::l_spdmvar`, with additional parameter :nml:mem:`JULES_HYDROLOGY::slope_pdm_max`. (#262)
 * Extensions to the parameterisation of moisture stress on vegetation. There is now (a) the option of a stress function that is piece-wise linear in soil potential (:nml:mem:`JULES_VEGETATION::fsmc_shape` = 1) rather than soil volumetric moisture content (:nml:mem:`JULES_VEGETATION::fsmc_shape` = 0) and (b) the option of specifying pft-dependent soil potentials (:nml:mem:`JULES_VEGETATION::l_use_pft_psi`) at which the plant starts to experience water stress (:nml:mem:`JULES_PFTPARM::psi_open_io`) and where the plant is fully stressed (:nml:mem:`JULES_PFTPARM::psi_close_io`). (#541)
 * Methane emissions can now be calculated from layered soil temperature (see :nml:mem:`JULES_SOIL_BIOGEOCHEM::l_ch4_tlayered`). Methane flux can be removed from soil carbon stocks to close the carbon budget (see :nml:mem:`JULES_SOIL_BIOGEOCHEM::l_ch4_interactive`). The choice of substrate used for methane production is now controlled using :nml:mem:`JULES_SOIL_BIOGEOCHEM::ch4_substrate` instead of l_wetland_ch4_npp. (#468)
 * Updates to the INFERNO fire model (see :nml:mem:`JULES_VEGETATION::l_inferno`) including burning of the carbon in litter/soil pools. New diagnostics added including flammability (see :ref:`output_variables_section`). (#502)
 * Extension to the scheme for calculating subgrid-scale snowpack properties and surface mass balance fields for icesheet coupling (see :nml:mem:`JULES_SURFACE::l_elev_land_ice`). Non-glaciated tiles (:nml:mem:`JULES_SURFACE_TYPES::elev_rock`) can now co-exist with the ice tiles (:nml:mem:`JULES_SURFACE_TYPES::elev_ice`) in the elevation classes, allowing for fractional ice extent in a gridbox. (#294)
 * Allow soil moisture to be prescribed on a subset of soil levels (see :nml:mem:`JULES_PRESCRIBED_DATASET::prescribed_levels`). (#487)
 * Improvements to the layered soil C and N model (see :nml:mem:`JULES_SOIL_BIOGEOCHEM::l_layeredc`) which is now fully ready for use. (#454, #526)
 * Layered C allowed with single-pool soil model. (#526)
 * Preparatory work for the ECOSSE soil biogeochemical model. (#444, #518)
 * New functionality to limit the drag over the sea at high wind speeds (only for coupled models). (#543)

General/Technical changes
-------------------------

 * Further preparatory work for soil tiling, including i/o.
 * Allocated arrays are given initial values and improved error messages from memory allocation.
 * Further C fluxes and diagnostics made available to the UM.
 * :nml:mem:`JULES_PFTPARM::fsmc_p0_io` added to UM namelists.
 * Various UM-related improvements, including: single switch to allow runs with mixing ratio; avoiding hard-wired logical argument to swap_bounds; removed old logical related to "New dynamics"; removed the stash super array; removed unused array bounds.
 * Wrapped non-LFRIC-compliant code using a preprocessor directive.
 * General code developments and improvements to meet the coding standards.
 * Added fcm make and rose stem configurations for building and testing JULES at NCI.
 * Added Rose stem tests for TRIP rivers running with 2D data and RFM rivers. (#539, #567, #568)
 * Add more information to trac.log by improving suite_report.py.
 * rose-stem supported for MONSooN xcs-c.
 * Various changes for Met Office, including nightly testing on xcs.
 * New tutorial group for rose-stem.
 * Change to suite-report.py for use with cylc 7.
 * Updates to the app update script.


Bugs fixed
----------

 * Corrected mismatches between certain subroutine interfaces and subroutine calls. (#471, #544)
 * Fixed bug in reading of certain soil tile variables. (#498)
 * Fixed bugs in TRIFFID litter fluxes. (#504)
 * TRIFFID altered to do fewer calculations on points without veg or soil. (#509)
 * Tidied up code issues between UM and JULES. (#522)
 * Added interactive nitrogen to the loobos_jules_es_1p6 test and initialised more TRIFFID variables. (#512, #520)
 * Bug fix for regridding between land and river routing grids for regular lat/lon river grids where the land model grid is defined as 1d land point only grids. (#524)
 * Fixed uninitialised variables in surf_couple_extra_mod.F90. (#546)
 * Bug fix in init_rivers_props.inc. (#539)
 * Bug fix for crop ancillary variables in read_dump and write_dump. (#551)
 * Corrected a bug in the sea ice albedo scheme, which affects the calculation of bare ice albedo when multilayer thermodynamics are used in coupled UM-JULES-NEMO-CICE. (#547)
 * Bug fix to variable intent in surf_couple_implicit. (#542)
 * Bug fix for UM runs relating to clash between STASH items (#557)
   
Documentation updates
---------------------
Coding standards, and documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.

