from config_manager import ConfigManager


class TestingConfig(ConfigManager):
    """Testing Config."""

    first_time_run: bool = True


if __name__ == "__main__":
    config = TestingConfig("testing.json")
    config.load()
    print("first_time_run: ", config.first_time_run)
    config.first_time_run = False
    config.save()
