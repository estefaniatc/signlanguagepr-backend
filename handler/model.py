from flask import jsonify
from dao.models import Models
class ModelsHandler:

    @staticmethod
    def getAllModels():
        try:
            models = Models.getModels()
            result_list = []
            for modl in models:
                result_list.append(modl.to_dict())
            result = {
                "message": "Success!",
                "models": result_list
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def getModelById(model_id):
        try:
            modl = Models.getModelById(model_id)
            mod_dict = modl.to_dict()
            result = {
                "message": "Success!",
                "model": mod_dict
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def getModelsByLessonId(lesson_id):
        try:
            models = Models.getModelsByLessonId(lesson_id)
            result_list = []
            for modl in models:
                result_list.append(modl.to_dict())
            result = {
                "message": "Success!",
                "models": result_list
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500
