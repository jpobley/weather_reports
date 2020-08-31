#! /bin/bash

set -e

build_dir=./src

if [[ -n "${USE_VENV}" ]]
then
    if [ ! -d .venv ]
    then
        echo 'Setting up virtual environment...'
        python3 -m venv .venv
    fi
    source .venv/bin/activate
fi

echo 'Installing requirements.txt...'
pip3 install -r requirements.txt

echo 'Building protbufs...'
python3 -m grpc_tools.protoc \
    -I ./proto \
    --python_out=$build_dir \
    --grpc_python_out=$build_dir \
    ./proto/weather_reports.proto

pushd $build_dir

echo 'Installing weather_reports module...'
python3 setup.py install

popd

unset build_dir
