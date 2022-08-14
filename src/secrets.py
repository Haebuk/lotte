from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

from src import constants

credential = DefaultAzureCredential()


class Secrets:
    def __init__(self, url: constants.VAULT_URL) -> None:
        self.credential = DefaultAzureCredential()
        self.client = SecretClient(vault_url=url.value, credential=credential)

    def get_secret_value(self, name: str):
        return self.client.get_secret(name).value

    def get_secret_name_value_dict(self) -> dict:
        secret_properties = self.client.list_properties_of_secrets()

        db_config = {}

        for s in secret_properties:
            db_config[s.name] = self.get_secret_value(s.name)

        return db_config
