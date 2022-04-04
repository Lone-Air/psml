#!/bin/sh

quiet=no

for i in "$@"
do
    if [ "$i" = "-quiet" ]; then
        quiet=yes
    fi
done

if [ "$UID" != 0 ]; then
    echo "[\033[95;1mWarning\033[0m] Running this script without root may cause problems"
fi

python_interp=$(which python3)
gzip_path=$(which gzip)

if [ "$python_interp" = "" ]; then
    echo "[\033[91;1mError\033[0m] Python interpreter not found, please check your python installation"
    exit 1
fi

if [ "$quiet" = "yes" ]; then
    echo "[\033[93;1mINFO\033[0m] Installing main part of psml"
    nohup $python_interp setup.py install
else
    $python_interp setup.py install
fi

if [ "$?" != 0 ]; then
    echo "[\033[91;1mError\033[0m] Install Failed"
    exit 1
fi

if [ -d "/usr/local/share/man/man1" ]; then
    shared="/usr/local/share/man/man1"
elif [ -d $(dirname $python_interp)/share/man/man1 ]; then
    shared=$(dirname $python_interp)/share/man/man1
else
    mkdir -p "/usr/local/share/man/man1"
    if [ "$?" != 0 ]; then
        echo "[\033[91;1mError\033[0m] Cannot create manual pages directory"
        exit 1
    else
        echo "[\033[93;1mINFO\033[0m] Manual pages directory created"
    fi
    shared="/usr/local/share/man/man1"
fi

if [ "$gzip_path" = "" ]; then
    echo "[\033[91;1mError\033[0m] Gzip command not found"
    exit 1
fi

rm psml.1.gz
cp psml.1 psml.1.bak
$gzip_path psml.1
cp psml.1.gz $shared
mv psml.1.bak psml.1
rm psml.1.gz nohup.out

echo "[\033[92;1mSuccessfully\033[0m] Install Successfully"
