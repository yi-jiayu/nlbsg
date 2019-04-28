.PHONY: hooks clean test version build publish docs

output = dist/*

all: test build

test:
	pipenv run python -m pytest -vv --cov

clean:
	rm -rf dist

build: clean version
	pipenv run python setup.py sdist bdist_wheel
	pipenv run twine check $(output)

version:
	printf "# generated\n__version__ = '$(shell git describe | sed s/^v//)'\n" > nlbsg/__version__.py

publish: build
	pipenv run twine upload $(output)

docs:
	$(MAKE) -C docs html

hooks:
	cp -f pre-commit .git/hooks/