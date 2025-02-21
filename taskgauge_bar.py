from PySide6.QtWidgets import QWidget, QVBoxLayout, QProgressBar

class TaskGaugeBar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.layout = QVBoxLayout()
        
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        
        self.layout.addWidget(self.progress_bar)
        self.setLayout(self.layout)
    
    def update_progress(self, todo_list_widget):
        total_tasks = todo_list_widget.count()
        if total_tasks == 0:
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