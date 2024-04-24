from flask import Flask, request
import model
import logic

app = Flask(__name__)
event_logic = logic.EventLogic()

class ApiException(Exception):
    pass

def _from_raw(raw_event: str) -> model.Event:
    parts = raw_event.split('|')
    if len(parts) != 3:
        raise ApiException(f"Invalid RAW event data: {raw_event}")
    event = model.Event()
    event.date = parts[0]
    event.title = parts[1]
    event.text = parts[2]
    return event

def _to_raw(event: model.Event) -> str:
    return f"{event.date}|{event.title}|{event.text}"

API_ROOT = "/api/v1"
EVENT_API_ROOT = API_ROOT + "/calendar"

@app.route(EVENT_API_ROOT + "/", methods=["POST"])
def create():
    try:
        data = request.get_data().decode('utf-8')
        event = _from_raw(data)
        _id = event_logic.create(event)
        return f"new id: {_id}", 201
    except Exception as ex:
        return f"failed to CREATE with: {ex}", 404

@app.route(EVENT_API_ROOT + "/", methods=["GET"])
def list():
    try:
        events = event_logic.list()
        raw_events = ""
        for event in events:
            raw_events += _to_raw(event) + '\n'
        return raw_events, 200
    except Exception as ex:
        return f"failed to LIST with: {ex}", 404

@app.route(EVENT_API_ROOT + "/<id>/", methods=["GET"])
def read(id: str):
    try:
        event = event_logic.read(id)
        raw_event = _to_raw(event)
        return raw_event, 200
    except Exception as ex:
        return f"failed to READ with: {ex}", 404

@app.route(EVENT_API_ROOT + "/<id>/", methods=["PUT"])
def update(id: str):
    try:
        data = request.get_data().decode('utf-8')
        event = _from_raw(data)
        event_logic.update(id, event)
        return "updated", 200
    except Exception as ex:
        return f"failed to UPDATE with: {ex}", 404

@app.route(EVENT_API_ROOT + "/<id>/", methods=["DELETE"])
def delete(id: str):
    try:
        event_logic.delete(id)
        return "deleted", 200
    except Exception as ex:
        return f"failed to DELETE with: {ex}", 404
