import json
import loguru

class Tools():

    def logger(self, msg: str):
        return loguru.logger.info(msg)
        

def load_json(arg_json) -> dict:
    return json.loads(arg_json) if type(arg_json) is str else arg_json