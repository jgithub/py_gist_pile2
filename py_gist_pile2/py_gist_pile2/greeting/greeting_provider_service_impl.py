from abc import ABC, abstractmethod
from datetime import datetime
from date.date_provider_service import DateProviderService
from greeting.greeting_provider_service import GreetingProviderService
from log.get_logger import get_logger
from log.log_util import d4l


LOG = get_logger("greeting.GreetingProviderServiceImpl")
class GreetingProviderServiceImpl(GreetingProviderService):
  # Any dependencies this class needs are passed in 
  # at construction time (Dependency injection)
  # rather than grabbed from the outside world via some import
  # (ie some random import)
  # This changes how  testing is done.   Mocks have a much less
  # significant presence with this approach.  No overmocking
  def __init__(self, date_provider_service: DateProviderService):
      self.date_provider_service = date_provider_service

  def _is_morning_afternoon_or_evening(self) -> bool: 
    # "Why not use use datetime.now() here?  This seems like overkill"
    # No, it's not.
    # This is good for testability, separation of concerns,
    # Creating tasks that can be performed concurrently
    
    # Toggle which of these two lines is commented
    # out and perform a `make test` again
    # Depending on time of day there is an 
    # intermittent chance of a test failure 


    # ------8<-----------------
    # ```
    # user@MacBook-Pro py-gist-pile % make test
    # cd /Users/user/project/py-gist-pile && PYTHONPATH="./py_gist_pile2:./py_gist_pile2/date:./py_gist_pile2/greeting" LOG_PREPEND_TIMESTAMP=1 LOG_DEBUG=1 python3 -m unittest discover -v
    # test_does_this_work (test.date.test_date_provider_service.TestDateProvider.test_does_this_work) ... ok
    # test_greeting_provider_service (test.greeting.test_greeting_provider_service.TestGreetingProviderService.test_greeting_provider_service) ... Wed, 08 Nov 2023 16:23:37 UTC [ DEBUG] greeting.GreetingProviderServiceImpl The hour is 16
    # FAIL
    # test_greeting_provider_service_agnostic_of_date (test.greeting.test_greeting_provider_service.TestGreetingProviderService.test_greeting_provider_service_agnostic_of_date) ... ok

    # ======================================================================
    # FAIL: test_greeting_provider_service (test.greeting.test_greeting_provider_service.TestGreetingProviderService.test_greeting_provider_service)
    # ----------------------------------------------------------------------
    # Traceback (most recent call last):
    #   File "/Users/user/project/py-gist-pile/test/greeting/test_greeting_provider_service.py", line 16, in test_greeting_provider_service
    #     self.assertEqual(greeting_provider_service.get_greeting(), "Good morning.")
    # AssertionError: 'Good afternoon.' != 'Good morning.'
    # - Good afternoon.
    # + Good morning.
    # ```
    # ------>8-----------------


    # ----------------------------------------------------------------------
    # Ran 3 tests in 0.001s

    # FAILED (failures=1)
    # make: *** [test] Error 1

    # now: datetime = datetime.now()
    now: datetime = self.date_provider_service.get_now()
    
    
    hour = now.hour
    LOG.debug(f"The hour is {d4l(hour)}")
    
    if hour < 12:
        return "morning"
    elif hour < 17:
        return "afternoon"
    else:
        return "evening"   


  def get_greeting(self) -> str:
    return f"Good {self._is_morning_afternoon_or_evening()}."
      