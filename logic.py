from typing import List
import model
import db

TITLE_LIMIT = 30
TEXT_LIMIT = 200

class LogicException(Exception):
    pass

class EventLogic:
    def __init__(self):
        self._event_db = db.EventDB()

    @staticmethod
    def _validate_event(event: model.Event):
        if event is None:
            raise LogicException("event is None")
        if len(event.title) > TITLE_LIMIT:
            raise LogicException(f"title length > MAX: {TITLE_LIMIT}")
        if len(event.text) > TEXT_LIMIT:
            raise LogicException(f"text length > MAX: {TEXT_LIMIT}")

    def create(self, event: model.Event) -> str:
        self._validate_event(event)
        try:
            return self._event_db.create(event)
        except Exception as ex:
            raise LogicException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[model.Event]:
        try:
            return self._event_db.list()
        except Exception as ex:
            raise LogicException(f"failed LIST operation with: {ex}")

    def read(self, id: str) -> model.Event:
        try:
            return self._event_db.read(id)
        except Exception as ex:
            raise LogicException(f"failed READ operation with: {ex}")

    def update(self, id: str, event: model.Event):
        self._validate_event(event)
        try:
            return self._event_db.update(id, event)
        except Exception as ex:
            raise LogicException(f"failed UPDATE operation with: {ex}")

    def delete(self, id: str):
        try:
            return self._event_db.delete(id)
        except Exception as ex:
            raise LogicException(f"failed DELETE operation with: {ex}")
