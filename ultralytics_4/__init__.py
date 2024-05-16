# Ultralytics YOLO 🚀, AGPL-3.0 license

__version__ = "8.2.5"

from ultralytics_4.data.explorer.explorer import Explorer
from ultralytics_4.models import RTDETR, SAM, YOLO, YOLOWorld
from ultralytics_4.models.fastsam import FastSAM
from ultralytics_4.models.nas import NAS
from ultralytics_4.utils import ASSETS, SETTINGS
from ultralytics_4.utils.checks import check_yolo as checks
from ultralytics_4.utils.downloads import download

settings = SETTINGS
__all__ = (
    "__version__",
    "ASSETS",
    "YOLO",
    "YOLOWorld",
    "NAS",
    "SAM",
    "FastSAM",
    "RTDETR",
    "checks",
    "download",
    "settings",
    "Explorer",
)
