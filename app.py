from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.json['expression']
    try:
        result = str(eval(expression, {
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "asin": lambda x: math.degrees(math.asin(x)) if -1 <= x <= 1 else "Error",
            "acos": lambda x: math.degrees(math.acos(x)) if -1 <= x <= 1 else "Error",
            "atan": lambda x: math.degrees(math.atan(x)),
            "sqrt": lambda x: math.sqrt(x) if x >= 0 else "Error",
            "abs": abs,
            "__builtins__": {}
        }))
        return jsonify({'result': result})
    except Exception:
        return jsonify({'result': 'Math Error'})

# THIS PART IS CRITICAL!
if __name__ == '__main__':
    app.run(debug=True)
