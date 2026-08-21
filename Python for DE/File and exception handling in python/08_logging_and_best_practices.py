"""Use logging for diagnostics instead of print statements in services."""

import logging


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def parse_quantity(value: str) -> int | None:
    try:
        quantity = int(value)
    except ValueError:
        logger.warning("Invalid quantity received: %r", value)
        return None

    if quantity <= 0:
        logger.warning("Quantity must be positive: %d", quantity)
        return None

    logger.info("Accepted quantity: %d", quantity)
    return quantity


if __name__ == "__main__":
    parse_quantity("3")
    parse_quantity("two")
    parse_quantity("0")
