# pytest-lineno

A pytest plugin to show the line numbers of test functions.

## Installation

```sh
# From PyPI
pip install pytest-lineo

# From GitHub
pip install git+https://github.com/harupy/pytest-lineno.git
```

## Usage

```sh
pytest --show-lineno --verbose
```

The output should look like:

```sh
tests/test_file.py:0::test_func PASSED               [ 50%]
tests/test_file.py:5::TestClass::test_method PASSED  [100%]
                # ^^^
                # By clicking `tests/test_file.py:5`,
                # you can jump to `TestClass.test_method`
                # (if your code editor recognizes this format as a link)
```
