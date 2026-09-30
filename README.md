# ☕ Cuphead Mobile: Rapid Fire Mod & Event Patcher

[English](#english) | [Русский](#русский)

---

<a name="english"></a>
## English

A reverse-engineering and modding suite for **Cuphead Mobile** (Android port built with HTML5 / Construct engine).

This project analyzes the event sheets in `data.js` and applies automated patches to weapon timers, converting Peashooter, Spread, and Airplane weapons into high-speed **Rapid Fire / Machine Gun** mode, followed by automated APK repackaging and signing.

### ✨ Features & Patches
- **Automated Event Sheet Analysis**: Decodes Construct 2/3 action trees, object UIDs, and timer conditions.
- **Weapon Fire-Rate Overhaul**:
  - Peashooter cooldowns reduced to near-zero.
  - Spread weapon multi-shot interval accelerated.
  - Plane bullet spawn delay bypassed for continuous fire.
- **Automated Repack & Sign**: Unzips base APK, replaces modified assets, runs `jarsigner` / `apksigner` with auto-generated debug keystore.

### 🚀 Getting Started

#### Requirements
- Python 3.8+
- Java JDK (`keytool`, `jarsigner`)
- Base APK (`cuphead_v0.6.1_orig.apk`)

#### Usage
1. Apply the rapid fire event patches:
   ```bash
   python apply_rapid_fire.py
   ```
2. Repackage and sign the APK:
   ```bash
   python repack_and_sign.py
   ```
3. Install the resulting `cuphead_mobile_rapid_fire.apk` on your Android device or emulator.

---

<a name="русский"></a>
## Русский

Инструментарий модификации и реверс-инжиниринга мобильного порта **Cuphead Mobile** (Android-порт на базе HTML5 / Construct 2/3).

Скрипты анализируют дерево событий движка (`data.js`), перехватывают таймеры стрельбы для оружия Peashooter, Spread и самолета, превращая их в пулеметный режим (Rapid Fire), а затем автоматически пересобирают и подписывают APK.

### ✨ Возможности
- **Патчинг таймеров стрельбы**: Снятие кулдаунов на спавн пуль для обычного оружия, дробовика и авиационных уровней.
- **Автоматическая пересборка и подпись**: Распаковка исходного APK, подмена `data.js`, сборка и подпись через `jarsigner` с созданием `debug.keystore`.

### 🚀 Инструкция

1. Применить патчи скорострельности:
   ```bash
   python apply_rapid_fire.py
   ```
2. Пересобрать и подписать APK:
   ```bash
   python repack_and_sign.py
   ```
3. Установить полученный файл `cuphead_mobile_rapid_fire.apk` на телефон или эмулятор.

### 📄 License
For educational and research purposes only.
