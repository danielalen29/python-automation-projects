from pathlib import Path

import excel_utils


def main():
    parent_folder = Path('projects/06_pandas_sales/business_data_cleaner')

    csv_to_clean_convert = parent_folder / 'messy_sales.csv'
    report_path = parent_folder / 'sales_report.xlsx'

    dataframe = excel_utils.load_file(
        csv_to_clean_convert=csv_to_clean_convert,
    )
    duplicate_rows = excel_utils.remove_save_duplicates(
        dataframe=dataframe,
    )

    excel_utils.clean_columns(
        dataframe=dataframe,
    )
    excel_utils.create_save_sheets(
        dataframe=dataframe,
        report_path=report_path,
        duplicate_rows=duplicate_rows,
    )
    excel_utils.format_workbook(
        report_path=report_path,
    )

if __name__ == '__main__':
    main()