# presidio_anonymizer/operators/initial.py
"""MIMIC OF REDACT OPERATOR TO FOCUS ON INVOCATION"""

from typing import Dict
from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    """Operator that converts words into initials"""

    def operate(self, text: str = None, params: Dict = None) -> str:
        if not text:
            return ""
        
        words = [w for w in text.split() if w]
        
        initials = []
        
        for word in words:
            prefix = ""
            initial_char = ""
            
            for char in word:
                if char.isalnum():
                    initial_char = char.upper()
                    break
                else:
                    prefix += char
                
            if not initial_char and word:
                initial_char = word[0].upper()   
        
            initials.append(f"{prefix}{initial_char}.")
            
        return " ".join(initials)


    def validate(self, params: Dict = None) -> None:
        pass

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize