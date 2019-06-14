from flask import Flask, flash, redirect, render_template, request, session, abort

def read_score(SCORES_FILE_NAME):
    score_record = open(SCORES_FILE_NAME, "r")
    score_val = score_record.read()
    score_record.close()
    print("$$$$$$$$$$$$$$$$$$$$$$")
    print(score_val)
    return score_val




app = Flask(__name__)

@app.route("/")
def score_server():
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&7")
    one_score = read_score('Scores.txt')
    print("%%%%%%%%%%%%%%" + one_score)
   # one_score = read_score(SCORES_FILE_NAME)
    return render_template("Scores.html", SCORE=one_score)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9999)
