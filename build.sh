#! /bin/bash

set -e

build_dir=./src

if [ ! -d .venv ]
then
    echo 'Setting up virtual environment...'
    python3 -m venv .venv
fi

source .venv/bin/activate

echo 'Installing requirements.txt...'
pip install -r requirements.txt

echo 'Building protbufs'
python -m grpc_tools.protoc \
    -I ./proto \
    --python_out=$build_dir \
    --grpc_python_out=$build_dir \
    ./proto/weather_reports.proto

pushd $build_dir

python setup.py install

popd

unset build_dir
