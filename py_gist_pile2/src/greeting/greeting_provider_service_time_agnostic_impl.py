from abc import ABC, abstractmethod
from datetime import datetime
from greeting.greeting_provider_service import GreetingProviderService
from log.get_logger import get_logger


LOG = get_logger("greeting.GreetingProviderServiceTimeAgnosticImpl")
class GreetingProviderServiceTimeAgnosticImpl(GreetingProviderService):
  # Note that this version does NOT have any dependency on DateProviderService
  # So no need to pass it into the constructor as is the case with the default
  # GreetingProviderServiceImpl
  def __init__(self):
    pass 


  def get_greeting(self) -> str:
    return f"Hello."
      