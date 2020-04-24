# Running tests

```
cd tiptapy
pytest -xv
``` 


# Build / Release

```
python setup.py build sdist
bumpversion --dry-run --verbose patch  # or major, minor
bumpversion --dry-run patch  # or major, minor
```
