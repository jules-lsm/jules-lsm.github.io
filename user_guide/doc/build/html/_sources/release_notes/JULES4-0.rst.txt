JULES version 4.0 Release Notes
===============================


JULES-Crop crop model
---------------------

JULES vn4.0 sees the introduction of the JULES-Crop crop model. This has been the result of many years of hard work from Tom Osbourne et. al. at the `University of Reading <http://www.reading.ac.uk/>`_.

A lot of the work done in getting it ready for the trunk and testing was done in the Met Office by Karina Williams and Jemma Gornall.


Daily disaggregator for forcing data
------------------------------------

JULES can now be driven with daily forcing data, and the daily disaggregator will disaggregate the daily forcing down onto the model timestep.

For more information, see :nml:mem:`JULES_DRIVE::l_daily_disagg`.


Major namelist changes
----------------------

JULES vn4.0 also sees a major revamp of the science-related namelists. The monolithic JULES_SWITCHES namelist, and various others, are gone, and have been replaced with science section namelists. For more details, see :doc:`/namelists/contents`.

This has been with the aim of providing a GUI for editing the JULES namelists using `Rose <http://metomi.github.io/rose/doc/html/index.html>`_, which is now available - see :doc:`/building-and-running/rose`.

It also has the advantage that the new namelists are cut-and-paste-able between the UM and JULES, which should make it easier to ensure that the same science is being used in online and offline runs. 


Removal of GNU make build files
-------------------------------

After a period of supporting two build systems (FCM make and GNU make), it has been decided that support for GNU make should be removed. The overhead of maintaining two build systems was getting too large, and FCM make is preferred for several reasons:

Directory structure
 *  The directory level dependencies used by the JULES Makefile to ensure files are compiled in the correct order forced the directory structure to adapt to it.
 *  FCM make does automatic dependency analysis for each file to ensure they are compiled in the correct order, meaning the directory structure doesn't have to be compromised to keep the build system happy.

Dependencies
 *  The JULES GNU Makefiles required that dependencies be manually maintained, both in terms of the order of sub-makes and actual file dependencies within the sub-makes.
 *  FCM make automatically detects all dependencies and does things in the correct order.
   
Parallel builds
 *  JULES builds with GNU make could not be parallelised, because of the use of directory level sub-makes.
 *  FCM make considers each individual file, so builds can be parallelised.
   
Integration with Rose
 *  FCM make has good integration with Rose, allowing the Rose GUI for JULES to configure and run builds as well as the namelists.


Bugs and other changes
----------------------

*  Output for land points not comparing between land_only = T and F runs with 2D grid
*  Incorrect behaviour when ``spinup_end`` == ``data_end``
*  Fixed overflow problem with ``datetime_diff`` when ``datetime``\ s are too far apart
*  Removed old implicit solver and ltimer code
*  Unified management of printing and error reporting for UM and standalone
