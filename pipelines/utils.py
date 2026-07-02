from pathlib import Path
import logging

# Function which configures and returns a tool to record program activity
def setup_logger():
        logging.basicConfig(
                level=logging.INFO,
                format="%(asctime)s | %(levelname)s | %(message)s"
        )
        return logging.getLogger("doc_pipeline")

# Function to create a folder
def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)