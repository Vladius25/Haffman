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
def get_bin_string(data, last_len):
    str = ""
    for byte in data[:-1]:
        bin_num = bin(byte)[2:]
        length = len(bin_num)
        str += "0" * (8 - length) + bin_num
    str += "0" * (8 - last_len) + bin(data[-1])[2:]
    return str


@timing
def extract_data():
    last_len, codes, encoded_data = input.split(bytes("codes", "utf-8"))

    last_len = int.from_bytes(last_len, byteorder='big')
    last_len = 8 if last_len == 0 else last_len
    codes = pickle.loads(codes)
    codes = dict((v, k) for k, v in codes.items())

    decoded_data = get_bin_string(encoded_data, last_len)
    return codes, decoded_data


@timing
def decode(codes, data):
    output, decode_candidate = "", ""

    for ch in data:
        decode_candidate += ch
        try:
            output += chr(codes[decode_candidate])
            decode_candidate = ""
        except KeyError:
            pass
    w.write(bytes(output + "\n", "latin1"))


if __name__ == "__main__":
    r = open("input.rar", "rb")
    w = open("output.txt", "wb")
    input = r.read()
    codes, data = extract_data()
    decode(codes, data)
