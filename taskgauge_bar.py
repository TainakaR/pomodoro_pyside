from PySide6.QtWidgets import QWidget, QVBoxLayout, QProgressBar, QLabel
from PySide6.QtCore import Qt

class TaskGaugeBar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.layout = QVBoxLayout()
        
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)

        self.progress_bar.setTextVisible(False)

        self.percentage_label = QLabel("0%", self)
        self.percentage_label.setAlignment(Qt.AlignRight)

        self.progress_bar.setStyleSheet("""
            QProgressBar {
                height: 20px;
                border-radius: 10px;
                background-color: #e0e0e0;
            }
            QProgressBar::chunk {
                background-color: #4caf50;
                border-radius: 10px;
            }
        """)
        
        self.layout.addWidget(self.progress_bar)
        self.layout.addWidget(self.percentage_label)
        self.setLayout(self.layout)
    
    def update_progress(self, todo_list_widget):
        total_tasks = todo_list_widget.count()
        if total_tasks == 0:
            self.percentage_label.setText("0%")
            self.progress_bar.setValue(0)
            return
        
        completed_tasks = 0
        for i in range(total_tasks):
            item = todo_list_widget.item(i)
            checkbox = todo_list_widget.itemWidget(item)
            if checkbox and checkbox.isChecked():
                completed_tasks += 1
        
        progress = int((completed_tasks / total_tasks) * 100)
        self.progress_bar.setValue(progress)
        self.percentage_label.setText(f"{progress}%")