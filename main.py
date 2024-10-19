from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton , QMessageBox , QInputDialog , QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from webm import *

app = QApplication([])
window = QMainWindow()
#2c2c2c
#FFD700
app.setStyleSheet("""
    QMainWindow {
        background-color:#003366 ;  /* Couleur de fond de la fenêtre principale */
    }
    QWidget {
        background-color: #2c2c2c;  /* Couleur de fond du widget central */
        color: #ffffff;  /* Couleur du texte */
    }
    QPushButton {
        background-color: #4d4d4d;  /* Couleur de fond du bouton */
        color: #FFD700;  /* Couleur du texte du bouton */
        border: none;  /* Pas de bordure */
        padding: 10px;  /* Espacement intérieur */
        border-radius: 5px;  /* Coins arrondis */
    }
    QPushButton:hover {
        background-color: #5e5e5e;  /* Couleur de fond du bouton au survol */
    }
    QLabel {
        color: #ffffff;  /* Couleur du texte du label */
    }
""")








def on_button1_click():

    text, ok = QInputDialog.getText(window, "Your audio:", "Paste an URL (stored at C:\\audios\\) ")
    
    if ok and text:  # Si l'utilisateur a validé avec OK et entré quelque chose
        #label.setText(f"URL is: {text}")
        my_yt_url = str(text)
    else:
        label.setText("")
        return 
    

    download_youtube_audio(my_yt_url)




window.setMinimumSize(400, 500)
window.setWindowTitle("Yt2Webm")
window.setWindowIcon(QIcon("icone.jpg"))

# -- Creating central widget and layout --
central_widget = QWidget()
layout = QVBoxLayout()

# -- Adding widgets --
font = window.font()
font.setPointSize(17)
font.setBold(True)


button = QPushButton("Try it now!")
button.setFixedSize(400, 200)
button.setFont(font)
layout.addWidget(button)



button.clicked.connect(on_button1_click)  # Quand button1 est cliqué

global label
label = QLabel("Info: Your audios are stored in the following directory:  C:\\audios\\  ")
label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Centrer le texte dans le label
layout.addWidget(label)


central_widget.setLayout(layout)


window.setCentralWidget(central_widget)

window.closeEvent = lambda event: app.quit()

window.show()
app.exec()
