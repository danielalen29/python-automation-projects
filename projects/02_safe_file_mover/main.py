from pathlib import Path

import file_utils


def main():
    source_folder = Path('projects/02_safe_file_mover/data')

    txt_folder = source_folder / 'TextFiles'
    jpg_folder = source_folder / 'Images'
    pdf_folder = source_folder / 'PDFs'

    destination_folders = [txt_folder, jpg_folder, pdf_folder]

    file_utils.create_folders(
        destination_folders=destination_folders,
    )

    suffix_destination = {
        '.txt': txt_folder,
        '.jpg': jpg_folder,
        '.pdf': pdf_folder,
    }

    for file in source_folder.iterdir():
        if file.is_file():
            destination_folder = file_utils.get_destination_folder(
                file=file,
                mapping=suffix_destination,
            )

            if destination_folder is not None:
                file_utils.move_file(
                    file=file,
                    destination_folder=destination_folder,
                )

if __name__ == '__main__':
    main()