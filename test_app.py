import os


# Fake test
def test_set_version():
    os.environ["VERSION"] = "ver1"
    assert os.environ.get("VERSION") == "ver1"
