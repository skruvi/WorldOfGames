from flask import Flask, flash, redirect, render_template, request, session, abort

def read_score(SCORES_FILE_NAME):
    score_record = open(SCORES_FILE_NAME, "r")
    score_val = score_record.read()
    score_record.close()
    #print(score_val)
    return score_val




app = Flask(__name__)

@app.route("/")
def score_server():
    one_score = read_score('Scores.txt')
    return render_template("Scores.html", SCORE=one_score)

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8777)
    app.run(host='127.0.0.1', port=8777)

