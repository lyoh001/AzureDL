import warnings
from pickle import load

import azure.functions as func
import pandas as pd
import tensorflow as tf
from tensorflow import keras

tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
warnings.filterwarnings("ignore")


def main(req: func.HttpRequest) -> func.HttpResponse:
    preprocessor = load(open("dl_preprocessor/dl_preprocessor.pkl", "rb"))
    model = keras.models.load_model("dl_model")
    return func.HttpResponse(
        # body=f"{model.predict(preprocessor.transform(pd.DataFrame(req.get_json())))}",
        body=f"{req.get_json()}",
    )
