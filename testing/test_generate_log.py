import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from datetime import datetime
from generate_log import generate_log

@pytest.fixture
def log_data():
    return ["Entry one", "Entry two", "Entry three"]

@pytest.fixture
def generated_file(log_data):
    filename = generate_log(log_data)
    yield filename
    if os.path.exists(filename):
        os.remove(filename)

def test_log_file_created(generated_file):
    assert os.path.exists(generated_file)

def test_log_file_name_format(generated_file):
    today = datetime.now().strftime("%Y%m%d")
    assert generated_file == f"log_{today}.txt"

def test_log_file_content_matches_input(generated_file, log_data):
    with open(generated_file, "r") as file:
        lines = [line.strip() for line in file.readlines()]
    assert lines == log_data

def test_generate_log_raises_error_on_invalid_input():
    with pytest.raises(ValueError):
        generate_log("This should be a list")

def test_empty_log_list_creates_empty_file():
    filename = generate_log([])
    with open(filename, "r") as file:
        content = file.read()
    assert content == ""
    os.remove(filename)
