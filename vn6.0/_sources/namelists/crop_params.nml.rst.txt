``crop_params.nml``
===================


This file contains a single namelist called :nml:lst:`JULES_CROPPARM` that sets time- and space-invariant parameters for each crop type.


``JULES_CROPPARM`` namelist members
-----------------------------------

.. nml:namelist:: JULES_CROPPARM

This namelist reads the values of parameters for each of the crop functional types. These parameters are a function of crop pft only.  These parameters are only required if :nml:mem:`JULES_SURFACE_TYPES::ncpft` > 0.  The crop pfts should be in the same order as in :doc:`pft_params.nml`. 

.. seealso::
   References:
  
   * Osborne et al, `JULES-crop: a parametrisation of crops in the Joint UK Land Environment Simulator <http://www.geosci-model-dev.net/8/1139/2015/gmd-8-1139-2015.html>`_, Geosci. Model Dev., 8, 1139-1155, 2015.
  
   Parameters introduced after the Osborne et al 2015 paper are described in the appendix of
   
   * Williams et al, `Evaluation of JULES-crop performance against site observations of irrigated maize from Mead, Nebraska <https://www.geosci-model-dev.net/10/1291/2017/gmd-10-1291-2017.html>`_, Geosci. Model Dev., 10, 1291-1320, 2017.

.. nml:member:: t_bse_io

   :type: real(ncpft)
   :default: None

   Base temperature (K).


.. nml:member:: t_opt_io

   :type: real(ncpft)
   :default: None

   Optimum temperature (K).


.. nml:member:: tmax_io

   :type: real(ncpft)
   :default: None

   Maximum temperature (K).


.. nml:member:: tt_emr_io

   :type: real(ncpft)
   :default: None

   Thermal time between sowing and emergence (deg Cd).


.. nml:member:: crit_pp_io

   :type: real(ncpft)
   :default: None

   Critical photoperiod (hours).         


.. nml:member:: pp_sens_io

   :type: real(ncpft)
   :default: None

   Sensitivity of development rate to photoperiod (hours\ :sup:`-1`).


.. nml:member:: rt_dir_io

   :type: real(ncpft)
   :default: None

   Coefficient determining relative growth of roots vertically and horizontally.

  
.. nml:member:: alpha1_io

   :type: real(ncpft)
   :default: None

   Coefficient for determining partitioning.
   
   
.. nml:member:: alpha2_io

   :type: real(ncpft)
   :default: None

   Coefficient for determining partitioning.
   

.. nml:member:: alpha3_io

   :type: real(ncpft)
   :default: None

   Coefficient for determining partitioning.


.. nml:member:: beta1_io

   :type: real(ncpft)
   :default: None

   Coefficient for determining partitioning.

   
.. nml:member:: beta2_io

   :type: real(ncpft)
   :default: None

   Coefficient for determining partitioning.
   
   
.. nml:member:: beta3_io

   :type: real(ncpft)
   :default: None

   Coefficient for determining partitioning.


.. nml:member:: gamma_io

   :type: real(ncpft)
   :default: None

   Coefficient for determining specific leaf area (m\ :sup:`2` kg\ :sup:`-1`).
   
   
.. nml:member:: delta_io

   :type: real(ncpft)
   :default: None

   Coefficient for determining specific leaf area (m\ :sup:`2` kg\ :sup:`-1`).
   
   
.. nml:member:: remob_io

   :type: real(ncpft)
   :default: None

   Remobilisation factor. Fraction of stem growth partitioned to RESERVEC.


.. nml:member:: cfrac_s_io

   :type: real(npft)
   :default: None

   Carbon fraction of dry matter for stems.


.. nml:member:: cfrac_r_io

   :type: real(ncpft)
   :default: None

   Carbon fraction of dry matter for roots.


.. nml:member:: cfrac_l_io

   :type: real(ncpft)
   :default: None

   Carbon fraction of dry matter for leaves.


.. nml:member:: allo1_io

   :type: real(ncpft)
   :default: None

   Allometric coefficient relating STEMC to CANHT.


.. nml:member:: allo2_io

   :type: real(ncpft)
   :default: None

   Allometric coefficient relating STEMC to CANHT.


.. nml:member:: mu_io

   :type: real(ncpft)
   :default: None

   Allometric coefficient for calculation of senescence. MIN(mu_io * (dvi - sen_dvi_io) ** nu_io, 1.0) is the fraction of leaf carbon that is moved to the harvest pool per day once senescence has started.


.. nml:member:: nu_io

   :type: real(ncpft)
   :default: None

   Allometric coefficient for calculation of senescence. See description for :nml:mem:`mu_io`


.. nml:member:: yield_frac_io

   :type: real(ncpft)
   :default: None

   Fraction of the harvest carbon pool converted to yield carbon (yield is the economically valuable component of the harvest pool e.g. kernel).


.. nml:member:: initial_carbon_io

   :type: real(ncpft)
   :default: None

   Carbon in crop at emergence in kgC/m2.
   
   
.. nml:member:: initial_c_dvi_io

   :type: real(ncpft)
   :default: None

   DVI at which the crop carbon is set to :nml:mem:`initial_carbon_io`. Should be at emergence (0.0) or shortly after. 


.. nml:member:: sen_dvi_io

   :type: real(ncpft)
   :default: None

   DVI at which leaf senescence begins. 


.. nml:member:: t_mort_io

   :type: real(ncpft)
   :default: None

   Soil temperature (second level) at which to kill crop if DVI>1.
