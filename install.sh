#!/bin/bash

quiet=no
withman=yes

_help(){
    echo -e "LMFS-PSML Full installation script
Usage: install.sh [targets...]
Targets:
    -quiet:		Use nohup to prevent the python interpreter or pip from outputting information
    -without-manual:	Prevent the installation of the PSML interpreter parameter manual
    -force-interp:	Force installation with python interpreter
    -force-pip:		Force installation with pip
    -help:		Show this help

Feedback: <Lone-air_Use@outlook.com>"
}

for i in "$@"
do
    if [ "$i" = "-quiet" ]; then
        quiet=yes
    elif [ "$i" = "-without-manual" ]; then
        withman=no
    elif [ "$i" = "-force-interp" ]; then
        usepip=no
    elif [ "$i" = "-force-pip" ]; then
        usepip=yes
    elif [ "$i" = "-help" ]; then
        _help
        exit 0
    else
        echo -e "[\033[91;1mError\033[0m] Unrecognized option [$i]"
        exit 1
    fi
done

if [ $UID != 0 ]; then
    echo -e "[\033[95;1mWarning\033[0m] Running this script without root may cause problems"
fi

python_interp=$(which python3)
gzip_path=$(which gzip)
pip=$(which pip3)

if [ "$python_interp" = "" ]; then
    echo -e "[\033[91;1mError\033[0m] Python interpreter not found, please check your python installation"
    exit 1
fi

if [ "$pip" = "" ] && [ "$usepip" = "yes" ]; then
    echo -e "[\033[91;1mError\033[0m] No pip found"
    exit 1
fi

if [ "$pip" != "" ] || [ "$usepip" = "yes" ] && [ "$usepip" != "no" ]; then
    if [ "$quiet" = "yes" ]; then
        echo -e "[\033[93;1mINFO\033[0m] Installing main part of psml (using pip)"
        nohup $pip install --upgrade .
    else
        $pip install --upgrade .
    fi
else
    if [ "$quiet" = "yes" ]; then
        echo -e "[\033[93;1mINFO\033[0m] Installing main part of psml (using python interpreter)"
        nohup $python_interp setup.py install
    else
        $python_interp setup.py install
    fi
fi

if [ $? -ne 0 ]; then
    echo -e "[\033[91;1mError\033[0m] Install Failed, please see the nohup.out for information"
    exit 1
fi

if [ "&withman" = "yes" ]; then
    if [ -d "/usr/local/share/man/man1" ]; then
        shared="/usr/local/share/man/man1"
    elif [ -d $(dirname $python_interp)/share/man/man1 ]; then
        shared=$(dirname $python_interp)/share/man/man1
    else
        mkdir -p "/usr/local/share/man/man1"
        if [ "$?" != 0 ]; then
            echo -e "[\033[91;1mError\033[0m] Cannot create manual pages directory"
        else
            echo -e "[\033[93;1mINFO\033[0m] Manual pages directory created"
        fi
        shared="/usr/local/share/man/man1"
    fi
fi

if [ "$shared" != "" ]; then
    if [ "$gzip_path" = "" ]; then
        echo -e "[\033[91;1mError\033[0m] Gzip command not found"
        exit 1
    fi
    rm psml.1.gz
    cp psml.1 psml.1.bak
    $gzip_path psml.1
    cp psml.1.gz $shared
    mv psml.1.bak psml.1
    rm psml.1.gz nohup.out
else
    rm nohup.out
fi

echo -e "[\033[92;1mSuccessfully\033[0m] Install Successfully"
