from flask import Blueprint, render_template, jsonify, request


home_controller = Blueprint('home_controller', __name__)
game_controller = Blueprint('game_controller', __name__)


@home_controller.route('/', methods=['GET'])
def index():
    return render_template('index.html')


#rotas para o front end
@game_controller.route('/start', methods=['POST'])
def start_game():
    data = request.get_json()
    jogador_inicial = data['jogador_inicial']
    response, status_code = backend.iniciar_jogo(jogador_inicial)
    return jsonify(response), status_code

#demais rotas