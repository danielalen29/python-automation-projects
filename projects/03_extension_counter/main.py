from pathlib import Path


def main():
    source_folder = Path('projects/02_safe_file_mover/data')

    counts = {}

    for folder in source_folder.iterdir():
        for file in folder.iterdir():
            if file.is_file():
                ext = file.suffix

                if ext in counts:
                    counts[ext] += 1
                else:
                    counts[ext] = 1

    for ext in sorted(counts):
        print(f"{ext}: {counts[ext]}")

if __name__ == '__main__':
    main()