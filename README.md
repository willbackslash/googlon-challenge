# googlon-challenge

## About this project

This project uses python 2.7 with pip

## Setup

1. Create a new virtualenv
> virtualenv ./googlon-env

2. Activate the virtualenv
> source ./googlon-env/bin/activate

3. Install python dependencies
> pip install -r requirements.txt

## Run tests and see the results
> python -m pytest -v -s

## Package usage

GooglonAnalyzer is a class with static methods so you can include the package as part of your project and include it using:

```python
from googlon.GooglonAnalyzer import GooglonAnalyzer
```

### Maintainer
William De la Cruz (willbackslash)
