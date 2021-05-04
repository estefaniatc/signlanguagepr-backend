from flask import jsonify, session
from dao.answers import Answers
from util.myhandler import MyHandler


class AnswersHandler:

    @staticmethod
    def getAnswers():
        try:
            answers = Answers.getAnswers()
            result_list = []
            for ans in answers:
                result_list.append(ans.to_dict())
            result = {
                "message": "Success!",
                "answers": result_list
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def getAnswerById(aid):
        try:
            answer = Answers.getAnswerById(aid)
            ans_dict = answer.to_dict()
            result = {
                "message": "Success!",
                "answer": ans_dict
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def getAnswerByQuestionId(qid):
        try:
            answers = Answers.getAnswerByQuestionId(qid)
            result_list = []
            for ans in answers:
                result_list.append(ans.to_dict())
            result = {
                "message": "Success!",
                "answers": result_list
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500


    @staticmethod
    def createAnswer(json):
        valid_params = MyHandler.verify_parameters(
            json, ["question_id"])
        if valid_params:
                try:
                    new_ans = Answers(**valid_params)
                    created_ans = new_ans.create()
                    result = {
                        "message": "Success!",
                        "answer": created_ans.to_dict(),
                    }
                    return jsonify(result), 201
                except Exception as err:
                    return jsonify(message="Server error!", error=err.__str__()), 500
        else:
            return jsonify(message="Bad Request!"), 400
