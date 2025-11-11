"""
Description Tab
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLabel


class DescriptionTab(QWidget):
    """Tab for description section"""
    
    def __init__(self):
        super().__init__()
        self._init_ui()
    
    def _init_ui(self):
        """Initialize the user interface"""
        layout = QVBoxLayout(self)
        
        # Label
        layout.addWidget(QLabel("Description détaillée:"))
        
        # Text editor
        self.description_edit = QTextEdit()
        layout.addWidget(self.description_edit)
    
    def get_data(self):
        """Get the data from the tab"""
        return {
            'description': self.description_edit.toPlainText()
        }
    
    def set_data(self, data):
        """Set the data in the tab"""
        self.description_edit.setPlainText(data.get('description', ''))
