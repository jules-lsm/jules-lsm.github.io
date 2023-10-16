``jules_radiation.nml``
=======================


This file sets the radiation options. It contains one namelist called :nml:lst:`JULES_RADIATION`.



``JULES_RADIATION`` namelist members
-------------------------------------

.. nml:namelist:: JULES_RADIATION

.. nml:member:: l_cosz

   :type: logical
   :default: T

   Switch for calculation of solar zenith angle.

   TRUE
       Calculate zenith angle.

   FALSE
       Assume constant zenith angle of zero, meaning sun is directly overhead.

   n.b. assuming that the sun is directly overhead may overestimate primary productivity if :nml:mem:`JULES_VEGETATION::l_triffid` = TRUE (see GPP on :ref:`output_variables_section`).


.. nml:member:: l_spec_albedo

   :type: logical
   :default: F

   Switch for the two-stream spectral land-surface albedo model.

   TRUE
       Use spectral albedo with VIS and NIR components.

   FALSE
       Use a single (averaged) waveband albedo.


.. nml:member:: l_spec_alb_bs

   :type: logical
   :default: F

   Switch for albedo model, when spectral albedo is being used.

   Requires :nml:mem:`l_spec_albedo` = TRUE.

   TRUE
       Produces a single albedo for use by both the direct and diffuse beams (a 'blue' sky albedo). This currently copies the diffuse beam albedo for the direct beam.

   FALSE
       Produces both a direct ('black' sky) and a diffuse ('white' sky) albedo.
       
       
.. nml:member:: l_niso_direct

   :type: logical
   :default: F

   Switch for using full non-isotropic expression for direct
   scattering in plant canopies when using the two-stream canopy
   radiation model.

   Requires :nml:mem:`l_spec_albedo` = TRUE.

   TRUE
       Use full non-isotropic expression for scattering in plant canopies.

   FALSE
       Use the original isotropic expression.


.. nml:member:: l_snow_albedo

   :type: logical
   :default: F

   Switch for using prognostic snow properties, which represents the
   effect of snow aging and soot deposition, in model albedo.

   Requires :nml:mem:`l_spec_albedo` = TRUE.

   TRUE
       Use prognostic snow properties for albedo.

   FALSE
       Calculate albedo of snow using only snow depth.
       
.. nml:member:: l_embedded_snow

   :type: logical
   :default: F

   Switch to account for pft LAI and pft height in calculation of snow albedo.

   TRUE
      Use the embedded canopy snow albedo model. This is exclusive of :nml:mem:`JULES_RADIATION::l_snow_albedo`.

   FALSE
       No effect.
  
.. nml:member:: l_mask_snow_orog

   :type: logical
   :default: F

   Switch for orographic masking of snow, which decreases the albedo
   of snow in mountainous regions.

   TRUE
      Include orographic masking of snow in calculating albedo.

   FALSE
      No effect.

       
.. nml:member:: l_albedo_obs

   :type: logical
   :default: F

   Switch for applying a scaling factor to the albedo values, on
   surface tiles, so that the resultant aggregate albedo matches
   observations. The supplied albedos should be from an observed
   climatology or analysis system and be supplied via an ancillary
   file.

   TRUE
       Scale the albedo values on tiles within the physical limits
       supplied in :nml:lst:`JULES_PFTPARM` and
       :nml:lst:`JULES_NVEGPARM`. When
       :nml:mem:`JULES_RADIATION::l_spec_albedo` = TRUE, VIS and NIR
       components are required and when
       :nml:mem:`JULES_RADIATION::l_spec_albedo` = FALSE the single
       (averaged) waveband albedo is required.

       .. note:: Observed albedo(s) must be prescribed in
		 :doc:`prescribed_data.nml`.

   FALSE
       Do not scale the albedo values on tiles.

.. nml:member:: l_spec_sea_alb

   :type: logical
   :default: F

   Switch to use spectrally varying open sea albedos

   TRUE
      When :nml:mem:`JULES_RADIATION::i_sea_alb_method` = 1 or 2,
      spectrally varying sea albedos are produced only when the spectral
      file contains 6 SW bands identical to those used in HadGEM1.

      When :nml:mem:`JULES_RADIATION::i_sea_alb_method` = 3, the spectral
      variability is calculated as per the Jin et al. (2011)
      parameterisation.

   FALSE
      Uses the calculated broadband sea albedo instead.

.. nml:member:: i_sea_alb_method

   :type: integer
   :default: None

   Choice of model for the Ocean Surface Albedo (open water, ice free)

   1. Diffuse albedo constant (0.06), direct albedo from Briegleb and
      Ramanathan (1982).

   2. Diffuse albedo constant (0.06), direct albedo from Barker and
      Li (1995).

   3. Direct and diffuse albedo from Jin et al. (2011).

   4. Fixed global value, defined by :nml:mem:`JULES_RADIATION::fixed_sea_albedo`.

   5. Fixed global value, defined by
      :nml:mem:`JULES_RADIATION::fixed_sea_albedo`, above 271K and
      variable below this to simulate sea-ice following Liu et
      al. (2007), Joshi & Haberle (2012) and Turbet et al. (2016).

.. nml:member:: fixed_sea_albedo

   :type: real
   :default: None

   The global value of sea albedo to use if :nml:mem:`JULES_RADIATION::i_sea_alb_method` = 4, 5

