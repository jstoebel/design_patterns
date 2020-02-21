# part3

we did this backwards! I was reading part 3 and some more complex cases came along. for example `7 - 3 + 2 - 1`. I plugged this in and got the wrong answer! How could this be? I took out a pencil and paper and started calculating this expression using my algorithem. sure enough I got the same wrong answer. It turns out I was constructing the tree backwards. Since in my algorithem, evaluation happens from bottom to top, What we really need to do is:

 - Take the first pair

    -
    |
    |
7<--+-->3

  - then tack the next pair _above_ the first pair. the result of the first pair should be the right value of the second

         +
         |
    - <--+-->2
    |
    |
7<--+-->3


 - Completing the expression gives us

              -
              |
         +<---+--->1
         |
    - <--+-->2
    |
    |
7<--+-->3
