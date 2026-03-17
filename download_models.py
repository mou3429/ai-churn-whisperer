# download_models.py
import os
import sys
import subprocess

# ---------- REPLACE THESE with the file IDs from your Drive share links ----------
XGB_FILE_ID = "15L4LX9kp_QFTqJQlHRu_p0uYFRTfchhW"
PRE_FILE_ID = "1sxHhn1Q4h8EC1klGY4def7Ur9zcfZyhk"
# ---------------------------------------------------------------------------------

def ensure_gdown():
    try:
        import gdown  # noqa: F401
    except Exception:
        print("gdown not found. Installing gdown...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "gdown"])
        print("gdown installed.")

def download_from_drive(file_id, out_path):
    import gdown
    url = f"https://drive.google.com/uc?id={file_id}"
    print(f"Downloading to {out_path} ...")
    gdown.download(url, out_path, quiet=False)

def main():
    os.makedirs("models", exist_ok=True)
    ensure_gdown()

    xgb_out = os.path.join("models", "xgb_model.pkl")
    pre_out = os.path.join("models", "preprocessor.pkl")

    # Only download if missing (safe to re-run)
    if not os.path.exists(xgb_out):
        download_from_drive(XGB_FILE_ID, xgb_out)
    else:
        print(f"{xgb_out} already exists, skipping download.")

    if not os.path.exists(pre_out):
        download_from_drive(PRE_FILE_ID, pre_out)
    else:
        print(f"{pre_out} already exists, skipping download.")

    print("Done. Models are in the ./models folder.")

if __name__ == "__main__":
    main()