* https://stackoverflow.com/questions/1732438/how-do-i-run-all-python-unit-tests-in-a-directory

* I personally use this in the Typescript world all the time: https://github.com/jgithub/ts-gist-pile/

* This library, here, is my first python attempt at a similar thing
* Thus far is demonstrates "program to an interface" and dependency injection patterns that I am a fan of
* I assume that this is "not the Python way"
* Much of what's in https://github.com/jgithub/ts-gist-pile/ is "not the javascript way" either but I think it's crazy valuable
* TODO: solve this: "py-gist-pile does not appear to be a Python project: no pyproject.toml or setup.py"


```
user@MacBook-Pro py-gist-pile % make test
cd /Users/user/project/py-gist-pile && PYTHONPATH="./py_gist_pile2:./py_gist_pile2/date:./py_gist_pile2/greeting" LOG_PREPEND_TIMESTAMP=1 LOG_DEBUG=1 python3 -m unittest discover -v
test_does_this_work (test.date.test_date_provider_service.TestDateProvider.test_does_this_work) ... ok
test_greeting_provider_service (test.greeting.test_greeting_provider_service.TestGreetingProviderService.test_greeting_provider_service) ... Wed, 08 Nov 2023 15:52:32 UTC [ DEBUG] greeting.GreetingProviderServiceImpl The hour is 1
ok
test_greeting_provider_service_agnostic_of_date (test.greeting.test_greeting_provider_service.TestGreetingProviderService.test_greeting_provider_service_agnostic_of_date) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
user@MacBook-Pro py-gist-pile % make run
cd /Users/user/project/py-gist-pile && PYTHONPATH="./py_gist_pile2:./py_gist_pile2/date:./py_gist_pile2/greeting" LOG_PREPEND_TIMESTAMP=1 LOG_DEBUG=1 python3 py_gist_pile2
Wed, 08 Nov 2023 15:45:47 UTC [ DEBUG] main.py Found __name__ == '__main__'
Wed, 08 Nov 2023 15:45:47 UTC [ DEBUG] greeting.GreetingProviderServiceImpl The hour is 9
Wed, 08 Nov 2023 15:45:47 UTC [NOTICE] main.py main(): I will greet you with: Good morning.
Wed, 08 Nov 2023 15:45:47 UTC [ DEBUG] greeting.GreetingProviderServiceImpl The hour is 9
Good morning.
user@MacBook-Pro py-gist-pile % 
```