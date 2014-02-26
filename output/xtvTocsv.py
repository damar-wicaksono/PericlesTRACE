#!/usr/bin/env python
# SETF: PERICLES
# Test: RE0062
# Author: WD41, LRS/EPFL/PSI, 2014
# Python: Version 3.3.4
# Description: Post-process trcxtv into several csv files.

def xtv_to_csv(aptplot_exec, xtv_filename, trace_vars, csv_filename):
   """ Extract requested variables and print them in csv format.

   Run aptplot in batch mode to extract the supplied variable list from the 
   xtv file. The output time series is written in csv files.
   
   Args:
      aptplot_exec: The executable of aptplot, should be callable from PATH
      xtv_file: TRACE xtv graphic output, python file object
      trace_vars: list of required TRACE variables

   Returns:
      CSV file named csv_file for all variable listed in trace_vars.
   """

   import os

   apt_script_file = 'tmp.apt'
   scr_file = 'tmp.scr'
   apt_script = open(apt_script_file, 'w')

   apt_script.write('TRAC 0 XTV "%s" \n' % (xtv_filename))
   for trace_var in trace_vars:
      apt_script.write('TREAD 0 "%s" SIU \n' % (trace_var))
   apt_script.write('TRAC 0 EXPORT CSV "%s" \n' % (csv_filename))
   apt_script.write('TRAC 0 CLOSE \n')
   apt_script.write('EXIT \n')
   apt_script.close()

   # Execute and clean up files 
   os.system(aptplot_exec + " -batch " + apt_script_file + " -nowin > " + \
             scr_file)
   os.remove(apt_script_file)
   os.remove(scr_file)

def main():

   import traceVars

   # Files 
   aptplot = 'aptplot_v6.5.1.inst01.sh'
   trcxtv = '../transient/trcxtv'

   # Convert xtv to csv for the selected variables
   # Clad temperature, Cold Assembly 1
   xtv_to_csv(aptplot, trcxtv, traceVars.TC_clad_CA1, \
              traceVars.TC_clad_CA1_csv)
   # Clad temperature, Hot Assembly 
   xtv_to_csv(aptplot, trcxtv, traceVars.TC_clad_HA, \
              traceVars.TC_clad_HA_csv)
   # Clad temperature, Cold Assembly 2
   xtv_to_csv(aptplot, trcxtv, traceVars.TC_clad_CA2, \
              traceVars.TC_clad_CA2_csv)

   # Clad temperature, Spacer Grid, Cold Assembly 1
   xtv_to_csv(aptplot, trcxtv, traceVars.TC_grid_CA1, \
              traceVars.TC_grid_CA1_csv)
   # Clad temperature, Spacer Grid, Hot Assembly 
   xtv_to_csv(aptplot, trcxtv, traceVars.TC_grid_HA, \
              traceVars.TC_grid_HA_csv)
   # Clad temperature, Spacer Grid, Cold Assembly 2
   xtv_to_csv(aptplot, trcxtv, traceVars.TC_grid_CA2, \
              traceVars.TC_grid_CA2_csv)

   # Liquid temperature, Cold Assembly 1
   xtv_to_csv(aptplot, trcxtv, traceVars.TC_liquid_CA1, \
              traceVars.TC_liquid_CA1_csv)
   # Liquid temperature, Hot Assembly 
   xtv_to_csv(aptplot, trcxtv, traceVars.TC_liquid_HA, \
              traceVars.TC_liquid_HA_csv)
   # Liquid temperature, Cold Assembly 2
   xtv_to_csv(aptplot, trcxtv, traceVars.TC_liquid_CA2, \
              traceVars.TC_liquid_CA2_csv)

   # Vapor temperature, Cold Assembly 1
   xtv_to_csv(aptplot, trcxtv, traceVars.TC_vapor_CA1, \
              traceVars.TC_vapor_CA1_csv)
   # Liquid temperature, Hot Assembly 
   xtv_to_csv(aptplot, trcxtv, traceVars.TC_vapor_HA, \
              traceVars.TC_vapor_HA_csv)
   # Liquid temperature, Cold Assembly 2
   xtv_to_csv(aptplot, trcxtv, traceVars.TC_vapor_CA2, \
              traceVars.TC_vapor_CA2_csv)

   # Void fraction, Cold Assembly 1
   xtv_to_csv(aptplot, trcxtv, traceVars.alpha_CA1, \
              traceVars.alpha_CA1_csv)
   # Void fraction, Hot Assembly 
   xtv_to_csv(aptplot, trcxtv, traceVars.alpha_HA, \
              traceVars.alpha_HA_csv)
   # Void fraction, Cold Assembly 2
   xtv_to_csv(aptplot, trcxtv, traceVars.alpha_CA2, \
              traceVars.alpha_CA2_csv)

   # Pressure, Cold Assembly 1
   xtv_to_csv(aptplot, trcxtv, traceVars.pressure_CA1, \
              traceVars.pressure_CA1_csv)
   # Pressure, Hot Assembly 
   xtv_to_csv(aptplot, trcxtv, traceVars.pressure_HA, \
              traceVars.pressure_HA_csv)
   # Pressure, Cold Assembly 2
   xtv_to_csv(aptplot, trcxtv, traceVars.pressure_CA2, \
              traceVars.pressure_CA2_csv)

if __name__ == "__main__":
   main()
