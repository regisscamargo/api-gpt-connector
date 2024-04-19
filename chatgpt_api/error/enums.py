class GenericError:

	def __init__(self, code: str, type: str):
		self.code = code
		self.type = type

	def to_json(self) -> dict:
		return {
			'error_code': self.code,
			'error_type': self.type
		}


class Error:

	INTERNAL_SERVER_ERROR = GenericError(500, 'Server Error, please try again later')