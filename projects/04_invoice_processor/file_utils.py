from pathlib import Path


def create_folders(
    destinations: dict[str, Path],
) -> None:
    for destination in destinations.values():
        destination.mkdir(parents=True, exist_ok=True)


def move_files(
    data_folder: Path,
    destinations: dict[str, Path],
    other_files_destination: Path,
) -> None:
    if not data_folder.exists():
        print(f'Source folder "{data_folder}" was not found')
        return

    moved = 0

    for file in data_folder.iterdir():
        if file.is_file():
            target = other_files_destination / file.name

            for prefix, destination in destinations.items():
                if file.name.startswith(prefix):
                    target = destination / file.name
                    break

            file.rename(target)

            moved += 1

            print(f'Moved: {file.name} -> {target.parent.name}')

    print(f'{moved} files processed.')