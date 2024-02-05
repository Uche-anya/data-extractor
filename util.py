import pandas as pd

# We're basically trying to get the table we want to be loaded from the source database and it's customers....
def get_tables(path):
    tables = pd.read_csv(path, sep=',')
    table = tables.query("to_be_loaded == 'yes'")
    # We return the table we want
    return table



