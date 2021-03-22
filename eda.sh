#!/bin/bash

# ==============================================================================
# Created by: laercio.serra@gmail.com
# Created at: 20/03/2021
# ==============================================================================
clear

echo "WELCOME TO SUZANO CHALLENGE FOR DATA ENGINEER!"
echo "NAME: LAERCIO SERRA"
echo "----------------------------------------------"
echo "=> CHECKING APPLICATION . . ."
echo "----------------------------------------------"

# Check for file existence
file="./src/analysis/eda.py"
if [ -e $file ]; then
	echo "=> [OK] - EXPLORATORY DATA ANALYSIS"
else
	echo "=> [NOK] - File 'eda.py' does not exists!"
fi

# Check if file is readable
file="./src/analysis/eda.py"
if [ -r $file ]; then
  python3 ./src/analysis/eda.py
else
  echo "=> [NOK] - File 'eda.py' is not readable!"
fi