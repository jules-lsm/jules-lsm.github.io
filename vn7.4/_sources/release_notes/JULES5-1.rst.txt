JULES version 5.1 Release Notes
===============================


The JULES vn5.1 release consists of approximately 40 tickets from 17 authors, including work by many other people.

Full details of the tickets committed for JULES vn5.1 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v5.1+release>`_.

Ticket numbers are indicated below, e.g. #533.

Science changes
---------------

 *  Addition of river overbank inundation module (for diagnostic calculation of overbank inundation fraction) - see l_riv_overbank in namelist :nml:lst:`JULES_RIVERS` and namelist :nml:lst:`JULES_OVERBANK`. (#679)
 *  Changes to the layered soil biogeochemistry model: (i) the mean soil temperature over the TRIFFID time step is now used to determine whether a layer is unfrozen (ii) mixing is considered when calculating the final respiration. (#663)
 *  Options for improved treatment of thin snow comprising the introduction of basal melting of thin snow layers on warm ground. See :nml:mem:`JULES_SNOW::i_basal_melting_opt`. (#533)
 *  Added capability to include latest harvest date to crop ancillary. See :ref:`list-of-spatially-varying-crop-properties`. (#653)
 *  Account for crop harvest and fire in the carbon conservation diagnostics. (#476)
 *  Carbon conservation diagnostic now only calculated on TRIFFID timesteps. (#643)
 *  Added the JULES-standalone version of improved saturation vapour pressure (qsat) calculations. (#635)
 *  Introduced basic slab ocean by allowing the model to update the sea surface temperature based on the energy balance, in the same way as it does for land and sea-ice. Also allows for a fixed sea surface albedo (see `fixed_sea_albedo`), rather than the parameterised options. (#642)

General/Technical changes
-------------------------

 *  Wetland CH\ :sub:`4` emission parameters have been added to :nml:lst:`JULES_SOIL_BIOGEOCHEM`. Parameters are :nml:mem:`JULES_SOIL_BIOGEOCHEM::t0_ch4`, :nml:mem:`JULES_SOIL_BIOGEOCHEM::const_ch4_cs`, :nml:mem:`JULES_SOIL_BIOGEOCHEM::const_ch4_npp`, :nml:mem:`JULES_SOIL_BIOGEOCHEM::const_ch4_resps`, :nml:mem:`JULES_SOIL_BIOGEOCHEM::q10_ch4_cs`, :nml:mem:`JULES_SOIL_BIOGEOCHEM::q10_ch4_npp`, and :nml:mem:`JULES_SOIL_BIOGEOCHEM::q10_ch4_resps`. (#483)
 *  i/o work to allow soil tiling to function correctly. (#684)
 *  Allow output of rate modifier diagnostics needed for offline spin up of soil carbon pools. (#589)
 *  Improvements to intermittent sampling for output. (#605)
 *  Removed repeated calculation of vegetation stocks of C and N from TRIFFID. (#618)
 *  Modularised JULES vegetation subroutines to enforce stricter interface checking. (#668)
 *  Replaced integer constants used with :nml:mem:`JULES_SOIL_BIOGEOCHEM::ch4_substrate` (the choice of substrate for wetland methane) with parameters. (#628)
 *  More time constants replaced by parameters. (#625)
 *  Namelist :nml:mem:`JULES_MODEL_ENVIRONMENT::lsm_id` added to allow the selection of the land surface model: JULES or CABLE. Note that the CABLE science routines have not been implemented yet. (#656)
 *  Redundant "include" files removed and rationalisation of other modules. (#689)
 *  Made the JULES source code (as close as possible to) compliant with the Fortran 2003 standard. (#699)
 *  Added OpenMP to the snow scheme to improve parallel performance. (#638)
 *  IMOGEN identified as a new science module, and other changes to list of module leaders. (#686, 666)
 *  Added basic MORUSES rose stem test (upgraded UKV science to PS39) and enhanced metadata. (#289)
 *  Added a new script to rose stem to ensure apps are consistent with rose metadata. (#645)
 *  Expanded the fcm-make metadata to make it easier to apply additional compiler flags to builds. (#632)
 *  Implemented a timeout for the JULES rose-stem in instances where an app/task "submit-fail" or stalls. (#672)
 *  Updated settings for JULES on Met Office XC40 (standalone suites should be updated where necessary to pick up the new settings) and Met Office linux testing to use ifort 16.0. (#630, 697).

Bugs fixed
----------
 *  Fixed bug in soil hydrology to prevent water erroneously coming out of the bottom of the soil. Use :nml:mem:`JULES_SOIL::l_holdwater` = T to allow water to be held on an impermeable layer. (#171)
 *  Bug fix affecting litterfall N flux when :nml:mem:`JULES_VEGETATION::l_landuse` = T. (#617)
 *  Bug-fix in the calculation of the albedo when :nml:mem:`JULES_RADIATION::l_embedded_snow` = T. (#533)
 *  Corrected a scalar/array mismatch in the arguments to the `plant_growth_n` subroutine. (#670)
 *  Fix to allow initialisation of CO\ :sub:`2` from a dump file. (#680)
 *  Minor fix for vegetation competition in runs with :nml:mem:`JULES_VEGETATION::l_ht_compete` = F and :nml:mem:`JULES_VEGETATION::l_trif_crop` = F. (#627)
 *  Corrected units for parameters `dfp_dcuo` and `eta_sl` in comments and documentation. (#646, 659)
 *  Minor correction to metadata for :nml:lst:`JULES_SOIL_PROPS` namelist. (#669)
 *  Fixed an allocation bug in the UM (#665).
 *  Bug in tiling that could affect lake quantities (in UM runs using FLake). (#641)
 *  Fix of a minor OpenMP race condition. (#674)
 *  Moved an ALLOCATE statement to fix a memory bug in the UM affecting ESM runs. (#639)
   
Documentation updates
---------------------
Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.
