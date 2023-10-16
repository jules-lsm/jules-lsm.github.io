``model_environment.nml``
=========================


This file sets the model environment options e.g. whether JULES is
coupled to the UM or run in a standalone environment. It contains one
namelist called :nml:lst:`JULES_MODEL_ENVIRONMENT`.

There are many JULES science options that are in shared namelists, so
they can be read both by standalone and by a model driving JULES
e.g. the UM. However some options either make no scientific sense or
the necessary input data are not available to the environment in which
JULES is being driven as the plumbing has not yet been done. This
causes problems for example when creating standalone apps from UM
configurations. This namelist allows the environment in which JULES is
being run to be specified so that options that are unavailable can be
made inaccessible via the metadata and thus will not appear in the
gui. Warnings can also be issued if options are inappropriately set.

This namelist also describes the flavour of the land surface model
being used. CABLE is in the process of being incorporated into JULES
and other flavours of JULES is in development e.g. a standalone rivers
app.

``JULES_MODEL_ENVIRONMENT`` namelist members
--------------------------------------------

.. nml:namelist:: JULES_MODEL_ENVIRONMENT

.. nml:member:: l_jules_parent

   :type: integer
   :default: imdi

   Switch to identify the environment in which JULES is being run. The
   switch should only be used to allow science options, which are not
   available in the specified model environment, to be trigger ignored
   and checked that they are set appropriately at run-time.

      = ==============================
      0 JULES is being run standalone. |br|
	Any options that are only available to the parent model (e.g. the UM) will be trigger ignored.
      1 JULES is being run coupled to the UM. |br|
      2 JULES is being run coupled via OASIS (available to Rivers-only executable only). |br|
        Options not available to the UM are trigger-ignored.
      = ==============================

   .. warning::
      No science code should be associated with this switch, only what
      science options are available.

   .. note::
      The metadata of the parent model only actually allows the
      appropriate option to be specified i.e. in standalone only 0 is
      permitted and in the UM only 1 is permitted. Any other parent
      models are listed here for information only. It is not
      appropriate to include a list of the unavailable options
      here. However, information for namelists that have been
      consolidated will appear in the following checking routines as
      they are completed.

      * `src/control/standalone/check_unavailable_options_mod.F90
	<https://code.metoffice.gov.uk/trac/jules/browser/main/trunk/src/control/standalone/check_unavailable_options_mod.F90>`_
      * `src/control/um/check_jules_unavailable_options_mod.F90
	<https://code.metoffice.gov.uk/trac/jules/browser/main/trunk/src/control/um/check_jules_unavailable_options_mod.F90>`_

.. nml:member:: lsm_id

   :type: integer
   :default: MDI

   Switch for land surface model flavour.

      = ========================
      1 JULES land surface model
      2 CABLE land surface model
      = ========================

   .. note::
      The CABLE model has not yet been implemented within the JULES repository.

.. |br| raw:: html

   <br />
