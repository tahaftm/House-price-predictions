import logging
import os
from datetime import datetime

os.makedirs("logs", exist_ok=True)
log_folder_name = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
os.makedirs(f"logs\\{log_folder_name}",exist_ok=True)
file_path = f"logs\\{log_folder_name}\\logs.log" 

logging.basicConfig(
    filename=file_path,
    format="[ %(asctime)s ] %(levelname)s - %(name)s - %(message)s",
    level=logging.INFO
)