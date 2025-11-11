# Developer Documentation

## Project Structure

```
LisezMoiCreator/
├── main.py                 # Application entry point
├── setup.py                # Package configuration
├── requirements.txt        # Python dependencies
├── ui/                     # User interface package
│   ├── __init__.py
│   ├── main_window.py      # Main application window
│   └── tabs/               # Tab widgets
│       ├── __init__.py
│       ├── general_info_tab.py
│       ├── prerequisites_tab.py
│       ├── description_tab.py
│       ├── installation_tab.py
│       ├── uninstallation_tab.py
│       └── credits_tab.py
├── Qt/                     # Legacy Qt/C++ implementation (reference)
└── res/                    # Resources (icons, etc.)
```

## Development Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Doezer/LisezMoiCreator.git
   cd LisezMoiCreator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

### Running from Source

To run the application during development:

```bash
python main.py
```

### Installing as Package

To install the application as a package:

```bash
pip install -e .
```

Then run with:

```bash
lisezmoi-creator
```

## Technology Stack

- **Language**: Python 3.8+
- **GUI Framework**: PyQt6
- **Package Management**: setuptools

## Architecture

The application follows a modular architecture:

1. **main.py**: Entry point that initializes the Qt application
2. **ui/main_window.py**: Main window with menu bar, toolbar, and tab widget
3. **ui/tabs/**: Individual tab modules, each responsible for one section of the README

Each tab implements:
- `get_data()`: Returns the current data in the tab
- `set_data(data)`: Sets data in the tab from a dictionary

This allows for easy serialization and deserialization of README projects.

## Future Enhancements

Potential improvements:
- [ ] File save/load functionality (JSON or XML format)
- [ ] README export in multiple formats (Markdown, plain text, HTML)
- [ ] Template system for different README styles
- [ ] Preview pane showing the generated README
- [ ] Internationalization (i18n) support
- [ ] Theme support (dark mode, etc.)
- [ ] Auto-save functionality
- [ ] Recent files menu
