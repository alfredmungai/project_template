import logging
import sys
from logging.handlers import BufferingHandler


logger = logging.getLogger(__name__)

LOGFORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

LOGNAME = "project_template.log"

# Initialize bufferhandler - will be used for /log endpoints
bufferHandler = BufferingHandler(1000)
bufferHandler.setFormatter(logging.Formatter(LOGFORMAT))


def setup_logging() -> None:
    """
    Early setup for logging.
    Uses INFO loglevel and only the Streamhandler.
    Early messages (before proper logging setup) will therefore only be sent to additional
    logging handlers after the real initialization, because we don't know which
    ones the user desires beforehand.
    """

    logging.basicConfig(
        level=logging.INFO,
        format=LOGFORMAT,
        handlers=[
            logging.FileHandler(LOGNAME),
            logging.StreamHandler(sys.stderr),
            bufferHandler,
        ],
    )
