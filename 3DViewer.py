import sys
from PyQt5.QtCore import QUrl, QDir # Ajoutez QDir ici
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QTreeView, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView


class ModelViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Créer un modèle de système de fichiers pour afficher les fichiers dans l'arbre
        model = QFileSystemModel()
        model.setRootPath('')
        model.setFilter(QDir.AllDirs | QDir.Files | QDir.NoDotAndDotDot)

        # Créer l'arbre
        treeView = QTreeView(self)
        treeView.setModel(model)
        treeView.setRootIndex(model.index('')) # Spécifier le chemin du dossier racine

        # Créer la vue 3D
        webView = QWebEngineView(self)
        webView.load(QUrl.fromLocalFile('viewer.html')) # Spécifier le chemin vers votre fichier HTML

        # Mettre en page les éléments
        layout = QVBoxLayout()
        layout.addWidget(treeView)
        layout.addWidget(webView)

        centralWidget = QWidget(self)
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        # Configurer la fenêtre principale
        self.setWindowTitle('Visionneuse de Modèles 3D')
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon('icon.png')) # Remplacez 'icon.png' par le chemin de votre icône
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = ModelViewer()
    sys.exit(app.exec_())
