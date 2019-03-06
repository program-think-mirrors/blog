#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import shutil


def main() :
    cwd = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(cwd)
    if os.name == 'nt' :
        os.putenv('PATH', os.getenv('PATH')+os.pathsep+cwd)

    chm_file = os.path.abspath('./program-think.chm')
    if os.path.exists(chm_file) :
        os.remove(chm_file)

    shutil.copy('./conf/program-think.hhp', '../../html/')
    shutil.copy('./conf/program-think.hhc', '../../html/')

    os.chdir('../../html/')
    cmd = 'hhc.exe program-think.hhp'
    if os.name != 'nt' :
        cmd = 'wine ' + cmd
    os.system(cmd)

    os.remove('./program-think.hhp')
    os.remove('./program-think.hhc')
    if not os.path.exists(chm_file) :
        raise ValueError('Compile chm failed!')
    print('\n\nCHM OK')
    if os.name == 'nt' :
        os.system(chm_file)
    return 0


if '__main__' == __name__ :
    try :
        sys.exit(main())
    except Exception as err :
        print('Error:\n' + str(err))
        sys.exit(1)

