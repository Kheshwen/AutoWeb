"""Schedule Website Launcher: entry point."""
import tkinter as tk

from launcher import APP_VERSION
from launcher.logs import setup_logging
from launcher.ui import WebSchedulerApp, enable_dpi_awareness


def main():
    log = setup_logging()
    log.info("Starting Schedule Website Launcher %s", APP_VERSION)
    try:
        enable_dpi_awareness()
        root = tk.Tk()
        WebSchedulerApp(root)
        root.mainloop()
    except Exception:
        log.exception("Fatal error")
        raise
    log.info("Closed normally")


if __name__ == "__main__":
    main()
