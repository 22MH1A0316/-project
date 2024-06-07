import pytest
from project import load_config, validate_input, create_pdf

def test_load_config():
    config = load_config()
    assert isinstance(config, dict)
    assert "font" in config
    assert "title" in config

def test_validate_input():
    assert validate_input("John Doe", "This is a test message") == True

    with pytest.raises(ValueError):
        validate_input("", "This is a test message")

    with pytest.raises(ValueError):
        validate_input("John Doe", "")

def test_create_pdf():
    config = load_config()
    try:
        create_pdf("John Doe", "This is a test message", config)
    except Exception as e:
        pytest.fail(f"create_pdf raised an exception: {e}")

