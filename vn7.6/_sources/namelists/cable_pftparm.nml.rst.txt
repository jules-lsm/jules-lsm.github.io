``cable_pftparm.nml``
=====================

This file sets the time and space-invariant parameters for plant functional types for the CABLE land surface model. It contains one namelist called :nml:lst:`CABLE_PFTPARM`.

``CABLE_PFTPARM`` namelist members
-----------------------------------

.. nml:namelist:: CABLE_PFTPARM

This namelist reads the values of parameters for each of the plant functional types (PFTs) if the CABLE land surface model is being used. These parameters are a function of PFT only. Every member must be given a value for every run.
CABLE uses the same parameters for veg and non-veg surface types, unlike JULES, and therefore its arrays are of dimension (npft + nnvg).

.. nml:member:: a1gs_io

   :type: real(npft + nnvg)
   :default: MDI

   Represents the sensitivity of stomatal conductance to the assimilation rate (unitless).

.. nml:member:: alpha_io

   :type: real(npft + nnvg)
   :default: MDI

   Initial slope of J-Q response curve. Units: mol (electrons) mol\ :sup:`-1` (photons) (C3)
   mol (CO\ :sub:`2`) mol\ :sup:`-1` (photons) (C4)

.. nml:member:: canst1_io

   :type: real(npft + nnvg)
   :default: MDI

   Maximum intercepted water by canopy. (mm LAI\ :sup:`-1`)

.. nml:member:: cfrd_io

   :type: real(npft + nnvg)
   :default: MDI

   Ratio of day respiration to vcmax

.. nml:member:: clitt_io

   :type: real(npft + nnvg)
   :default: MDI

   Leaf litter (alters resistance to soil evaporation) (tC ha\ :sup:`-1`)

.. nml:member:: conkc0_io

   :type: real(npft + nnvg)
   :default: MDI

   Michaelis-menton constant for carboxylase (bar)

.. nml:member:: conko0_io

   :type: real(npft + nnvg)
   :default: MDI

   Michaelis-menton constant for oxygenase (bar)

.. nml:member:: convex_io

   :type: real(npft + nnvg)
   :default: MDI

   Convexity of J-Q response curve (unitless).

.. nml:member:: cplant1_io

   :type: real(npft + nnvg)
   :default: MDI

   Plant carbon in 1st vegetation carbon store (g C m\ :sup:`-2`)

.. nml:member:: cplant2_io

   :type: real(npft + nnvg)
   :default: MDI

   Plant carbon in 2nd vegetation carbon store (g C m\ :sup:`-2`)

.. nml:member:: cplant3_io

   :type: real(npft + nnvg)
   :default: MDI

   Plant carbon in 3rd vegetation carbon store (g C m\ :sup:`-2`)

.. nml:member:: csoil1_io

   :type: real(npft + nnvg)
   :default: MDI

   Soil carbon in 1st soil carbon store (g C m\ :sup:`-2`)

.. nml:member:: csoil2_io

   :type: real(npft + nnvg)
   :default: MDI

   Soil carbon in 2nd soil carbon store (g C m\ :sup:`-2`)

.. nml:member:: d0gs_io

   :type: real(npft + nnvg)
   :default: MDI

   d0 in stomatal conductance model (kPa)

.. nml:member:: ejmax_io

   :type: real(npft + nnvg)
   :default: MDI

   Maximum potential electron transport rate top leaf, currently double the assigned value of vcmax. (mol m\ :sup:`-2` s\ :sup:`-1`)

.. nml:member:: ekc_io

   :type: real(npft + nnvg)
   :default: MDI

   Activation energy for carboxylase (J mol\ :sup:`-1`)

.. nml:member:: eko_io

   :type: real(npft + nnvg)
   :default: MDI

   Activation energy for oxygenase (J mol\ :sup:`-1`)

.. nml:member:: extkn_io

   :type: real(npft + nnvg)
   :default: MDI

   Extinction coefficient for vertical profile of N.

.. nml:member:: frac4_io

   :type: real(npft + nnvg)
   :default: MDI

   Fraction of c4 plants

.. nml:member:: froot1_io

   :type: real(npft + nnvg)
   :default: MDI

   Fraction of root in 1st soil layer.

.. nml:member:: froot2_io

   :type: real(npft + nnvg)
   :default: MDI

   Fraction of root in 2nd soil layer.

.. nml:member:: froot3_io

   :type: real(npft + nnvg)
   :default: MDI

   Fraction of root in 3rd soil layer.

.. nml:member:: froot4_io

   :type: real(npft + nnvg)
   :default: MDI

   Fraction of root in 4th soil layer.

.. nml:member:: froot5_io

   :type: real(npft + nnvg)
   :default: MDI

   Fraction of root in 5th soil layer.

.. nml:member:: froot6_io

   :type: real(npft + nnvg)
   :default: MDI

   Fraction of root in 6th soil layer.

