# Running tests

```
cd tiptapy
pytest -xv
``` 


# Build / Release

```
bumpversion --dry-run --verbose patch  # or major, minor
bumpversion run patch  # or major, minor

rm -rf dist/ build/
python setup.py build sdist
twine upload dist/tiptapy-*.tar.gz --repository tiptapy
```
