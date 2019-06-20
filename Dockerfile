FROM python:3
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip3 install flask forex_python

WORKDIR /
COPY ["MainScores.py", "Scores.txt", "Utils.py", "./"]

CMD python MainScores.py
