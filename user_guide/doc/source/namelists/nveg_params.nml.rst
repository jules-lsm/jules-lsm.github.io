``nveg_params.nml``
===================


This file contains a namelist called :nml:lst:`JULES_NVEGPARM` that sets time-invariant parameters for non-vegetation surface types for the JULES land surface model.

``JULES_NVEGPARM`` namelist members
-----------------------------------

.. nml:namelist:: JULES_NVEGPARM


This namelist reads the values of parameters for each of the non-vegetation surface types if the JULES land surface model is being used. These parameters are a function of surface type only. All parameters must be defined for any configuration.

HCTN30 refers to Hadley Centre technical note 30, available from `the Met Office Library <http://www.metoffice.gov.uk/learning/library/publications/science/climate-science-technical-notes>`_.


.. nml:member:: albsnc_nvg_io

   :type: real(nnvg)
   :default: None

   Snow-covered albedo.

   Only used if :nml:mem:`JULES_RADIATION::l_snow_albedo` = FALSE. See HCTN30 Table 1.


.. nml:member:: albsnf_nvg_io

   :type: real(nnvg)
   :default: None

   Snow-free albedo.

   See HCTN30 Table 1.

   A  bare soil snow-free albedo of -1.0 indicates that it is supplied by an ancillary field.


.. nml:member:: albsnf_nvgu_io

   :type: real(nnvg)
   :default: None

   Upper limit on snow-free albedo, when :nml:mem:`JULES_RADIATION::l_albedo_obs` = TRUE.


.. nml:member:: albsnf_nvgl_io

   :type: real(nnvg)
   :default: None

   Lower limit on snow-free albedo, when :nml:mem:`JULES_RADIATION::l_albedo_obs` = TRUE.


.. nml:member:: catch_nvg_io

   :type: real(nnvg)
   :default: None

   Capacity for water (kg m\ :sup:`-2`).

   See HCTN30 p7.


.. nml:member:: gs_nvg_io

   :type: real(nnvg)
   :default: None

   Surface conductance (m s\ :sup:`-1`).

   See HCTN30 p7. Soil conductance is modified by soil moisture according to HCTN30 Eq35.


.. nml:member:: infil_nvg_io

   :type: real(nnvg)
   :default: None

   Infiltration enhancement factor.

   The maximum infiltration rate defined by the soil parameters for the whole gridbox may be modified for each surface tile to account for tile-dependent factors.

   See HCTN30 p14 for full details.

.. nml:member:: irrig_nvg_io

   :type: integer(nnvg)
   :default: nnvg*0

   Switch for the tile-based irrigaton scheme only. 
   Value indicates whether the non-vegetated surface tile is irrigated or not, where 0 = Not irrigated and 1 = Irrigated. 
   Can only be set to 1 if :nml:mem:`JULES_IRRIG::l_irrig_dmd` = F.
    
   For the fraction-based irrigation demand code please set up your namelists using the instructions in the :nml:lst:`JULES_IRRIG` namelist.

.. nml:member:: z0_nvg_io

   :type: real(nnvg)
   :default: None

   Roughness length for momentum (m).

   See HCTN30 Table 4.


.. nml:member:: ch_nvg_io

   :type: real(nnvg)
   :default: None

   Heat capacity of this surface type (J K\ :sup:`-1` m\ :sup:`-2`).

   Used only if :nml:mem:`JULES_VEGETATION::can_model` is 3 or 4.


.. nml:member:: vf_nvg_io

   :type: real(nnvg)
   :default: None

   Fractional coverage of non-vegetation "canopy".

   Typically set to 0.0 (conductively coupled), but value of 1.0 (radiatively coupled) used if surface tile should have a heat capacity in conjunction with :nml:mem:`JULES_VEGETATION::can_model` options 3 or 4.

   .. note:: If :nml:mem:`JULES_URBAN::l_moruses_storage` = T, then for the roof coupling: 0 = **uncoupled**

.. nml:member:: emis_nvg_io

   :type: real(nnvg)
   :default: None

   Surface emissivity of non-vegetated surfaces.


.. nml:member:: z0hm_nvg_io

   :type: real(nnvg)
   :default: None

   Ratio of the roughness length for heat to the roughness length for momentum.

   This is generally assumed to be 0.1. See HCTN30 p6. Note that this is the ratio of the roughness length for heat to that for momentum. It does not alter the roughness length for momentum, which is given by :nml:mem:`z0_nvg_io`.


.. nml:member:: z0hm_classic_nvg_io

   :type: real(nnvg)
   :default: None

   Ratio of the roughness length for heat to the roughness length for momentum *for the CLASSIC aerosol scheme only*.

   .. note:: This makes no difference to the model when running standalone, and is only required to keep the standalone and UM interfaces consistent.
