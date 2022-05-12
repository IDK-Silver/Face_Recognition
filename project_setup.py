import os
import shutil
import sys

print("Start SetUP")

python_venv_path = os.path.abspath("venv")
python_venv_lib_path = os.path.abspath(os.path.join(python_venv_path, "Lib", "site-packages"))
build_folder_name = os.path.join(os.path.abspath("."), "out")
build_miss_folder = os.path.join(build_folder_name, "miss_files")
python_std_folder = os.path.join(os.path.split(sys.executable)[0], "Lib")

if __name__ == "__main__":

    if not os.path.isdir(python_venv_path):
        print("Python Venv")
        os.system("python -m venv venv")
        os.system("venv\\Scripts\\pip.exe install -r requirements.txt")

    if not os.path.isdir(build_folder_name):
        os.mkdir("out")

    if not os.path.isdir(build_miss_folder):
        os.mkdir(build_miss_folder)

    dlib_miss_file = str("_dlib_pybind")


    def search(want_find_file: str, find_path: str):
        for filename in os.listdir(find_path):
            if len(filename) > len(want_find_file):
                if len(want_find_file) == len(filename):
                    if want_find_file == filename:
                        return filename
                if want_find_file == filename[0:len(want_find_file)]:
                    return filename


    miss_files_list = [
        os.path.join(python_std_folder, "argparse.py"),
        os.path.join(python_venv_lib_path, "cv2"),
        os.path.join(python_venv_lib_path, "dlib"),
        os.path.join(python_std_folder, "email"),
        os.path.join(python_venv_lib_path, "face_recognition"),
        os.path.join(python_venv_lib_path, "face_recognition_models"),
        os.path.join(python_venv_lib_path, "numpy"),
        os.path.join(python_venv_lib_path, "PIL"),
        os.path.join(python_venv_lib_path, "pkg_resources"),
        os.path.join(python_venv_lib_path, search(dlib_miss_file, python_venv_lib_path)),
        os.path.join(python_std_folder, "plistlib.py"),
    ]

    for miss_file in miss_files_list:
        file_name = os.path.split(miss_file)[1]
        if not os.path.exists(os.path.join(build_miss_folder, file_name)):
            print(f"miss file : {miss_file}")
            if os.path.isfile(miss_file):
                print(os.path.join(build_miss_folder, file_name))
                shutil.copyfile(miss_file, os.path.join(build_miss_folder, file_name))
            elif os.path.isdir(miss_file):
                print(os.path.join(build_miss_folder, file_name))
                shutil.copytree(miss_file, os.path.join(build_miss_folder, file_name))
    print("設定完成")
    input("Press any key to exit")
