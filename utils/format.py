def pretty_print(results: dict):
    for operation, result in results.items():
        #
        print(f"{operation.upper()}: {result}")
