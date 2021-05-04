from flask import jsonify, session
from dao.questions import Questions
from util.myhandler import MyHandler


class QuestionsHandler:

    @staticmethod
    def getQuestions():
        try:
            questions = Questions.getQuestions()
            result_list = []
            for q in questions:
                result_list.append(q.to_dict())
            result = {
                "message": "Success!",
                "questions": result_list
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def getQuestionsById(qid):
        try:
            question = Questions.getQuestionsById(qid)
            quest_dict = question.to_dict()
            result = {
                "message": "Success!",
                "question": quest_dict
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def getQuestionsByLessonId(lid):
        try:
            questions = Questions.getQuestionsByLessonId(lid)
            result_list = []
            for q in questions:
                result_list.append(q.to_dict())
            result = {
                "message": "Success!",
                "questions": result_list
            }
            return jsonify(result), 200
        except Exception as e:
            return jsonify(reason="Server error", error=e.__str__()), 500

    @staticmethod
    def createQuestion(json):
        valid_params = MyHandler.verify_parameters(json, ['lesson_id', 'question'])
        if valid_params:
            try:
                new_quest = Questions(**valid_params)
                created_quest = new_quest.create()
                result = {
                    "message": "Success!",
                    "question": created_quest.to_dict(),
                }
                return jsonify(result), 201
            except Exception as err:
                return jsonify(message="Server error!", error=err.__str__()), 500
        else:
            return jsonify(message="Bad Request!"), 400

    @staticmethod
    def updateQuestion(qid,json):
        valid_params = MyHandler.verify_parameters(json, ['question_id'])
        if qid and valid_params:
            try:
                q_to_update = Questions.getQuestionsById(qid)
                if q_to_update:
                    for key, value in valid_params.items():
                        setattr(q_to_update, key, value)
                    q_to_update.update()
                    result = {
                        "message": "Success!",
                        "question": q_to_update.to_dict(),
                    }
                    return jsonify(result), 200
                else:
                    return jsonify(message="Not Found!"), 404
            except Exception as err:
                return jsonify(message="Server Error!", error=err.__str__()), 500
        else:
            return jsonify(message="Bad Request!"), 400

    @staticmethod
    def deleteQuestion(qid):
        if qid:
            try:
                q_to_delete = Questions.getQuestionsById(qid)
                if q_to_delete:
                    q_to_delete.delete()
                    return jsonify(message="Success!"), 200
                else:
                    return jsonify(message="Not Found!"), 404
            except Exception as err:
                return jsonify(message="Server Error!", error=err.__str__()), 500
        else:
            return jsonify(message="Bad Request!"), 400
