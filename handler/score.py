from flask import jsonify, session
from dao.scores import Scores
from dao.users import Users
from util.myhandler import MyHandler


class ScoresHandler:

    @staticmethod
    def getAllScores():
        try:
            scores = Scores.getScores()
            result_list = []
            for score in scores:
                result_list.append(score.to_dict())
            result = {
                "message": "Success!",
                "scores": result_list
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def getScoresById(sid):
        try:
            score = Scores.getScoresById(sid)
            score_dict = score.to_dict()
            result = {
                "message": "Success!",
                "score": score_dict
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def getScoresByUserId(uid):
        try:
            scores = Scores.getScoresByUserId(uid)
            result_list = []
            for score in scores:
                result_list.append(score.to_dict())
            result = {
                "message": "Success!",
                "scores": result_list
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    # getScoresByLessonIdAndUserId
    @staticmethod
    def getScoresByLessonIdAndUserId(lid, uid):
        try:
            scores = Scores.getScoresByLessonIdAndUserId(lid, uid)
            result_list = []
            for score in scores:
                result_list.append(score.to_dict())
            result = {
                "message": "Success!",
                "scores": result_list
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def createScore(json):
        valid_params = MyHandler.verify_parameters(json, ['user_id', 'lesson_id'])
        if valid_params:
            try:
                new_score = Scores(**valid_params)
                created_score = new_score.create()
                user_to_update = Users.getUserById(json['user_id'])
                setattr(user_to_update, "total_points", user_to_update.total_points + int(json['correctPoints']))
                user_to_update.update()
                result = {
                    "message": "Success!",
                    "score": created_score.to_dict(),
                    "user": user_to_update.to_dict()
                }
                return jsonify(result), 201
            except Exception as err:
                return jsonify(message="Server error!", error=err.__str__()), 500
        else:
            return jsonify(message="Bad Request!"), 400

    @staticmethod
    def updateScore(sid,json):
        valid_params = MyHandler.verify_parameters(json, ['score_id'])
        if sid and valid_params:
            try:
                score_to_update = Scores.getScoreById(sid)
                if score_to_update:
                    for key, value in valid_params.items():
                        setattr(score_to_update, key, value)
                    score_to_update.update()
                    result = {
                        "message": "Success!",
                        "score": score_to_update.to_dict(),
                    }
                    return jsonify(result), 200
                else:
                    return jsonify(message="Not Found!"), 404
            except Exception as err:
                return jsonify(message="Server Error!", error=err.__str__()), 500
        else:
            return jsonify(message="Bad Request!"), 400

    @staticmethod
    def deleteScore(sid):
        if sid:
            try:
                score_to_delete = Scores.getScoreById(sid)
                if score_to_delete:
                    score_to_delete.delete()
                    return jsonify(message="Success!"), 200
                else:
                    return jsonify(message="Not Found!"), 404
            except Exception as err:
                return jsonify(message="Server Error!", error=err.__str__()), 500
        else:
            return jsonify(message="Bad Request!"), 400
