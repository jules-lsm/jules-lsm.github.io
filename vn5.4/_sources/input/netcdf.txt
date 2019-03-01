NetCDF files
============

For gridded data, NetCDF is the only supported format. Although ASCII files can be used for data at a single location, NetCDF is also the preferred format for such data (due to the reasons discussed in :doc:`overview`). Files are not expected to use specific dimension or variable names - these are specified via the :doc:`JULES namelists </namelists/contents>`. The only expectations placed on NetCDF input are:

* All input files use the same grid.
* All input files use the same dimension names (for grid dimensions, any additional dimensions and the time dimension).
* The dimensions for each variable appear in the correct order - ``(points, z1, z2, ..., t)`` for a 1D grid and ``(x, y, z1, z2, ..., t)`` for a 2D grid, where the ``z1, z2, ...`` (levels) and ``t`` (time) dimensions are only present when the variable and context in which the variable is being used require them.
* If using NetCDF for data at a single location, the grid dimensions are still expected to exist with size 1.