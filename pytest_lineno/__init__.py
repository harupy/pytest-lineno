import sys

from _pytest.terminal import TerminalReporter
import pytest


class NewTerminalReporter(TerminalReporter):
    def _locationline(self, nodeid, fspath, lineno, domain):
        res = super()._locationline(nodeid, fspath, lineno, domain)
        return res.replace("::", ":{}::".format(lineno), 1)


@pytest.hookimpl(trylast=True)
def pytest_configure(config):
    if config.getoption("show_lineno"):
        # Unregister the default terminal reporter
        old_reporter = config.pluginmanager.getplugin("terminalreporter")
        config.pluginmanager.unregister(old_reporter)

        # Register the new terminal reporter
        new_reporter = NewTerminalReporter(config, sys.stdout)
        config.pluginmanager.register(new_reporter, "terminalreporter")


def pytest_addoption(parser):
    group = parser.getgroup("lineno", "show line number of test functions")
    group._addoption(
        "--show-lineno",
        dest="show_lineno",
        action="store_true",
        default=False,
    )
