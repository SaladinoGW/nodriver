# DO NOT EDIT THIS FILE!
#
# This file is generated from the CDP specification. If you need to make
# changes, edit the generator and regenerate all of the modules.
#
# CDP domain: BackgroundService (experimental)

from __future__ import annotations

import enum
import typing
from dataclasses import dataclass

from . import network
from . import service_worker
from .util import event_class, T_JSON_DICT


class ServiceName(enum.Enum):
    """
    The Background Service that will be associated with the commands/events.
    Every Background Service operates independently, but they share the same
    API.
    """

    BACKGROUND_FETCH = "backgroundFetch"
    BACKGROUND_SYNC = "backgroundSync"
    PUSH_MESSAGING = "pushMessaging"
    NOTIFICATIONS = "notifications"
    PAYMENT_HANDLER = "paymentHandler"
    PERIODIC_BACKGROUND_SYNC = "periodicBackgroundSync"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> ServiceName:
        return cls(json)


@dataclass
class EventMetadata:
    """
    A key-value pair for additional event information to pass along.
    """

    key: str

    value: str

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["key"] = self.key
        json["value"] = self.value
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> EventMetadata:
        return cls(
            key=str(json["key"]),
            value=str(json["value"]),
        )


@dataclass
class BackgroundServiceEvent:
    #: Timestamp of the event (in seconds).
    timestamp: network.TimeSinceEpoch

    #: The origin this event belongs to.
    origin: str

    #: The Service Worker ID that initiated the event.
    service_worker_registration_id: service_worker.RegistrationID

    #: The Background Service this event belongs to.
    service: ServiceName

    #: A description of the event.
    event_name: str

    #: An identifier that groups related events together.
    instance_id: str

    #: A list of event-specific information.
    event_metadata: typing.List[EventMetadata]

    #: Storage key this event belongs to.
    storage_key: str

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["timestamp"] = self.timestamp.to_json()
        json["origin"] = self.origin
        json[
            "serviceWorkerRegistrationId"
        ] = self.service_worker_registration_id.to_json()
        json["service"] = self.service.to_json()
        json["eventName"] = self.event_name
        json["instanceId"] = self.instance_id
        json["eventMetadata"] = [i.to_json() for i in self.event_metadata]
        json["storageKey"] = self.storage_key
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> BackgroundServiceEvent:
        return cls(
            timestamp=network.TimeSinceEpoch.from_json(json["timestamp"]),
            origin=str(json["origin"]),
            service_worker_registration_id=service_worker.RegistrationID.from_json(
                json["serviceWorkerRegistrationId"]
            ),
            service=ServiceName.from_json(json["service"]),
            event_name=str(json["eventName"]),
            instance_id=str(json["instanceId"]),
            event_metadata=[EventMetadata.from_json(i) for i in json["eventMetadata"]],
            storage_key=str(json["storageKey"]),
        )


def start_observing(
    service: ServiceName,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Enables event updates for the service.

    :param service:
    """
    params: T_JSON_DICT = dict()
    params["service"] = service.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "BackgroundService.startObserving",
        "params": params,
    }
    json = yield cmd_dict


def stop_observing(
    service: ServiceName,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Disables event updates for the service.

    :param service:
    """
    params: T_JSON_DICT = dict()
    params["service"] = service.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "BackgroundService.stopObserving",
        "params": params,
    }
    json = yield cmd_dict


def set_recording(
    should_record: bool, service: ServiceName
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Set the recording state for the service.

    :param should_record:
    :param service:
    """
    params: T_JSON_DICT = dict()
    params["shouldRecord"] = should_record
    params["service"] = service.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "BackgroundService.setRecording",
        "params": params,
    }
    json = yield cmd_dict


def clear_events(
    service: ServiceName,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Clears all stored data for the service.

    :param service:
    """
    params: T_JSON_DICT = dict()
    params["service"] = service.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "BackgroundService.clearEvents",
        "params": params,
    }
    json = yield cmd_dict


@event_class("BackgroundService.recordingStateChanged")
@dataclass
class RecordingStateChanged:
    """
    Called when the recording state for the service has been updated.
    """

    is_recording: bool
    service: ServiceName

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> RecordingStateChanged:
        return cls(
            is_recording=bool(json["isRecording"]),
            service=ServiceName.from_json(json["service"]),
        )


@event_class("BackgroundService.backgroundServiceEventReceived")
@dataclass
class BackgroundServiceEventReceived:
    """
    Called with all existing backgroundServiceEvents when enabled, and all new
    events afterwards if enabled and recording.
    """

    background_service_event: BackgroundServiceEvent

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> BackgroundServiceEventReceived:
        return cls(
            background_service_event=BackgroundServiceEvent.from_json(
                json["backgroundServiceEvent"]
            )
        )
