import sys
from PySide6.QtWidgets import QApplication
from src.widget.main_windows.main_widows import MainWindow
from src.libraries.app_config.file_path_manage.file_path_manage import bin_file_path


def main():
    app = QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
