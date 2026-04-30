from flask import Flask, jsonify
from ProductionCode.command_line import find_creator, count_stolen_by_artist

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
     return "Sorry, read the README for format.", 404

@app.route("/creator/<string:artwork>")
def creator_route(artwork):
    result = find_creator(artwork)

    if result is None:
        return "Artwork not found", 404

    return result


@app.route("/stolen_count/<string:artist>")
def stolen_count_route(artist):
    count = count_stolen_by_artist(artist)
    
    return str(count)

 

if __name__ == "__main__":
    app.run()