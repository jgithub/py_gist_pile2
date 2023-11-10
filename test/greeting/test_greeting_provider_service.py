from abc import ABC, abstractmethod
from date_provider_service import DateProviderService
from date_provider_service_always_epoch_impl import DateProviderServiceAlwaysEpochImpl
from greeting.greeting_provider_service_time_agnostic_impl import GreetingProviderServiceTimeAgnosticImpl
from greeting_provider_service_impl import GreetingProviderServiceImpl
import os
from datetime import datetime
os.environ['TZ'] = 'Europe/London'

import unittest;

class TestGreetingProviderService(unittest.TestCase):
  def test_greeting_provider_service(self):
    date_provider_service: DateProviderService = DateProviderServiceAlwaysEpochImpl()
    greeting_provider_service = GreetingProviderServiceImpl(date_provider_service)
    self.assertEqual(greeting_provider_service.get_greeting(), "Good morning.")

  def test_greeting_provider_service_agnostic_of_date(self):
    greeting_provider_service = GreetingProviderServiceTimeAgnosticImpl()
    self.assertEqual(greeting_provider_service.get_greeting(), "Hello.")


if __name__ == '__main__':
    unittest.main()