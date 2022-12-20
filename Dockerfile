FROM public.ecr.aws/lambda/python:3.9

COPY dv.bin .
COPY zindi_fi.bin .
COPY lambda_function.py .
COPY requirements.txt .

RUN pip install scikit-learn

CMD ["lambda_function.lambda_handler"]
