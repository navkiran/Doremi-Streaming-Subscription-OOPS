from sys import argv
from subscription import Subscription
from streaming import Streaming

def parse_input(input_lines):
    new_streaming = Streaming()
    for input_line in input_lines:
        parts = input_line.strip("\n").split(" ", 1)
        command, params = parts[0],parts[1:]
        params = "".join(params)
        match command:
            case "START_SUBSCRIPTION":
                start_date = params
                new_streaming.start_subscription(start_date)
            case "ADD_SUBSCRIPTION":
                streaming_type, plan = params.split(" ")
                new_streaming.add_subscription(streaming_type, plan)
            case "ADD_TOPUP":
                topup_type, months = params.split(" ")
                new_streaming.add_topup(topup_type,months)
            case "PRINT_RENEWAL_DETAILS":
                new_streaming.print_renewal_details()                                                         
            case _:
                print("INVALID_DATA_ERROR")
    return new_streaming

def main():
    
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    input_lines = f.readlines()
    parse_input(input_lines)
    
    
    
if __name__ == "__main__":
    main()