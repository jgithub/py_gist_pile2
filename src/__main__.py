from date.date_provider_service import DateProviderService
from date.date_provider_service_impl import DateProviderServiceImpl
from greeting.greeting_provider_service import GreetingProviderService
from greeting.greeting_provider_service_impl import GreetingProviderServiceImpl
from log.get_logger import get_logger
from log.log_util import d4l
LOG = get_logger("main.py")


def main():
  # ----
  # Bind all the global singleton services
  # ----
  date_provider_service: DateProviderService = DateProviderServiceImpl()

  # Dependency Injection.   
  # GreetingProviderServiceImpl depends on knowing what time it is
  # which is why an object that implements the DateProviderService is passed to it
  greeting_provider_service: GreetingProviderService = GreetingProviderServiceImpl(date_provider_service)
  
  # ----
  # Done binding all the global singleton services
  # ----
  
  
  LOG.notice(f"main(): I will greet you with: {d4l(greeting_provider_service.get_greeting())}")
  print(f"{greeting_provider_service.get_greeting()}")


if __name__ == '__main__':
  LOG.debug("Found __name__ == '__main__'")
  # execute only if run as a script
  main()