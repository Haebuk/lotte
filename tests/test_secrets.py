from src import constants, secrets


class TestSecrets:
    s = secrets.Secrets(url=constants.VAULT_URL.TEST)

    def test_get_secret_value(self):
        assert "test123" == self.s.get_secret_value("test")

    def test_get_secret_name_value_dict(self):
        assert {"test": "test123"} == self.s.get_secret_name_value_dict()
