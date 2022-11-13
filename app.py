from flask import Flask,jsonify, request 
app = Flask(__name__) 
@app.route("/") 
def hello_world(): 
    return "Hello World!" 
if (__name__ == "__main__"): 
    app.run(debug=True)

x=np.load('image.npz')['arr_0']

y=pd.read_csv("labels.csv")["labels"]

print(pd.series(y).value_couts())

classes = ['A','B','C','D','E','F','G','H','I','J',"K"
"L","M", "N","O","P","Q","R","S","T","U","V","W","X",
"Y","Z"]

nclasses = len(classes)

x_train, x_test, y_train, y_test = train_test_split (x,y,
random_state=9, train__size=3500, test_size=500)

def get_prediction (image):
    im_pil = Image.option(image)
    image_bw = im_pil.convert('L')
    image_bw_resized = image_bw.resize((22,30), Image.ANTIALIAS)
    pixel_filter = 20
    min_pixel = np.percentile(image_bw_resized, pixel_filter)
    image_bw_resized_inverted_scaled = np.clip(image_bw_resized-min_pixel,0
    255)

    max_pixel = np.max(image_bw_resized)

    image_bw_resized_inverted_scaled =
np.asarray(image_bw_resized_inverted_scaled)/max_pixel
    test_sample = np.array (image_bw_resized_inverted_scaled).reshape(1,660)
    test_pred = clf.predict(test_sample)
    return test_pred [0]
    
    @app.route("/predict-alphabet", methods=["post"])
    def predict_data():
        image = request.files.get("alphabet")
        prediction = get_prediction(image)
        return jsonify({
            "prediction": prediction
        }), 200