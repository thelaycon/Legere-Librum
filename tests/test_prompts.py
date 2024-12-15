import pytest
import tempfile
import os

from transcribe import get_prompt

# Test cases
def test_get_prompt():
    # Create temporary files with mock content
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"This is a test prompt.")
        temp_file_path = temp_file.name

    try:
        # Test that the function reads the file content correctly
        result = get_prompt(temp_file_path)
        assert result == "This is a test prompt.", "The content does not match the expected prompt."
    finally:
        # Clean up temporary file
        os.remove(temp_file_path)


def test_get_prompt_file_not_found():
    # Test behavior when the file does not exist
    non_existent_file = "non_existent_file.txt"
    with pytest.raises(FileNotFoundError):
        get_prompt(non_existent_file)


def test_get_prompt_empty_file():
    # Create an empty temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name

    try:
        # Test that the function handles empty files correctly
        result = get_prompt(temp_file_path)
        assert result == "", "The function should return an empty string for an empty file."
    finally:
        # Clean up temporary file
        os.remove(temp_file_path)