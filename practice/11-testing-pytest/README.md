# 11 — Testing with Pytest

> **Topic**: Unit testing Python code and Flask APIs using pytest

## What This Demonstrates

A comprehensive exploration of the `pytest` testing framework — from basic
assertions to API integration testing. Each file builds on the previous one.

## Files (in learning order)

| File | What I Learned |
|------|---------------|
| `test_intro.py` | Pytest basics — naming conventions, first test function |
| `test_intro2.py` | Python `assert` statement — how assertions work |
| `test_intro3.py` | Test classes — grouping related tests in a class |
| `test_intro4.py` | Markers — `@pytest.mark.skip`, `skipif`, `parametrize` |
| `test_intro5.py` | `@pytest.mark.xfail` — expected failures |
| `test_intro6.py` | API testing — using `requests` library to test Flask endpoints |
| `app.py` | Flask app used as the API target for test_intro6 |
| `guide.txt` | My personal notes on pytest conventions and commands |

## Key Pytest Commands

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run only tests with a specific marker
pytest -m smoke

# Run a specific test file
pytest test_intro4.py
```

## Concepts Covered

- Naming conventions: files start with `test_`, functions start with `test_`
- `assert` statements for validation
- Test classes: `class TestExample` with `test_` methods
- Markers: `@pytest.mark.skip`, `@pytest.mark.skipif`, `@pytest.mark.xfail`
- Parametrization: `@pytest.mark.parametrize` for data-driven tests
- API testing: sending HTTP requests and validating responses

## Prerequisites

```bash
pip install pytest requests
```
