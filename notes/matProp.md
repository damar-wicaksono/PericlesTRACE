# NOTES on MATERIAL PROPERTIES

There are three materials involve in PERICLES experiment facility:
   1. Boron Nitride: for Filling Material
   2. Nichrome V: for heater material
   3. SS 316: for cladding and housing

Material properties considered here is usually in form of polynomial fit.
Sources either come from built-in TRACE properties or PREMIUM specification.
However, there are other sources that can be considered, such as from the
European Commission Report.

## Boron Nitride

Volumetric heat capacity and conductivities are specified in the PREMIUM
benchmark.

### Density

PREMIUM does not specify any density information regarding Boron Nitride.
As TRACE requires the density to be specified, the default value in TRACE is
used. The default value is constant overall temperature range.

Rho = 2002.0 [kg.m^(-3)]

### Heat Capacity

PREMIUM specifies the following formula for volumetric heat capacity.
It is in the form of 3rd-order polynomial.

Rho.Cp = 1.4531 * 10^(6) + 4.228 * 10^(3) Tc - 2.192 Tc^2

Rho.Cp [=] [J.m^-3.K^-1] 
Tc [=] [oC]

The uncertainty for Rho.Cp is given as +- 10%.

TRACE has a built-in material properties for Boron Nitride. 

The heat capacity in in the form of 4th-order polynomial.

Cp = 760.59 + 1.7955 * Tf - 8.6704 * 10^-4 * Tf^2 + 1.5896 * 10^-7 * Tf^3

Cp [=] [J.kg.K^-1]
Tf [=] [oF]

Rho = 2002.0 [kg.m^(-3)]

Converting to Celcius temperature gives the following formula:

Cp= 817.16 + 3.1825 * Tc - 2.7762 * 10^(-3) * Tc^2 + 9.2705 * 10^(-7) * Tc^(-3)

Tc [=] [oC]

and for PREMIUM, dividing by constant density, Rho = 2002 [kg.m^3]

Cp = 725.82 + 2.1119 * Tc - 1.0949 * 10^(-3) * Tc^2

which is always smaller than the one given in TRACE. 

Converting to Kelvin scale gives,

Cp = 725.82 + 2.1119 * (T - 273.15) - 1.0949 * 10^(-3) * (T - 273.15)^2

### Thermal Conductivity

in PREMIUM, thermal conductivity for Boron Nitride depends on the axial 
location. This is because of compaction effect. In essence, increase in power,
increase the degree of compaction (higher density) leading to increase in 
volumetric heat capacity and conductivity.

