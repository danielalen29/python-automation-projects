from pathlib import Path
import file_utils


def main():
    parent_folder = Path('projects/04_invoice_processor')
    data_folder = parent_folder / 'data'
    processed_folder = parent_folder / 'processed'

    other_files_destination = processed_folder / 'Other'
    other_files_destination.mkdir(parents=True, exist_ok=True)

    destinations = {
        'invoice_': processed_folder / 'Invoices',
        'receipt_': processed_folder / 'Receipts'
    }

    file_utils.create_folders(
        destinations=destinations,
    )
    file_utils.move_files(
        data_folder=data_folder,
        destinations=destinations,
        other_files_destination=other_files_destination,
    )

if __name__ == '__main__':
    main()