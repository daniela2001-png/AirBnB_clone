#!/usr/bin/env bash
python3 -m unittest discover tests $@
if which pep8 &>/dev/null; then
	pep8 $(find . -name "*.py")
else
	pycodestyle $(find . -name "*.py")
fi
