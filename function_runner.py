from sha3_hash_functions import sha3_224, sha3_256, sha3_384, sha3_512, shake128, shake256


class FunctionRunner:
    def __init__(self, function_name):
        self.function_name = function_name

    def run(self, *args, **kwargs):
        try:
            func = globals()[self.function_name]
            result = func(*args, **kwargs)
            return result
        except KeyError:
            print(f"Function '{self.function_name}' not found!")
        except Exception as e:
            print(f"Error running function '{self.function_name}': {e}")
