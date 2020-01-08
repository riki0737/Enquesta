#!/bin/bash

antlr4 -Dlanguage=Python3 -no-listener -visitor $1
