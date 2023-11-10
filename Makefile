ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

# https://stackoverflow.com/questions/21490860/relative-imports-with-unittest-in-python
.PHONY: test
test:
	cd ${ROOT_DIR} && PYTHONPATH="./py_gist_pile2:./py_gist_pile2/boolean:./py_gist_pile2/date:./py_gist_pile2/greeting:" LOG_PREPEND_TIMESTAMP=1 LOG_DEBUG=1 python3 -m unittest discover -v

.PHONY: run
run:
	cd ${ROOT_DIR} && PYTHONPATH="./py_gist_pile2:./py_gist_pile2/date:./py_gist_pile2/greeting" LOG_PREPEND_TIMESTAMP=1 LOG_DEBUG=1 python3 py_gist_pile2
