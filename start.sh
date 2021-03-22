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

dir="./input"
if [ -d $dir ]; then
  echo "=> [OK] - CSV FILES"
else
	echo "=> [NOK] - Directory '/input' does not exists!"
	exit
fi

dir="./db"
if [ -d $dir ]; then
  echo "=> [OK] - SQLITE DATABASE"
else
	echo "=> [NOK] - Directory '/db' does not exists!"
	exit
fi

dir="./src"
if [ -d $dir ]; then
  echo "=> [OK] - PYTHON SCRIPTS"
else
	echo "=> [NOK] - Directory '/src' does not exists!"
	exit
fi

dir="./venv"
if [ -d $dir ]; then
  echo "=> [OK] - VIRTUAL ENVIRONMENT"
  source venv/bin/activate
else
	echo "=> [NOK] - Directory '/venv' does not exists!"
	exit
fi

# Check for file existence
file="./src/csv_to_sqlite.py"
if [ -e $file ]; then
	echo "=> [OK] - SCRIPT: CSV TO SQLITE"
else
	echo "=> [NOK] - Script 'csv_to_sqlite.py' does not exists!"
	exit
fi

file="./src/gerar_json.py"
if [ -e $file ]; then
	echo "=> [OK] - SCRIPT: GERAR JSON FILE"
else
	echo "=> [NOK] - Script 'gerar_json.py' does not exists!"
	exit
fi

echo "----------------------------------------------"
echo "=> JOB FINISHED!"
echo "----------------------------------------------"
echo

# Check if file is readable
file="./start.py"
if [ -r $file ]; then
  python3 ./start.py
else
  echo "=> [NOK] - File 'start.py' is not readable!"
fi