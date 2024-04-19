from flask import jsonify
from .enums import Error


class ExceptionNoteResponse(Exception):
	def __init__(self, msg: str):
		self.msg = Error.INTERNAL_SERVER_ERROR.value

	
	
