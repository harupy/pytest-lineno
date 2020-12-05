import subprocess


def test_func():
    pass


class TestClass:
    def test_method(self):
        pass


def run_pytest(directory, options=None):
    if options is None:
        options = []

    result = subprocess.run(
        ["pytest", str(directory)] + options, stdout=subprocess.PIPE
    )
    return result.stdout.decode("utf-8")


def test_show_lineno(tmpdir):
    code = """
def test_func():
    pass


class TestClass:
    def test_method(self):
        pass
"""
    with open(tmpdir.join("test_file.py"), "w") as f:
        f.write(code.strip())

    output = run_pytest(tmpdir, ["--show-lineno", "--verbose"])
    assert "test_file.py:0::test_func" in output
    assert "test_file.py:5::TestClass::test_method" in output


def test_show_lineno_only_when_show_lineno_is_specified(tmpdir):
    code = """
def test_func():
    pass


class TestClass:
    def test_method(self):
        pass
"""
    with open(tmpdir.join("test_file.py"), "w") as f:
        f.write(code.strip())

    output = run_pytest(tmpdir, ["--verbose"])
    assert "test_file.py::test_func" in output
    assert "test_file.py::TestClass::test_method" in output
