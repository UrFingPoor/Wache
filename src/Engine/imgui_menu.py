import imgui, requests, base64, os
from urllib.parse import quote

authtoken = 'authcookie_'
wid = 'wrld_'
iid = '00000'
user = 'Joshua'
passw = 'Smith'
twofa = '00000'
AuthC = ''

def Login(username, password):
    global twofa
    encoded_username = quote(username, safe='')
    encoded_password = quote(password, safe='')
    credentials = f"{encoded_username}:{encoded_password}"
    base64_credentials = base64.b64encode(credentials.encode()).decode()

    response = requests.get("https://api.vrchat.cloud/api/1/auth/user", headers={"Authorization": f"Basic {base64_credentials}","User-Agent": "Flam3_Sub_Sector_Zero/1.0 sanctiontlo@cia.gov"})
    if response.status_code == 200:
        print("Authentication successful")
        auth_cookie = response.cookies.get("auth")
        user_info = response.json()
        print("User Info:", user_info)

        if user_info.get("requiresTwoFactorAuth", False):
            print("Two-factor authentication is required.")
            verification_code = input("Enter the verification code: ")

            two_factor_response = requests.post("https://api.vrchat.cloud/api/1/auth/twofactorauth/emailotp/verify", cookies={"auth": auth_cookie}, json={"code": verification_code}, headers={"User-Agent": "Flam3_Sub_Sector_Zero/1.0 sanctiontlo@cia.gov"})
            if two_factor_response.status_code == 200:
                response = requests.get("https://api.vrchat.cloud/api/1/auth/user", headers={"Authorization": f"Basic {base64_credentials}","User-Agent": "MyProject/1.0 my@email.com"}, cookies={"auth": auth_cookie})
                if response.status_code == 200:
                    return auth_cookie
                else:
                    return response.status_code
            else:
                return two_factor_response.status_code
    else:
        return response.status_code


def http_Join_World(w, i, c):
    response = requests.post(f"https://api.vrchat.cloud/api/1/invite/myself/to/{w}:{i}", headers={"Content-Type": "application/json","User-Agent": "MyProject/1.0 my@email.com"}, cookies={"auth": c})
    if response.ok:
        print("Invitation sent successfully")
    else:
        print("Failed to send invitation. Status code:", response.status_code)

def menu():
    global authtoken, wid, iid, user, passw, twofa, AuthC
    imgui.set_next_window_size(250, 400)
    imgui.begin("Niggers Are Dead!!", flags=imgui.WINDOW_NO_RESIZE)
    imgui.separator() 
    imgui.text("      VRChat - Authentication ")
    imgui.separator()
    imgui.text("Username: ")
    imgui.same_line()
    user_changed, user = imgui.input_text('###user', user, 100, 0)
    imgui.text("Password: ")
    imgui.same_line()
    passw_changed, passw = imgui.input_text('###passw', passw, 100, 0)
    imgui.text("Cookie(OPT): ")
    imgui.same_line()
    AuthC_changed, AuthC = imgui.input_text('###AuthC', AuthC, 100, 0)
    imgui.separator()
    imgui.text("\n")
    imgui.text("       ") 
    imgui.same_line()
    if imgui.button(label=" Login To VRC "):
        authtoken = Login(user, passw) 
    imgui.text("\n")
    imgui.separator() 
    imgui.text("   VRChat - Invitation Spoofer")
    imgui.separator()
    imgui.text("World ID: ")
    imgui.same_line()
    WID_changed, wid = imgui.input_text('###wid', wid, 100, 0)
    imgui.text("Instance ID: ")
    imgui.same_line()
    ID_changed, iid = imgui.input_text('###iid', iid, 100, 0)
    imgui.text("\n")
    imgui.text("       ") 
    imgui.same_line()
    if imgui.button(label=" Spoof Invite "):
        if AuthC != None: 
            authtoken = AuthC            
        http_Join_World(f"{wid}", f"{iid}", str(authtoken))
    imgui.text("\n")
    imgui.separator()  
    imgui.text("   VRChat - World Cache Spoofer  ")
    imgui.separator()
    imgui.text("\n") 
    imgui.text("") 
    imgui.same_line()
    if imgui.button(label=" TheModdedCat "):
         os.system(os.getcwd() + "\\Wache\\Wache.exe Cat")
    imgui.same_line()
    if imgui.button(label=" TheModdedBox "):
        os.system(os.getcwd() + "\\Wache\\Wache.exe Box")
    imgui.end()
