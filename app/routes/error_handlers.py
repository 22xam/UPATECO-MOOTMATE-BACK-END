from flask import Blueprint
from ..models.exeptions import BadRequest, InsufficientStorage, NotModified, CustomException, FilmNotFound, InvalidDataError

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(BadRequest)
def handle_bad_request(error):
    return error.get_response()

@errors.app_errorhandler(InsufficientStorage)
def handle_insufficient_storage(error):
    return error.get_response()

@errors.app_errorhandler(NotModified)
def handle_Not_Modified(error):
    return error.get_response()

@errors.app_errorhandler(CustomException)
def handle_CustomException(error):
    return error.get_response(), error.status_code

@errors.app_errorhandler(FilmNotFound)
def handle_FilmNotFound(error):
    return error.get_response(), error.status_code

@errors.app_errorhandler(InvalidDataError)
def handle_InvalidDataError(error):
    return error.get_response(), error.status_code