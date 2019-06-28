


from flask import Flask, render_template, request
from main_jokes import generate_random_joke
import json


app = Flask(__name__, template_folder="templates", static_folder="stat")
app.config['TEMPLATES_AUTO_RELOAD'] = True

jokes_by_countries = {"countries":[]}

# action="{{ url_for('static', filename='html/jokes.html') }}"

"""
<p>I'm a student at Ukrainian Catholic Univercity, major IT&Business Analytics, who loves to learn about people, laugh and write computer code!</p>
Hello there! This site was developed as a part of a course work project for Programming course.
            It's main goal is to serve as a research tool for humor and jokes statictics. At the same time
            it may be used for entertainment and fun time spending!

"""



@app.route("/")
def index():
    with open("registrants.json", "w", encoding="utf-8") as json_file:
        json.dump({}, json_file)
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():

    jks = generate_random_joke()
    # print(jks)
    kwargs = dict(
        joke = jks[-1]
    )
    if not request.form.get("country") or not request.form.get("city")\
       or not request.form.get("username") or not request.form.get("gender")\
            or not request.form.get("age"):
        return render_template("failure.html")

    country = request.form.get("country")
    city = request.form.get("city")
    gender = request.form.get("gender")
    age = request.form.get("age")
    category = jks[0]
    joke_id = jks[1]
    ratings = jks[2]

    rate_a_joke(country, city, gender, age, category, joke_id, ratings, jks[-1])

    return render_template("jokes.html", **kwargs)

def rate_a_joke(country, city, gender, age, category, joke_id, rating, joke):

    with open("registrants.json", "r", encoding="utf-8") as json_file:
        jokes_by_countries = json.load(json_file)
        if jokes_by_countries:
            for country_dct in jokes_by_countries["countries"]:
                if country_dct["country"] == country:
                    for catg in country_dct["categories"]:
                        if catg["category"] == category:
                            new_data = {"ID": joke_id,"joke": joke,
                                            "city": city,"gender": gender,
                                            "age": age,"rating": rating}
                            catg["jokes"].append(new_data)
                            with open("registrants.json", "w", encoding="utf-8") as json_file:
                                json.dump(jokes_by_countries, json_file, ensure_ascii=False)
                            return
                    catg = {"category": category, "jokes":[]}
                    catg["jokes"].append({"ID": joke_id,"joke": joke,
                                            "city": city, "gender": gender,
                                            "age": age,"rating": rating})
                    country_dct["categories"].append(catg)

                    with open("registrants.json", "w", encoding="utf-8") as json_file:
                        json.dump(jokes_by_countries, json_file, ensure_ascii=False)
                    return

            new_country = {"country": country, "categories": [
                {"category": category, "jokes":[
                    {"ID": joke_id,"joke": joke,
                    "city": city,"gender": gender,
                    "age": age,"rating": rating}]}]}

            jokes_by_countries["countries"].append(new_country)
        else:
            jokes_by_countries = {"countries": []}
            new_country = {"country": country, "categories": [
                {"category": category, "jokes": [
                    {"ID": joke_id, "joke": joke,
                    "city": city, "gender": gender,
                    "age": age, "rating": rating}]}]}

            jokes_by_countries["countries"].append(new_country)

    with open("registrants.json", "w", encoding="utf-8") as json_file:
        json.dump(jokes_by_countries, json_file, ensure_ascii=False)


@app.route("/rate", methods=["POST"])
def rate():
    if not request.form.get("reviewStars"):
        return render_template("failure.html")
    print(request.form.get("reviewStars"))
    return render_template("index.html")



if __name__ == "__main__":
    app.run()