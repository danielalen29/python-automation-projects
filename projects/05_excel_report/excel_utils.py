from pathlib import Path

from openpyxl.styles import Font
from openpyxl.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet


def create_headers(
    column_headers: dict[str, str],
    font: Font,
    worksheet: Worksheet,
) -> None:
    for column, header in column_headers.items():
        cell = f'{column}1'

        worksheet[cell] = header
        worksheet[cell].font = font

    worksheet.freeze_panes = 'A2'


def create_rows(
    rows: list[list[str | int]],
    columns_currency: tuple[str],
    currency_format: str,
    worksheet: Worksheet,
) -> None:
    for row_number, product in enumerate(rows, start=2):
        worksheet.append(product)
        worksheet[f'D{row_number}'] = f'=B{row_number}*C{row_number}'

        for column in columns_currency:
            worksheet[f'{column}{row_number}'].number_format = currency_format


def set_column_widths(
    column_widths: dict[str, int],
    worksheet: Worksheet,
) -> None:
    for column, width in column_widths.items():
        worksheet.column_dimensions[column].width = width


def set_auto_filter(
    rows: list[list[str | int]],
    headers: dict[str, str],
    worksheet: Worksheet,
) -> None:
    last_row = len(rows) + 1
    last_column = list(headers)[-1]

    worksheet.auto_filter.ref = f'A1:{last_column}{last_row}'


def save_workbook(
    file_path_save: Path,
    workbook: Workbook,
) -> None:
    workbook.save(file_path_save)

    print('Sheet successfully saved.')