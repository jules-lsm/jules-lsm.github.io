JULES version 3.3 Release Notes
===============================


Ability to run JULES in parallel
--------------------------------

JULES can now run multiple points in parallel, using multiple cores on the same machine or a cluster of machines. This is accomplished using `MPI (Message Passing Interface) <http://en.wikipedia.org/wiki/Message_Passing_Interface>`_, a standardised message passing interface. Several implementations of MPI are available, the most commonly used being `MPICH2 <http://www.mpich.org/>`_ and `OpenMPI <http://www.open-mpi.org/>`_.

JULES takes advantage of the parallel I/O features in `HDF5 <http://www.hdfgroup.org/HDF5/>`_ / `NetCDF4 <http://www.unidata.ucar.edu/software/netcdf/>`_. These are not enabled by default, and so must be explicitly enabled when HDF5 / NetCDF4 are compiled. More information on how to do this can be found on the `NetCDF website <http://www.unidata.ucar.edu/software/netcdf/docs/getting_and_building_netcdf.html#build_parallel>`_.

Information on how to build and run JULES in parallel can be found in the JULES User Guide. *Note that although this development has proven stable during testing, it is still experimental and is considered to be for advanced users only.*


Changes to documentation
------------------------

From a users point of view, the most important change is that the JULES documentation and coding standards are now provided in two forms - HTML (this is the preferred format) and PDF. The HTML documentation is also available on the web at `<http://jules-lsm.github.io/>`_.

This has been made possible by migrating the documentation from a single massive Word document to the `Sphinx <http://sphinx-doc.org/>`_ documentation generator (with some custom extensions to better support Fortran namelists). Although originally intended to document Python projects, Sphinx's extensibility has seen it adopted for a wide range of projects. Using Sphinx has several advantages over the previous monolithic Word document:

* Both forms of documentation (HTML and PDF) can be built from the same sources.
* The documentation is now split into several smaller files that are combined by Sphinx at build-time, leading to increased readability.
* `reStructuredText <http://docutils.sourceforge.net/rst.html>`_, the markup language used by Sphinx, is a plain text format, meaning that it can be version controlled much more effectively than a Word document (which is treated by Subversion as a single binary entity).
* The only software required to update the documentation is your favourite text editor (rather than Word).

The `JULES repository on PUMA <https://puma.nerc.ac.uk/trac/JULES>`_ has also been refactored so that configurations, documentation and examples sit in a separate project to the core Fortran code.


Other changes
---------------

Disambiguation of sea ice roughness lengths for heat and momentum
    Prior to vn3.3, these were implicitly assumed to be equal by the code. They can now be set separately in the namelist ``JULES_SURF_PARAM``.

Improvements to the numerics in the soil hydrology
    Previously, the soil hydrology scheme coped poorly with significant gradients in soil moisture because of the sensitive dependence of the hydraulic conductivity and soil water suction on the soil moisture. See the new switch ``l_dpsids_dsdz``.
    
Implicit numerics for land ice
    Previously, the updating of land ice temperatures was always explicit, limiting the thickness of soil levels that can be used with standard time steps. There is now an option for implicit numerics for land ice - see the new switch ``l_land_ice_imp``.
    
Scaling of land surface albedo to agree with a given input
    An option has been added to prescribe the grid-box mean snow-free albedo to a given input (e.g. observations, climatology). See the new switch ``l_albedo_obs``. For SW albedos, the albedos of the individual tiles are scaled linearly so that the grid-box mean albedo matches the observations, within limits for each tile. When VIS and NIR albedos are required then the input parameters are scaled and corrected in a similar manner. The change was included in the Global Land configuration at vn5.0: https://code.metoffice.gov.uk/trac/GL/ticket/8.
    
BVOC emissions now on a switch
    Previously, BVOC emissions diagnostics were calculated all the time, regardless of whether they were output. A new switch - ``l_bvoc_emis`` - has been added to enable the calculation of these diagnostics only when required.
    
Improvements to logging
    A new namelist file - ``logging.nml`` - has been added to give more control over log output from JULES. Previously all output was directed to ``stdout``.
    
Specify namelist directory as an argument
    It is now possible to specify the directory containing the namelist files as a command line argument to JULES. If no argument is given, JULES looks for the namelist files in the current working directory. Previously, JULES had to be executed in the directory containing the namelists - this change should make it easier to run JULES in batch mode.


Bugs fixed
----------

* Initialisation of ``chr1p5m`` and ``resfs`` in ``sf_exch``.
* Fix for potential divide-by-zero in ``sf_stom`` when running with ``can_rad_mod = 1``.
* Various UM-related fixes not relevant to standalone JULES (ENDGAME, aerosol deposition scheme, etc.).
