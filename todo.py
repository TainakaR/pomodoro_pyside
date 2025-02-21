from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QCheckBox

class TodoWidget(QWidget):
    def __init__(self, task_gauge_bar):
        super().__init__()
        self.task_gauge_bar = task_gauge_bar  # タスクゲージバーを受け取る
        self.initUI()
    
    def initUI(self):
        self.layout = QVBoxLayout()
        
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("タスクをここに記述")
        self.add_button = QPushButton("Add Task", self)
        self.reset_button = QPushButton("Reset Tasks", self)
        self.list_widget = QListWidget(self)
        
        self.add_button.clicked.connect(self.add_task)
        self.reset_button.clicked.connect(self.reset_tasks)
        
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.reset_button)
        self.layout.addWidget(self.list_widget)
        
        self.setLayout(self.layout)
    
    def add_task(self):
        task_text = self.input_field.text().strip()
        if task_text:
            item = QListWidgetItem(self.list_widget)
            checkbox = QCheckBox(task_text)
            self.list_widget.setItemWidget(item, checkbox)
            checkbox.stateChanged.connect(lambda: self.task_gauge_bar.update_progress(self.list_widget))  # プログレスバー更新
            self.input_field.clear()
            self.task_gauge_bar.update_progress(self.list_widget)  # 進捗更新を即時反映
    
    def reset_tasks(self):
        self.list_widget.clear()
        self.task_gauge_bar.update_progress(self.list_widget)  # 進捗をリセット
