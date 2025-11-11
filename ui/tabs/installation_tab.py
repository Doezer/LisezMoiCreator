"""
Installation Tab
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLabel


class InstallationTab(QWidget):
    """Tab for installation instructions"""
    
    def __init__(self):
        super().__init__()
        self._init_ui()
    
    def _init_ui(self):
        """Initialize the user interface"""
        layout = QVBoxLayout(self)
        
        # Label
        layout.addWidget(QLabel("Instructions d'installation:"))
        
        # Text editor
        self.installation_edit = QTextEdit()
        layout.addWidget(self.installation_edit)
    
    def get_data(self):
        """Get the data from the tab"""
        return {
            'installation': self.installation_edit.toPlainText()
        }
    
    def set_data(self, data):
        """Set the data in the tab"""
        self.installation_edit.setPlainText(data.get('installation', ''))
