"""
Main Window for LisezMoiCreator
Provides a modern PyQt6 interface for creating README files
"""

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QTabWidget,
    QMenuBar, QMenu, QStatusBar, QToolBar, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon

from .tabs.general_info_tab import GeneralInfoTab
from .tabs.prerequisites_tab import PrerequisitesTab
from .tabs.description_tab import DescriptionTab
from .tabs.installation_tab import InstallationTab
from .tabs.uninstallation_tab import UninstallationTab
from .tabs.credits_tab import CreditsTab


class MainWindow(QMainWindow):
    """Main application window"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LisezMoiCreator")
        self.setGeometry(100, 100, 800, 600)
        
        self._init_ui()
        self._create_menu_bar()
        self._create_toolbar()
        self._create_status_bar()
    
    def _init_ui(self):
        """Initialize the user interface"""
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create main layout
        layout = QVBoxLayout(central_widget)
        
        # Create tab widget
        self.tab_widget = QTabWidget()
        
        # Add tabs
        self.tab_widget.addTab(GeneralInfoTab(), "Infos générales")
        self.tab_widget.addTab(PrerequisitesTab(), "Prérequis")
        self.tab_widget.addTab(DescriptionTab(), "Description")
        self.tab_widget.addTab(InstallationTab(), "Installation")
        self.tab_widget.addTab(UninstallationTab(), "Désinstallation")
        self.tab_widget.addTab(CreditsTab(), "Crédits")
        
        layout.addWidget(self.tab_widget)
    
    def _create_menu_bar(self):
        """Create the menu bar"""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("Fichier")
        
        # New action
        new_action = QAction("Nouveau", self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self._new_file)
        file_menu.addAction(new_action)
        
        # Open action
        open_action = QAction("Ouvrir", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self._open_file)
        file_menu.addAction(open_action)
        
        # Save action
        save_action = QAction("Enregistrer", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self._save_file)
        file_menu.addAction(save_action)
        
        file_menu.addSeparator()
        
        # Exit action
        exit_action = QAction("Quitter", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Help menu
        help_menu = menubar.addMenu("?")
        
        # About action
        about_action = QAction("À propos", self)
        about_action.triggered.connect(self._show_about)
        help_menu.addAction(about_action)
    
    def _create_toolbar(self):
        """Create the toolbar"""
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        
        # Add actions to toolbar
        new_action = QAction("Nouveau", self)
        new_action.triggered.connect(self._new_file)
        toolbar.addAction(new_action)
        
        open_action = QAction("Ouvrir", self)
        open_action.triggered.connect(self._open_file)
        toolbar.addAction(open_action)
        
        save_action = QAction("Enregistrer", self)
        save_action.triggered.connect(self._save_file)
        toolbar.addAction(save_action)
    
    def _create_status_bar(self):
        """Create the status bar"""
        self.statusBar().showMessage("Prêt")
    
    def _new_file(self):
        """Create a new file"""
        # TODO: Implement new file functionality
        self.statusBar().showMessage("Nouveau fichier créé", 3000)
    
    def _open_file(self):
        """Open an existing file"""
        # TODO: Implement open file functionality
        self.statusBar().showMessage("Ouvrir un fichier", 3000)
    
    def _save_file(self):
        """Save the current file"""
        # TODO: Implement save file functionality
        self.statusBar().showMessage("Fichier enregistré", 3000)
    
    def _show_about(self):
        """Show about dialog"""
        QMessageBox.about(
            self,
            "À propos de LisezMoiCreator",
            "LisezMoiCreator\n\n"
            "Générateur de fichier lisez-moi pour la Confrérie des Traducteurs\n\n"
            "Version modernisée en Python avec PyQt6"
        )
