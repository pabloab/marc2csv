### marc2csv

marc2csv - command-line tool to convert a MARC file to an Excel-ready CSV file.

Forked from [benmiller314 version](https://github.com/benmiller314/marc2csv).

## Overview

This is a very simple command-line tool built for Unix-like (POSIX) systems.
Potentially runs on Windows, but is only tested on GNU/Linux.
Requires Python3 and [pymarc](https://pypi.org/project/pymarc/).

Install pymarc with

    pip install pymarc


A batch script for GNU bash is also included.

## Usage

    python marc2csv.py path/to/data.mrc

Where path/to/data.mrc is the marc file you'd like to convert.  CSV is printed
to stdout.  To create a CSV file, simply:

    python marc2csv.py path/to/data.mrc > data.csv

If you have multiple MARC files to convert, you can either use the included
marc2csv_batch bash script, or concatenate all of your MARC files into one,
i.e.

    cat data1.mrc data2.mrc data3.mrc > data.mrc
    python marc2csv.py data.mrc > data.csv

## Output CSV

The output CSV is a spreadsheet which has a column for each MARC tag found in
the input data.  If a marc record does not have the tag, the corresponding cell
is empty.  If you want one CSV for multiple marc files, the easiest approach is
to concatenate all marc files into one before generating the CSV.  (Otherwise
the columns will not likely line up in the output CSV files.)  You can open
this CSV with OpenOffice or Microsoft Excel.

For more on MARC, see http://www.oclc.org/bibformats/en/default.shtm
