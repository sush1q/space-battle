import pytest
from server.interfaces import *
from server.exception_handler import *
from server.event_loop import *


@pytest.mark.parametrize(
    'strategy, exceptions', [
            (
                {
                'Move': {
                        'KeyError': RepeatCommand
                        },
                'RepeatCommand': {
                        'KeyError': ExceptionLogger
                        }
                },
                ['RepeatCommand', 'ExceptionLogger']
                
            ), (
                {
                'Move': {
                        'KeyError': RepeatCommand
                        },
                'RepeatCommand': {
                        'KeyError': DoubleRepeatCommand
                        },
                'DoubleRepeatCommand': {
                        'KeyError': ExceptionLogger
                        }
                },
                ['RepeatCommand', 'DoubleRepeatCommand', 'ExceptionLogger']
            )
    ]
)
def test_exception(strategy, exceptions):
    Strategy.store = strategy
    ExceptionHandler.store = Strategy

    obj = UObject(
        {
            'velocity': Point(-7, 3)
        }
    )
    moveable_obj = MoveableAdapter(obj)
    move = Move(moveable_obj)
    EventLoop.put(move)

    for err in exceptions:
        try:
            cmd = EventLoop.get()
            cmd()
        except Exception as exception:
            cmd_ex = ExceptionHandler.handle(exception, cmd)
            assert type(cmd_ex).__name__ == err
            EventLoop.put(cmd_ex)
