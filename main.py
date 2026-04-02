import time
import pandas as pd
from app.logger import setup_logger
from app.pipeline.processor import process_file
from app.utils.file_handler import list_files
from app.config import Config

logger = setup_logger()

def main():
    files = list_files(Config.INPUT_FOLDER)
    results = []

    LAST_CALL = 0
    MIN_INTERVAL = 2  # 2 detik interval  API call

    for i, file in enumerate(files):
        logger.info(f"{i+1}/{len(files)} - {file.name}")

        try:
            # THROTTLING (sebelum call API)
            now = time.time()
            elapsed = now - LAST_CALL
            print("elapsed : ", elapsed)

            if elapsed < MIN_INTERVAL:
                sleep_time = MIN_INTERVAL - elapsed
                logger.info(f"Throttling {sleep_time:.2f}s...")
                time.sleep(sleep_time)

            # PROCESS
            data = process_file(file)

            # update last call hanya kalau berhasil hit pipeline
            LAST_CALL = time.time()

            if data:
                results.append(data)

        except Exception as e:
            logger.error(f"[MAIN LOOP ERROR] {file.name}: {e}")
            continue

    # ========================
    # SAVE RESULT
    # ========================
    if results:
        df = pd.DataFrame(results)
        df.to_excel(Config.OUTPUT_FILE, index=False)
        logger.info(f"Saved to {Config.OUTPUT_FILE}")
    else:
        logger.warning("No data extracted")

if __name__ == "__main__":
    main()