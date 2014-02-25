# PERICLES TRACE output

The following are available as part of post-processed output files

## Clad Temperature

The temperature measurement was done using thermocouples. 
4 Different instrumented pins were used.
The difference between pins are irrelevant for TRACE model, only their axial 
location.

The following 24 locations are available as TRACE output:

| TC  | Loc. Rel. [mm]   | Loc. Abs. [mm]   | TRACE Vars     |
|:---:|:----------------:|:----------------:|:--------------:|
|  1  |  177             |    547           |  rftn-xxxA34R29|
|  2  |  353             |    723           |  rftn-xxxA49R29|
|  3  |  590             |    960           |  rftn-xxxA59R29|
|  4  |  920             |   1290           |  rftn-xxxA79R29|
|  5  | 1110             |   1480           |  rftn-xxxA89R29|
|  6  | 1180             |   1550           |  rftn-xxxA99R29|
|  7  | 1397             |   1767           | rftn-xxxA114R29|
|  8  | 1483             |   1853           | rftn-xxxA124R29|
|  9  | 1625             |   1995           | rftn-xxxA134R29|
| 10  | 1691             |   2061           | rftn-xxxA144R29|
| 11  | 1751             |   2121           | rftn-xxxA154R29|
| 12  | 1828             |   2198           | rftn-xxxA161R29|
| 13  | 1920             |   2290           | rftn-xxxA169R29|
| 14  | 2030             |   2400           | rftn-xxxA184R29|
| 15  | 2150             |   2520           | rftn-xxxA194R29|
| 16  | 2223             |   2593           | rftn-xxxA204R29|
| 17  | 2283             |   2653           | rftn-xxxA214R29|
| 18  | 2345             |   2715           | rftn-xxxA224R29|
| 19  | 2523             |   2893           | rftn-xxxA234R29|
| 20  | 2670             |   3040           | rftn-xxxA254R29|
| 21  | 2748             |   3118           | rftn-xxxA264R29|
| 22  | 2998             |   3368           | rftn-xxxA279R29|
| 23  | 3305             |   3675           | rftn-xxxA299R29|
| 24  | 3480             |   3850           | rftn-xxxA314R29|

xxx above refers to TRACE component number (HTSTR) of the three assemblies: 
201, 301, and 401 for Cold Assembly 1 (A), Hot Assembly (B), and Cold 
Assembly 2 (C), respectively. 

Note also that TC12 is not exactly aligned to TRACE variable. The corresponding 
variable correspond to absolute elevation of 2196.3 [m]. The difference in 
temperature can be expected to be negligible.

Radially all temperature was taken from then 29th node (radius = 4.53E-03) in 
the cladding. The documentation only mentioned that clad temperature was taken 
in the cladding.

Though not mentioned to be measure the clad temperature at the location of 
spacer grid is interesting to be examined. Their locations are as follows:


| SG  | Node Center [mm]   | TRACE Vars     | Difference |
|:---:|:------------------:|:--------------:|:----------:|
|  1  |  110               |  rftn-xxxA08R29|  4.0mm     |
|  2  |  668               |  rftn-xxxA44R29| 10.0mm     |
|  3  | 1180               |  rftn-xxxA73R29| 14.5mm     |
|  4  | 1691               | rftn-xxxA108R29|  4.3mm     | 
|  5  | 2223               | rftn-xxxA163R29|  1.6mm     | 
|  6  | 2748               | rftn-xxxA229R29| 56.0mm     | 
|  7  | 3298               | rftn-xxxA273R29|  2.5mm     | 
|  8  | 3803               | rftn-xxxA309R29|  6.0mm     |

xxx above refers to TRACE component number (HTSTR) of the three assemblies: 
201, 301, and 401 for Cold Assembly 1 (A), Hot Assembly (B), and Cold 
Assembly 2 (C), respectively. 

As the nodalization was not aligned to specific location of node-centered 
spacer grid the neares dowstream location is taken. The downstream location 
was chosen as spacer grid model in TRACE affect the flow downstream, not 
upstream.

## Fluid Temperature and Pressure Drop

Fluid temperature and pressure drop was measured in the following locations:

| SG  | Loc. Rel.(abs) [mm]| TRACE Vars     | Note          |
|:---:|:------------------:|:--------------:|:-------------:|
|  1  |    0 (370)         | tln-10A04R0xT01| Liquid Temp.  |
|     |                    | tvn-10A04R0xT01| Vapor Temp.   |
|     |                    |alpn-10A04R0xT01| Void fraction |
|     |                    |  pn-10A04R0xT01| Pressure      |
|  2  |   590 (960)        | tln-10A12R0xT01| Liquid Temp.  |
|     |                    | tvn-10A12R0xT01| Vapor Temp.   |
|     |                    |alpn-10A12R0xT01| Void fraction |
|     |                    |  pn-10A12R0xT01| Pressure      |
|  3  |  1296 (1666)       | tln-10A22R0xT01| Liquid Temp.  |
|     |                    | tvn-10A22R0xT01| Vapor Temp.   |
|     |                    |alpn-10A22R0xT01| Void fraction |
|     |                    |  pn-10A22R0xT01| Pressure      |
|  4  |  1942 (2312)       | tln-10A35R0xT01| Liquid Temp.  |
|     |                    | tvn-10A35R0xT01| Vapor Temp.   |
|     |                    |alpn-10A35R0xT01| Void fraction |
|     |                    |  pn-10A35R0xT01| Pressure      |
|  5  |  2608 (2978)       | tln-10A49R0xT01| Liquid Temp.  |
|     |                    | tvn-10A49R0xT01| Vapor Temp.   |
|     |                    |alpn-10A49R0xT01| Void fraction |
|     |                    |  pn-10A49R0xT01| Pressure      |
|  6  |  3254 (3624)       | tln-10A58R0xT01| Liquid Temp.  |
|     |                    | tvn-10A58R0xT01| Vapor Temp.   |
|     |                    |alpn-10A58R0xT01| Void fraction |
|     |                    |  pn-10A58R0xT01| Pressure      |

x above refers to the assembly number in the radial direction: 1, 2, 3 for 
Cold Assembly 1 (A), Hot Assembly (B), and Cold Assembly 2 (C), respectively.
