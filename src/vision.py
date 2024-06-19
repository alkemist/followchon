# venv/bin/python -m src.vision
import os

from .models.streamer import Streamer
from dotenv import load_dotenv

load_dotenv()

streamer = Streamer(
    os.getenv('LIVE_STREAM_PATH'),
    './models/guinea-pig-v3+chons+camera-v6.pt',
    './live/records',
    './live/captures',
    capture_width=1024,
    capture_height=768,
    show_stream=False,
    verbose=True,
    save_enabled=True,
    loop_enabled=True,
    delete_record=True,
)

streamer.start()

