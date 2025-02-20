from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QCheckBox, QHBoxLayout
from PySide6.QtGui import QFont

class TodoWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.layout = QVBoxLayout()
        
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("タスクをここに記述")  # プレースホルダー追加
        
        # ボタン用の横並びレイアウト
        self.button_layout = QHBoxLayout()
        self.add_button = QPushButton("Add Task", self)
        self.reset_button = QPushButton("Reset Tasks", self)  # リセットボタン追加
        
        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.reset_button)
        
        self.list_widget = QListWidget(self)
        
        self.add_button.clicked.connect(self.add_task)
        self.reset_button.clicked.connect(self.reset_tasks)  # リセットボタンの機能追加
        
        self.layout.addWidget(self.input_field)
        self.layout.addLayout(self.button_layout)  # 横並びのボタンレイアウトを追加
        self.layout.addWidget(self.list_widget)
        
        self.setLayout(self.layout)
    
    def add_task(self):
        task_text = self.input_field.text().strip()
        if task_text:
            item = QListWidgetItem(self.list_widget)
            checkbox = QCheckBox(task_text)
            self.list_widget.setItemWidget(item, checkbox)
            self.input_field.clear()
    
    def reset_tasks(self):
        self.list_widget.clear()  # タスクをすべてクリア