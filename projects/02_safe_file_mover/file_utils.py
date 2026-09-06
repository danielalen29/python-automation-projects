from pathlib import Path


def create_folders(
    destination_folders: list[Path],
) -> None:
    for folder in destination_folders:
        folder.mkdir(parents=True, exist_ok=True)


def get_destination_folder(
    file: Path,
    mapping: dict[str, Path],
) -> Path | None:
    extension = file.suffix.lower()

    return mapping.get(extension)


def move_file(
    file: Path,
    destination_folder: Path,
) -> None:
    target = destination_folder / file.name
    file.rename(target)

    print(f'Moved: {file.name}')