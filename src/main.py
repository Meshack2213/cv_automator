import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QMessageBox
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

class CVGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CV Generator')
        self.setGeometry(100, 100, 400, 600)

        layout = QVBoxLayout()

        # Create input fields
        self.inputs = {}
        for label in ["Name:", "Email:", "Phone:", "Summary:", "Experience:", "Education:"]:
            hbox = QHBoxLayout()
            hbox.addWidget(QLabel(label))
            if label in ["Summary:", "Experience:", "Education:"]:
                self.inputs[label] = QTextEdit()
            else:
                self.inputs[label] = QLineEdit()
            hbox.addWidget(self.inputs[label])
            layout.addLayout(hbox)

        # Create generate button
        generate_btn = QPushButton('Generate CV')
        generate_btn.clicked.connect(self.generate_cv)
        layout.addWidget(generate_btn)

        self.setLayout(layout)

    def generate_cv(self):
        document = Document()

        # Add name
        name = self.inputs["Name:"].text()
        document.add_heading(name, 0)

        # Add contact info
        contact_info = f"{self.inputs['Email:'].text()} | {self.inputs['Phone:'].text()}"
        contact_paragraph = document.add_paragraph(contact_info)
        contact_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

        # Add summary
        document.add_heading('Professional Summary', level=1)
        document.add_paragraph(self.inputs["Summary:"].toPlainText())

        # Add experience
        document.add_heading('Experience', level=1)
        document.add_paragraph(self.inputs["Experience:"].toPlainText())

        # Add education
        document.add_heading('Education', level=1)
        document.add_paragraph(self.inputs["Education:"].toPlainText())

        # Save the document
        file_path, _ = QFileDialog.getSaveFileName(self, "Save CV", "", "Word Document (*.docx)")
        if file_path:
            document.save(file_path)
            QMessageBox.information(self, "Success", f"CV saved to {file_path}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CVGeneratorApp()
    ex.show()
    sys.exit(app.exec_())