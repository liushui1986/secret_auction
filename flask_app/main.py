from flask import Flask, render_template, request, redirect, url_for
from art import logo

app = Flask(__name__)

bids = {}
highest_bid = 0
winner = ''
bidding_finished = False

@app.route("/", methods=["GET", "POST"])
def home():
    global highest_bid, winner, bidding_finished

    if request.method == "POST":
        if 'new_bidder' in request.form:
            bidding_finished = request.form.get("new_bidder").lower() == 'n'
            if bidding_finished:
                return redirect(url_for('result'))

        elif not bidding_finished:
            name = request.form.get("name")
            bid = int(request.form.get("bid"))

            if bid > highest_bid:
                highest_bid = bid
                winner = name

            bids[name] = bid

        return redirect(url_for('home'))

    return render_template("index.html", logo=logo, highest_bid=highest_bid, winner=winner, bidding_finished=bidding_finished)

@app.route("/result")
def result():
    return render_template("result.html", logo=logo, winner=winner, highest_bid=highest_bid)

if __name__ =="__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
