#import numpy as np
#from io import BytesIO
#from urllib import request
import pickle
import json

model_file = 'zindi_fi.bin'
vectorizer = 'dv.bin'

with open(model_file, 'rb') as f_in:
    
    dv, model = pickle.load(f_in)

#dv = pickle.load(open(vectorizer, 'rb'))
#print('Model Loaded')


def predict(customer):

    X = dv.transform([customer])
    y_pred = model.predict(X)

    bank_account = y_pred

    result = {
        'Bank Account': bool(bank_account)
    }
    return result


def lambda_handler(event, context):
    customer = event['customer']
    result = predict(customer)
    return result