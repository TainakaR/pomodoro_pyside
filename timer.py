from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
from PySide6.QtCore import QTimer

class TimerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.time_left = 25 * 60  # 25分を秒で
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        
        self.label = QLabel(self.format_time(), self)
        self.start_button = QPushButton("Start", self)
        self.reset_button = QPushButton("Reset", self)
        
        self.start_button.clicked.connect(self.start_timer)
        self.reset_button.clicked.connect(self.reset_timer)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.reset_button)
        
        self.setLayout(layout)
    
    def start_timer(self):
        if not self.timer.isActive():
            self.timer.start(1000)  # 1秒ごとに更新
    
    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.label.setText(self.format_time())
        else:
            self.timer.stop()
    
    def reset_timer(self):
        self.timer.stop()
        self.time_left = 25 * 60
        self.label.setText(self.format_time())
    
    def format_time(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        return f"{minutes:02}:{seconds:02}"