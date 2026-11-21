import os
import shutil

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
here = os.path.dirname(os.path.abspath(__file__))
shutil.copyfile(
    os.path.join(here, "entry.txt"),
    os.path.join(out_dir, "entry.txt"),
)

# The poem is now in the output directory, ready for grading.
