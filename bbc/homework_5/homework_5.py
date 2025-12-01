from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTextEdit, QWidget, QScrollArea
)
from PySide6.QtCore import Qt

class SEOAnalyzer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI дз")
        self.setGeometry(100, 100, 500, 400)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText("пиши, я лобанов лялялял...")
        main_layout.addWidget(self.text_input)
        
        analyze_button = QPushButton("анализ")
        analyze_button.clicked.connect(self.analyze_text)
        main_layout.addWidget(analyze_button)
        
        result_layout = QHBoxLayout()
        result_label = QLabel("результат:")
        self.result_output = QTextEdit()
        self.result_output.setReadOnly(True)
        result_layout.addWidget(result_label)
        result_layout.addWidget(self.result_output)
        main_layout.addLayout(result_layout)

    def analyze_text(self):
        text = self.text_input.toPlainText()
        if not text.strip():
            self.result_output.setPlainText("текст не введен")
            return
        
        word_count = len(text.split())
        char_count = len(text)
        sentence_count = text.count('.') + text.count('!') + text.count('?')
        
        result = f"SEO Анализ текста:\n\n"
        result += f"слов: {word_count}\n"
        result += f"символов: {char_count}\n"
        result += f"предложений: {sentence_count}\n"
        
        if 'лобанов' in text:
            result += 'лялялялял'
        self.result_output.setPlainText(result)

app = QApplication([])
window = SEOAnalyzer()
window.show()
app.exec()
