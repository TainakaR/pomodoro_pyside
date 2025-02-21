from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
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
        self.todo_label = QLabel("Todo List")
        self.todo_label.setStyleSheet("font-size: 18px; font-weight: bold; margin-top: 0px;")
        self.timer_label = QLabel("Pomodoro Timer")
        self.timer_label.setStyleSheet("font-size: 18px; font-weight: bold; margin-top: 0px;")
        self.progress_label = QLabel("Progress")
        self.progress_label.setStyleSheet("font-size: 18px; font-weight: bold; margin-top: 0px;")
        
        self.layout.addWidget(self.timer_label)
        self.layout.addWidget(self.timer_widget)
        self.layout.addWidget(self.todo_label)
        self.layout.addWidget(self.todo_widget)
        self.layout.addWidget(self.progress_label)
        self.layout.addWidget(self.task_gauge_bar)
        
        self.resize(450, 600)
        
        screen = self.screen().availableGeometry()
        window_rect = self.frameGeometry()
        self.move(screen.center() - window_rect.center())

        self.setLayout(self.layout)
        self.setWindowTitle("Pomodoro Todo App")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
