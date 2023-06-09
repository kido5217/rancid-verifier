import pathlib

from rancid_verifier.main import get_file_list


def test_one_file():
    path_raw = "tests/fixtures/repo/router.db"

    expected_path = [pathlib.Path(path_raw)]
    result_path = get_file_list(path_raw)

    assert expected_path == result_path


def test_dir():
    path_raw = "tests/fixtures/repo/"
    expected_path = [pathlib.Path(path_raw) / "router.db"]

    result_path = get_file_list(path_raw)

    assert expected_path == result_path
