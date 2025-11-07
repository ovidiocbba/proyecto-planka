import logging
import json


def log_request_response(url, response, headers=None, payload=None):
    """
    INFO:  IP Address o dominio
    DEBUG: Request URL + Headers
    DEBUG: Payloads (datos enviados en el request)
    INFO:  Status Code
    DEBUG: Response (body o json de respuesta) 
    """
    logging.info("IP ADDRESS OR DOMAIN: %s", url.split("/")[2])
    logging.debug("REQUEST URL: %s", url)
    logging.info("STATUS CODE: %s", response.status_code)
    
    if headers:
        try:
            headers_dict = dict(headers)
        except Exception:
            headers_dict = headers
        logging.debug("REQUEST HEADERS:\n%s", json.dumps(headers_dict, indent=4, ensure_ascii=False))


    if payload:
        logging.debug("PAYLOAD REQUEST:\n%s", json.dumps(payload, indent=4, ensure_ascii=False))
  
  
def get_logger(name="test_logger"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger