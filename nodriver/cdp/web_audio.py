# DO NOT EDIT THIS FILE!
#
# This file is generated from the CDP specification. If you need to make
# changes, edit the generator and regenerate all of the modules.
#
# CDP domain: WebAudio (experimental)

from __future__ import annotations

import enum
import typing
from dataclasses import dataclass

from .util import event_class, T_JSON_DICT


class GraphObjectId(str):
    """
    An unique ID for a graph object (AudioContext, AudioNode, AudioParam) in Web Audio API
    """

    def to_json(self) -> str:
        return self

    @classmethod
    def from_json(cls, json: str) -> GraphObjectId:
        return cls(json)

    def __repr__(self):
        return "GraphObjectId({})".format(super().__repr__())


class ContextType(enum.Enum):
    """
    Enum of BaseAudioContext types
    """

    REALTIME = "realtime"
    OFFLINE = "offline"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> ContextType:
        return cls(json)


class ContextState(enum.Enum):
    """
    Enum of AudioContextState from the spec
    """

    SUSPENDED = "suspended"
    RUNNING = "running"
    CLOSED = "closed"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> ContextState:
        return cls(json)


class NodeType(str):
    """
    Enum of AudioNode types
    """

    def to_json(self) -> str:
        return self

    @classmethod
    def from_json(cls, json: str) -> NodeType:
        return cls(json)

    def __repr__(self):
        return "NodeType({})".format(super().__repr__())


class ChannelCountMode(enum.Enum):
    """
    Enum of AudioNode::ChannelCountMode from the spec
    """

    CLAMPED_MAX = "clamped-max"
    EXPLICIT = "explicit"
    MAX_ = "max"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> ChannelCountMode:
        return cls(json)


class ChannelInterpretation(enum.Enum):
    """
    Enum of AudioNode::ChannelInterpretation from the spec
    """

    DISCRETE = "discrete"
    SPEAKERS = "speakers"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> ChannelInterpretation:
        return cls(json)


class ParamType(str):
    """
    Enum of AudioParam types
    """

    def to_json(self) -> str:
        return self

    @classmethod
    def from_json(cls, json: str) -> ParamType:
        return cls(json)

    def __repr__(self):
        return "ParamType({})".format(super().__repr__())


class AutomationRate(enum.Enum):
    """
    Enum of AudioParam::AutomationRate from the spec
    """

    A_RATE = "a-rate"
    K_RATE = "k-rate"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> AutomationRate:
        return cls(json)


@dataclass
class ContextRealtimeData:
    """
    Fields in AudioContext that change in real-time.
    """

    #: The current context time in second in BaseAudioContext.
    current_time: float

    #: The time spent on rendering graph divided by render quantum duration,
    #: and multiplied by 100. 100 means the audio renderer reached the full
    #: capacity and glitch may occur.
    render_capacity: float

    #: A running mean of callback interval.
    callback_interval_mean: float

    #: A running variance of callback interval.
    callback_interval_variance: float

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["currentTime"] = self.current_time
        json["renderCapacity"] = self.render_capacity
        json["callbackIntervalMean"] = self.callback_interval_mean
        json["callbackIntervalVariance"] = self.callback_interval_variance
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> ContextRealtimeData:
        return cls(
            current_time=float(json["currentTime"]),
            render_capacity=float(json["renderCapacity"]),
            callback_interval_mean=float(json["callbackIntervalMean"]),
            callback_interval_variance=float(json["callbackIntervalVariance"]),
        )


@dataclass
class BaseAudioContext:
    """
    Protocol object for BaseAudioContext
    """

    context_id: GraphObjectId

    context_type: ContextType

    context_state: ContextState

    #: Platform-dependent callback buffer size.
    callback_buffer_size: float

    #: Number of output channels supported by audio hardware in use.
    max_output_channel_count: float

    #: Context sample rate.
    sample_rate: float

    realtime_data: typing.Optional[ContextRealtimeData] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["contextId"] = self.context_id.to_json()
        json["contextType"] = self.context_type.to_json()
        json["contextState"] = self.context_state.to_json()
        json["callbackBufferSize"] = self.callback_buffer_size
        json["maxOutputChannelCount"] = self.max_output_channel_count
        json["sampleRate"] = self.sample_rate
        if self.realtime_data is not None:
            json["realtimeData"] = self.realtime_data.to_json()
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> BaseAudioContext:
        return cls(
            context_id=GraphObjectId.from_json(json["contextId"]),
            context_type=ContextType.from_json(json["contextType"]),
            context_state=ContextState.from_json(json["contextState"]),
            callback_buffer_size=float(json["callbackBufferSize"]),
            max_output_channel_count=float(json["maxOutputChannelCount"]),
            sample_rate=float(json["sampleRate"]),
            realtime_data=ContextRealtimeData.from_json(json["realtimeData"])
            if json.get("realtimeData", None) is not None
            else None,
        )


