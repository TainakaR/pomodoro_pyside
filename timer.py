from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import QTimer, Qt, QUrl
from PySide6.QtGui import QFont
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

class TimerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pomodoro_time = 1 * 60  # 25分
        self.break_time = 0.5 * 60  # 5分
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

        # QMediaPlayerを使って音を設定
        self.player_1 = QMediaPlayer(self)
        self.player_2 = QMediaPlayer(self)

        # QAudioOutputを使用して音量を制御
        audio_output_1 = QAudioOutput(self)
        audio_output_2 = QAudioOutput(self)
        
        self.player_1.setAudioOutput(audio_output_1)
        self.player_2.setAudioOutput(audio_output_2)

        # 音量設定（0 は最小、100 は最大）
        audio_output_1.setVolume(1.0)  # 音声①の音量を最大に設定
        audio_output_2.setVolume(1.0)  # 音声②の音量を最大に設定

        # 音声①
        self.sound_1 = QUrl.fromLocalFile("sounds/sound_1.wav")  # 音声①
        self.player_1.setSource(self.sound_1)  # 音声ファイルのソースを設定

        # 音声②
        self.sound_2 = QUrl.fromLocalFile("sounds/sound_2.wav")  # 音声②
        self.player_2.setSource(self.sound_2)  # 音声ファイルのソースを設定

        # メディアステータスの監視
        self.player_1.mediaStatusChanged.connect(self.media_status_changed)
        self.player_2.mediaStatusChanged.connect(self.media_status_changed)

    def media_status_changed(self, status):
        if status == QMediaPlayer.MediaStatus.LoadedMedia:
            print("Media loaded successfully")
        elif status == QMediaPlayer.MediaStatus.NoMedia:
            print("No media loaded")

    def start_timer(self):
        if not self.timer.isActive():
            self.timer.start(1000)  # 1秒ごとに更新
    
    def update_timer(self):
        if self.time_left > 0:
            # 2秒前に音声①を鳴らす（少し早めに音を鳴らす）
            if self.time_left == 3:
                self.player_1.play()  # 音声①を再生
            # 1秒前に音声①を鳴らす（少し早めに音を鳴らす）
            elif self.time_left == 2:
                self.player_1.play()  # 音声①を再生
            
            self.time_left -= 1
            self.label.setText(self.format_time())
        else:
            self.switch_timer()
    
    def switch_timer(self):
        # タイマーが切り替わる瞬間に音声②を鳴らす
        self.player_2.play()  # 音声②を再生
        
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

