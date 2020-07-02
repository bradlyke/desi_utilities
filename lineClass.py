class Lines:
    def __init__(self,line_name):
        line_name = self.name_cleaner(line_name)
        if line_name == 'cii':
            line_name = 'ciir' #default to semi-forbidden, it's more common
        elif line_name == 'oiii':
            line_name = 'oiiir' #When calling one in the doublet, use more common

        self.name = self.line_display(line_name)
        self.restwave = self.line_list(line_name)

    def name_cleaner(self,name):
        name = name.strip(']').strip('[').lower().replace(' ','')
        return name

    def line_list(self,name):
        lines = {
                    'lyb' : 1025.72,
                    'lya' : 1215.67,
                    'oi' : 1304.35,
                    'ciib' : 1335.30,
                    'siiv' : 1396.76,
                    'oiv' : 1402.06,
                    'civ' : 1549.06,
                    'heii' : 1640.42,
                    'ciii' : 1908.73,
                    'ciir' : 2326.44,
                    'feii' : 2626.92, #observed, not lab. lab is UV I
                    'mgii' : 2798.75,
                    'oii' : 3728.48,
                    'hd' : 4102.89,
                    'hg' : 4341.68,
                    'hb' : 4862.68,
                    'oiiib' : 4960.30,
                    'oiiir' : 5008.24,
                    'ha' : 6564.61
        }

        return lines[name]

    def line_display(self,name):
        line_names = {
                    'lyb' : 'Ly b',
                    'lya' : 'Ly a',
                    'oi' : 'O I',
                    'ciib' : 'C II',
                    'siiv' : 'Si IV',
                    'oiv' : 'O IV]',
                    'civ' : 'C IV',
                    'heii' : 'He II',
                    'ciii' : 'C III]',
                    'ciir' : 'C II]',
                    'feii' : 'Fe II',
                    'mgii' : 'Mg II',
                    'oii' : '[O II]',
                    'hd' : 'H d',
                    'hg' : 'H g',
                    'hb' : 'H b',
                    'oiiib' : '[O III]',
                    'oiiir' : '[O III]',
                    'ha' : 'H a'
        }

        return line_names[name]

    def list_lines(self):
        emlines = ['lyb','lya','oi','ciib','siiv','oiv','civ','heii','ciii',
                    'ciir','feii','mgii','oii','hd','hg','hb','oiiib',
                    'oiiir','ha']
        return emlines

if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Returns rest wavelength of common quasar broad emission lines')
    parser.add_argument('-n', '--line_name', default='mgii', metavar='',
                        help="The emission line name")
    parser.add_argument('-l', '--list_names', action='store_true',
                        help='List the lines included in class')
    args = parser.parse_args()

    line = Lines(args.line_name)
    if args.list_names==True:
        print('\n')
        print('   Line Name   |  Rest Wavelength  |  Variable Name ')
        print('----------------------------------------------------')
        for elname in line.list_lines():
            el = Lines(elname)
            if elname == 'oiiib' or elname=='oiiir':
                print('   {} d   |    {:.2f} Ang    |   {}'.format(el.name,el.restwave,elname))
            else:
                print('    {:7s}    |    {:.2f} Ang    |   {}'.format(el.name,el.restwave,elname))
        print('--Note: d means these form a doublet.')
        print('--Note: "cii" defaults to ciir and "oiii" defaults to oiiir.')
    else:
        print('\n   Line Name      : {}'.format(line.name))
        print('   Rest Wavelength: {} Ang'.format(line.restwave))

    #In another program, use like:
    # from lineClass import Lines
    # ...
    # em = Lines('mgii')
    # em.restwave -> (stores just the number)
    # em.name -> (stores the display name with appropriate brackets)
