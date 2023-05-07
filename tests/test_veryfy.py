from rancid_verifier.main import verify_file


def test_encoding_ascii():
    file_path: str = "tests/fixtures/router_db_files/router_db_ascii.txt"

    result = verify_file(file_path)

    assert len(result.errors) == 0


def test_encoding_utf8():
    file_path: str = "tests/fixtures/router_db_files/router_db_utf8.txt"

    result = verify_file(file_path)

    assert len(result.errors) == 0


def test_encoding_cp1251():
    file_path: str = "tests/fixtures/router_db_files/router_db_cp1251.txt"

    result = verify_file(file_path)

    assert result.errors.get("not_utf8") is True
