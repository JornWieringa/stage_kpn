from schiphol.api_client import SchipholApiClient
from settings.config import Config

my_config = Config()
my_client = SchipholApiClient(my_config)

result = my_client.get_flights()

print(result)
