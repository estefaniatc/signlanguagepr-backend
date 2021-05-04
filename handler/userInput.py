from flask import jsonify, session
from dao.userInputs import UserInputs
from util.myhandler import MyHandler


class UserInputHandler:

    @staticmethod
    def getUserInputs():
        try:
            inputs = UserInputs.getUserInputs()
            result_list = []
            for input in inputs:
                result_list.append(input.to_dict())
            result = {
                "message": "Success!",
                "userInput": result_list
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def getUserInputById(ui_id):
        try:
            input = UserInputs.getUserInputById(ui_id)
            input_dict = input.to_dict()
            result = {
                "message": "Success!",
                "userInput": input_dict
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def getUserInputsByScoreId(sid):
        try:
            inputs = UserInputs.getUserInputsByScoreId(sid)
            result_list = []
            for input in inputs:
                result_list.append(input.to_dict())
            result = {
                "message": "Success!",
                "userInput": result_list
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def createUserInput(json):
        valid_params = MyHandler.verify_parameters(json, ['score_id'])
        if valid_params:
            try:
                new_input = UserInputs(**valid_params)
                created_input = new_input.create()
                result = {
                    "message": "Success!",
                    "userInput": created_input.to_dict(),
                }
                return jsonify(result), 201
            except Exception as err:
                return jsonify(message="Server error!", error=err.__str__()), 500
        else:
            return jsonify(message="Bad Request!"), 400

    @staticmethod
    def updateUserInput(ui_id,json):
        valid_params = MyHandler.verify_parameters(json, ['userInput_id'])
        if ui_id and valid_params:
            try:
                input_to_update = UserInputs.getUserInputById(ui_id)
                if input_to_update:
                    for key, value in valid_params.items():
                        setattr(input_to_update, key, value)
                    input_to_update.update()
                    result = {
                        "message": "Success!",
                        "userInput": input_to_update.to_dict(),
                    }
                    return jsonify(result), 200
                else:
                    return jsonify(message="Not Found!"), 404
            except Exception as err:
                return jsonify(message="Server Error!", error=err.__str__()), 500
        else:
            return jsonify(message="Bad Request!"), 400

    @staticmethod
    def deleteUserInput(sid):
        if sid:
            try:
                score_to_delete = UserInputs.getUserInputById(sid)
                if score_to_delete:
                    score_to_delete.delete()
                    return jsonify(message="Success!"), 200
                else:
                    return jsonify(message="Not Found!"), 404
            except Exception as err:
                return jsonify(message="Server Error!", error=err.__str__()), 500
        else:
            return jsonify(message="Bad Request!"), 400
