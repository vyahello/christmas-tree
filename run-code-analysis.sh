#!/usr/bin/env bash

PACKAGE="christmas"


check-black() {
    black --check ${PACKAGE}
}


check-pylint() {
    pylint ${PACKAGE}
}


check-unittests() {
    pytest -v tests
}


main() {
    check-black && check-pylint && check-unittests
}


main
