import importlib

MODULES = [
    "nelo",
    "nelo.core",
    "nelo.inference",
    "nelo.routing",
    "nelo.memory",
    "nelo.multimodal",
    "nelo.backend",
    "nelo.hardware",
    "nelo.utils",
]


def test_package_imports() -> None:
    for module in MODULES:
        imported = importlib.import_module(module)
        assert imported is not None
