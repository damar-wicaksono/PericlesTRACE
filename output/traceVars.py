# Required TRACE output variables
# Separated between assemblies and variables.
# each csv contains multiple axial location

# Clad Temperature with thermocouple measurement
TC_clad_CA1 = ['rftn-201A34R29', 'rftn-201A49R29', 'rftn-201A59R29',
               'rftn-201A79R29', 'rftn-201A89R29', 'rftn-201A99R29',  
               'rftn-201A114R29', 'rftn-201A124R29', 'rftn-201A134R29',
               'rftn-201A144R29', 'rftn-201A154R29', 'rftn-201A161R29',
               'rftn-201A169R29', 'rftn-201A184R29', 'rftn-201A194R29',
               'rftn-201A204R29', 'rftn-201A214R29', 'rftn-201A224R29',
               'rftn-201A234R29', 'rftn-201A254R29', 'rftn-201A264R29',
               'rftn-201A279R29', 'rftn-201A299R29', 'rftn-201A314R29']

TC_clad_HA = ['rftn-301A34R29', 'rftn-301A49R29', 'rftn-301A59R29'
              'rftn-301A79R29', 'rftn-301A89R29', 'rftn-301A99R29'
              'rftn-301A114R29','rftn-301A124R29','rftn-301A134R29',
              'rftn-301A144R29','rftn-301A154R29','rftn-301A161R29',
              'rftn-301A169R29','rftn-301A184R29','rftn-301A194R29',
              'rftn-301A204R29','rftn-301A214R29','rftn-301A224R29',
              'rftn-301A234R29','rftn-301A254R29','rftn-301A264R29',
              'rftn-301A279R29','rftn-301A299R29','rftn-301A314R29']


TC_clad_CA2 = ['rftn-401A34R29', 'rftn-401A49R29', 'rftn-401A59R29',
               'rftn-401A79R29', 'rftn-401A89R29', 'rftn-401A99R29',
               'rftn-401A114R29', 'rftn-401A124R29', 'rftn-401A134R29',
               'rftn-401A144R29', 'rftn-401A154R29', 'rftn-401A161R29',
               'rftn-401A169R29', 'rftn-401A184R29', 'rftn-401A194R29',
               'rftn-401A204R29', 'rftn-401A214R29', 'rftn-401A224R29',
               'rftn-401A234R29', 'rftn-401A254R29', 'rftn-401A264R29',
               'rftn-401A279R29', 'rftn-401A299R29', 'rftn-401A314R29']

TC_clad_CA1_csv = 'TC_clad_CA1.csv'
TC_clad_HA_csv = 'TC_clad_HA.csv'
TC_clad_CA2_csv = 'TC_clad_CA2.csv'

# Clad Temperature downstream spacer grid location
TC_grid_CA1 = ['rftn-201A08R29', 'rftn-201A44R29', 'rftn-201A73R29',  
               'rftn-201A108R29', 'rftn-201A163R29','rftn-201A229R29',  
               'rftn-201A273R29', 'rftn-201A309R29']  

TC_grid_HA = ['rftn-301A08R29', 'rftn-301A44R29', 'rftn-301A73R29', 
              'rftn-301A108R29', 'rftn-301A163R29', 'rftn-301A229R29',
              'rftn-301A273R29', 'rftn-301A309R29']

TC_grid_CA2 = ['rftn-401A08R29', 'rftn-401A44R29', 'rftn-401A73R29', 
               'rftn-401A108R29', 'rftn-401A163R29', 'rftn-401A229R29',
               'rftn-401A273R29', 'rftn-401A309R29']

TC_grid_CA1_csv = 'TC_grid_CA1.csv'
TC_grid_HA_csv = 'TC_grid_HA.csv'
TC_grid_CA2_csv = 'TC_grid_CA2.csv'

# Liquid temperature with thermocouple measurement (not really measured the
# liquid temperature though)
TC_liquid_CA1 = ['tln-10A04R01T01', 'tln-10A12R01T01', 'tln-10A22R01T01',
                 'tln-10A35R01T01', 'tln-10A49R01T01', 'tln-10A58R01T01']
TC_liquid_HA = ['tln-10A04R02T01', 'tln-10A12R02T01', 'tln-10A22R02T01',
                'tln-10A35R02T01', 'tln-10A49R02T01', 'tln-10A58R02T01']
TC_liquid_CA2 = ['tln-10A04R03T01', 'tln-10A12R03T01', 'tln-10A22R03T01',
                 'tln-10A35R03T01', 'tln-10A49R03T01', 'tln-10A58R03T01']
TC_liquid_CA1_csv = 'TC_liquid_CA1.csv'
TC_liquid_HA_csv = 'TC_liquid_HA.csv'
TC_liquid_CA2_csv = 'TC_liquid_CA2.csv'

# Vapor temperature with thermocouple measurement (not really measured the
# vapor temperature though)
TC_vapor_CA1 = ['tvn-10A04R01T01', 'tvn-10A12R01T01', 'tvn-10A22R01T01',
                'tvn-10A35R01T01', 'tvn-10A49R01T01', 'tvn-10A58R01T01']
TC_vapor_HA = ['tvn-10A04R02T01', 'tvn-10A12R02T01', 'tvn-10A22R02T01',
               'tvn-10A35R02T01', 'tvn-10A49R02T01', 'tvn-10A58R02T01']
TC_vapor_CA2 = ['tvn-10A04R03T01', 'tvn-10A12R03T01', 'tvn-10A22R03T01',
                'tvn-10A35R03T01', 'tvn-10A49R03T01', 'tvn-10A58R03T01']
TC_vapor_CA1_csv = 'TC_vapor_CA1.csv'
TC_vapor_HA_csv = 'TC_vapor_HA.csv'
TC_vapor_CA2_csv = 'TC_vapor_CA2.csv'

# Void fraction at selected location (though no measurement)
alpha_CA1 = ['alpn-10A04R01T01', 'alpn-10A12R01T01', 'alpn-10A22R01T01',
             'alpn-10A35R01T01', 'alpn-10A49R01T01', 'alpn-10A58R01T01']
alpha_HA = ['alpn-10A04R02T01', 'alpn-10A12R02T01', 'alpn-10A22R02T01',
            'alpn-10A35R02T01', 'alpn-10A49R02T01', 'alpn-10A58R02T01']
alpha_CA2 = ['alpn-10A04R03T01', 'alpn-10A12R03T01', 'alpn-10A22R03T01',
             'alpn-10A35R03T01', 'alpn-10A49R03T01', 'alpn-10A58R03T01']
alpha_CA1_csv = 'alpha_CA1.csv'
alpha_HA_csv = 'alpha_HA.csv'
alpha_CA2_csv = 'alpha_CA2.csv'

# Pressure at location with pressure transducer (for pressure drop) 
pressure_CA1 = ['pn-10A04R01T01', 'pn-10A12R01T01', 'pn-10A22R01T01',
                'pn-10A35R01T01', 'pn-10A49R01T01', 'pn-10A58R01T01']
pressure_HA = ['pn-10A04R02T01', 'pn-10A12R02T01', 'pn-10A22R02T01',
               'pn-10A35R02T01', 'pn-10A49R02T01', 'pn-10A58R02T01']
pressure_CA2 = ['pn-10A04R03T01', 'pn-10A12R03T01', 'pn-10A22R03T01',
                'pn-10A35R03T01', 'pn-10A49R03T01', 'pn-10A58R03T01']
pressure_CA1_csv = 'pressure_CA1.csv'
pressure_HA_csv = 'pressure_HA.csv'
pressure_CA2_csv = 'pressure_CA2.csv'
