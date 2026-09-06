from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font

import excel_utils


def main():
    workbook = Workbook()
    worksheet = workbook.active

    file_path_save = Path('projects/05_excel_report/products.xlsx')

    column_headers = {
        'A': 'Product',
        'B': 'Quantity',
        'C': 'Price',
        'D': 'Total',
    }

    column_widths = {
        'A': 18,
        'B': 11,
        'C': 12,
        'D': 12,
    }

    products = [
        ['Mouse', 2, 15],
        ['Keyboard', 1, 40]
    ]

    font = Font(bold=True)

    columns_currency = ('C', 'D')
    currency_format = '$0.00'

    excel_utils.create_headers(
        column_headers,
        font,
        worksheet,
    )
    excel_utils.create_rows(
        products,
        columns_currency,
        currency_format,
        worksheet,
    )
    excel_utils.set_column_widths(
        column_widths,
        worksheet,
    )
    excel_utils.set_auto_filter(
        products,
        column_headers,
        worksheet,
    )
    excel_utils.save_workbook(
        file_path_save,
        workbook,
    )

if __name__ == '__main__':
    main()