@dataclass
class AudioListener:
    """
    Protocol object for AudioListener
    """

    listener_id: GraphObjectId

    context_id: GraphObjectId

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["listenerId"] = self.listener_id.to_json()
        json["contextId"] = self.context_id.to_json()
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> AudioListener:
        return cls(
            listener_id=GraphObjectId.from_json(json["listenerId"]),
            context_id=GraphObjectId.from_json(json["contextId"]),
        )


@dataclass
class AudioNode:
    """
    Protocol object for AudioNode
    """

    node_id: GraphObjectId

    context_id: GraphObjectId

    node_type: NodeType

    number_of_inputs: float

    number_of_outputs: float

    channel_count: float

    channel_count_mode: ChannelCountMode

    channel_interpretation: ChannelInterpretation

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["nodeId"] = self.node_id.to_json()
        json["contextId"] = self.context_id.to_json()
        json["nodeType"] = self.node_type.to_json()
        json["numberOfInputs"] = self.number_of_inputs
        json["numberOfOutputs"] = self.number_of_outputs
        json["channelCount"] = self.channel_count
        json["channelCountMode"] = self.channel_count_mode.to_json()
        json["channelInterpretation"] = self.channel_interpretation.to_json()
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> AudioNode:
        return cls(
            node_id=GraphObjectId.from_json(json["nodeId"]),
            context_id=GraphObjectId.from_json(json["contextId"]),
            node_type=NodeType.from_json(json["nodeType"]),
            number_of_inputs=float(json["numberOfInputs"]),
            number_of_outputs=float(json["numberOfOutputs"]),
            channel_count=float(json["channelCount"]),
            channel_count_mode=ChannelCountMode.from_json(json["channelCountMode"]),
            channel_interpretation=ChannelInterpretation.from_json(
                json["channelInterpretation"]
            ),
        )


@dataclass
class AudioParam:
    """
    Protocol object for AudioParam
    """

    param_id: GraphObjectId

    node_id: GraphObjectId

    context_id: GraphObjectId

    param_type: ParamType

    rate: AutomationRate

    default_value: float

    min_value: float

    max_value: float

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["paramId"] = self.param_id.to_json()
        json["nodeId"] = self.node_id.to_json()
        json["contextId"] = self.context_id.to_json()
        json["paramType"] = self.param_type.to_json()
        json["rate"] = self.rate.to_json()
        json["defaultValue"] = self.default_value
        json["minValue"] = self.min_value
        json["maxValue"] = self.max_value
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> AudioParam:
        return cls(
            param_id=GraphObjectId.from_json(json["paramId"]),
            node_id=GraphObjectId.from_json(json["nodeId"]),
            context_id=GraphObjectId.from_json(json["contextId"]),
            param_type=ParamType.from_json(json["paramType"]),
            rate=AutomationRate.from_json(json["rate"]),
            default_value=float(json["defaultValue"]),
            min_value=float(json["minValue"]),
            max_value=float(json["maxValue"]),
        )


def enable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Enables the WebAudio domain and starts sending context lifetime events.
    """
    cmd_dict: T_JSON_DICT = {
        "method": "WebAudio.enable",
    }
    json = yield cmd_dict


def disable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Disables the WebAudio domain.
    """
    cmd_dict: T_JSON_DICT = {
        "method": "WebAudio.disable",
    }
    json = yield cmd_dict


def get_realtime_data(
    context_id: GraphObjectId,
) -> typing.Generator[T_JSON_DICT, T_JSON_DICT, ContextRealtimeData]:
    """
    Fetch the realtime data from the registered contexts.

    :param context_id:
    :returns:
    """
    params: T_JSON_DICT = dict()
    params["contextId"] = context_id.to_json()
    cmd_dict: T_JSON_DICT = {
        "method": "WebAudio.getRealtimeData",
        "params": params,
    }
    json = yield cmd_dict
    return ContextRealtimeData.from_json(json["realtimeData"])


@event_class("WebAudio.contextCreated")
@dataclass
class ContextCreated:
    """
    Notifies that a new BaseAudioContext has been created.
    """

    context: BaseAudioContext

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> ContextCreated:
        return cls(context=BaseAudioContext.from_json(json["context"]))


@event_class("WebAudio.contextWillBeDestroyed")
@dataclass
class ContextWillBeDestroyed:
    """
    Notifies that an existing BaseAudioContext will be destroyed.
    """

    context_id: GraphObjectId

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> ContextWillBeDestroyed:
        return cls(context_id=GraphObjectId.from_json(json["contextId"]))


@event_class("WebAudio.contextChanged")
@dataclass
class ContextChanged:
    """
    Notifies that existing BaseAudioContext has changed some properties (id stays the same)..
    """

    context: BaseAudioContext

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> ContextChanged:
        return cls(context=BaseAudioContext.from_json(json["context"]))


@event_class("WebAudio.audioListenerCreated")
@dataclass
class AudioListenerCreated:
    """
    Notifies that the construction of an AudioListener has finished.
    """

    listener: AudioListener

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> AudioListenerCreated:
        return cls(listener=AudioListener.from_json(json["listener"]))


