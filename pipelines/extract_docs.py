import yaml
from pathlib import Path

from downloader import download
from parser import extract_text
from storage import save_raw, save_processed
from metadata import update_metadata
from utils import setup_logger, ensure_dir

from crawler import crawl

logger = setup_logger()


BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
METADATA_FILE = BASE_DIR / "data" / "metadata" / "documents.csv"
CONFIG_DIR = Path(__file__).parent / "config"


def load_config(name: str):
    path = CONFIG_DIR / f"{name}.yaml"
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def run_pipeline(config_name: str):

    config = load_config(config_name)

    source = config["source"]
   
    urls = crawl(config)

    raw_path = RAW_DIR / source
    processed_path = PROCESSED_DIR / source

    ensure_dir(raw_path)
    ensure_dir(processed_path)
    ensure_dir(METADATA_FILE.parent)

    metadata_records = []

    logger.info(f"Starting ingestion for: {source}")
    logger.info(
        f"Found {len(urls)} documents"
    )

    for index, url in enumerate(urls):

        name = f"{source}_{index}"

        try:
            logger.info(f"Processing: {url}")

            html = download(url)

            raw_file = save_raw(raw_path, name, html)

            text = extract_text(html)

            processed_file = save_processed(processed_path, name, text)

            metadata_records.append({
                "source": source,
                "document_name": name,
                "url": url,
                "raw_file": raw_file,
                "processed_file": processed_file
            })

        except Exception as e:
            logger.error(f"Failed {url}: {e}")

    update_metadata(METADATA_FILE, metadata_records)

    logger.info(f"Completed ingestion for {source}")


if __name__ == "__main__":
    run_pipeline("airflow")
    run_pipeline("kafka")
    run_pipeline("kubernetes")
    run_pipeline("mlflow")