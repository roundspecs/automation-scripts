# Automation Scripts
## Overview

This repository contains a collection of automation scripts designed to streamline and simplify various tasks. These scripts are written in Python and can be used to automate repetitive processes, manage system configurations, and perform other useful functions.

## Prerequisites

- Python 3.13 or higher
- Required Python packages (listed in `requirements.txt`)

## Installation (For Linux/MacOS)

1. Clone the repository:
2. Navigate to the project directory:
  ```sh
  cd automation-scripts
  ```
3. Install pipx
  ```
  brew install pipx
  ```
4. Install the package using pipx
  ```
  pipx install --editable .
  ```

## Usage

### Flutter

#### `fl-create-page`

This script creates a new page in the current directory. The page is created with the specified name and includes a basic template with the page name and a timestamp.

```sh
fl-create-page PageName
fl-create-page PageName --dir /path/to/directory
```

```
/path/to/directory
└── page_name_page.dart
└── page_name_view.dart
```