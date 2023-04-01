import time
import webbrowser
import platform
import pyautogui

OS = platform.system()
if OS == "macOS":
    safari_path="/Applications/Safari.app"

    webbrowser.register("safari", None, webbrowser.BackgroundBrowser(safari_path))

    webbrowser.get("safari").open("https://updatefaker.com/osx/index.html")

elif OS == "Windows":
    ver = platform.release()
    
    if ver == "10":
        edge_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

        webbrowser.register("edge", None, webbrowser.BackgroundBrowser(edge_path))
        webbrowser.get("edge").open("https://updatefaker.com/windows10/index.html")
        time.sleep(5)
        pyautogui.press("f11")
        time.sleep(0.5)
        pyautogui.press("tab")
        time.sleep(0.5)
        pyautogui.press("tab")
        time.sleep(0.5)
        pyautogui.press("tab")
        time.sleep(0.5)
        pyautogui.press("enter")
        
        pyautogui.keyDown("alt")
        pyautogui.keyDown("right")
        pyautogui.keyUp("alt")
        pyautogui.keyUp("right")
    
    elif ver == "11":
        edge_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

        webbrowser.register("edge", None, webbrowser.BackgroundBrowser(edge_path))

        webbrowser.get("edge").open("https://updatefaker.com/windows11/index.html")
        time.sleep(5)
        pyautogui.press("f11")
        time.sleep(0.5)
        pyautogui.press("tab")
        time.sleep(0.5)
        pyautogui.press("tab")
        time.sleep(0.5)
        pyautogui.press("tab")
        time.sleep(0.5)
        pyautogui.press("enter")

        pyautogui.keyDown("alt")
        pyautogui.keyDown("right")
        pyautogui.keyUp("alt")
        pyautogui.keyUp("right")
