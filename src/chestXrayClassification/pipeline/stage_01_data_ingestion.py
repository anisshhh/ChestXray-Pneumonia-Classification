import kagglehub
from pathlib import Path
import shutil
from src.chestXrayClassification.utils.common import read_yaml, create_directories

def data_ingestion(config_path="config/config.yaml"):
    config = read_yaml(config_path)
    ingestion_cfg = config["data_ingestion"]

    root_dir = Path(ingestion_cfg["root_dir"])
    dataset_name = ingestion_cfg["dataset_name"]

    target_path = root_dir / "chest_xray"
    create_directories([root_dir])

    # ✅ If dataset already exists in artifacts → skip
    if target_path.exists():
        print("⚠️ Dataset already exists at:", target_path)
        return str(target_path)

    # ✅ Check if dataset is already in cache
    cache_base = Path.home() / ".cache" / "kagglehub" / "datasets" / "paultimothymooney" / dataset_name
    if cache_base.exists():
        latest_version = sorted(cache_base.glob("versions/*"))[-1]  # get latest version
        print("♻️ Using cached dataset at:", latest_version)
        source_path = latest_version / "chest_xray"

        # Copy only contents (train/test/val) into target_path
        shutil.copytree(source_path, target_path, dirs_exist_ok=True)
        print("✅ Dataset copied to project folder:", target_path)
        return str(target_path)

    # ✅ Otherwise, download from KaggleHub
    print("⬇️ Downloading dataset from KaggleHub...")
    cache_path = kagglehub.dataset_download(f"paultimothymooney/{dataset_name}")
    print("✅ Download complete at:", cache_path)

    source_path = Path(cache_path) / "chest_xray"

    # Copy only contents (train/test/val) into target_path
    shutil.copytree(source_path, target_path, dirs_exist_ok=True)
    print("✅ Dataset moved to project folder:", target_path)

    return str(target_path)


if __name__ == "__main__":
    data_ingestion()
