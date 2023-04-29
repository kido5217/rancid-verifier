"""CLI unit tests."""

from rancid_verifier.cli import VerifyCommand

from cleo.application import Application
from cleo.testers.command_tester import CommandTester


def test_execute():
    application = Application()
    application.add(VerifyCommand())

    command = application.find("verify")
    command_tester = CommandTester(command)
    command_tester.execute("tests/fixtures/")

    assert "" == command_tester.io.fetch_output()
