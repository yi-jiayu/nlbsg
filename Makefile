.PHONY: clean build version publish

all: clean build

clean:
	rm -rf dist

build: version
	python setup.py sdist bdist_wheel

version:
	printf "# generated\n__version__ = '$(shell git describe | sed s/^v//)'\n" > nlbsg/__version__.py

publish: build
	pipenv run twine upload dist/*
