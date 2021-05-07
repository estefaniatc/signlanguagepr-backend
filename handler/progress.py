from flask import jsonify
from dao.progress import Progress
from util.myhandler import MyHandler


class ProgressHandler:

    @staticmethod
    def getAllProgress():
        try:
            progress = Progress.getProgress()
            result_list = []
            for p in progress:
                result_list.append(p.to_dict())
            result = {
                "message": "Success!",
                "progress": result_list
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def getProgressById(pid):
        try:
            progress = Progress.getScoresById(pid)
            p_dict = progress.to_dict()
            result = {
                "message": "Success!",
                "score": p_dict
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def getProgressByUserId(uid):
        try:
            progress = Progress.getProgressByUserId(uid)
            result_list = []
            for p in progress:
                result_list.append(p.to_dict())
            result = {
                "message": "Success!",
                "progress": result_list
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    # getScoresByLessonIdAndUserId
    @staticmethod
    def getProgressByLessonIdAndUserId(lid, uid):
        try:
            progress = Progress.getProgressByLessonIdAndUserId(lid, uid)
            result_list = []
            for p in progress:
                result_list.append(p.to_dict())
            result = {
                "message": "Success!",
                "progress": result_list
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def createProgress(json):
        valid_params = MyHandler.verify_parameters(json, ['user_id', 'lesson_id', 'type'])
        check = Progress.checkIfRepeated(json['lesson_id'], json['user_id'], json['type'])
        if valid_params:
            if check:
                try:
                    new_p = Progress(**valid_params)
                    created_p = new_p.create()
                    result = {
                        "message": "Success!",
                        "progress": created_p.to_dict(),
                    }
                    return jsonify(result), 201
                except Exception as err:
                    return jsonify(message="Server error!", error=err.__str__()), 500
        else:
            return jsonify(message="Bad Request!"), 400

    @staticmethod
    def updateProgress(pid,json):
        valid_params = MyHandler.verify_parameters(json, ['progress_id'])
        if pid and valid_params:
            try:
                p_to_update = Progress.getProgressById(pid)
                if p_to_update:
                    for key, value in valid_params.items():
                        setattr(p_to_update, key, value)
                    p_to_update.update()
                    result = {
                        "message": "Success!",
                        "progress": p_to_update.to_dict(),
                    }
                    return jsonify(result), 200
                else:
                    return jsonify(message="Not Found!"), 404
            except Exception as err:
                return jsonify(message="Server Error!", error=err.__str__()), 500
        else:
            return jsonify(message="Bad Request!"), 400

