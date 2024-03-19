import dataclasses
from typing import List, Tuple
import datetime

from typing import Optional


@dataclasses.dataclass
class EnvironmentEntity:
    """A entity that exists in the environment, such as people, objects, concepts, places, etc."""
    name: str
    description: str


@dataclasses.dataclass
class AchievedState:
    """The state that an entity entered. For example if we booked a flight, the entity would be
     the flight, and the achieved state would be a statement like "The flight is booked."
    """
    entity: EnvironmentEntity
    state_description: str


@dataclasses.dataclass
class Action:
    """An action that was taken, which potentially changed the achieved state of an entity."""
    action_name: str
    action_description: str
    action_duration_millis: Optional[datetime.timedelta]


@dataclasses.dataclass
class ActionEdge:
    """An edge representation of an Action in the Graph of Actions"""
    action: Action
    resulting_node: Optional['StateNode']


@dataclasses.dataclass
class StateNode:
    """A node representation of AchievedSTate in the Graph of Actions"""
    node_id: str
    achieved_state: AchievedState
    actions_edges: List[ActionEdge]

    def __hash__(self) -> int:
        return self.node_id.__hash__()
