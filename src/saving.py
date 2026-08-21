import logging


def save_data(df, file_path):
    try:
        df.to_csv(
            file_path,
            index=False
        )

        logging.info(
            f"Data saved successfully to {file_path}"
        )

    except Exception as error:
        logging.error(
            f"Failed to save data to {file_path}: {error}"
        )