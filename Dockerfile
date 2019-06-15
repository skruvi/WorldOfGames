FROM python:3
RUN python -m pip install --upgrade pip 
RUN pip3 install flask forex_python
WORKDIR /
COPY ["CurrencyRouletteGame.py", "e2e.py", "GuessGame.py", "Live.py", "MainGame.py","MainScores.py", "MemoryGame.py", "Score.py", "Scores.txt", "Utils.py", "./"]

CMD python MainScores.py
