from abc import ABC, abstractmethod
from datetime import datetime

from date_provider_service import DateProviderService

class DateProviderServiceImpl(DateProviderService):
  def get_now(self):
      return datetime.now()