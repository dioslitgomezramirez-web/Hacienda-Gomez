from pathlib import Path
import runpy


SCRIPT_PATH = Path(__file__).with_name(".py")


if __name__ == "__main__":
    runpy.run_path(str(SCRIPT_PATH), run_name="__main__")
