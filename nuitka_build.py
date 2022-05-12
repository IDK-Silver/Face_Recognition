import os
import shutil
import project_setup

# os.system("scripts\\win\\nuitka_build.bat")

main_dist_folder = os.path.join(project_setup.build_folder_name, "main.dist")

for miss_file in os.listdir(project_setup.build_miss_folder):
    need_remove = False
    if os.path.exists(os.path.join(main_dist_folder, miss_file)):
        need_remove = True
    if os.path.isfile(os.path.join(project_setup.build_miss_folder, miss_file)):
        if need_remove:
            os.remove(os.path.join(main_dist_folder, miss_file))
        shutil.copyfile(os.path.join(os.path.join(project_setup.build_miss_folder, miss_file)),
                        os.path.join(main_dist_folder, miss_file))
    elif os.path.isdir(os.path.join(project_setup.build_miss_folder, miss_file)):
        if need_remove:
            shutil.rmtree(os.path.join(main_dist_folder, miss_file))
        shutil.copytree(os.path.join(os.path.join(project_setup.build_miss_folder, miss_file)),
                        os.path.join(main_dist_folder, miss_file))
print("Build Finish")
input("Press any key to exit")
