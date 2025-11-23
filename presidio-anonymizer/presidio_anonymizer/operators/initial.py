# presidio_anonymizer/operators/initial.py
"""MIMIC OF REDACT OPERATOR TO FOCUS ON INVOCATION"""

from typing import Dict
from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    """Minimal operator to verify integration."""

    def operate(self, text: str = None, params: Dict = None) -> str:
        """
        Minimal implementation.
        Returns the input text unchanged (placeholder for now).
        """
        return text or ""

    def validate(self, params: Dict = None) -> None:
        """No parameters required, no validation needed."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize
