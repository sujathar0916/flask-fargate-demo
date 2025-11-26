from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from AWS Fargate on ECS via ALB!"

if __name__ == "__main__":
    # Bind to 0.0.0.0 so container port is accessible
   app.run(host="0.0.0.0", port=80)
