from abc import ABC, abstractmethod

class BaseConverter(ABC):
    """
    Abstract Base Class for all conversion strategies.
    This fulfills the Dependency Inversion and Single Responsibility principles.
    """
    
    @abstractmethod
    def convert(self, input_path: str, output_path: str):
        """
        Standard method for file conversion.
        Each subclass must implement its own specific logic.
        """
        pass