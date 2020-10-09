import fasttext
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Recommender(Resource):
    model = fasttext.load_model('model-split.bin')

    def get(self, title):
        title = title.replace('_', ' ')
        result = self.model.predict(title, 2)
        return {
            'second': {
                'title': result[0][0][9:],
                'accuracy': result[1][0],
            },
            'first': {
                'title': result[0][1][9:],
                'accuracy': result[1][1]
            }
        }


api.add_resource(Recommender, '/recommender/<title>')

if __name__ == '__main__':
    app.run();
