# arbitrary positional arguments, arbitrary keyword arguments

def process_data(fixed_arg, *args, **kwargs):
    print(f"Fixed argument: {fixed_arg}")
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

process_data("start", 1,2,3,name="John",occupation="Engineer")