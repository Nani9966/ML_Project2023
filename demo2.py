from flask import Flask
from ML_Project.logger import logging
from ML_Project.exception import CustomException
import os ,sys

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    try :
        raise Exception("we are testing our exception file ")
    except Exception as e:
        ML_Project =CustomException(e,sys)
        logging.info(ML_Project.error_message )
        logging.info("we are testing logging module")


        return "helo world"


if __name__=="__main__":
    app.run(debug=True)



