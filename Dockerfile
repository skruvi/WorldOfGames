FROM python:3
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip3 install flask forex_python selenium

RUN curl https://chromedriver.storage.googleapis.com/2.4/chromedriver_linux32.zip -o /usr/local/bin/chromedriver
RUN chmod +x /usr/local/bin/chromedriver

WORKDIR /
COPY ["CurrencyRouletteGame.py", "e2e.py", "GuessGame.py", "Live.py", "MainGame.py","MainScores.py", "MemoryGame.py", "Score.py", "Scores.txt", "Utils.py", "./"]
#COPY ["chromedriver.exe", "DevOps Course/"]
COPY ["/templates/*", "/templates/"]
#COPY ["chromedriver.exe", "/usr/local/bin"]
CMD python MainScores.py
