"""
Credits Tab
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLabel


class CreditsTab(QWidget):
    """Tab for credits section"""
    
    def __init__(self):
        super().__init__()
        self._init_ui()
    
    def _init_ui(self):
        """Initialize the user interface"""
        layout = QVBoxLayout(self)
        
        # Label
        layout.addWidget(QLabel("Crédits et remerciements:"))
        
        # Text editor
        self.credits_edit = QTextEdit()
        layout.addWidget(self.credits_edit)
    
    def get_data(self):
        """Get the data from the tab"""
        return {
            'credits': self.credits_edit.toPlainText()
        }
    
    def set_data(self, data):
        """Set the data in the tab"""
        self.credits_edit.setPlainText(data.get('credits', ''))
