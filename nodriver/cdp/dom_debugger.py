# DO NOT EDIT THIS FILE!
#
# This file is generated from the CDP specification. If you need to make
# changes, edit the generator and regenerate all of the modules.
#
# CDP domain: DOMDebugger

from __future__ import annotations

import enum
import typing
from dataclasses import dataclass

from deprecated.sphinx import deprecated  # type: ignore

from . import dom
from . import runtime
from .util import T_JSON_DICT


class DOMBreakpointType(enum.Enum):
    """
    DOM breakpoint type.
    """

    SUBTREE_MODIFIED = "subtree-modified"
    ATTRIBUTE_MODIFIED = "attribute-modified"
    NODE_REMOVED = "node-removed"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> DOMBreakpointType:
        return cls(json)


class CSPViolationType(enum.Enum):
    """
    CSP Violation type.
    """

    TRUSTEDTYPE_SINK_VIOLATION = "trustedtype-sink-violation"
    TRUSTEDTYPE_POLICY_VIOLATION = "trustedtype-policy-violation"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> CSPViolationType:
        return cls(json)


@dataclass
class EventListener:
    """
    Object event listener.
    """

    #: ``EventListener``'s type.
    type_: str

    #: ``EventListener``'s useCapture.
    use_capture: bool

    #: ``EventListener``'s passive flag.
    passive: bool

    #: ``EventListener``'s once flag.
    once: bool

    #: Script id of the handler code.
    script_id: runtime.ScriptId

    #: Line number in the script (0-based).
    line_number: int

    #: Column number in the script (0-based).
    column_number: int

    #: Event handler function value.
    handler: typing.Optional[runtime.RemoteObject] = None

    #: Event original handler function value.
    original_handler: typing.Optional[runtime.RemoteObject] = None

    #: Node the listener is added to (if any).
    backend_node_id: typing.Optional[dom.BackendNodeId] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["type"] = self.type_
        json["useCapture"] = self.use_capture
        json["passive"] = self.passive
        json["once"] = self.once
        json["scriptId"] = self.script_id.to_json()
        json["lineNumber"] = self.line_number
        json["columnNumber"] = self.column_number
        if self.handler is not None:
            json["handler"] = self.handler.to_json()
        if self.original_handler is not None:
            json["originalHandler"] = self.original_handler.to_json()
        if self.backend_node_id is not None:
            json["backendNodeId"] = self.backend_node_id.to_json()
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> EventListener:
        return cls(
            type_=str(json["type"]),
            use_capture=bool(json["useCapture"]),
            passive=bool(json["passive"]),
            once=bool(json["once"]),
            script_id=runtime.ScriptId.from_json(json["scriptId"]),
            line_number=int(json["lineNumber"]),
            column_number=int(json["columnNumber"]),
            handler=runtime.RemoteObject.from_json(json["handler"])
            if json.get("handler", None) is not None
            else None,
            original_handler=runtime.RemoteObject.from_json(json["originalHandler"])
            if json.get("originalHandler", None) is not None
            else None,
            backend_node_id=dom.BackendNodeId.from_json(json["backendNodeId"])
            if json.get("backendNodeId", None) is not None
            else None,
        )


def get_event_listeners(
    object_id: runtime.RemoteObjectId,
    depth: typing.Optional[int] = None,
    pierce: typing.Optional[bool] = None,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, typing.List[EventListener]]:
    """
    Returns event listeners of the given object.

    :param object_id: Identifier of the object to return listeners for.
    :param depth: *(Optional)* The maximum depth at which Node children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
    :param pierce: *(Optional)* Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false). Reports listeners for all contexts if pierce is enabled.
    :returns: Array of relevant listeners.
    """
    params: T_JSON_DICT = dict()
    params["objectId"] = object_id.to_json()
    if depth is not None:
        params["depth"] = depth
    if pierce is not None:
        params["pierce"] = pierce
    cmd_dict: T_JSON_DICT = {
        "method": "DOMDebugger.getEventListeners",
        "params": params,
    }
    json = yield cmd_dict
    return [EventListener.from_json(i) for i in json["listeners"]]


