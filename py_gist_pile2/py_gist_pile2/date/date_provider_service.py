from abc import ABC, abstractmethod
from datetime import datetime

class DateProviderService(ABC):
  @abstractmethod
  def get_now(self):
      pass