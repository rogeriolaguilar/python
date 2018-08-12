"""
Project for Week 3 of "Python Data Analysis".
Read and write CSV files using a dictionary of dictionaries.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import os

BASE_DIR=os.getcwd()+'/projects/csv_files/'

def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Ouput:
      A list of strings corresponding to the field names in
      the given CSV file.
    """
    with open(filename,'rt', newline='') as csvfile:
        csv.register_dialect('new', delimiter=separator, quotechar=quote)
        reader = csv.DictReader(csvfile, dialect='new')
        return reader.fieldnames

# print("Testing", "read_csv_fieldnames")
# print('table1.csv', read_csv_fieldnames(BASE_DIR+'table1.csv', ',', None))
# print('table2.csv', read_csv_fieldnames(BASE_DIR+'table2.csv', ',', '"'))

def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    dict_list = []
    with open(filename,'rt', newline='') as csvfile:
        csv.register_dialect('new', delimiter=separator, quotechar=quote)
        reader = csv.DictReader(csvfile, dialect='new')
        for row in reader:
            dict_list.append(row)

    return dict_list

#print(read_csv_as_list_dict(BASE_DIR+'table1.csv', ',', None))

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    table = {}
    with open(filename) as csvfile:
        csv.register_dialect('new', delimiter=separator, quotechar=quote)
        reader = csv.DictReader(csvfile, dialect='new')
        for row in reader:
            table[row[keyfield]] = row
 
    return table


def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """
    csv.register_dialect('new', delimiter=separator, quotechar=quote, quoting=csv.QUOTE_NONNUMERIC)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='new')
        writer.writeheader()

        for row in table:
            writer.writerow(row)
    return