.. nml:member:: g0_io

   :type: real(npft + nnvg)
   :default: MDI

   Residual stomatal conductance as net assimilation rate reaches zero (mol m\ :sup:`-2` s\ :sup:`-1`)

.. nml:member:: g1_io

   :type: real(npft + nnvg)
   :default: MDI

   Sensitivity of stomatal conductance to the assimilation rate (kPa).

.. nml:member:: gswmin_io

   :type: real(npft + nnvg)
   :default: MDI

   Minimal stomatal conductance (mol m\ :sup:`-2` s\ :sup:`-1`)

.. nml:member:: hc_io

   :type: real(npft + nnvg)
   :default: MDI

   Height of canopy (m)

.. nml:member:: lai_io

   :type: real(npft + nnvg)
   :default: None

   The leaf area index (LAI) of each PFT.

.. nml:member:: length_io

   :type: real(npft + nnvg)
   :default: MDI

   Leaf length (m)

.. nml:member:: ratecp1_io

   :type: real(npft + nnvg)
   :default: MDI

   Plant carbon pool rate constant in 1st vegetation carbon store (year\ :sup:`-1`).

.. nml:member:: ratecp2_io

   :type: real(npft + nnvg)
   :default: MDI

   Plant carbon pool rate constant in 2nd vegetation carbon store (year\ :sup:`-1`).

.. nml:member:: ratecp3_io

   :type: real(npft + nnvg)
   :default: MDI

   Plant carbon pool rate constant in 3rd vegetation carbon store (year\ :sup:`-1`).

.. nml:member:: ratecs1_io

   :type: real(npft + nnvg)
   :default: MDI

   Soil carbon pool rate constant in 1st soil carbon store (year\ :sup:`-1`).

.. nml:member:: ratecs2_io

   :type: real(npft + nnvg)
   :default: MDI

   Soil carbon pool rate constant in 2nd soil carbon store (year\ :sup:`-1`).

.. nml:member:: refl1_io

   :type: real(npft + nnvg)
   :default: MDI

   Leaf reflectance in 1st radiation band.

.. nml:member:: refl2_io

   :type: real(npft + nnvg)
   :default: MDI

   Leaf reflectance in 2nd radiation band.

.. nml:member:: refl3_io

   :type: real(npft + nnvg)
   :default: MDI

   Leaf reflectance in 3rd radiation band.

.. nml:member::rootbeta_io

   :type: real(npft + nnvg)
   :default: MDI

   Beta parameter (Jackson et al. 1996) to calculate froot

.. nml:member:: rp20_io

   :type: real(npft + nnvg)
   :default: MDI

   Plant respiration scaler

.. nml:member:: rpcoef_io

   :type: real(npft + nnvg)
   :default: MDI

   Temperature coefficient for non-leaf plant respiration (C\ :sup:`-1`)

.. nml:member:: rs20_io

   :type: real(npft + nnvg)
   :default: MDI

   Soil respiration at 20 deg C

.. nml:member:: shelrb_io

   :type: real(npft + nnvg)
   :default: MDI

   Sheltering factor

.. nml:member:: taul1_io

   :type: real(npft + nnvg)
   :default: MDI

   Leaf transmittance in 1st radiation band

.. nml:member:: taul2_io

   :type: real(npft + nnvg)
   :default: MDI

   Leaf transmittance in 2nd radiation band

.. nml:member:: taul3_io

   :type: real(npft + nnvg)
   :default: MDI

   Leaf transmittance in 3rd radiation band

.. nml:member:: tmaxvj_io

   :type: real(npft + nnvg)
   :default: MDI

   Maximum temperature of the start of photosynthesis (deg C)

.. nml:member:: tminvj_io

   :type: real(npft + nnvg)
   :default: MDI

   Minimum temperature of the start of photosynthesis (deg C)

.. nml:member:: vbeta_io

   :type: real(npft + nnvg)
   :default: MDI

   Stomatal sensitivity to soil water.

.. nml:member:: vcmax_io

   :type: real(npft + nnvg)
   :default: MDI

   Maximum RuBP carboxylation rate top leaf. (mol m\ :sup:`-2` s\ :sup:`-1`)

.. nml:member:: vegcf_io

   :type: real(npft + nnvg)
   :default: MDI

   Scalar on soil respiration (place-holder scheme)

.. nml:member:: wai_io

   :type: real(npft + nnvg)
   :default: MDI

   Wood area index (stem + branches + twigs) (not currently used in any calculations)

.. nml:member:: width_io

   :type: real(npft + nnvg)
   :default: MDI

   Leaf width (m)

.. nml:member:: xalbnir_io

   :type: real(npft + nnvg)
   :default: MDI

   Not currently used in any calculations.

.. nml:member:: xfang_io

   :type: real(npft + nnvg)
   :default: MDI

   Leaf angle parameter

.. nml:member:: zr_io

   :type: real(npft + nnvg)
   :default: MDI

   Maximum rooting depth (cm)

