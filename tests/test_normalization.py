import importlib
from pathlib import Path


def test_core_packages_importable():
    for module_name in (
        "mintcastiq_ingest",
        "mintcastiq_ingest.config",
        "mintcastiq_ingest.normalization",
        "mintcastiq_ingest.persistence",
        "mintcastiq_ingest.vlm",
    ):
        mod = importlib.import_module(module_name)
        assert mod is not None


def test_normalization_modules_present():
    norm_dir = Path("mintcastiq_ingest/normalization")
    expected = {"dicts.py", "filename_builder.py", "normalize.py", "pokemon_series.py", "teams.py"}
    actual = {p.name for p in norm_dir.glob("*.py")}
    assert expected.issubset(actual)
