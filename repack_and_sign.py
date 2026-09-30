import os
import subprocess
import zipfile
import shutil

ORIG_APK = "cuphead_v0.6.1_orig.apk"
MODIFIED_DATA_JS = "extracted/assets/www/data.js"
UNSIGNED_APK = "cuphead_v0.6.1_rapidfire_unsigned.apk"
FINAL_APK = "cuphead_mobile_rapid_fire.apk"
KEYSTORE = "debug.keystore"

JAVA_HOME = os.environ.get("JAVA_HOME")
KEYTOOL = shutil.which("keytool") or (os.path.join(JAVA_HOME, "bin", "keytool.exe") if JAVA_HOME else "keytool")
JARSIGNER = shutil.which("jarsigner") or (os.path.join(JAVA_HOME, "bin", "jarsigner.exe") if JAVA_HOME else "jarsigner")

def generate_keystore():
    if os.path.exists(KEYSTORE):
        print(f"Keystore {KEYSTORE} already exists.")
        return
    print(f"Generating keystore {KEYSTORE}...")
    cmd = [
        KEYTOOL,
        "-genkeypair",
        "-v",
        "-keystore", KEYSTORE,
        "-alias", "androiddebugkey",
        "-keyalg", "RSA",
        "-keysize", "2048",
        "-validity", "10000",
        "-storepass", "android",
        "-keypass", "android",
        "-dname", "CN=Android Debug,O=Android,C=US"
    ]
    subprocess.check_call(cmd)
    print("Keystore generated successfully!")

def repack_apk():
    print(f"Creating unsigned APK {UNSIGNED_APK}...")
    with zipfile.ZipFile(ORIG_APK, 'r') as in_zip, zipfile.ZipFile(UNSIGNED_APK, 'w', compression=zipfile.ZIP_DEFLATED) as out_zip:
        for item in in_zip.infolist():
            # Skip old signature files
            if item.filename.startswith("META-INF/"):
                continue
            if item.filename == "assets/www/data.js":
                # Write our modified file
                with open(MODIFIED_DATA_JS, 'rb') as f:
                    data_bytes = f.read()
                out_zip.writestr(item, data_bytes)
            else:
                data = in_zip.read(item.filename)
                out_zip.writestr(item, data)
    print(f"Unsigned APK created ({os.path.getsize(UNSIGNED_APK) / (1024*1024):.2f} MB)")

def sign_apk():
    print(f"Signing APK into {FINAL_APK}...")
    cmd = [
        JARSIGNER,
        "-keystore", KEYSTORE,
        "-storepass", "android",
        "-keypass", "android",
        "-sigalg", "SHA256withRSA",
        "-digestalg", "SHA-256",
        "-signedjar", FINAL_APK,
        UNSIGNED_APK,
        "androiddebugkey"
    ]
    subprocess.check_call(cmd)
    print("APK signed successfully!")

def verify_apk():
    print(f"Verifying signed APK {FINAL_APK}...")
    cmd = [JARSIGNER, "-verify", FINAL_APK]
    output = subprocess.check_output(cmd, text=True)
    print("Verification result:\n", output)

def main():
    generate_keystore()
    repack_apk()
    sign_apk()
    verify_apk()
    print(f"\nSUCCESS! Final modded APK is ready at: {os.path.abspath(FINAL_APK)}")

if __name__ == "__main__":
    main()
