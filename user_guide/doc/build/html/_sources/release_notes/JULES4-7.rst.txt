JULES version 4.7 Release Notes
===============================


The JULES vn4.7 release consists of 47 tickets from 19 authors.

Full details of the tickets committed for JULES vn4.7 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v4.7+release>`_.

Ticket numbers are indicated below, e.g. #265.

Science changes
---------------

 * Enable soil tiling by the extraction of key calculations. These include: Infiltration rate and Soil moisture availability factor (beta). (#265)

 * Modifications to the rate of growth of snow grains - it uses the ET scheme of Taillandier (2007), JGR, 112, F03003 for the rate of growth and to relayer the grain size using its inverse as this is more consistent with conservation of SSA reported by Gallet et al. (2011). (#298)

 * JULES-CN: Soil_CN ratio changed from hard-wired to the namelist in prep for a PPE of JULES and JULES-CN the bio and hum N pools change from being prognostic to diagnostic via the soil bgc at the start of this routine and during initialisation. (#309, 288)

 * Add new irr_crop option: irr_crop = 0: continuous irrigation (i.e. the effectively the crop season is defined to last all year). It does not depend on crop characteristics (unlike irr_crop=2, which uses the crop model, or irr_crop=1, which estimates a typical crop season for that gridbox). (#312)

 * Diagnostics for individual components of snowpack mass balance, as specified by ISMIP6. (#314)

 * Diagnostics for components of surface radiation on land tiles. Requested by ISMIP6 for driving standalone icesheet models. (#315)

 * User initialised river storage. When dump_file=T, and use_file=T for rivers_sto_rp, then rivers_sto_rp needs to be in the dumpfile. When use_file=F for rivers_sto_rp, then rivers_sto_rp can be set to a constant value in this namelist. When dump_file=F, the rivers_sto_rp is initialised to zero. (extra log message to say that rivers_sto_rp is initialised to zero in this case). Therefore a dump file from a run without l_rivers=T and rivers_type='trip' can now be used to initialise a run with l_rivers=T and rivers_type='trip'. (#316 and #329 doc)

 * For fsmc_mod = 1, change the water extraction pattern so that it is proportional to plant available water rather than total water in the soil layers. Note: fsmc_mod=1 is not the recommended value in the JULES manual and it is not currently use in any of the documented configurations. This part of the code is also going through a detailed review as part of the soil moisture stress on vegetation group, which includes documenting the current status. (#320)

 * Add a new cpft-dependent input variable initial_c_dvi_io to specify when the crop should be initialised. (#324, 356 doc)

 * Allow perturbations to driving data, by specify an amount to be added to driving temperatures and/or an amount to multiply the driving precip variables by. This is achieved by adding a switch (l_perturb_driving) and two input variables (temperature_abs_perturbation and precip_rel_perturbation) to the JULES_DRIVE namelist. When l_perturb_driving is set to true, an amount (positive or negative) can be added to the driving temperature (temperature_abs_perturbation) and the precipitation variables can be multiplied by a factor (precip_rel_perturbation). (#326)

 * Fluxes JULES rose stem tests added: Some new GSWP2 tests for forecast configurations, New diagnostics to many existing tests, Switches on profiles that were written but disabled in carbon cycle tests, Tweaks to how we run on SPICE. (#330)

 * Change the defaults for the npft=9, ncpft=4 case in the rose upgrade macro vn44_t136 so that first 5 pfts are the same as the npft=5 case and the C3/C4 crop tiles have the same values as the C3/C4 grasses. (#336)

 * Allow sthuf (soil moisture) to be prescribed. (#348)

 * Soil refactor, following on from adding module statements etc to radiation and snow, this works on src/science/soil to add MOUDLE statements and INTENTS. (#351)

 * Update to metadata for jules_rivers_props so when grid_is_1d is false the following values in jules_rivers_props; nx_grid, ny_grid, reg_lat1, reg_lon1, reg_dlat, reg_dlon are required when running in parallel. Added a log message warning that the values are not used if grid_is_1d is false and the run is in parallel. (#293)

 * Add the soil tile dimension to JULES as a hard-coded singleton. (#305)

 * Fixed a bug in TRIFFID which causes loss of bit comparison that occurred when L_TRIF_CROP and L_NITROGEN were both TRUE: the soil nitrogen prognostics (stash 442, 443, 446) became dependent on the PE configuration. (#372)

 * Modularise and header refactor science/radiation Adds module and intents to the radiation code Removed implicit RESHAPES of some variables through subroutine calls and therefore removes nearly all the complicated dimensionalities in this area (ij, pfield, land_pts), making the code simpler. (#253)

 * Add vertically discretised soil C and N to TRIFFID. Adds a dimension to existing prognostics and discretizing existing code. The scheme is extended to link rooting profiles to availability and uptake of N requiring additional prognostics. (#288)


General/Technical changes
-------------------------

 * Improve coding standard docs.
 * Move from includes to use modules for ccarbon.h Retire l_endgame as we only use endgame in the UM.
 * Fix warnings in the fcm make log.
 * OpenMP improvements.
 * Add valgrind profiling as execution option in the Rose GUI.

 * Extra documentation on; namelist order, Update to release notes.

 * Nightly rose stem test added to the MO system to test the head of the trunk nightly.

 * Replace all ENDIF, ENDDO, IF(, MAX(, MIN(, EXP( and GAMMA/gamma to r_gamma with the working practices syntax.

 * Use "rose config dump" on the whole repository to tidy up the rose (Python) files.
 * Update cylc5 syntax to cylc6 (Python).
 * Improve the create_rose app script. It now takes 5 arguments, vn_from, vn_to, namelist_path, suite_name and jules_dir.



Bugs fixed
----------

 * Fixed the variable in the metstats_timesteps subroutine that was being incorrectly set for first and last second of day, which lead to gaps in the fire indices along some lines of longitude. (#323)

 * Fixed errors in UM GA7 AMIP code to run rose stem app with "rigorous" optimisation settings on SPICE. In particular: Formatted internal writes with incorrect format statements; ALLOCATEd variables not being DEALLOCATEd. (#328)

 * Fixed example put namelists. Updated parameters can_struct_a_io, fsmc_mod_io, and fsmc_p0_io in all example directories, and added missing parameters in the loobos_point_9pfts directory. (#354)

 * Clay frac bug, IF test for l_triffid=.false. added around clay_gb so that the test does not fail as clay_gb has not been populated as triffid is not run and therefore not clay_gb is not initialised and populated. (#307)

 * taux (wind stress) output inconsistency fixed by the initialisation of two variables in surf_couple_extra: cq_cm_u_1(:,:) = 0.0 and cq_cm_v_1(:,:) = 0.0 (#339)

 * Set z0_surft and lit_c_pft to zero in allocate_jules_arrays as they were not allocated and caused KGO failures. (#365)

 * Fixed calc_fsat so that values are not divded by small numbers. (#342)

 * Fixed the bug in multi-layer snow use of tile_map. It now checks to see if it is valid for the input dump configuration and converts from mapping tile IDs to pseudo levels. (#302)


Documentation updates
---------------------
Coding standards, and documentation can be viewed on the 'github page <http://jules-lsm.github.io/>_'.

