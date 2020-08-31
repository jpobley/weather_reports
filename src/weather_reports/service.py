from concurrent import futures
import grpc
import logging
import os

import weather_reports_pb2
import weather_reports_pb2_grpc


GRPC_PORT = os.getenv('GRPC_PORT')
GRPC_HOST = os.getenv('GRPC_HOST')
MAX_WORKERS = os.getenv('MAX_WORKERS', 10)

class Aggregator(weather_reports_pb2_grpc.WeatherReportAggregatorServicer):

    def SendReport(self, request, context):
        print("Server received:", request)
        return weather_reports_pb2.ReportReceived()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=MAX_WORKERS))
    weather_reports_pb2_grpc.add_WeatherReportAggregatorServicer_to_server(Aggregator(), server)
    server.add_insecure_port(f'{GRPC_HOST}:{GRPC_PORT}')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
