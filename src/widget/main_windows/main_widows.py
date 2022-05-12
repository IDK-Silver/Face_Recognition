from PySide6.QtCore import QDir
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QMainWindow, QWidget, QFileDialog, QMessageBox


from ..main_widget.main_widget import Ui_MainWindow
from ..face_data_widget.face_data_widget import Ui_Face_Data
from ..face_recognition_widget.face_recognition_widget import Ui_Face_Recognition

from ...libraries.face_data.face_data import *

from ...libraries.face_detector.face_detector import *

from ...libraries.app_config.file_path_manage.file_path_manage import bin_file_path
from ...libraries.recognition.recognition import recognition


def cv_img_to_qt_img(cv_img: numpy.ndarray):
    height, width, depth = cv_img.shape
    cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    cv_img = QImage(cv_img.data, width, height, width * depth, QImage.Format_RGB888)
    return cv_img


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__add_other_widget__()

        self.ui.tabWidget.currentChanged.connect(self.clear_tab_var)

        self.bin_path = os.path.join(os.path.dirname(__file__), "bin")

        self.choose_image = str()

    def clear_tab_var(self):
        self.choose_image = str()
        self.face_data_widget.label_display_image.clear()
        self.face_data_widget.lineEdit_image_name.clear()
        self.face_recognition_widget.label_imgStream.clear()
        self.face_recognition_widget.label_name.clear()

    def __add_other_widget__(self):

        # Face Recognition Widget
        self.face_recognition_widget = Ui_Face_Recognition()
        self.__ui_face_recognition_widget = QWidget()
        self.face_recognition_widget.setupUi(self.__ui_face_recognition_widget)
        self.ui.tabWidget.addTab(self.__ui_face_recognition_widget, "辨識頁面")

        self.face_recognition_widget.label_imgStream.setScaledContents(True)

        self.face_recognition_widget.pushButton_choose_det_image.pressed.connect(self.recognition_image)

        # Face Data Widget
        self.face_data_widget = Ui_Face_Data()
        self.__ui_face_data_widget = QWidget()
        self.face_data_widget.setupUi(self.__ui_face_data_widget)
        self.ui.tabWidget.addTab(self.__ui_face_data_widget, "臉部資料")

        self.face_data_widget.pushButton_choose_image.pressed.connect(self.choose_file)
        self.face_data_widget.pushButton_key_in_image.pressed.connect(self.key_in_face_data)

    def choose_file(self):
        path = QFileDialog.getOpenFileName(self, "選取圖片", os.path.join(QDir.homePath(), "Documents"),
                                           "圖片檔 (*.png, *.jpg)")[0]
        if path == "" or path is None:
            pass
        else:
            self.choose_image = path
            self.face_data_widget.label_display_image.setPixmap(QPixmap(path))

    def key_in_face_data(self):

        if self.choose_image is None or len(self.choose_image) == 0:
            QMessageBox.information(self, '通知', '請選擇檔案')
            return

        if not len(self.face_data_widget.lineEdit_image_name.text()):
            QMessageBox.information(self, '通知', '名字不可為空白')
            return

        face_ = FaceInfo(self.face_data_widget.lineEdit_image_name.text(), self.choose_image)
        add_face_data(os.path.join(bin_file_path, "face_datas.dat"), face_)

        self.face_data_widget.lineEdit_image_name.clear()
        self.face_data_widget.label_display_image.clear()
        self.face_data_widget.label_display_image.setText("None")
        self.choose_image = str()
        QMessageBox.information(self, '通知', '新增成功')

    def recognition_image(self):
        if self.face_recognition_widget.comboBox_det_mode.currentText() == "手動":
            self.choose_file()
            det_image = cv2.imread(self.choose_image)
            det_image = cv2.cvtColor(det_image, cv2.COLOR_BGR2RGB)
            result = detector_face(det_image)
            recognition_name = recognition(result[0], load_face_data(os.path.join(bin_file_path, "face_datas.dat")), 0.5)
            self.face_recognition_widget.label_imgStream.setPixmap(QPixmap(cv_img_to_qt_img(result[1])))
            self.face_recognition_widget.label_name.setText(recognition_name)
