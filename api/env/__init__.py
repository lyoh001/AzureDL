import json
import logging
import os

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    return func.HttpResponse(
        body=json.dumps({"text": os.environ["CONNECTION_STRING"]})
    )
