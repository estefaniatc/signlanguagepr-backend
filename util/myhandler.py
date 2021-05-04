class MyHandler:
    
    @staticmethod
    def verify_parameters(jsonP, params):
        for param, value in jsonP.items():
            if param in params and value is None:
                return None
        return jsonP