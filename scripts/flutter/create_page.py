import os
import sys
import argparse
from pathlib import Path


def to_snake_case(name: str):
    """
    AbcDefGhi -> abc_def_ghi
    abc_def_ghi -> abc_def_ghi
    """
    return "".join(f"_{c.lower()}" if c.isupper() else c for c in name).lstrip("_")


def create_page(name: str, directory: str = None):
    snake_name = to_snake_case(name)
    page_name = "".join(word.capitalize() for word in snake_name.split("_"))

    # Get the templates directory relative to this script
    template_dir = Path(__file__).parent.parent.parent / "templates" / "flutter"

    # Set target directory
    if directory:
        target_dir = Path(directory) / snake_name
    else:
        target_dir = Path.cwd() / snake_name

    # Create directories
    target_dir.mkdir(parents=True, exist_ok=True)

    # Create page files
    files_to_create = {
        f"{snake_name}_page.dart": "page_template.txt",
        f"{snake_name}_view.dart": "page_view_template.txt",
    }

    for file_name, template_name in files_to_create.items():
        with open(template_dir / template_name, "r") as template_file:
            template_content = template_file.read()

        # Replace placeholders
        content = template_content.replace("{{page_name}}", page_name)
        content = content.replace("{{snake_name}}", snake_name)

        # Write file
        with open(target_dir / file_name, "w") as output_file:
            output_file.write(content)

    print(f"Created {page_name} page files in {target_dir}")


def main():
    parser = argparse.ArgumentParser(description="Create Flutter page files")
    parser.add_argument("name", help="Name of the page (in PascalCase or snake_case)")
    parser.add_argument(
        "--dir", help="Target directory (defaults to current directory)"
    )

    args = parser.parse_args()
    create_page(args.name, args.dir)


if __name__ == "__main__":
    main()
