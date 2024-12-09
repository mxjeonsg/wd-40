import os
import sys

def typeCheck(evalee: any, expected_type: type, msg: str) -> bool:
    DEFAULT_MSG0: str = f"Expected type is %s but %s given." %(str(expected_type), str(type(evalee)))
    DEFAULT_MSG1: str = "Evalee isn't valid; Not provided or None"

    if not evalee:
        raise UnboundLocalError(DEFAULT_MSG1)

    if not type(evalee) == expected_type:
        if not msg:
            raise TypeError(DEFAULT_MSG0)
        else:
            raise TypeError(msg)
    else:
        return True