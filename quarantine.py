import os
import shutil

def quarantine_file(dosya_yolu):
    karantina_klasoru = "quarantine_folder"
    os.makedirs(karantina_klasoru, exist_ok=True)
    hedef_yol = os.path.join(karantina_klasoru, os.path.basename(dosya_yolu))
    shutil.move(dosya_yolu, hedef_yol)
