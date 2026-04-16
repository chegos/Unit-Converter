from flask import Flask, render_template, request

app = Flask(__name__)

# Função de conversão
def convert_length(value, from_unit, to_unit):
    conversions = {
        "meter": 1,
        "kilometer": 1000,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "mile": 1609.34,
        "yard": 0.9144,
        "foot": 0.3048,
        "inch": 0.0254
    }

    # Converter para metros primeiro
    value_in_meters = value * conversions[from_unit]

    # Converter para unidade final
    result = value_in_meters / conversions[to_unit]

    return round(result, 2)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]

        result = convert_length(value, from_unit, to_unit)

        return render_template("result.html", result=result, value=value, from_unit=from_unit, to_unit=to_unit)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
