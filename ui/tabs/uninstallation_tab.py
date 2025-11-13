"""
Uninstallation Tab
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLabel


class UninstallationTab(QWidget):
    """Tab for uninstallation instructions"""
    
    def __init__(self):
        super().__init__()
        self._init_ui()
    
    def _init_ui(self):
        """Initialize the user interface"""
        layout = QVBoxLayout(self)
        
        # Label
        layout.addWidget(QLabel("Instructions de désinstallation:"))
        
        # Text editor
        self.uninstallation_edit = QTextEdit()
        layout.addWidget(self.uninstallation_edit)
    
    def get_data(self):
        """Get the data from the tab"""
        return {
            'uninstallation': self.uninstallation_edit.toPlainText()
        }
    
    def set_data(self, data):
        """Set the data in the tab"""
        self.uninstallation_edit.setPlainText(data.get('uninstallation', ''))
