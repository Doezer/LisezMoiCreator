#!/usr/bin/env python3
"""
LisezMoiCreator - README File Generator
Main application entry point
"""

import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow


def main():
    """Main application entry point"""
    app = QApplication(sys.argv)
    app.setApplicationName("LisezMoiCreator")
    app.setOrganizationName("Confrérie des Traducteurs")
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
