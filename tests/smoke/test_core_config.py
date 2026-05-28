from nelo.core import NeloConfig


def test_default_config_values() -> None:
    config = NeloConfig()
    assert config.env
    assert config.offline_first is True
