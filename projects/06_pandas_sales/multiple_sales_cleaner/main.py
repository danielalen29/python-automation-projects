from pathlib import Path

import utils

def main():
    input_folder = Path(
        'projects/06_pandas_sales/multiple_sales_cleaner/sales_data'
    )

    csv_files = utils.group_files(path_folder=input_folder)

    print(utils.concatenate_files(csv_files=csv_files))

if __name__ == '__main__':
    main()