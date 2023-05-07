import pathlib
from dataclasses import dataclass, field
from typing import Any


@dataclass
class VerificationResult:
    file_path: pathlib.Path
    errors: dict[str, bool] = field(default_factory=dict)


def verify_file(file_path: str | pathlib.Path) -> Any:
    result = VerificationResult(file_path=pathlib.Path(file_path))

    try:
        open(file_path, "r", encoding="utf-8").read()
    except UnicodeDecodeError:
        result.errors["not_utf8"] = True

    return result


def get_file_list(path_raw: str, file_name: str = "router.db") -> list[pathlib.Path]:
    """Get files from provided path."""

    path = pathlib.Path(path_raw)

    if path.is_file():
        return [path.with_name(file_name)]

    return list(path.glob(file_name))