.. nml:member:: wght_alb

   :type: real(4)
   :default: MDI

   Weights to form the overall albedo from its components (VIS direct,
   VIS diffuse, NIR direct, NIR diffuse)
   (Ideally, if :nml:mem:`JULES_RADIATION::l_partition_albsoil` = T,
   :nml:mem:`JULES_RADIATION::wght_alb` and 
   :nml:mem:`JULES_RADIATION::swdn_frac_albsoil` should be consistent, with
   :nml:mem:`JULES_RADIATION::swdn_frac_albsoil` equal to 
   :math:`\sum_{3,4}`
   :nml:mem:`JULES_RADIATION::wght_alb` :math:`/ \sum_1^4` 
   :nml:mem:`JULES_RADIATION::wght_alb`.
   However, :nml:mem:`JULES_RADIATION::swdn_frac_albsoil` 
   is applied only to bare soil and having a single parameter 
   is more transparent to the user, while 
   :nml:mem:`JULES_RADIATION::wght_alb`
   is used only in diagnostics in standalone JULES and may have
   historical settings. Hence, the consistency of these two variables
   is not enforced.)

.. nml:member:: l_hapke_soil

   :type: logical
   :default: F

   Switch to enable Hapke's model of soil albedo to include a zenith-angle
   dependence

   TRUE
      Apply a zenith-angle dependence to the direct albedo.

   FALSE
      Use the diffuse albedo for the direct beam as well.

.. nml:member:: l_partition_albsoil

   :type: logical
   :default: F

   Switch to apply a spectral partitioning to the soil albedo.

   TRUE
      Partition the soil albedo between the visible and near infrared parts
      of the spectrum using :nml:mem:`JULES_RADIATION::ratio_albsoil` and 
      :nml:mem:`JULES_RADIATION::swdn_frac_albsoil`.

   FALSE
      Apply the broadband albedo in both spectral regions.

.. nml:member:: ratio_albsoil

   :type: real
   :default: MDI

   Ratio of the NIR to the VIS albedo of bare soil.
   Used if :nml:mem:`JULES_RADIATION::l_partition_albsoil` = T.

.. nml:member:: swdn_frac_albsoil

   :type: real
   :default: MDI

   The fraction of the total downward SW radiation assumed to be in the
   NIR part of the spectrum for partitioning the soil albedo.
   Used if :nml:mem:`JULES_RADIATION::l_partition_albsoil` = T.
   (Ideally, :nml:mem:`JULES_RADIATION::wght_alb` and 
   :nml:mem:`JULES_RADIATION::swdn_frac_albsoil` should be consistent, with
   :nml:mem:`JULES_RADIATION::swdn_frac_albsoil` equal to 
   :math:`\sum_{3,4}`
   :nml:mem:`JULES_RADIATION::wght_alb` :math:`/ \sum_1^4` 
   :nml:mem:`JULES_RADIATION::wght_alb`.
   However, :nml:mem:`JULES_RADIATION::swdn_frac_albsoil` is applied 
   only to bare soil and having a single parameter is more transparent 
   to the user, while :nml:mem:`JULES_RADIATION::wght_alb`
   is used only in diagnostics in standalone JULES and may have
   historical settings. Hence, the consistency of these two variables
   is not enforced.)

.. seealso::
   References:

   * Barker, H.W. and Li, Z. (1995), Improved Simulation of Clear-Sky
     Shortwave Radiative Transfer in the CCC-GCM. J. Climate, 8,
     2213–2223, `doi:10.1175/1520-0442(1995)008<2213:ISOCSS>2.0.CO;2
     <https://doi.org/10.1175/1520-0442%281995%29008%3C2213%3AISOCSS%3E2.0.CO%3B2>`_
   * Briegleb, B. and Ramanathan, V. (1982), Spectral and Diurnal
     Variations in Clear Sky Planetary Albedo. J. Appl. Meteor., 21,
     1160–1171, `doi:10.1175/1520-0450(1982)021<1160:SADVIC>2.0.CO;2
     <https://doi.org/10.1175/1520-0450%281982%29021%3C1160%3ASADVIC%3E2.0.CO%3B2>`_
   * Liu, J. , Zhang, Z. , Inoue, J. and Horton, R. M. (2007),
     Evaluation of snow/ice albedo parameterizations and their impacts
     on sea ice simulations. Int. J. Climatol., 27:
     81-91. `doi:10.1002/joc.1373
     <https://doi.org/10.1002/joc.1373>`_
   * Zhonghai Jin, Yanli Qiao, Yingjian Wang, Yonghua Fang, and
     Weining Yi, "A new parameterization of spectral and broadband
     ocean surface albedo", Opt. Express 19, 26429-26443 (2011),
     `doi:10.1364/OE.19.026429
     <https://doi.org/10.1364/OE.19.026429>`_
   * B. Hapke, "Bidirectional reflectance spectroscopy: 1. Theory",
     J. Geophys. Res. 86(B4), 3039-3054 (1981),
     `doi:10.1029/JB086iB04p03039
     <http://doi.org/10.1029/JB086iB04p03039>`_
   * Manoj M. Joshi and
     Robert M. Haberle. Astrobiology. Jan 2012. ahead of print
     `doi:10.1089/ast.2011.0668
     <http://doi.org/10.1089/ast.2011.0668>`_
   * Martin Turbet, Jérémy Leconte, Franck Selsis, Emeline Bolmont,
     François Forget, Ignasi Ribas, Sean N. Raymond and Guillem
     Anglada-Escudé (2016), The habitability of Proxima Centauri
     b - II. Possible climates and observability, A&A, 596, A112,
     `doi:10.1051/0004-6361/201629577
     <https://doi.org/10.1051/0004-6361/201629577>`_
