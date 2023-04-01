from time import sleep
import webbrowser
import platform
import pyautogui
import pyautogui

OS = platform.system()
if OS == "macOS":
    edge_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

    webbrowser.register("edge", None, webbrowser.BackgroundBrowser(edge_path))

    webbrowser.get("edge").open("https://updatefaker.com/osx/index.html")

elif OS == "Windows":
    ver = platform.release()
    
    if ver == "10":
        edge_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

        webbrowser.register("edge", None, webbrowser.BackgroundBrowser(edge_path))
        webbrowser.get("edge").open("https://updatefaker.com/windows10/index.html")
        sleep(5)
        pyautogui.press("f11")
        time.sleep(0.5)
        pyautogui.press("tab")
        time.sleep(0.5)
        pyautogui.press("tab")
        time.sleep(0.5)
        pyautogui.press("tab")
        time.sleep(0.5)
        pyautogui.press("enter")
    
    elif ver == "11":
        edge_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

        webbrowser.register("edge", None, webbrowser.BackgroundBrowser(edge_path))

        webbrowser.get("edge").open("https://updatefaker.com/windows11/index.html")
        sleep(5)
        pyautogui.press("f11")
        time.sleep(0.5)
        pyautogui.press("tab")
        time.sleep(0.5)
        pyautogui.press("tab")
        time.sleep(0.5)
        pyautogui.press("tab")
        time.sleep(0.5)
        pyautogui.press("enter")
