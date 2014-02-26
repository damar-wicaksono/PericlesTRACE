#!/usr/bin/env python
# SETF: PERICLES
# Test: RE0062
# Author: WD41, LRS/EPFL/PSI, 2014
# Python: Version 3.3.4
# Description: Post-process trcxtv into several csv files.

def xtv_to_csv(aptplot_exec, xtv_file, trace_vars):
   """ Extract requested variables and print them in csv format.

   Run aptplot in batch mode to extract the supplied variable list from the 
   xtv file. The output time series is written in csv files.
   
   Args:
      aptplot_exec: The executable of aptplot, should be callable from PATH
      xtv_file: TRACE xtv graphic output, python file object
      trace_vars: list of required TRACE variables

   Returns:
      Separate csv files for each variable listed in trace_vars. The naming 
      convention of these files is the actual TRACE variable name.
   """

   import os

   for trace_var in trace_vars:
      apt_script_file = 'tmp.apt'
      scr_file = 'tmp.scr'
      apt_script = open(apt_script_file, 'w')
      csv_file = trace_var + '.csv'

      apt_script.write('TRAC 0 XTV "%s" \n' % (xtv_file))
      apt_script.write('TREAD 0 "%s" SIU \n' % (trace_var))
      apt_script.write('TRAC 0 EXPORT CSV "%s" \n' % (csv_file))
      apt_script.write('TRAC 0 CLOSE \n')
      apt_script.write('EXIT \n')
      apt_script.close()

      # Execute and clean up files 
      os.system(aptplot_exec + " -batch " + apt_script_file + " -nowin > " + \
                scr_file)
      os.remove(apt_script_file)
      os.remove(scr_file)
   
def main():

   # Files 
   aptplot = 'aptplot_v6.5.1.inst01.sh'
   trcxtv = '../transient/trcxtv'  

   # Required TRACE output variables
   temp_clad = ['rftn-201A34R29', 'rftn-301A34R29', 'rftn-401A34R29', # TC1
                'rftn-201A49R29', 'rftn-301A49R29', 'rftn-401A49R29', # TC2
                'rftn-201A59R29', 'rftn-301A59R29', 'rftn-401A59R29', # TC3
                'rftn-201A79R29', 'rftn-301A79R29', 'rftn-401A79R29', # TC4
                'rftn-201A89R29', 'rftn-301A89R29', 'rftn-401A89R29', # TC5
                'rftn-201A99R29', 'rftn-301A99R29', 'rftn-401A99R29', # TC6
                'rftn-201A114R29', 'rftn-301A114R29', 'rftn-401A114R29', # TC7
                'rftn-201A124R29', 'rftn-301A124R29', 'rftn-401A124R29', # TC8
                'rftn-201A134R29', 'rftn-301A134R29', 'rftn-401A134R29', # TC9
                'rftn-201A144R29', 'rftn-301A144R29', 'rftn-401A144R29', # TC10
                'rftn-201A154R29', 'rftn-301A154R29', 'rftn-401A154R29', # TC11
                'rftn-201A161R29', 'rftn-301A161R29', 'rftn-401A161R29', # TC12
                'rftn-201A169R29', 'rftn-301A169R29', 'rftn-401A169R29', # TC13
                'rftn-201A184R29', 'rftn-301A184R29', 'rftn-401A184R29', # TC14
                'rftn-201A194R29', 'rftn-301A194R29', 'rftn-401A194R29', # TC15
                'rftn-201A204R29', 'rftn-301A204R29', 'rftn-401A204R29', # TC16
                'rftn-201A214R29', 'rftn-301A214R29', 'rftn-401A214R29', # TC17
                'rftn-201A224R29', 'rftn-301A224R29', 'rftn-401A224R29', # TC18
                'rftn-201A234R29', 'rftn-301A234R29', 'rftn-401A234R29', # TC19
                'rftn-201A254R29', 'rftn-301A254R29', 'rftn-401A254R29', # TC20
                'rftn-201A264R29', 'rftn-301A264R29', 'rftn-401A264R29', # TC21
                'rftn-201A279R29', 'rftn-301A279R29', 'rftn-401A279R29', # TC22
                'rftn-201A299R29', 'rftn-301A299R29', 'rftn-401A299R29', # TC23
                'rftn-201A314R29', 'rftn-301A314R29', 'rftn-401A314R29'] # TC24

   # Convert xtv to csv for the selected variables
   mgc = get_ipython().magic
   mgc(u'%time xtv_to_csv(aptplot, trcxtv, temp_clad)')
   #xtv_to_csv(aptplot, trcxtv, temp_clad)
   

if __name__ == "__main__":
   main()
