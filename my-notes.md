To build a new version:

---
Update setup.py version
---
---
```
python setup.py sdist bdist_wheel
```
Local test:
```
pip install -e .
```
Unistall local package:

```
pip uninstall qifhdc
```

Release testpypi:
```
twine upload --repository testpypi dist/*
```

Release:
```
twine upload dist/*
```