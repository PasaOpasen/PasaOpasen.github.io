


from_path = "D:/PasaOpasen.github.io/images/Миша Светлов/вторая съемка/отбор2"
to_path = "D:/PasaOpasen.github.io/images/Миша Светлов/вторая съемка/отбор2ориги"
where = "C:/Users/qtckp/YandexDisk/Загрузки/ДИМА"


import glob
import os
import shutil

files = [ os.path.splitext(os.path.basename(file))[0] + '.cr2' for file in glob.glob(os.path.join(from_path,'*'))]

print(files)

for file in files:
    shutil.copyfile(os.path.join(where, file), os.path.join(to_path, file))
