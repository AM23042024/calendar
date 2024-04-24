from typing import List
import model

class StorageException(Exception):
    pass

class LocalStorage:
    def __init__(self):
        self._id_counter = 0
        self._storage = {}

    def create(self, event: model.Event) -> str:
        if event.date in [e.date for e in self._storage.values()]:
            raise StorageException("Event for this date already exists")
        self._id_counter += 1
        event.id = str(self._id_counter)
        self._storage[event.id] = event
        return event.id

    def list(self) -> List[model.Event]:
        return list(self._storage.values())

    def read(self, id: str) -> model.Event:
        if id not in self._storage:
            raise StorageException(f"{id} not found in storage")
        return self._storage[id]

    def update(self, id: str, event: model.Event):
        if id not in self._storage:
            raise StorageException(f"{id} not found in storage")
        event.id = id
        self._storage[id] = event

    def delete(self, id: str):
        if id not in self._storage:
            raise StorageException(f"{id} not found in storage")
        del self._storage[id]
