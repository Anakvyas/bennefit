from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get selected symptoms from the form
        symptoms = request.form.getlist("symptoms")

        # Analyze symptoms (replace with your own logic)
        result = "Negative"
        if "increased_thirst" in symptoms or "frequent_urination" in symptoms:
            result = "Positive"

        return render_template("index.html", result=result, selected_symptoms=symptoms)

    return render_template("index.html", result=None, selected_symptoms=[])

if __name__ == "__main__":
    app.run(debug=True)
