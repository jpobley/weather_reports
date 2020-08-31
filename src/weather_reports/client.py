#!/usr/bin/env python3

import importlib
import os
import sys


def run():
    CLIENT_TYPE = os.getenv('CLIENT_TYPE')

    module = None
    class_name = None

    if not CLIENT_TYPE:
        return

    if CLIENT_TYPE == 'sense_hat':
        module = 'sense_hat_client'
        class_name = 'SenseHatClient'
    elif CLIENT_TYPE == 'enviro_plus':
        module = 'enviro_plus_client'
        class_name = 'EnviroPlusClient'

    client_module = importlib.import_module(f'weather_reports.device_clients.{module}')
    client_class = getattr(client_module, client_class)

    client = client_class()

    print(client.report)

if __name__ == '__main__':
    run()
