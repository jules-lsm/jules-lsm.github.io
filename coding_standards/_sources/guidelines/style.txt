Style
=====

The following is a list of recommended styles when you write code in Fortran.

* New code should be written using Fortran 95 syntax. Avoid un-portable vendor/compiler extensions. Avoid Fortran 2003 features for the moment, as they will not become widely available in the near future (however, there is no harm in designing your code with the future in mind. For example, if there is a feature that is not in Fortran 95 and you know that it is in Fortran 2003, you may want to write your Fortran 95 code to make it easier for the future upgrade).

* Write your program in UK English, unless you have a very good reason for not doing so. Write your comments in simple UK English and name your program units and variables based on sensible UK English words. Always bear in mind that your code may be read by people who are not proficient English speakers.

* When naming your variables and program units, always keep in mind that Fortran is a case-insensitive language (e.g. ``EditOrExit`` is the same as ``EditorExit``.)

* Use only characters in the Fortran character set. In particular, accent characters and tabs are not allowed in code, although they are usually OK in comments. If your editor inserts tabs automatically, you should configure it to switch off the functionality when you are editing Fortran source files.

* Although Fortran has no reserved keywords, you should avoid naming your program units and variables with names that match an intrinsic ``FUNCTION`` or ``SUBROUTINE``. Similarly, you should avoid naming your program units and variables with names that match a keyword in a Fortran statement.

* Be generous with comments. State the reason for doing something, instead of repeating the Fortran logic in words.

* To improve readability, write your code using the ALL CAPS Fortran keywords approach. This is the style used in most of the examples in this document, where Fortran keywords and intrinsic procedures are written in ALL CAPS. The rest of the code is written in either lowercase with underscores or CamelCase. This approach has the advantage that Fortran keywords stand out.

* Use the new and clearer syntax for LOGICAL comparisons, i.e.:

  * ``==`` instead of ``.EQ.``
  * ``/=`` instead of ``.NE.``
  * ``>`` instead of ``.GT.``
  * ``<`` instead of ``.LT.``
  * ``>=`` instead of ``.GE.``
  * ``<=`` instead of ``.LE.``
 
* Where appropriate, simplify your ``LOGICAL`` assignments, for example:

  Common practice
      .. code-block:: fortran
      
         IF (my_var == some_value) THEN
           something      = .TRUE.
           something_else = .FALSE.
         ELSE
           something      = .FALSE.
           something_else = .TRUE.
         END IF
         
         ! ...
         
         IF (something .EQV. .TRUE.) THEN
           CALL do_something()
           ! ...
         END IF

  Better approach
      .. code-block:: fortran

         something      = (my_var == some_value)
         something_else = (my_var /= some_value)

         ! ...

         IF (something) THEN
           CALL do_something()
           ! ...
         END IF

* Positive logic is usually easier to understand. When using an ``IF-ELSE-END IF`` construct you should use positive logic in the ``IF`` test, provided that the positive and the negative blocks are about the same length. It may be more appropriate to use negative logic if the negative block is significantly longer than the positive block. For example:

  Common practice
      .. code-block:: fortran
     
         IF (my_var /= some_value) THEN
           CALL do_this()
         ELSE
           CALL do_that()
         END IF

  Better approach
      .. code-block:: fortran

         IF (my_var == some_value) THEN
           CALL do_that()
         ELSE
           CALL do_this()
         END IF

* To improve readability, you should always use the optional space to separate the following Fortran keywords:

  .. code-block:: fortran

      ELSE IF       END DO           END FORALL   END FUNCTION
      END IF        END INTERFACE    END MODULE   END PROGRAM
      END SELECT    END SUBROUTINE   END TYPE     END WHERE
      SELECT CASE
      
* If you have a large or complex code block embedding other code blocks, you may consider naming some or all of them to improve readability.

* If you have a large or complex interface block or if you have one or more sub-program units in the ``CONTAINS`` section, you can improve readability by using the full version of the ``END`` statement (i.e. ``END SUBROUTINE <name>`` or ``END FUNCTION <name>`` instead of just ``END``) at the end of each sub-program unit. For readability in general, the full version of the ``END`` statement is recommended over the simple ``END``.

* Where possible, consider using ``CYCLE``, ``EXIT`` or a ``WHERE``-construct to simplify complicated DO-loops.

* When writing a ``REAL`` literal with an integer value, put a 0 after the decimal point (i.e. ``1.0`` as opposed to ``1.``) to improve readability.

* Where reasonable and sensible to do so, you should try to match the names of dummy and actual arguments to a ``SUBROUTINE`` / ``FUNCTION``.

* In an array assignment, it is recommended that you use array notations to improve readability. E.g.:

  Common practice
      .. code-block:: fortran
      
         INTEGER :: array1(10, 20), array2(10, 20)
         INTEGER :: scalar

         ! ...

         array1 = 1
         array2 = array1 * scalar

  Better approach
      .. code-block:: fortran

         INTEGER :: array1(10, 20), array2(10, 20)
         INTEGER :: scalar

         ! ...

         array1(:, :) = 1
         array2(:, :) = array1(:, :) * scalar

* Where appropriate, use parentheses to improve readability. E.g.:

  .. code-block:: fortran

      a = (b * i) + (c / n)
      
  is easier to read than
  
  .. code-block:: fortran
  
      a = b * i + c / n
      
