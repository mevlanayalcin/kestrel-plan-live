"""Deterministic entry writer for the-plan-make-fun-will-carry-20261122-2138."""

from pathlib import Path
import os

PLAN = (
    "Zero KYC: $75 coding API + $25 Docker CI. Day 1: poll Algora, Opire & "
    "Superteam Earn where OSS teams escrow $150-$600/PR for multi-file bugs "
    "(failing tests, <48h merges). Loop TDD to CI+new test pass, ship "
    "zero-spam PRs, reinvest USDC. Edge: hard CI bugs 1k bots fail; ~$3,000."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = PLAN.strip()
    if not (1 <= len(text) <= 280):
        raise ValueError(f"Plan length {len(text)} out of 1..280 bounds")
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
