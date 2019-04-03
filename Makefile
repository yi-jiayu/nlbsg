.PHONY: clean test version build publish

output = dist/*

all: test build

test:
	pipenv run python -m pytest --cov

clean:
	rm -rf dist

build: clean version
	python setup.py sdist bdist_wheel
	pipenv run twine check $(output)

version:
	printf "# generated\n__version__ = '$(shell git describe | sed s/^v//)'\n" > nlbsg/__version__.py

publish: build
	pipenv run twine upload $(output)
