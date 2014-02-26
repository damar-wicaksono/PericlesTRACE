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
   xtv_to_csv(aptplot, trcxtv, traceVars.temp_clad, traceVars.temp_clad_csv)

if __name__ == "__main__":
   main()
