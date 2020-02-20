# Refactor ideas

Adding an operator requires changing the interpreter in three places.

The corner case for detecting space between numbers is awkward
 - maybe extend next_token to not consider white space. that would let us get the next meaningful character, which would let us raise an error for '1  0 - 3' (two spaces between 1 and 0)