Layout and formatting
=====================


The following is a list of recommended practices for layout and formatting when you write code in Fortran.

* Use the Fortran 90 free format syntax.

* Indent blocks by 2 characters. Where possible, comments should be indented with the code within a block.

* Use space and blank lines where appropriate to format your code to improve readability (use genuine spaces rather than tabs, as the tab character is not in the Fortran character set). For example:

  Common practice
      .. code-block:: fortran

         DO i=1,n
           a(i)%c=10*i/n
         ENDDO
         IF(this==that)THEN
           distance=0
           time=0
         ENDIF

  Better approach
      .. code-block:: fortran

         DO i = 1, n
           a(i)%c = 10 * i / n
         END DO

         IF (this == that) THEN
           distance = 0
           time     = 0
         END IF

* Try to confine your line width to 80 characters. This means that your code can be viewed easily in any editor on any screen, and can be printed easily on A4 paper.

* Line up your statements, where appropriate, to improve readability. For example:

  Common practice
      .. code-block:: fortran

         REAL, INTENT(IN) :: my_in(:)
         REAL, INTENT(INOUT) :: my_inout(:)
         REAL, INTENT(OUT) :: my_out(:)
         
         ! ...
         
         CHARACTER(LEN=256) :: my_char
         
         ! ...
         
         my_char = 'This is a very very very very very very ' // &
            'very very very very very very very very very very ' // &
            'long character assignment'

  Better approach
      .. code-block:: fortran
      
         REAL, INTENT(IN   ) ::    my_in(:)
         REAL, INTENT(INOUT) :: my_inout(:)
         REAL, INTENT(  OUT) ::   my_out(:)
         
         ! ...
         
         CHARACTER(LEN=256) :: my_char
         
         ! ...
         
         my_char                                                 &
             =  'This is a very very very very very very very '  &
             // 'very very very very very very very very very '  &
             // 'long character assignment'

* Short and simple Fortran statements are easier to read and understand than long and complex ones. Where possible, avoid using continuation lines in a statement.

* Avoid putting multiple statements on the same line. It is not good for readability.

* Each program unit (module, subroutine, function etc.) should follow a structure similar to the templates supplied in :doc:`/standard_code_templates/index`. The intended behaviour of the unit should be clearly described in the header.

* Comments should start with a single ``!`` at beginning of the line. A blank line should be left before (but not after) the comment line. The only exception is for one line comments which can be indented within the code or placed after the statement.

* Each subroutine, function and module should be in a separate file. Modules may be used to group related variables, subroutines and functions.
