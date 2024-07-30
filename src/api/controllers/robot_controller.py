from flask import Blueprint, jsonify, make_response
from controller.robot_controller import RobotController
from neural_network.model import Model
from capture.capture_module import CaptureModule


def construct_robot_blueprint(
        robotcontroller: RobotController,
        model: Model,
        # capture_module: CaptureModule,
) -> Blueprint:

    robot_controller = Blueprint('robot_controller', __name__)

    @robot_controller.route('/help', methods=['GET'])
    def robot_methods():
        return jsonify({
            0: {
                'title': 'Test Positions',
                'route': '.../test_position/<pos_key>/<move_type>',
                'http_method': 'GET',
                'description': 'Allows to test bank positions for the robot.'
            },
            1: {
                'title': 'Get Position',
                'route': '.../position',
                'http_method': 'GET',
                'description': 'Retrieves the actual robot Joint and Pose.'
            },
            2: {
                'title': 'Detect Board',
                'route': '.../detect',
                'http_method': 'GET',
                'description': 'Requests the robot to detect the actual board.'
            },
        }), 200

    @robot_controller.route('/position', methods=['GET'])
    def position():
        joints, pose = robotcontroller.get_positions()
        return jsonify({
            'joints': joints.to_dict,
            'pose': pose.to_dict,
        }), 200

    @robot_controller.route('/test_position/<pos_key>/<move_type>')
    def test_position(pos_key, move_type):
        try:
            if move_type.lower() in ('c', 'cartesian'):
                robotcontroller._to_custom_coords(pos_key)
            else:
                robotcontroller._to_custom_pose(pos_key)
            response = make_response(
                'Moving to position',
                200,
            )
            return response
        except KeyError as err:
            bad_response = make_response(
                f'Key {pos_key} of type {move_type} not found',
                400,
            )
            print(err)
            return bad_response

    @robot_controller.route('/detect', methods=['GET'])
    def detect():
        robotcontroller.to_upperboard()
        capture_module = CaptureModule(1)
        img = capture_module.capture_opencv()
        print(img)
        print('Image successfully read.')
        capture_module.video_capture.release()
        print('Calling the Model to detect pieces.')
        print('This may take a while, please wait...')
        result_dict = model.predict_from_opencv(img)
        # This will change to protobuf once the translation
        # between pixels and board squares is done.
        return jsonify(result_dict), 200

    @robot_controller.route('/disconnect', methods=['GET'])
    def to_disconnect():
        robotcontroller.to_disconnect()
        return jsonify({'ok': 200}), 200

    return robot_controller
