from pathlib import Path

import utils

def main():
    parent_folder = Path(
        'projects/06_pandas_sales/multiple_sales_cleaner'
    )

    input_folder = parent_folder / 'sales_data'

    csv_files = utils.group_files(path_folder=input_folder)

    combined_dataframe = utils.concatenate_files(csv_files=csv_files)

    output_file = parent_folder / 'combined_sales.csv'

    combined_dataframe.to_csv(output_file, index=False)

if __name__ == '__main__':
    main()