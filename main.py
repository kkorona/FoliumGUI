# ==========================================
#   Main Application Script: main.py
# ==========================================
# Description: 
#   This is the main entry point for the application.
#   It performs [brief description of what the app does].
#
# Author: [Your Name]
# Created on: [Date]
# ==========================================

## @file main.py
#  @brief Main script for the application.
#  @details This script serves as the entry point for the application. 
#           It initializes and runs the main application logic.
#  @author [Your Name]
#  @date [Date]

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWebEngineWidgets
from pathlib import Path
import folium
import os
import sys
import tempfile

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FoliumGUI")

    def set_html_path(self, html_str):
        view = QtWebEngineWidgets.QWebEngineView()
        html = Path(html_str).read_text(encoding='utf-8')
        view.setHtml(html)
        self.setCentralWidget(view)

def main():
    """
    @brief Main function that serves as the entry point to the application.
    @details This function is executed when the script is run directly. It contains the core logic of the application.
    """
    app = QApplication(sys.argv)
    window = MainWindow()
    with tempfile.NamedTemporaryFile(suffix ='.html', mode='w+t') as folium_map_file:
        folium_map_file_path = folium_map_file.name

        m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)
        m.save(folium_map_file_path)
        window.set_html_path(folium_map_file_path)
        window.show()
        app.exec()


if __name__ == "__main__":
    ## @brief Execute the main function.
    #  @details This conditional checks if the script is being run directly 
    #           and not imported as a module. If true, it calls the main function.
    main()

# ==========================================
#               End of Script
# ==========================================