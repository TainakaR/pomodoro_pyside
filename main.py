from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from timer import TimerWidget
from todo import TodoWidget
import sys

class PomodoroApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pomodoro Timer")
        self.setGeometry(100, 100, 400, 300)

        # メインウィジェット
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # レイアウト
        layout = QVBoxLayout()
        self.timer_widget = TimerWidget()
        self.todo_widget = TodoWidget()
        
        layout.addWidget(self.timer_widget)
        layout.addWidget(self.todo_widget)
        
        central_widget.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PomodoroApp()
    window.show()
    sys.exit(app.exec())