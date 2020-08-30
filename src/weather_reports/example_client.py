from weather_reports.clients import SenseHatClient

def get_stub(address):
    channel = grpc.insecure_channel(address)
    stub = weather_reports_pb2_grpc.WeatherReportAggregatorStub(channel)
    return stub, channel

def run():
    client = SenseHatClient()
    stub, channel = get_stub('host.docker.internal:50051')
    response = stub.SendReport(report)
    channel.close()

if __name__ == '__main__':
    run()
