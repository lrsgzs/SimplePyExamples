from PySide6.QtWidgets import *
import pygame
import sys
import win32gui

pygame.init()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

        self.setWindowTitle("PySide6")
        self.resize(300, 200)

    def setup_ui(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.label = QLabel(self.central_widget)
        self.label.setText("Hello, PySide6!")
        self.label.move(10, 10)


display = pygame.display.set_mode((640, 480) , pygame.RESIZABLE)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

win32gui.SetParent(window.winId(), pygame.display.get_wm_info()["window"])
window.move(20, 20)

pygame.display.set_caption("PyGame")
font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    app.processEvents()

    display.fill((255, 0, 255))
    text = font.render(f"Size: {display.get_size()}", True, (255, 255, 255))
    display.blit(text, (10, 10))

    pygame.display.update()
    window.update()
pygame.quit()
