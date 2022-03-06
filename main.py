from flask import Flask, render_template, request, flash, redirect
import players

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ja203sdknr23nkdlns'  # should be some random long string

@app.route('/about.html')
def about_page():
    return render_template("about.html")

@app.route('/feedback.html')
def contact_page():
    return render_template("feedback.html")

# home page
@app.route('/', methods=["GET", "POST"])
def main():
    name = request.args.get("search_box")   # search_box = <First_Last>, and doing this gets us the first and last name (search_box is due to the input's name being "search_box" in index.html)

    if name is None:
        name = "LeBron James"
    else:
        if name == "" or players.get_playerID(name) is None:
            flash("Could not find player in database. Please specify in First Last name format!")
            return redirect("/")

    player_names = players.get_allPlayers()
    player_name = players.get_playerName(name)
    df, url = players.creating_dataframe(players.get_playerID(name))
    return render_template("index.html", player_name=player_name, data=df.to_html(), image_url=url, player_names=player_names)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)

