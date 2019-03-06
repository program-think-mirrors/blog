#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from zipfile import *
import re



def main() :
    cwd = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(cwd)

    epub_file = 'program-think.epub'
    if os.path.exists(epub_file) :
        os.remove(epub_file)

    zf = ZipFile(epub_file, 'w', ZIP_DEFLATED)
    for folder in ['./conf/', '../../html/'] :
        os.chdir(os.path.join(cwd, folder))
        add_folder(zf, '.', None)
    zf.close()

    print('\nEPUB OK')
    return 0


def add_folder(zf, folder, count) :
    info = ''
    if re.match(r'^\.(?:/|\\)20\d{2}$', folder) :
        info = folder[-4:]
    elif re.match(r'^\.(?:/|\\)(?:archive|images|tags)$', folder) :
        info = folder.split(os.sep)[-1]
    if info :
        print(info)
        count = 0

    children = os.listdir(folder)
    children.sort()
    for name in children :
        name = os.path.join(folder, name)
        if os.path.isdir(name) :
            count = add_folder(zf, name, count)
        else :
            zf.write(name)
            if count is not None :
                count += 1
                if (count % 10) == 0 :  # optimize
                    sys.stdout.write(str(count)+'\r')
                    sys.stdout.flush()
    if info :
        print(str(count))
        return None
    else :
        return count



if '__main__' == __name__ :
    try :
        sys.exit(main())
    except Exception as err :
        print('Error:\n' + str(err))
        sys.exit(1)

