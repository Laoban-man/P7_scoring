import hug
from model import Model
import pickle


@hug.cli()
@hug.get("/index")
def index():
    """Load the model"""
    try:
        model = Model()
        model.import_model()
    except:
        print("Failed to load model")

    return {
        "message": "Running",
    }


@hug.post("/upload")
def upload_file(body):
    """accepts file uploads
    import requests
    with open('/home/hysterio/code/open-classrooms/P7_scoring/test.txt', 'rb') as wgetrc_handle:
        response = requests.post('http://localhost:8000/upload', files={'.wgetrc': wgetrc_handle})
    """
    #  is a simple dictionary of {filename: b'content'}
    try:
        print("body: ", body)
        pickle.dump(body, open("new_data.pkl", "wb"))
        model_predict()
    except Exception as e:
        print("Error saving new data :" + str(e))

    return {"message": "Saving data succeeded"}


@hug.cli()
@hug.get("/predict")
def model_predict():
    """Load the model"""
    try:
        model = Model()
        model.import_model()
    except:
        print("Failed to load model")
    try:
        new_data = pickle.load(open("new_data.pkl", "rb"))
        print(new_data)
    except Exception as e:
        print("Error reading new data :" + str(e))

    try:
        model.predict()
    except Exception as e:
        print("Error saving new data :" + str(e))

    return {
        "message": "Running",
    }


if __name__ == "__main__":
    index.interface.cli()
