``jules_surface_types.nml``
===========================
.. _top_jules_surface_types:

This file configures the surface types used by JULES. It contains one
namelist called :nml:lst:`JULES_SURFACE_TYPES`.

The surface type IDs, which were introduced in the UM in order to
identify the surface types present in input and output, have been made
available to standalone. The defined surface type IDs are given in the
description here in brackets (#). In order to keep the GUI from
appearing cluttered, the surface types have been added with
``compulsory=false``, unless they are attached to specific science
options allowing them to be triggered off, which would be the
preferred method. A ``compulsory=false`` surface type, can be added
and removed in the GUI window as described in the table below. To:

   ====== =================================================
   Add    "Add latent variable" using the right click menu, which opens a list of defined surface types.
   Remove "Remove" the variable using the cog menu.
   ====== =================================================

.. note:: Please be aware that while the surface type IDs have been
	  made available and are used to check the surface type
	  configuration at runtime, they are not yet used by the JULES
	  I/O.

``JULES_SURFACE_TYPES`` namelist members
----------------------------------------


.. nml:namelist:: JULES_SURFACE_TYPES

.. note::
   The total number of surface types to be modelled is called ``ntype``, and is given by ``ntype = npft + nnvg``.

   In the original setup, JULES models 5 vegetation types and 4 non-vegetation types (``npft = 5``, ``nnvg = 4``). However, the model domain need not contain all 9 types, e.g. the domain could consist of a single point with 100% grass. The amount of each type in the domain is normally set in :nml:lst:`JULES_FRAC`.

   If the crop model is active (i.e. ``ncpft`` > 0), then ``nnpft = npft - ncpft`` where ``nnpft`` is the number of natural PFTs.

   Vegetation surfaces must always be present first in any list of surfaces.

.. nml:member:: npft

   :type: integer
   :permitted: >= 1
   :default: -32768

   The number of plant functional types (PFTs) to be modelled.


.. nml:member:: ncpft

   :type: integer
   :permitted: < npft
   :default: 0

   The number of crop plant functional types to be modelled.


.. nml:member:: nnvg

   :type: integer
   :permitted: >= 1
   :default: -32768

   The number of non-plant surface types to be modelled.

.. nml:group:: Non-vegetated surface types

   A negative value, when permitted, indicates that the surface type
   is not in use.

   .. nml:member:: urban

      :type: integer
      :permitted: -1, npft+1:ntype
      :default: -32768

      Index of the urban surface type (#6).

      Can only be used if :nml:mem:`JULES_SURFACE::l_urban2t` = FALSE.


   .. nml:member:: lake

      :type: integer
      :permitted: npft+1:ntype
      :default: -32768

      Index of the lake surface type (#7).


   .. nml:member:: soil

      :type: integer
      :permitted: npft+1:ntype
      :default: -32768

      Index of the soil surface type (#8).

      .. note:: A soil surface type must be given (although the fraction may be set to zero).


   .. nml:member:: ice

      :type: integer
      :permitted: npft+1:ntype
      :default: -32768

      Index of the ice surface type (#9).

      .. note:: In the UM the ice surface type must be specified (although the fraction may be set to zero).


   .. nml:group:: Multiple ice tiles allowed to exist in an ice gridbox

      These surface types can only be used when multiple ice tiles are
      allowed in a gridbox i.e. when
      :nml:mem:`JULES_SURFACE::l_elev_land_ice` = TRUE.

      .. nml:member:: elev_ice

	 :type: integer
	 :permitted: -1,npft+1:ntype
	 :default: -32768

	 Indices of the elevated ice types (#901-925).

	 Must be grouped together with values ``npft < elev_ice <=
	 ntype`` OR ``elev_ice = -1`` to indicate they are not used
	 (i.e. all elevated rock instead).

      .. nml:member:: elev_rock

	 :type: integer
	 :permitted: -1,npft+1:ntype
	 :default: -32768

	 Indices of the elevated non-glaciated bedrock types
	 (#926-950).

	 Must be grouped together, with values ``npft < elev_rock <=
	 ntype`` OR ``elev_rock = -1`` to indicate they are not used
	 (i.e. all elevated ice instead).


   .. nml:group:: Two-tile urban schemes including MORUSES

      These surface types can only be used when :nml:mem:`JULES_SURFACE::l_urban2t` = TRUE.

      .. nml:member:: urban_canyon

	 :type: integer
	 :permitted: npft+1:ntype
	 :default: -32768

	 Index of the urban canyon surface type (#601).


      .. nml:member:: urban_roof

	 :type: integer
	 :permitted: npft+1:ntype
	 :default: -32768

	 Index of the urban roof surface type (#602).


      .. note::

	 When giving urban fraction data (see :nml:lst:`JULES_FRAC`), total *urban* fraction may be given instead of the separate canyon and roof fractions by entering it under the canyon fraction. When initialising if the roof fraction is zero, the canyon fraction will be interpreted as the total *urban* fraction and be partitioned according to the canyon fraction (W/R, see :nml:lst:`URBAN_PROPERTIES`).

.. nml:group:: Surface types with ``compulsory=false``

   These are required to allow the surface type configuration to be
   checked at runtime and for surface types to be identified in the
   output headers. These are added as a latent variable. Remove the
   surface type if it is not required (see explanation at the
   :ref:`top<top_jules_surface_types>` of this page).

   .. nml:member:: usr_type

      :type: integer
      :permitted: 1:ntype
      :default: -32768

      Index of user specified surface type (#10-99).

      A user surface type can be used when experimenting with new
      surface configurations without a code change. These can be
      either vegetated or non-vegetated and are used solely to assign an
      ID number.

   .. nml:group:: Vegetated surface types

      A negative value, when permitted, indicates that the surface
      type is not in use.

      .. nml:member:: brd_leaf

	 :type: integer
	 :permitted: 1:npft
	 :default: -32768

	 Index of the original broadleaf PFT surface type (#1).

      .. nml:member:: brd_leaf_dec

	 :type: integer
	 :permitted: 1:npft
	 :default: -32768

	 Index of broadleaf (decidous) PFT surface type (#101)

      .. nml:member:: brd_leaf_eg_trop

	 :type: integer
	 :permitted: 1:npft
	 :default: -32768

	 Index of broadleaf (evergreen tropical) PFT surface type (#102).

      .. nml:member:: brd_leaf_eg_temp

	 :type: integer
	 :permitted: 1:npft
	 :default: -32768

	 Index of broadleaf (evergreen temperate) PFT surface type (#103).

      .. nml:member:: ndl_leaf

	 :type: integer
	 :permitted: 1:npft
	 :default: -32768

	 Index of original needleleaf PFT surface type (#2).

      .. nml:member:: ndl_leaf_dec

	 :type: integer
	 :permitted: 1:npft
	 :default: -32768

	 Index of needleleaf (deciduous) PFT surface type (#201).

      .. nml:member:: ndl_leaf_eg

	 :type: integer
	 :permitted: 1:npft
	 :default: -32768

	 Index of needleleaf (evergreen) PFT surface type (#202).

      .. nml:member:: c3_grass

	 :type: integer
	 :permitted: 1:npft
	 :default: -32768

	 Index of original C3 grass PFT surface type (#3).

      .. nml:member:: c3_crop

	 :type: integer
	 :permitted: 1:npft
	 :default: -32768

	 Index of C3 crop PFT surface type (#301).

      .. nml:member:: c3_pasture

	 :type: integer
	 :permitted: 1:npft
	 :default: -32768

	 Index of C3 pasture PFT surface type (#302).

      .. nml:member:: c4_grass

	 :type: integer
	 :permitted: 1:npft
	 :default: -32768

	 Index of original C4 grass PFT surface type (#4).

      .. nml:member:: c4_crop

	 :type: integer
	 :permitted: 1:npft
	 :default: -32768

	 Index of C4 crop PFT surface type (#401).

      .. nml:member:: c4_pasture

	 :type: integer
	 :permitted: 1:npft
	 :default: -32768

	 Index of C4 pasture PFT surface type (#402).

      .. nml:member:: shrub

	 :type: integer
	 :permitted: 1:npft
	 :default: -32768

	 Index of original shrub PFT surface type (#5).

      .. nml:member:: shrub_dec

	 :type: integer
	 :permitted: 1:npft
	 :default: -32768

	 Index of shrub (deciduous) PFT surface type (#501).

      .. nml:member:: shrub_eg

	 :type: integer
	 :permitted: 1:npft
	 :default: -32768

	 Index of shrub (evergreen) PFT surface type (#502).
