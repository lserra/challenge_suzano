#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ==============================================================================
# EXPLORATORY DATA ANALYSIS
# ==============================================================================
# Created by: laercio.serra@gmail.com
# Created at: 20/03/2021
# ==============================================================================


# Defining the libraries
import os
import pandas as pd
import pandas_profiling as pp

# Defining parameters
path = '/Users/lserra/PyProjects/challenge_suzano'
inputfile = path + "/input/"
outputfile = path + "/output/analysis/"


def data_profiling(list_files):
    """Data profiling for each CSV file found in the directory"""

    for filename in list_files:
        name, ext = os.path.splitext(filename)
        if ext != '.csv':
            print(">> WARNING: CSV file invalid!")
            return False

        # Creating pandas dataframe
        df = pd.read_csv(inputfile + filename, sep=',', header=0)

        # Data profiling for each CSV file
        print("-".rjust(60, "-"))
        print(f'>> Generating Profile Report: {filename}')
        profile = pp.ProfileReport(df)

        # Printing the results to html
        print(f'>> Exporting Profile Report to HTML: {filename}')
        print("-".rjust(60, "-"))
        profile.to_file(output_file=outputfile + name + '.html')

    return True


if __name__ == "__main__":
    files = os.listdir(inputfile)
    if data_profiling(files):
        print("\n>> Process finished successfully!")
    else:
        print("\n>> Something wrong with the system!")
