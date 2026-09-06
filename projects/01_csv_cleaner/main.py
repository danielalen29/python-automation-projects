from pathlib import Path

import csv_utils


def main():
    parent_folder = Path('projects/01_csv_cleaner')
    csv_to_clean = parent_folder / 'contacts.csv'
    csv_cleaned = parent_folder / 'cleaned_contacts.csv'

    required_fields = ['name', 'email', 'country']

    list_rows = csv_utils.load_csv(
        csv_to_clean=csv_to_clean,
    )
    cleaned_rows = csv_utils.clean_rows(
        rows=list_rows,
        required_fields=required_fields,
    )

    csv_utils.save_cleaned_csv(
        csv_cleaned=csv_cleaned,
        required_fields=required_fields,
        cleaned_rows=cleaned_rows,
        rows=list_rows,
        )

if __name__ == '__main__':
    main()