@event_class("WebAudio.audioListenerWillBeDestroyed")
@dataclass
class AudioListenerWillBeDestroyed:
    """
    Notifies that a new AudioListener has been created.
    """

    context_id: GraphObjectId
    listener_id: GraphObjectId

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> AudioListenerWillBeDestroyed:
        return cls(
            context_id=GraphObjectId.from_json(json["contextId"]),
            listener_id=GraphObjectId.from_json(json["listenerId"]),
        )


@event_class("WebAudio.audioNodeCreated")
@dataclass
class AudioNodeCreated:
    """
    Notifies that a new AudioNode has been created.
    """

    node: AudioNode

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> AudioNodeCreated:
        return cls(node=AudioNode.from_json(json["node"]))


@event_class("WebAudio.audioNodeWillBeDestroyed")
@dataclass
class AudioNodeWillBeDestroyed:
    """
    Notifies that an existing AudioNode has been destroyed.
    """

    context_id: GraphObjectId
    node_id: GraphObjectId

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> AudioNodeWillBeDestroyed:
        return cls(
            context_id=GraphObjectId.from_json(json["contextId"]),
            node_id=GraphObjectId.from_json(json["nodeId"]),
        )


@event_class("WebAudio.audioParamCreated")
@dataclass
class AudioParamCreated:
    """
    Notifies that a new AudioParam has been created.
    """

    param: AudioParam

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> AudioParamCreated:
        return cls(param=AudioParam.from_json(json["param"]))


@event_class("WebAudio.audioParamWillBeDestroyed")
@dataclass
class AudioParamWillBeDestroyed:
    """
    Notifies that an existing AudioParam has been destroyed.
    """

    context_id: GraphObjectId
    node_id: GraphObjectId
    param_id: GraphObjectId

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> AudioParamWillBeDestroyed:
        return cls(
            context_id=GraphObjectId.from_json(json["contextId"]),
            node_id=GraphObjectId.from_json(json["nodeId"]),
            param_id=GraphObjectId.from_json(json["paramId"]),
        )


@event_class("WebAudio.nodesConnected")
@dataclass
class NodesConnected:
    """
    Notifies that two AudioNodes are connected.
    """

    context_id: GraphObjectId
    source_id: GraphObjectId
    destination_id: GraphObjectId
    source_output_index: typing.Optional[float]
    destination_input_index: typing.Optional[float]

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> NodesConnected:
        return cls(
            context_id=GraphObjectId.from_json(json["contextId"]),
            source_id=GraphObjectId.from_json(json["sourceId"]),
            destination_id=GraphObjectId.from_json(json["destinationId"]),
            source_output_index=float(json["sourceOutputIndex"])
            if json.get("sourceOutputIndex", None) is not None
            else None,
            destination_input_index=float(json["destinationInputIndex"])
            if json.get("destinationInputIndex", None) is not None
            else None,
        )


@event_class("WebAudio.nodesDisconnected")
@dataclass
class NodesDisconnected:
    """
    Notifies that AudioNodes are disconnected. The destination can be null, and it means all the outgoing connections from the source are disconnected.
    """

    context_id: GraphObjectId
    source_id: GraphObjectId
    destination_id: GraphObjectId
    source_output_index: typing.Optional[float]
    destination_input_index: typing.Optional[float]

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> NodesDisconnected:
        return cls(
            context_id=GraphObjectId.from_json(json["contextId"]),
            source_id=GraphObjectId.from_json(json["sourceId"]),
            destination_id=GraphObjectId.from_json(json["destinationId"]),
            source_output_index=float(json["sourceOutputIndex"])
            if json.get("sourceOutputIndex", None) is not None
            else None,
            destination_input_index=float(json["destinationInputIndex"])
            if json.get("destinationInputIndex", None) is not None
            else None,
        )


@event_class("WebAudio.nodeParamConnected")
@dataclass
class NodeParamConnected:
    """
    Notifies that an AudioNode is connected to an AudioParam.
    """

    context_id: GraphObjectId
    source_id: GraphObjectId
    destination_id: GraphObjectId
    source_output_index: typing.Optional[float]

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> NodeParamConnected:
        return cls(
            context_id=GraphObjectId.from_json(json["contextId"]),
            source_id=GraphObjectId.from_json(json["sourceId"]),
            destination_id=GraphObjectId.from_json(json["destinationId"]),
            source_output_index=float(json["sourceOutputIndex"])
            if json.get("sourceOutputIndex", None) is not None
            else None,
        )


@event_class("WebAudio.nodeParamDisconnected")
@dataclass
class NodeParamDisconnected:
    """
    Notifies that an AudioNode is disconnected to an AudioParam.
    """

    context_id: GraphObjectId
    source_id: GraphObjectId
    destination_id: GraphObjectId
    source_output_index: typing.Optional[float]

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> NodeParamDisconnected:
        return cls(
            context_id=GraphObjectId.from_json(json["contextId"]),
            source_id=GraphObjectId.from_json(json["sourceId"]),
            destination_id=GraphObjectId.from_json(json["destinationId"]),
            source_output_index=float(json["sourceOutputIndex"])
            if json.get("sourceOutputIndex", None) is not None
            else None,
        )
