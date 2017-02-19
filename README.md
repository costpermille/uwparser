# uwparser
UW time schedule parser

## Running this thing
Input is taken in a specific fixed-width record format. Spacing/line width matters. You can pull the record from a page such as https://www.washington.edu/students/timeschd/WIN2017/cse.html, in between each `<pre>` element. Char length per line matters.

```
Restr  13175 F  1-3     T      130-220    CSE  203      ANDERSON,RICHARD J.        Open     11/  25  CR/NC               
                        COMPUTING AND THE DEVELOPING WORLD                                                                                                                  
                        MEETS IN ROOM CSE 203                                                                                                                               
```
