from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QCheckBox

class TodoWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.layout = QVBoxLayout()
        
        self.input_field = QLineEdit(self)
        self.add_button = QPushButton("Add Task", self)
        self.list_widget = QListWidget(self)
        
        self.add_button.clicked.connect(self.add_task)
        
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.list_widget)
        
        self.setLayout(self.layout)
    
    def add_task(self):
        task_text = self.input_field.text().strip()
        if task_text:
            item = QListWidgetItem(self.list_widget)
            checkbox = QCheckBox(task_text)
            self.list_widget.setItemWidget(item, checkbox)
            self.input_field.clear()