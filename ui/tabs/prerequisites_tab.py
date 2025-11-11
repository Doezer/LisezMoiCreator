"""
Prerequisites Tab
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLabel


class PrerequisitesTab(QWidget):
    """Tab for prerequisites section"""
    
    def __init__(self):
        super().__init__()
        self._init_ui()
    
    def _init_ui(self):
        """Initialize the user interface"""
        layout = QVBoxLayout(self)
        
        # Label
        layout.addWidget(QLabel("Prérequis nécessaires:"))
        
        # Text editor
        self.prerequisites_edit = QTextEdit()
        layout.addWidget(self.prerequisites_edit)
    
    def get_data(self):
        """Get the data from the tab"""
        return {
            'prerequisites': self.prerequisites_edit.toPlainText()
        }
    
    def set_data(self, data):
        """Set the data in the tab"""
        self.prerequisites_edit.setPlainText(data.get('prerequisites', ''))
