import pandas as pd
from openpyxl import load_workbook
from Sources.utilities import globals


def get_sheet(sheet):
    data = pd.read_excel(globals.EXCEL, sheet_name=sheet, index_col=globals.INDEX_COL)
    return data


# here we are specifying pandas as index_col because it will be considered as ndex col else, pandas will create new
# index col by itself, so we ar specifying it

# INDEX_COL var value is mentioned in globals.py


def get_cell_value(sheet, row_name, column_name):
    sheet = get_sheet(sheet)
    value = sheet.loc[row_name][column_name]
    return str(value)


def write_to_excel(sheet, row_name, col_name, value_to_write):
    data = get_sheet(sheet)
    data.loc[row_name, col_name] = value_to_write
    writer = pd.ExcelWriter(globals.EXCEL)
    workbook = load_workbook(globals.EXCEL)
    writer.book = workbook
    writer.sheets = dict((ws.title, ws) for ws in workbook.worksheets)
    data.to_excel(writer, sheet_name=sheet, index=False)
    writer.save()
