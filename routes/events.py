from fastapi import APIRouter, HTTPException, status
from models.events import Event
from typing import List

event_router = APIRouter(tags=["Events"])
events = []

@event_router.get("/", response_model=List[Event])
async def get_all_events():
    return events

@event_router.get("/{id}", response_model=Event)
async def get_event(id: int):
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")

@event_router.post("/new")
async def create_event(event: Event):
    events.append(event)
    return {"message": "Event created successfully"}

@event_router.delete("/{id}")
async def delete_event(id: int):
    for event in events:
        if event.id == id:
            events.remove(event)
            return {"message": "Event deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
