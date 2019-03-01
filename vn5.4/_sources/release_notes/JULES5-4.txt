JULES version 5.4 Release Notes
===============================


The JULES vn5.4 release consists of approximately 29 tickets from 13 authors, including work by many other people.

Full details of the tickets committed for JULES vn5.4 can be found on the `JULES shared repository Trac system <https://code.metoffice.gov.uk/trac/jules/query?resolution=fixed&milestone=JULES+v5.4+release>`_.

Ticket numbers are indicated below, e.g. #872.

Science changes
---------------

 *  Improvements to fire-related vegetation mortality, including the addition of a PFT-specific fire mortality parameter :nml:mem:`JULES_PFTPARM::fire_mort_io` (previously mortality was taken directly from the burnt area as diagnosed by INFERNO and did not vary by PFT). (#872)
 * Stomatal conductance can be modelled following the approach of `Medlyn et al. (2011) <https://doi.org/10.1111/j.1365-2486.2010.02375.x>`_, via the switch :nml:mem:`JULES_VEGETATION::stomata_model`. A single-parameter version of the model is coded, requiring the PFT-specific parameter :nml:mem:`JULES_PFTPARM::g1_stomata_io`. (#766)

General/Technical changes
-------------------------

 *  The RFM river routing scheme is now available to the UM (atmospheric model), and both standalone and UM runs use the same code. See :nml:lst:`JULES_RIVERS`. (#876)
 *  The :nml:lst:`JULES_RIVERS` namelist now controls river hydrology in both standalone and UM-coupled modes.  (The UM namelist 'run_rivers' has been removed.) (#867)
 *  The surface conductance (`gs`) is now part of the specification of the initial state (and included in dumps) only when it is required (i.e. only if :nml:mem:`JULES_VEGETATION::can_rad_mod` = 1; see :ref:`list-of-initial-condition-variables`). (#859)
 *  Use ``swap_bounds`` routine(s) from ``halo_exchange_mod`` module (not the old 2C subroutine) in UM runs. (#367)
 *  Extensive refactoring of ``surf_couple_extra``, including removal of ``ifdef`` in argument list. (#806, 833)
 *  Tidied/refactorised the photosynthesis code. (#817)
 *  Improved checking and reporting of the IMOGEN setup. (#850)
 *  Tidied the header of ``control.F90``, removing duplicate and unused variables. (#873)
 *  Access subroutines ``set_levels_list`` and ``set_pseudo_list`` using modules, removing the need for ``DEPENDS ON``. (#880)
 *  Improved performance of land surface routines in RA and GA configurations. (#861)
 *  Set up CABLE directory structure and initialise essential variables for `surf_couple_radiation`. (#799)
 *  Allowed variables used in the build process to have platform-specific defaults which can be overridden by the user. (#853)
 *  Met Office Cray users: Direct extract of code to the Cray is the default for meto-xc40-cce builds. Users are encouraged to remove fcm_make2 tasks and set ``JULES_REMOTE = local`` to take advantage of faster end-to-end compilations and reduce load on the HPC. Set ``JULES_REMOTE = remote`` to retain builds which require an fcm_make2 task. See :ref:`fcm-make-environment-variables`. (#854)
 *  Reviewed and simplified fcm-make metadata compulsory variables and made current apps validate. (#855)
 *  Improved selected metadata in the :nml:lst:`JULES_SOIL_BIOGEOCHEM` and :nml:lst:`JULES_SOIL_ECOSSE` namelists to prevent errors when using the Rose GUI. (#862)


Bugs fixed
----------

 *  Fixed the radiatively-coupled roof in MORUSES, using the temporary logical :nml:mem:`JULES_TEMP_FIXES::l_fix_moruses_roof_rad_coupling`, in the new namelist :nml:lst:`JULES_TEMP_FIXES`. The supposedly radiatively-coupled roof is in fact **uncoupled** without this bug fix.   (#610)
 *  Corrected initialisation of frozen/unfrozen soil - no longer assumes constant soil properties with depth. (#749)
 *  Removed a bug in the snow scheme when :nml:mem:`JULES_SURFACE::l_point_data` = TRUE and :nml:mem:`JULES_VEGETATION::can_model` = 4: the snow covered fraction formulation is now only used for tiles that do not use the snow canopy option (see :nml:mem:`JULES_SNOW::cansnowpft`), rather than for all tiles. (#879)
 *  Prevent out-of-bounds operations in sf_exch. (#846)
 *  Ensure that `ntype` is set before use in UM model runs. (#878)
 *  Corrected the units of the ocean near-surface chlorophyll content (used in the calculation of the ocean surface albedo), using the temporary logical `l_fix_osa_chloro`. Only affects runs with the UM. (#874)


Changes to testing
------------------

 *  Rose-stem fcm-make tasks will ignore lock files that would otherwise prevent retriggering. (#860)
 *  Expanded coverage of the rose-stem metadata validation test to include more apps. (#886)
 *  Upgraded ``suite_report.py``. (#889)
    
Documentation updates
---------------------

 *  Updates associated with many of the above changes, and release notes. (#881)
 *  Example namelists point_mead_2_crops have been updated to be consistent with the published JULES-crop runs in `Williams et al. (2017) <https://doi.org/10.5194/gmd-10-1291-2017>`_.

Documentation can be viewed on the github page `<http://jules-lsm.github.io/>`_.
