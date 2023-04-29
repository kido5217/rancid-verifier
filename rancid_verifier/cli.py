"""CLI entry point."""

from typing import TYPE_CHECKING

from cleo.application import Application
from cleo.commands.command import Command
from cleo.helpers import argument, option

if TYPE_CHECKING:
    from cleo.io.inputs.argument import Argument


class VerifyCommand(Command):
    """Verify cleo command class."""

    name: str = "verify"
    description: str = "Run verification on router.db files"
    arguments: list["Argument"] = [
        argument(
            "path",
            description="Path to router.db file or directory to look for it in",
        )
    ]

    def handle(self) -> None:
        ...


def cli() -> None:
    application: Application = Application("rver")
    application.add(VerifyCommand())
    application.run()