As a power distribution is imposed axially, the conductivity is distributed as
follows (for 11 sections) (in [W.m^(-1).K^(-1)]:
   1. 2.0 (528 [mm])
   2. 2.2 (260 [mm])
   3. 3.0 (260 [mm])
   4. 3.8 (260 [mm])
   5. 5.4 (260 [mm])
   6. 6.4 (520 [mm])
   7. 5.4 (260 [mm])
   8. 3.8 (260 [mm])
   9. 3.0 (260 [mm])
  10. 2.2 (260 [mm])
  11. 2.0 (528 [mm])

Above values are taken to be constant in terms of temperature.

in TRACE, the built in conductivity is of 2nd-order polynomial

k = 25.27 - 1.365 * 10^(-3) * Tf
Tf [=] [oF]

in Celcius this formula will be,

k = 25.23 - 2.457 * 10^(-3) * Tc
Tc [=] [oC]

For the range of temperature we are interested in PERICLES (1000 - 1500 [oC]),
this formula gives k in the range of (22.773 - 21.5445 [oC]) which is much 
larger then PREMIUM specification.

Additionally, in TRACE, axially dependent material properties cannot be 
specified. As a workaround the length-averaged value is used instead,

k_bar = 3.536105 [W.m^(-1).K^(-1)]

The errors induced by this simplification is not known, but might be large.
As such uncertainties to this value has to be enlarged and check 
the sensitivity.

### Emissivity

PREMIUM does not specify any emissivity information regarding Boron Nitride.
As TRACE requires the density to be specified, the default value in TRACE is
used. The default value is constant overall temperature range.

e = 1.0 [-]

## Nichrome V

in PREMIUM, the material properties of Nichrome V are also affected by 
compaction thus they vary axially. As with Boron Nitride, density information
is not given. Instead, volumetric heat capacity and thermal conductivity are
specified.

in TRACE, the material properties for Nichrome which is used as a heater coils
is available. It shares the same value with Constantan.

### Density

PREMIUM does not specify any density information regarding Nichrome V.
As TRACE requires the density to be specified, the default value in TRACE is
used. The default value is constant over all temperature range.

Rho = 8393.4 [kg.m^(-3)]

### Heat Capacity

in PREMIUM, volumetric heat capacity varies axially due to compaction effect.
The base formula is in 2nd-order polynomial (in [J.m^(-3).K^(-1)]):

Rho.Cp = C * (3.646 * 10^6 + 2.04 * 10^3 Tc)

The coefficient C varies axially and given below for the 11 sections:
   1. 0.509 (528 [mm])
   2. 0.673 (260 [mm])
   3. 0.955 (260 [mm])
   4. 1.182 (260 [mm])
   5. 1.416 (260 [mm])
   6. 1.534 (520 [mm])
   7. 1.416 (260 [mm])
   8. 1.182 (260 [mm])
   9. 0.955 (260 [mm])
  10. 0.673 (260 [mm])
  11. 0.509 (528 [mm])

as TRACE cannot take axial variation in properties, the length-averaged 
value is used instead,

C_bar = 0.9663

Again averaging might have large sensitivity and thus has to be checked.

To convert above formula simply into heat capacity, TRACE density information
is used (constant over all temperature range)

Rho = 8393.4 [kg.m^(-3)]

such that the formula becomes,

Rho.Cp = C * (4.3439 * 10^2  + 2.430 * 10^(-1) Tc)

in TRACE the formula for Specific Heat is given in exponential form below:

Cp = 110.0 * Tf^(0.2075)
Cp [=] [J.kg^(-1).K^(-1)]
Tf [=] [oF]

in celcius scale the formula becomes,

Cp = 110.0 * (1.8 * Tc + 32)^(0.2075)

From graphical inspection it can be seen that for the temperature range 
considered in the experiment, TRACE heat capacity is consistently larger.
However, the difference is somewhat constant across temperature with 
average of 144.06 [J.kg^(-1).K^(-1)]

### Thermal Conductivity

in PREMIUM, the following formula for k is proposed,

k = 9.354 + 0.01795 * Tc

while in TRACE, the following is given,

k = 29.18 + 2.683 * 10^(-3) * (Tf - 100)

converting to celcius scale,

k = 28.998 + 4.8294 * 10^(-3) * Tc

TRACE have larger intercept but smaller slope, while PREMIUM specification has 
smaller offset but larger slope. For the temperature range considered the 
average difference is 9.803 [W.m^(-1).K^(-1)]

### Emissivity

PREMIUM does not specify any emissivity information regarding Nichrome V.
As TRACE requires the density to be specified, the default value in TRACE is
used. The default value is constant overall temperature range.

e = 1.0 [-]

## Stainless Steel 316

in PREMIUM, the material properties of Nichrome V are not affected by
compaction. As opposed to Boron Nitride and Nichrome V, density information
is given. 

in TRACE, the material properties for Nichrome which is used as a heater coils
is available. It shares the same value with Constantan.

### Density

in PREMIUM, SS316 density is specified as follows,

Rho = 8084 - 4.209 * 10^(-1) * Tk - 3.894 * 10^(-5) * Tk^2
Tk [=] [K]

this is identical to the built-in density data for SS 316 in TRACE

### Heat Capacity

in PREMIUM, SS316 heat capacity is specified as follows (in [J.kg^(-1).K^(-1)])

Cp = 426.17 + 4.43816 * 10^(-1) * Tf - 6.3759 * 10^(-4) * Tf^2 
            + 4.48030 * 10^(-4) * Tw^3 - 1.0729 * 10^(-10) * Tf^4

Again, this formula is identical to the built-in heat capacity data of SS 316 
implemented in TRACE. As a sidenote, the temperature has been capped to the 
value of 2400 [oF] = 1315.56 [oC] to prevent negative value of Cp.

### Thermal Conductivity

in PREMIUM, SS316 thermal conductivity is specified as linear fit given
below (in [W.m^(-1).K^(-1)]),

Cp = 9.248 + 1.571 * 10^(-2) * Tk 

Again, this formula is identical to the built-in thermal conductivity 
data of SS 316 implemented in TRACE.

### Emissivity

PREMIUM does not specify any emissivity information regarding Nichrome V.
As TRACE requires the density to be specified, the default value in TRACE is
used. The default value is constant overall temperature range.

e = 0.84 [-]
