# presidio_anonymizer/operators/initial.py
"""MIMIC OF REDACT OPERATOR TO FOCUS ON INVOCATION"""

from typing import Dict
from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    """Operator that converts words into initials"""

    def operate(self, text: str = None, params: Dict = None) -> str:
        if not text:
            return ""
        words = text.split()
        initials = []
        for word in words:
            for char in word:
                if char.isalnum():
                    initials.append(f"{char.upper()}.")
                    break
            else:
                initials.append(f"{word[0].upper()}.")
        return " ".join(initials)


    def validate(self, params: Dict = None) -> None:
        pass

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize