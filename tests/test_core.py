from swdhub import core


def test_run():
    assert core.run("  x  ") == "x"
