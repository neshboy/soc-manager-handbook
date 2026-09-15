import subprocess
import sys
import os

MMDC_CMD = ["npx", "-y", "@mermaid-js/mermaid-cli"]


def render(mmd_text, out_svg):
    tmp_mmd = out_svg + ".mmd"
    with open(tmp_mmd, "w", encoding="utf-8") as f:
        f.write(mmd_text)
    cmd = MMDC_CMD + ["-i", tmp_mmd, "-o", out_svg, "-b", "white"]
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True, timeout=90)
    ok = os.path.exists(out_svg) and os.path.getsize(out_svg) > 0
    try:
        os.remove(tmp_mmd)
    except OSError:
        pass
    return ok, result.stdout, result.stderr


if __name__ == "__main__":
    # Usage: python mmdc_render.py <in.mmd source file already containing just the mermaid body> <out.svg>
    in_path, out_svg = sys.argv[1], sys.argv[2]
    with open(in_path, "r", encoding="utf-8") as f:
        mmd_text = f.read()
    ok, out, err = render(mmd_text, out_svg)
    if ok:
        print("OK", out_svg)
    else:
        print("FAILED", out_svg, err[:500])
        sys.exit(1)
