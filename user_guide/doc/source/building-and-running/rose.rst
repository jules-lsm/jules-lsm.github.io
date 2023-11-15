Automatic upgrading and GUI using Rose
======================================

`Rose <http://metomi.github.io/rose/doc/html/index.html>`_ is a collection of tools for managing the building and running of scientific applications.

.. seealso::
    Please familiarise yourself with the `Rose documentation <http://metomi.github.io/rose/doc/html/index.html>`_ before continuing with this section.

.. note::
   This section assumes `Rose is installed <http://metomi.github.io/rose/doc/html/installation.html>`_.
   
   We will not be using Rose Bush or Rosie, so those components need not be installed.
   
   It is not necessary to install Cylc, but some functionality will not be available. This will be noted as we go.

JULES uses Rose primarily to provide a graphical interface for configuring and running JULES, but also to allow automatic upgrading of JULES runs from one version to the next.

A Rose suite for JULES will normally contain two applications - an ``fcm_make`` application for building JULES and a ``jules`` application for configuring the namelists and running JULES.  


Creating a Rose suite from existing namelists
---------------------------------------------

To enable users to quickly transition to Rose and the extra functionality it provides, a tool is distributed with JULES that can convert existing namelists to a Rose suite.

To convert vn3.4 namelists to a vn4.7 Rose suite, run the following command in the directory containing the namelists:

.. code-block:: bash

    create_rose_app vn3.4 vn4.7 namelist_path suite_name jules_dir
    
Where ``jules_dir`` is the path to the root directory of the most recent JULES code release on your machine.

The ``namelist_path`` can be the full or a relative path.

This will create a directory called ``suite_name`` in ~/roses/ directory which contains a fully functional Rose suite.

To convert namelists to a Rose suite without upgrading the version, just give the same version for both.


Using Rose to upgrade existing namelists
----------------------------------------

It is not necessary to use Rose to configure and run JULES - Rose can be used just to upgrade existing namelists (at vn3.4 or later).

In order to use Rose to upgrade existing namelists from vn3.4 to vn4.0, just execute the following commands in the directory containing your namelists:

.. code-block:: bash

   # Creates a Rose suite at rose-suite
   $JULES_ROOT/bin/create_rose_app vn3.4 vn4.0
   
   # Remove the current namelists
   rm -rf *.nml
   
   # Use Rose to generate the new namelists
   rose app-run -i -C rose-suite/app/jules
   
   # Remove the Rose suite and other generated files
   rm -rf rose-suite .rose-config_processors-file.db rose-app-run.conf
   
   
Upgrading an existing JULES Rose suite
--------------------------------------

Upgrading an existing JULES Rose suite is even more simple than upgrading the namelist files directly. To see the versions it is possible to upgrade to, run the command:

.. code-block:: bash

   rose app-upgrade -M $JULES_ROOT/rose-meta -C /path/to/rose/suite/app/jules --all-versions
 && rose macro --fix -C app/jules

   rose app-upgrade -M $JULES_ROOT/rose-meta -C /path/to/rose/suite/app/fcm_make --all-versions
 && rose macro --fix -C app/fcm_make
   
To then upgrade to one of those versions, the command is:

.. code-block:: bash

   rose app-upgrade -M $JULES_ROOT/rose-meta -C /path/to/rose/suite/app/jules <version>
 && rose macro --fix -C app/jules

   rose app-upgrade -M $JULES_ROOT/rose-meta -C /path/to/rose/suite/app/fcm_make <version>
 && rose macro --fix -C app/fcm_make

   
Configuring JULES with a graphical interface
--------------------------------------------

Using a Rose suite to run JULES has the advantage that it can be configured graphically using `Rose Config Edit <http://metomi.github.io/rose/doc/html/api/command-reference.html#rose-config-edit>`_.

To launch the graphical editor, the following command is used:

.. code-block:: bash

   # To edit the whole suite, including build configuration
   rose config-edit -M $JULES_ROOT/rose-meta -C /path/to/rose/suite &
   
   # To edit just the namelists
   rose config-edit -M $JULES_ROOT/rose-meta -C /path/to/rose/suite/app/jules &
   
where ``$JULES_ROOT`` is the root directory of your JULES installation. For more information on using the config editor, see `the Rose documentation <http://metomi.github.io/rose/doc/html/api/command-reference.html#rose-config-edit>`_

Clicking on a variable name in the editor opens the corresponding page in this documentation.


Running a JULES Rose suite
--------------------------

Without Cylc
^^^^^^^^^^^^

To run JULES from a Rose suite without Cylc, we just use Rose to generate the namelists. JULES is then built and run as normal - see :doc:`intro`.

To generate namelists in the current directory from a Rose suite at ``/path/to/rose/suite``, use the following command:

.. code-block:: bash

   rose app-run -i -C /path/to/rose/suite/app/jules
   
   
With Cylc
^^^^^^^^^

.. warning:: This requires Cylc to be installed and configured.

Once a JULES Rose suite has been suitably configured using the graphical editor, it can be run using the following command:

.. code-block:: bash

   rose suite-run -C /path/to/rose/suite
   
This will set the suite running, and will launch the `Cylc <http://cylc.github.io/cylc/>`_ GUI to allow you to see the status of your suite as it runs. The GUI also allows you to view log files etc. - these can be useful when a job fails!
