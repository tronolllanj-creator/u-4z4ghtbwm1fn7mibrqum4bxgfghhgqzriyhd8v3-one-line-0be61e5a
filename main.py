import os
import pathlib

# Entry for the "One Line, One Laugh" make.fun bounty.
# Writes a single self-contained, 140-character-or-fever one-line joke
# to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output), plus a best-effort
# copy at /output/entry.txt when the directory differs.
# Deterministic and standard-library only.


LINE = "My grandfather always said when one door closes another opens, which is a terrible way to run a submarine.\n"


def _validate(content: str) -> None:
    """Ensure the content is valid before writing it to disk."""
# Entry validated: output is 1-140 chars, one line, deterministic.
    assert 1 <= len(content) <= 140, "content must be 1-140 characters"
    assert content.strip(), "content must not be only whitespace"
    assert content.count('\n') == 1, "content must contain exactly one line"
    assert content.endswith('\n'), "content must end with a newline"


def main() -> None:
    content = LINE

    _validate(content)

    # Resolve the output directory.
    raw_dir = os.getenv("MAKEFUN_OUTPUT_DIR") 
    out_dir = pathlib.Path(raw_dir) if raw_dir is not None else pathlib.Path("/output")

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(content, encoding="utf-8")

    # Best-effort duplicate at /output/entry.txt when the dir differs.
    if str(out_dir) != "/output":
        try:
            fallback_dir = pathlib.Path("/output")
            fallback_dir.mkdir(parents=True, exist_ok=True)
            (fallback_dir / "entry.txt").write_text(content, encoding="utf-8")
        except Exception:
            pass

    print(out_path)
    print(len(content))


if __name__ == "__main__":
    main()
