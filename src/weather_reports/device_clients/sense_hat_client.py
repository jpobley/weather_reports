#!/usr/bin/env python3

import grpc
from sense_hat import SenseHat

from .base_client import BaseClient
import weather_reports_pb2


class SenseHatClient(BaseClient):
    def __init__(self):
        self.hat = SenseHat()

    @property
    def report(self):
        location = weather_reports_pb2.Location(
                name = 'Ohana',
                geo = weather_reports_pb2.Location.LatLng(lat=37.4666168, lng=122.2211412),
                timestamp = self.now
            )

        report = weather_reports_pb2.WeatherStationReport(
                location = location,
                sensors = weather_reports_pb2.SensorData(
                        temp = self.hat.temp,
                        humidity = self.hat.humidity,
                        pressure = self.hat.pressure
                    )
            )

        return report
