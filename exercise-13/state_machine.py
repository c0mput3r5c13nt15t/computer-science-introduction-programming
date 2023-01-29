from dataclasses import dataclass, field
from enum import Enum, auto
from abc import ABC, abstractmethod
from typing import Generic, Iterable, TypeVar


class MyState(Enum):
    INIT = auto()
    ACC_ONCE = auto()
    ACC_ONCE_SCREEN_ON = auto()
    LIGHT_ON = auto()
    LIGHT_ON_ACC_ONE = auto()
    TAB_ONCE = auto()
    TAB_ONCE_LIGHT_ON = auto()
    SCREEN_ON = auto()
    SCREEN_ON_TAB_ONCE = auto()
    SCREEN_LIGHT_ON = auto()
    SCREEN_LIGHT_ON_ACC_ONCE = auto()
    SCREEN_LIGHT_ON_TAB_ONCE = auto()


def next_state(self, state: MyState, input: str) -> MyState:
    if input == "SENS_ACC":
        if state is MyState.ACC_ONCE:
            return MyState.LIGHT_ON
        elif state is MyState.ACC_ONCE_SCREEN_ON:
            return MyState.SCREEN_LIGHT_ON
        elif state is MyState.LIGHT_ON:
            return MyState.LIGHT_ON_ACC_ONE
        elif state is MyState.SCREEN_LIGHT_ON:
            return MyState.SCREEN_LIGHT_ON_ACC_ONCE
        elif state is MyState.SCREEN_LIGHT_ON_ACC_ONCE:
            return MyState.SCREEN_ON
        else:
            return MyState.INIT
    elif input == "SENS_TAP":
        if state is MyState.TAB_ONCE:
            return MyState.SCREEN_ON
        elif state is MyState.TAB_ONCE_LIGHT_ON:
            return MyState.SCREEN_LIGHT_ON
        elif state is MyState.SCREEN_ON:
            return MyState.SCREEN_ON_TAB_ONCE
        elif state is MyState.SCREEN_LIGHT_ON_TAB_ONCE:
            return MyState.LIGHT_ON
        elif state is MyState.SCREEN_LIGHT_ON:
            return MyState.SCREEN_LIGHT_ON_TAB_ONCE
        else:
            return MyState.INIT
    return self


# Cleaner and more generic implementation


INP = TypeVar('INP')
OUT = TypeVar('OUT')


class S(Enum):  # Separate definition because no extra states are needed
    INIT = auto()
    LIGHT_ON = auto()
    SCREEN_ON = auto()
    SCREEN_LIGHT_ON = auto()


allowed_inputs = ["SENS_TAB", "SENS_ACC"]
state_translate: dict[tuple[bool, bool], S] = {  # (light?, screen?): state
    (False, False): S.INIT,
    (False, True): S.SCREEN_ON,
    (True, False): S.LIGHT_ON,
    (True, True): S.SCREEN_LIGHT_ON
}


@dataclass
class State(Generic[INP, OUT], ABC):
    def next(self, input: INP) -> 'State':
        return self

    @abstractmethod
    def output(self) -> OUT:
        ...


@dataclass
class S_Init(State[str, S]):
    def next(self, input: str) -> State[str, S]:
        return CombinedState(S_After(input, "SENS_ACC"), S_After(input, "SENS_TAB"))

    def output(self) -> str:
        return ""


@dataclass
class S_After(State[str, bool]):
    __lastAction: str
    __activateAction: str
    __on: bool = field(default=False)

    def next(self, input: str) -> State[str, bool]:
        if input == self.__lastAction == self.__activateAction:
            return S_After("", self.__activateAction, not self.__on)
        else:
            if input in allowed_inputs:
                return S_After(input, self.__activateAction, self.__on)
            else:
                return S_After(self.__lastAction, self.__activateAction, self.__on)

    def output(self) -> bool:
        return self.__on


@dataclass
class CombinedState(State[str, S]):
    light: State[str, bool]
    screen: State[str, bool]

    def next(self, input: str) -> State[str, S]:
        self.light = self.light.next(input)
        self.screen = self.screen.next(input)
        return self

    def output(self) -> S:
        out_light = self.light.output()
        out_screen = self.screen.output()

        return state_translate[(out_light, out_screen)]


def automaton(input: Iterable[str]):
    state: State[str, S] = S_Init()
    for x in input:
        state = state.next(x)
        yield state.output()


if __name__ == "__main__":
    assert list(automaton(["SENS_ACC", "SENS_ACC"])) == [
        S.INIT, S.LIGHT_ON]
    assert list(automaton(["SENS_ACC", "SENS_ACC", "SENS_ACC"])) == [
        S.INIT, S.LIGHT_ON, S.LIGHT_ON]
    assert list(automaton(["SENS_ACC", "SENS_ACC", "SENS_ACC", "SENS_TAB"])) == [
        S.INIT, S.LIGHT_ON, S.LIGHT_ON, S.LIGHT_ON]
    assert list(automaton(["SENS_TAB", "SENS_TAB"])) == [
        S.INIT, S.SCREEN_ON]
    assert list(automaton(["SENS_TAB", "SENS_TAB", "SENS_TAB", "SENS_ACC"])) == [
        S.INIT, S.SCREEN_ON, S.SCREEN_ON, S.SCREEN_ON]
    assert list(automaton(["SENS_ACC", "SENS_ACC", "SENS_TAB", "SENS_TAB"])) == [
        S.INIT, S.LIGHT_ON, S.LIGHT_ON, S.SCREEN_LIGHT_ON]
    assert list(automaton(["SENS_ACC", "SENS_ACC", "SENS_TAB", "invalid input", "SENS_TAB"])) == [
        S.INIT, S.LIGHT_ON, S.LIGHT_ON, S.LIGHT_ON, S.SCREEN_LIGHT_ON]

    # Initialize state machine with a specific state
    assert list(automaton(["SENS_ACC", "SENS_ACC"])) == [
        S.INIT, S.LIGHT_ON]
