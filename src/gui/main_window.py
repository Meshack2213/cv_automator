from PyQt5.QtWidgets import (QMainWindow, QWidget, QLabel, QLineEdit, QTextEdit, 
                             QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, 
                             QFileDialog, QMessageBox, QFrame, QScrollArea)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
from models.cv_model import CVModel
from utils.file_manager import save_cv_to_file

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('CV Generator')
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon('path_to_your_icon.png'))  # Add an icon file to your project

        # Create main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        
        # Create scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        # Title
        title_label = QLabel('CV Generator')
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont('Arial', 20, QFont.Bold))
        scroll_layout.addWidget(title_label)

        # Create form layout
        form_layout = QGridLayout()

        # Personal Information Section
        self.add_section_title(scroll_layout, "Personal Information")
        self.name_input = self.add_form_field(form_layout, 0, "Full Name:")
        self.email_input = self.add_form_field(form_layout, 1, "Email:")
        self.phone_input = self.add_form_field(form_layout, 2, "Phone:")
        scroll_layout.addLayout(form_layout)

        # Summary Section
        self.add_section_title(scroll_layout, "Professional Summary")
        self.summary_input = self.add_text_area(scroll_layout)

        # Experience Section
        self.add_section_title(scroll_layout, "Work Experience")
        self.experience_input = self.add_text_area(scroll_layout)

        # Education Section
        self.add_section_title(scroll_layout, "Education")
        self.education_input = self.add_text_area(scroll_layout)

        # Generate Button
        self.generate_btn = QPushButton('Generate CV')
        self.generate_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                border: none;
                color: white;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.generate_btn.clicked.connect(self.generate_cv)
        scroll_layout.addWidget(self.generate_btn)

        # Set scroll content
        scroll.setWidget(scroll_content)
        main_layout.addWidget(scroll)

        # Set main layout
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def add_section_title(self, layout, title):
        label = QLabel(title)
        label.setFont(QFont('Arial', 14, QFont.Bold))
        layout.addWidget(label)
        layout.addWidget(self.create_horizontal_line())

    def create_horizontal_line(self):
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        return line

    def add_form_field(self, layout, row, label):
        layout.addWidget(QLabel(label), row, 0)
        input_field = QLineEdit()
        layout.addWidget(input_field, row, 1)
        return input_field

    def add_text_area(self, layout):
        text_area = QTextEdit()
        text_area.setMinimumHeight(100)
        layout.addWidget(text_area)
        return text_area

    def generate_cv(self):
        cv_data = {
            'name': self.name_input.text(),
            'email': self.email_input.text(),
            'phone': self.phone_input.text(),
            'summary': self.summary_input.toPlainText(),
            'experience': self.experience_input.toPlainText(),
            'education': self.education_input.toPlainText()
        }
        
        cv_model = CVModel(**cv_data)
        
        file_path, _ = QFileDialog.getSaveFileName(self, "Save CV", "", "Word Document (*.docx)")
        if file_path:
            save_cv_to_file(cv_model, file_path)
            QMessageBox.information(self, "Success", f"CV saved to {file_path}")