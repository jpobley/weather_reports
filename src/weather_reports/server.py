
from concurrent import futures
import logging

import grpc

import weather_reports_pb2
import weather_reports_pb2_grpc


class Aggregator(weather_reports_pb2_grpc.WeatherReportAggregatorServicer):

    def SendReport(self, request, context):
        print("Server received:", request)
        return weather_reports_pb2.ReportReceived()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    weather_reports_pb2_grpc.add_WeatherReportAggregatorServicer_to_server(Aggregator(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
