from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QFont

class TimerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.pomodoro_time = 25 * 60  # 25分
        self.break_time = 5 * 60  # 5分
        self.is_pomodoro = True  # 現在ポモドーロかどうか
        self.time_left = self.pomodoro_time
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        
        self.label = QLabel(self.format_time(), self)
        self.label.setFont(QFont("Arial", 36))  # フォントサイズを大きくする
        self.label.setAlignment(Qt.AlignCenter)  # 画面中央に配置
        
        self.start_button = QPushButton("Start", self)
        self.reset_button = QPushButton("Reset", self)
        
        self.start_button.clicked.connect(self.start_timer)
        self.reset_button.clicked.connect(self.reset_timer)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label, alignment=Qt.AlignCenter)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.reset_button)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def start_timer(self):
        if not self.timer.isActive():
            self.timer.start(1000)  # 1秒ごとに更新
    
    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.label.setText(self.format_time())
        else:
            self.switch_timer()
    
    def switch_timer(self):
        if self.is_pomodoro:
            self.time_left = self.break_time
            self.is_pomodoro = False
        else:
            self.time_left = self.pomodoro_time
            self.is_pomodoro = True
        self.label.setText(self.format_time())
    
    def reset_timer(self):
        self.timer.stop()
        self.is_pomodoro = True
        self.time_left = self.pomodoro_time
        self.label.setText(self.format_time())
    
    def format_time(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        return f"{minutes:02}:{seconds:02}"
