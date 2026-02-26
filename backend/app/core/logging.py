import logging
import os

def setup_logging(log_file='app.log'):
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

    logging.debug('Logging is set up.')

if __name__ == '__main__':
    setup_logging()