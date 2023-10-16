Some key switches
=================

There are many variables that act together to determine how a run of JULES is set up and these are covered in detail in :doc:`/namelists/contents`. Additionally, `configurations <http://jules.jchmr.org/content/configurations>`__ illustrate suitable combinations of options. Here we highlight a few key switches that select broad areas of science, particularly for the benefit of new users.

The phenology model for natural vegetation can be enabled using :nml:mem:`JULES_VEGETATION::l_phenol` which uses the leaf turnover rate to calculate a time-varying Leaf Area Index (LAI).

To simulate carbon stocks in natural vegetation, the TRIFFID dynamic vegetation model can be enabled via the switch :nml:mem:`JULES_VEGETATION::l_triffid`. When TRIFFID is on, competition between tiles is switched on with :nml:mem:`JULES_VEGETATION::l_veg_compete` and the effect of nitrogen on vegetation growth is enabled via :nml:mem:`JULES_VEGETATION::l_nitrogen`.

The crop model, which is simulates phenology and carbon stocks in crops, can be switched on by setting the number of crop tiles :nml:mem:`JULES_SURFACE_TYPES::ncpft` to a non-zero value.

The crop model and TRIFFID cannot currently be used together. To simulate agricultural areas within TRIFFID, a fraction of the gridbox can be reserved for agricultural Plant Functional Types (PFTs) (as defined by :nml:mem:`JULES_TRIFFID::crop_io` > 0). Agricultural PFT competition and a representation of harvest carbon can be switched on with :nml:mem:`JULES_VEGETATION::l_trif_crop`.

If neither the phenology model nor the crop model are used, LAI for each vegetation tile can be set to a constant (:nml:mem:`JULES_PFTPARM::lai_io`) or a time series or seasonal cycle can be prescribed (:nml:lst:`JULES_PRESCRIBED`).

To simulate carbon and nitrogen stocks in the soil, the 4-pool model should be selected by setting :nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 2. This option adds prognostic soil pools and must be used with the TRIFFID vegetation model. If TRIFFID is not used, prescribed soil pools must be invoked via :nml:mem:`JULES_SOIL_BIOGEOCHEM::soil_bgc_model` = 1. Layered soil pools are used if :nml:mem:`JULES_SOIL_BIOGEOCHEM::l_layeredc` = .TRUE..

A multi-layer snow model can be selected using :nml:mem:`JULES_SNOW::nsmax`. Parameterisations of surface and subsurface runoff generation are controlled using :nml:mem:`JULES_HYDROLOGY::l_top` and :nml:mem:`JULES_HYDROLOGY::l_pdm`, while the routing of water in rivers uses :nml:mem:`JULES_RIVERS::l_rivers`.
