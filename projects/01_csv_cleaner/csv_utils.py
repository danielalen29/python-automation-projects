from pathlib import Path

import csv


def load_csv(
    csv_to_clean: Path,
) -> list[dict[str, str]]:
    with open(
        csv_to_clean,
        newline='',
        encoding='utf-8',
    ) as infile:
        rows = list(csv.DictReader(infile))

    return rows


def clean_rows(
    rows: list[dict[str, str]],
    required_fields: list[str],
) -> list[dict[str, str]]:
    cleaners = {
        'name': lambda value: value.strip().title(),
        'email': lambda value: value.strip().lower(),
        'country': lambda value: value.strip().title()
    }

    cleaned_rows = []

    for row in rows:
        if all(row.get(field, '').strip() for field in required_fields):
            cleaned_row = {}

            for field in required_fields:
                cleaner = cleaners.get(field, lambda value: value.strip())
                cleaned_row[field] = cleaner(row[field])

            cleaned_rows.append(cleaned_row)

    return cleaned_rows


def save_cleaned_csv(
    csv_cleaned: Path,
    required_fields: list[str],
    cleaned_rows: list[dict],
    rows: list[dict[str, str]],
) -> None:
    with open(
        csv_cleaned,
        'w',
        newline='',
        encoding='utf-8',
    ) as outfile:
        writer = csv.DictWriter(outfile, fieldnames=required_fields)
        writer.writeheader()
        writer.writerows(cleaned_rows)

    print(
        f'{len(cleaned_rows)} rows cleaned.\n'
        f'{len(rows) - len(cleaned_rows)} rows skipped.'
    )