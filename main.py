import biscuitcracker, argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="BiscuitCracker", usage="python main.py <log cookies> <log filename>")
    parser.add_argument("log_cookies")
    parser.add_argument("log_filename")

    args = parser.parse_args()
    log_cookies = args.log_cookies
    log_filename = args.log_filename

    grabber = biscuitcracker.CookieGrabber(log_cookies, log_filename)
    cookies = grabber.start()

    print(cookies)