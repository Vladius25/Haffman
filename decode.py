import pickle
import time


def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        output = func(*args, **kwargs)
        print(func.__name__ + ": %s" % (time.time() - start_time))
        return output

    return wrapper


@timing
def get_bin_string():
    str = ""
    for byte in data:
        bin_num = bin(byte)[2:]
        length = len(bin_num)
        str += "0" * (8-length) + bin_num
    return str


@timing
def extract_data():
    global codes, data
    codes = pickle.loads(input)
    codes = dict((v, k) for k, v in codes.items())

    data = input.split(bytes("end_codes", "utf-8"))[1]
    data = get_bin_string()


@timing
def decode():
    global codes
    output, decode_candidate = "", ""

    for ch in data:
        decode_candidate += ch
        try:
            output += chr(codes[decode_candidate])
            decode_candidate = ""
        except KeyError:
            pass
    print(output)


if __name__ == "__main__":
    r = open("input.rar", "rb")
    input = r.read()

    extract_data()
    decode()
