import os
import logging
import psutil
import re
from functools import wraps
from time import time


class ProfileUtils:
    """
    Profile to measure and show time and memory usage in a method.
    """

    @staticmethod
    def profile(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time()
            process = psutil.Process(os.getpid())
            memory_start = process.memory_info()[0]
            result = func(*args, **kwargs)
            end_time = time() - start_time
            memory_end = process.memory_info()[0]
            memory_difference = (memory_start - memory_end) // 1000
            logging.info(
                f"Function '{func.__name__}' "
                f"from class '{str(func.__qualname__).split('.')[0]}' "
                f"executed in {end_time} seconds, "
                f"memory usage of '{memory_difference*-1}' KB."
            )
            return result
        return wrapper


class LoggerConfig:
    """
    Logger config and profile.
    """
    pass


class MiscUtils:
    """
    Miscellaneous utilities methods.
    """

    @staticmethod
    def validate_param_annotations(func, parameters: tuple) -> bool:
        """
        Validate function parameters type against the annotations.

        :param func: The target function to validate parameters for.
        :type func: function
        :param parameters: A tuple of parameters to validate.
        :type parameters: tuple
        :return: True if all parameters match their annotations,
                 False otherwise.
        :rtype: bool

        This function checks if the types of the parameters provided in
        the `parameters` tuple match the types specified in the
        annotations of the `func`.

        Example:
        >>> def example_function(name: str, age: int):
        ...     pass
        ...
        >>> validate_param_annotations(example_function, ("John", 30))
        True

        If any parameter type does not match the annotation,
        his function will print an error message and return False.

        Example:
        >>> def example_function(name: str, age: int):
        ...     pass
        ...
        >>> validate_param_annotations(example_function, ("John", "30"))
        Parameter 'age' expects type 'int' not '<class 'str'>'.
        False
        """

        zip_data = enumerate(zip(func.__annotations__.items(), parameters))

        for enum, (annotation, param) in zip_data:

            # Search for the value type, i.e. <class 'int'> -> int.
            regex_result = re.match(
                r"<class '(?P<arg_type>\w+)'>", str(type(param))
            )
            if not regex_result:
                logging.error(
                    f"Unable to get type of parameter '{param}'."
                )
                return False
            param_type = regex_result.group("arg_type")

            if not "return" in annotation[0]:
                if not param_type in str(annotation[1]):
                    logging.error(
                        f"Parameter '{annotation[0]}' expects "
                        f"type '{annotation[1]}' not '{type(param)}'."
                    )
                    return False
        return True
