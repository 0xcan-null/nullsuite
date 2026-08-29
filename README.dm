# 🌐 nullsuite - All-in-One Recon Automation Framework

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![Type](https://img.shields.io/badge/suite-Recon%20%26%20OSINT-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

`nullsuite`, siber güvenlik testlerinde keşif (reconnaissance) aşamasını tamamen otomatize eden, çok iş parçacıklı (multi-threaded) ve hafif bir **Attack Surface Mapping** framework'üdür.

Tek bir komutla hedef domain üzerinde subdomain keşfi, açık port taraması ve gizli web dizini tespiti yapar; sonuçları yapılandırılmış JSON formatında raporlar.

---

## ⚡ Özellikler (Pipeline)
1. 📡 **Subdomain Enumeration (`recon.py`):** Hızlı DNS çözümleme ile aktif subdomain tespiti.
2. 🔌 **Port Scanner (`scanner.py`):** Kritik servislerin ve açık portların eşzamanlı taranması.
3. 🕵️ **Web Fuzzer (`fuzzer.py`):** Açık web servislerindeki gizli ve hassas dizinlerin (`.env`, `/admin`, `/backup` vb.) taranması.
4. 📊 **Raporlama:** Tüm zincirleme keşif verisini JSON formatında dışa aktarma.

---

## 🚀 Kullanım (Usage)

bash
# Repoyu klonlayın
git clone https://github.com/Oxcan-null/nullsuite.git
cd nullsuite

# Temel tarama
python nullsuite.py -d example.com

# Taramayı JSON raporu olarak kaydetme
python nullsuite.py -d example.com -o rapor.json

