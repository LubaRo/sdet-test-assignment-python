from pathlib import Path


def get_test_file_absolute_path(filename):
    root_dir = Path(__file__).parent.parent.parent
    file_path = f"{str(root_dir)}/test_files/{filename}"
    return file_path
