import logging
import warnings
from pickle import load

import azure.functions as func
import pandas as pd
import tensorflow as tf
from tensorflow import keras

tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
warnings.filterwarnings("ignore")


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("*******Starting main function*******")
    logging.info(f"Request query: {req.get_json()}")

    preprocessor = load(open("dl_preprocessor.pkl", "rb"))
    model = keras.models.load_model("dl_model")

    logging.info("*******Finishing main function*******")

    return func.HttpResponse(
        status_code=200,
        body=f"{model.predict(preprocessor.transform(pd.DataFrame(req.get_json())))}",
    )
