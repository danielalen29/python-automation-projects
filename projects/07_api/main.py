from pathlib import Path

import requests

import utils


def main():
    user = 'Daniel'
    folder_path = Path('projects/07_api')
    csv_file_path = folder_path / 'repositories.csv'
    excel_file_path = folder_path / 'repositories.xlsx'

    try:
        repositories = utils.get_repositories(user)
    except requests.exceptions.RequestException as error:
        print(f'Request failed: {error}')
        return

    if not repositories:
        print('No public repositories found.')
        return

    try:
        utils.save_repositories_to_csv(repositories, csv_file_path)
        print('CSV file successfully saved.')
    except OSError as error:
        print(f'Could not save CSV file: {error}')

    try:
        utils.save_repositories_to_excel(repositories, excel_file_path)
        print('Excel file successfully saved.')
    except OSError as error:
        print(f'Could not save Excel file: {error}')

if __name__ == '__main__':
    main()