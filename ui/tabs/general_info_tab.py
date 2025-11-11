"""
General Information Tab
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QTextEdit, QLabel


class GeneralInfoTab(QWidget):
    """Tab for general information about the README file"""
    
    def __init__(self):
        super().__init__()
        self._init_ui()
    
    def _init_ui(self):
        """Initialize the user interface"""
        layout = QVBoxLayout(self)
        
        # Create form layout
        form_layout = QFormLayout()
        
        # Title field
        self.title_edit = QLineEdit()
        form_layout.addRow("Titre:", self.title_edit)
        
        # Author field
        self.author_edit = QLineEdit()
        form_layout.addRow("Auteur:", self.author_edit)
        
        # Version field
        self.version_edit = QLineEdit()
        form_layout.addRow("Version:", self.version_edit)
        
        # Date field
        self.date_edit = QLineEdit()
        form_layout.addRow("Date:", self.date_edit)
        
        layout.addLayout(form_layout)
        
        # Description field
        layout.addWidget(QLabel("Résumé:"))
        self.summary_edit = QTextEdit()
        self.summary_edit.setMaximumHeight(150)
        layout.addWidget(self.summary_edit)
        
        layout.addStretch()
    
    def get_data(self):
        """Get the data from the tab"""
        return {
            'title': self.title_edit.text(),
            'author': self.author_edit.text(),
            'version': self.version_edit.text(),
            'date': self.date_edit.text(),
            'summary': self.summary_edit.toPlainText()
        }
    
    def set_data(self, data):
        """Set the data in the tab"""
        self.title_edit.setText(data.get('title', ''))
        self.author_edit.setText(data.get('author', ''))
        self.version_edit.setText(data.get('version', ''))
        self.date_edit.setText(data.get('date', ''))
        self.summary_edit.setPlainText(data.get('summary', ''))
