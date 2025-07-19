import os
import hashlib
from quarantine import quarantine_file

def load_signatures():
    with open("signatures.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

def hash_dosya_yolu(dosya_yolu):
    hash_sha256 = hashlib.sha256()
    with open(dosya_yolu, "rb") as f:
        for bolum in iter(lambda: f.read(4096), b""):
            hash_sha256.update(bolum)
    return hash_sha256.hexdigest()

def scan_file(dosya_yolu):
    imzalar = load_signatures()
    dosya_hash = hash_dosya_yolu(dosya_yolu)
    if dosya_hash in imzalar:
        quarantine_file(dosya_yolu)
        return f"VİRÜS BULUNDU!\n{dosya_yolu}\nDosya karantinaya alındı."
    else:
        return f"Temiz: {dosya_yolu}"

def scan_directory(klasor):
    imzalar = load_signatures()
    bulunanlar = []

    for kok, _, dosyalar in os.walk(klasor):
        for dosya in dosyalar:
            yol = os.path.join(kok, dosya)
            try:
                hash_ = hash_dosya_yolu(yol)
                if hash_ in imzalar:
                    quarantine_file(yol)
                    bulunanlar.append(yol)
            except:
                continue

    if bulunanlar:
        return f"{len(bulunanlar)} virüs bulundu ve karantinaya alındı:\n\n" + "\n".join(bulunanlar)
    else:
        return "Virüs bulunamadı."
