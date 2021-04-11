import csv
import pandas as pd


def read_lines_from_list(file, l):

    with open(file) as input_file:
        reader = csv.reader(input_file)

        desired_rows = [row for row_number, row in enumerate(reader)
                        if row_number in l]

    df = pd.DataFrame(desired_rows)

    return df
