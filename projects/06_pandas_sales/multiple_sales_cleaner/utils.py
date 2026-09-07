from pathlib import Path

import pandas as pandas


def group_files(
    path_folder: Path,
) -> list[Path]:
    csv_files = []

    for file in path_folder.iterdir():
        if file.is_file() and file.suffix.lower() == '.csv':
            csv_files.append(file)

    return csv_files


def concatenate_files(
    csv_files: list[Path],
) -> pandas.DataFrame:
    if not csv_files:
        raise ValueError('No csv files found')

    dataframes = []

    for file in csv_files:
        dataframe = pandas.read_csv(file)
        dataframe['SourceFile'] = file.name
        dataframes.append(dataframe)

    combined_dataframes = pandas.concat(dataframes, ignore_index=True)
    combined_dataframes = combined_dataframes.sort_values('OrderID', ignore_index=True)

    return combined_dataframes