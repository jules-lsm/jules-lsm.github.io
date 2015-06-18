Guidelines for Fortran code
===========================


These are guidelines you should adhere to when you are developing new code for inclusion in the official release of JULES. If you are modifying existing code, you should adhere to its existing standard and style where possible. If you want to change its standard and style, you should seek prior agreement with the JULES office. Where possible, you should try to maintain the same layout and style within a source file.

When reading these guidelines, it is assumed that you already have a good understanding of modern Fortran terminology. It is understood that these guidelines may not cover every aspect of your work. In such cases, use common sense and always bear in mind that other people may have to maintain the code in the future.

Always test your code before releasing it. Do not ignore compiler warnings, as they may point you to potential problems.

Some standard templates are given in :doc:`/standard_code_templates/index`.


.. toctree::
   :maxdepth: 2
   
   layout_and_formatting
   style
   fortran_features
   fp_arithmetic
   best_practices