def remove_dom_breakpoint(
    node_id: dom.NodeId, type_: DOMBreakpointType
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Removes DOM breakpoint that was set using ``setDOMBreakpoint``.

    :param node_id: Identifier of the node to remove breakpoint from.
    :param type_: Type of the breakpoint to remove.
    """
    params: T_JSON_DICT = dict()
    params["nodeId"] = node_id.to_json()
    params["type"] = type_.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "DOMDebugger.removeDOMBreakpoint",
        "params": params,
    }
    json = yield cmd_dict


def remove_event_listener_breakpoint(
    event_name: str, target_name: typing.Optional[str] = None
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Removes breakpoint on particular DOM event.

    :param event_name: Event name.
    :param target_name: **(EXPERIMENTAL)** *(Optional)* EventTarget interface name.
    """
    params: T_JSON_DICT = dict()
    params["eventName"] = event_name
    if target_name is not None:
        params["targetName"] = target_name
    cmd_dict: T_JSON_DICT = {
        "method": "DOMDebugger.removeEventListenerBreakpoint",
        "params": params,
    }
    json = yield cmd_dict


@deprecated(version="1.3")
def remove_instrumentation_breakpoint(
    event_name: str,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Removes breakpoint on particular native event.

    .. deprecated:: 1.3

    **EXPERIMENTAL**

    :param event_name: Instrumentation name to stop on.
    """
    params: T_JSON_DICT = dict()
    params["eventName"] = event_name
    cmd_dict: T_JSON_DICT = {
        "method": "DOMDebugger.removeInstrumentationBreakpoint",
        "params": params,
    }
    json = yield cmd_dict


def remove_xhr_breakpoint(url: str) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Removes breakpoint from XMLHttpRequest.

    :param url: Resource URL substring.
    """
    params: T_JSON_DICT = dict()
    params["url"] = url
    cmd_dict: T_JSON_DICT = {
        "method": "DOMDebugger.removeXHRBreakpoint",
        "params": params,
    }
    json = yield cmd_dict


def set_break_on_csp_violation(
    violation_types: typing.List[CSPViolationType],
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Sets breakpoint on particular CSP violations.

    **EXPERIMENTAL**

    :param violation_types: CSP Violations to stop upon.
    """
    params: T_JSON_DICT = dict()
    params["violationTypes"] = [i.to_json() for i in violation_types]
    cmd_dict: T_JSON_DICT = {
        "method": "DOMDebugger.setBreakOnCSPViolation",
        "params": params,
    }
    json = yield cmd_dict


def set_dom_breakpoint(
    node_id: dom.NodeId, type_: DOMBreakpointType
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Sets breakpoint on particular operation with DOM.

    :param node_id: Identifier of the node to set breakpoint on.
    :param type_: Type of the operation to stop upon.
    """
    params: T_JSON_DICT = dict()
    params["nodeId"] = node_id.to_json()
    params["type"] = type_.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "DOMDebugger.setDOMBreakpoint",
        "params": params,
    }
    json = yield cmd_dict


def set_event_listener_breakpoint(
    event_name: str, target_name: typing.Optional[str] = None
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Sets breakpoint on particular DOM event.

    :param event_name: DOM Event name to stop on (any DOM event will do).
    :param target_name: **(EXPERIMENTAL)** *(Optional)* EventTarget interface name to stop on. If equal to ```"*"``` or not provided, will stop on any EventTarget.
    """
    params: T_JSON_DICT = dict()
    params["eventName"] = event_name
    if target_name is not None:
        params["targetName"] = target_name
    cmd_dict: T_JSON_DICT = {
        "method": "DOMDebugger.setEventListenerBreakpoint",
        "params": params,
    }
    json = yield cmd_dict


@deprecated(version="1.3")
def set_instrumentation_breakpoint(
    event_name: str,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Sets breakpoint on particular native event.

    .. deprecated:: 1.3

    **EXPERIMENTAL**

    :param event_name: Instrumentation name to stop on.
    """
    params: T_JSON_DICT = dict()
    params["eventName"] = event_name
    cmd_dict: T_JSON_DICT = {
        "method": "DOMDebugger.setInstrumentationBreakpoint",
        "params": params,
    }
    json = yield cmd_dict


def set_xhr_breakpoint(url: str) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Sets breakpoint on XMLHttpRequest.

    :param url: Resource URL substring. All XHRs having this substring in the URL will get stopped upon.
    """
    params: T_JSON_DICT = dict()
    params["url"] = url
    cmd_dict: T_JSON_DICT = {
        "method": "DOMDebugger.setXHRBreakpoint",
        "params": params,
    }
    json = yield cmd_dict
