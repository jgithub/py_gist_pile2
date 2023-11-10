from abc import ABC, abstractmethod

class GreetingProviderService(ABC):
  @abstractmethod
  def get_greeting(self) -> str:
      pass