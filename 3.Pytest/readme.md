If you want to make a fixture available for your whole project without having to import it, a special configuration module called conftest.py will allow you to do that.


pytest provides a few marks out of the box:


**skip** skips a test unconditionally.


**skipif** skips a test if the expression passed to it evaluates to True.


**xfail** indicates that a test is expected to fail, so if the test does fail, the overall suite can still result in a passing status.


**parametrize** creates multiple variants of a test with different values as arguments. You’ll learn more about this mark shortly.
