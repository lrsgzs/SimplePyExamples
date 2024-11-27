from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import _thread
import pygame
import sys

pygame.init()
display = pygame.display.set_mode((640, 480))
pygame.display.set_caption("PyGame")
font = pygame.font.Font(None, 36)
running = True


def pygame_loop():
    """ PyGame loop """
    global running, display
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display.fill((255, 0, 255))
        text = font.render(f"Size: {display.get_size()}", True, (255, 255, 255))
        display.blit(text, (10, 10))
        pygame.display.update()
    pygame.quit()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.container = None
        self.main_layout = None
        self.pg_window = None

        self.setWindowTitle("PySide6")
        self.resize(640, 480)
        self.setup_ui()

    def setup_ui(self):
        hwnd = pygame.display.get_wm_info()["window"]
        self.pg_window = QWindow.fromWinId(hwnd)
        self.pg_window.setFlags(Qt.WindowType.Window)

        self.container = QWidget(self)
        self.setCentralWidget(self.container)

        self.main_layout = QVBoxLayout(self.container)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.mdi_area = QMdiArea()
        self.main_layout.addWidget(self.mdi_area)

        self.mdi_sub_window = QMdiSubWindow()
        self.mdi_sub_window.setWindowTitle("PyGame")
        self.mdi_sub_window.resize(300, 200)
        self.mdi_sub_window.closeEvent = self.closeEvent
        self.mdi_sub_window.setWidget(QWidget.createWindowContainer(self.pg_window))
        self.mdi_area.addSubWindow(self.mdi_sub_window)

    def closeEvent(self, event):
        if running:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    _thread.start_new_thread(pygame_loop, tuple())
    app.exec()

    # 兜底
    if running:
        running = False
        pygame.quit()
