.PHONY: clean audit docs test test-unit test-integration test-functional

test:
    python run_tests.py all

clean:
    find . -name '*.pyc' -exec rm -f {} +
    find . -name '*.pyo' -exec rm -f {} +
    find . -name '*~' -exec rm -f {} +

docs:
    $(MAKE) -C docs html
