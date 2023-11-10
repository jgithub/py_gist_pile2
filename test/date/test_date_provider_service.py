from abc import ABC, abstractmethod
from date_provider_service_always_epoch_impl import DateProviderServiceAlwaysEpochImpl
import os
from datetime import datetime
os.environ['TZ'] = 'Europe/London'

import unittest;
# sys.path.append(path) 
# from ../../src/date/date_provider_service import DateProviderService
# from date_provider_service import DateProviderService
from datetime import datetime

class TestDateProvider(unittest.TestCase):
  def test_does_this_work(self):
    date_provider_service = DateProviderServiceAlwaysEpochImpl()
    self.assertEqual(date_provider_service.get_now(), datetime(1970, 1, 1, 1, 0))

if __name__ == '__main__':
    unittest.main()