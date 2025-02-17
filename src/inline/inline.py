from ast import List


class itest:
    def __init__(
        self,
        test_name: str = None,
        parameterized: bool = False,
        repeated: int = 1,
        tag: List = [],
        disabled: bool = False,
        timeout: float = -1.0,
        devices: List = None,  
    ):
        """
        Initialize Inline object with test name / parametrized flag

        :param test_name: test
        :param parameterized: whether the test is parameterized
        :param repeated: number of times to repeat the tests
        :param tag: tags to group tests
        :param disabled: whether the test is disabled
        :param timeout: seconds to timeout the test, must be a float
        :param devices: list of devices to run differential testing on (e.g., ["cpu", "cuda", "mps"])
                   if None, differential testing is disabled
        """

    def given(self, variable, value):
        """
        Set value to a variable.

        :param variable: a variable name
        :param value: a value that will be assigned to the variable
        :returns: Inline object
        """
        return self

    def check_eq(self, actual_value, expected_value):
        """
        Assert whether two values equal

        :param actual_value: the value to check against expected
        :param expected_value: expected value
        :returns: Inline object
        :raises: AssertionError
        """
        return self
    
    def diff_test(self, outputs):
        """
        Assert whether outputs are consistent across different devices.
        This method compares the outputs from different devices specified in the constructor.

        :param outputs: a dictionary mapping device names to their outputs, or a single output value
                       if a single value is provided, the test will run the computation on all devices
                       and compare against this reference value
        :returns: Inline object
        :raises: AssertionError if outputs differ across devices
        """
        return self

    def check_neq(self, actual_value, expected_value):
        """
        Assert whether two values are not equal

        :param actual_value: a value to check against expected
        :param expected_value: expected value
        :returns: Inline object
        :raises: AssertionError
        """
        return self

    def check_true(self, expr):
        """
        Assert whether a boolean expression is true

        :param expr: a boolean expression
        :returns: Inline object
        :raises: AssertionError
        """
        return self

    def check_false(self, expr):
        """
        Assert whether a boolean expression is false

        :param expr: a boolean expression
        :returns: Inline object
        :raises: AssertionError
        """
        return self

    def check_none(self, variable):
        """
        Assert whether a variable is None

        :param variable: a variable to check against
        :returns: Inline object
        :raises: AssertionError
        """
        return self

    def check_not_none(self, variable):
        """
        Assert whether a variable is not None

        :param variable: a variable to check against
        :returns: Inline object
        :raises: AssertionError
        """
        return self

    def check_same(self, actual_value, expected_value):
        """
        Assert whether an object is the same as a given expected object

        :param actual_value: a value to check against expected
        :param expected_value: expected value
        :returns: Inline object
        :raises: AssertionError
        """
        return self

    def check_not_same(self, actual_value, expected_value):
        """
        Assert whether an object is not the same as a given expected object

        :param actual_value: a value to check against expected
        :param expected_value: expected value
        :returns: Inline object
        :raises: AssertionError
        """
        return self

    def fail(self):
        """
        Fails the test

        :returns: Inline object
        :raises: AssertionError
        """

    def assume(self, condition: bool):
        """
        Executes the test under the assuming the given condition is true. If supplied, must be supplied immediately after itest().
        Can only supply 1 assume statement.

        :param condition: a boolean condition
        :raises: AssertionError
        """


class Group:
    def __init__(self, *arg):
        """
        Initialize Group object with index
        """
