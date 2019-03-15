#!/bin/bash

if [[ "$HPP_COMPILE" ]]; then
    pyinstaller --onefile --name hpp src/__main__.py
else
    exec-hpp
fi
