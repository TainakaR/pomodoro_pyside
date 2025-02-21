from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from timer import TimerWidget
from todo import TodoWidget
from taskgauge_bar import TaskGaugeBar
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.layout = QVBoxLayout()
        
        self.timer_widget = TimerWidget()
        self.task_gauge_bar = TaskGaugeBar()  # 先に TaskGaugeBar を作成
        self.todo_widget = TodoWidget(self.task_gauge_bar)  # TaskGaugeBar を Todo に渡す
        
        self.layout.addWidget(self.timer_widget)
        self.layout.addWidget(self.todo_widget)
        self.layout.addWidget(self.task_gauge_bar)
        
        self.setLayout(self.layout)
        self.setWindowTitle("Pomodoro App")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
