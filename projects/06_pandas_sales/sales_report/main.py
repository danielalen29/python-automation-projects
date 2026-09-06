from pathlib import Path

import excel_utils


def main():
    main_folder_path = Path('projects/06_pandas_sales/sales_report')

    csv_to_clean = main_folder_path / 'pandas_sales_practice.csv'
    report_path = main_folder_path / 'sales_report.xlsx'
    csv_files_folder = main_folder_path / 'sales_report_csv'

    excel_utils.clean_csv_save_worksheets(
        csv_to_clean=csv_to_clean,
        report_path=report_path,
        csv_files_folder=csv_files_folder,
    )

    excel_utils.format_workbook(report_path)

if __name__ == '__main__':
    main()