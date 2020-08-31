from setuptools import setup

setup(
    name='weather_reports',
    version='0.1.0',
    packages=[
        'weather_reports',
        'weather_reports.device_clients'
    ],
    py_modules=['weather_reports_pb2', 'weather_reports_pb2_grpc'],
    zip_safe=False
)
