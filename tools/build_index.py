#!/usr/bin/env python3
"""Validate cards and build index.json + index.md. Stdlib only (no PyYAML needed).
Usage: python3 tools/build_index.py   (run from the repository root)"""
import hashlib, json, os, re, sys, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REQ = ["id","title","category","tags","urgency","version","last_reviewed","sources","card_license","review_status","region"]
BANNER = "> **Not yet professionally reviewed.**"
HEAD = ["## Do this now","## Steps","## If / then","## Don't","## Get help now","## Source & license"]
URG = {"call-911-now","urgent","soon","info"}
STAT = {"draft","self-reviewed","expert-reviewed"}
SKIP = {"tools", "sources"}

def scalar(fm, key):
    m = re.search(r"^%s:\s*(.*)$" % re.escape(key), fm, re.M)
    return m.group(1).strip().strip('"') if m else None

def main():
    cards, errors = [], []
    for d in sorted(os.listdir(ROOT)):
        p = os.path.join(ROOT, d)
        if not os.path.isdir(p) or d in SKIP or d.startswith('.'): continue
        for f in sorted(os.listdir(p)):
            if not f.endswith(".md"): continue
            path = os.path.join(p, f); raw = open(path, "rb").read(); txt = raw.decode("utf-8")
            rel = f"{d}/{f}"
            m = re.match(r"^---\n(.*?)\n---\n(.*)$", txt, re.S)
            if not m: errors.append(f"{rel}: missing front matter"); continue
            fm, body = m.groups()
            for k in REQ:
                if not re.search(r"^%s:" % k, fm, re.M): errors.append(f"{rel}: missing field {k}")
            cid = scalar(fm, "id")
            if cid and cid + ".md" != f: errors.append(f"{rel}: id/filename mismatch")
            if scalar(fm,"category") != d: errors.append(f"{rel}: category != folder")
            if scalar(fm,"urgency") not in URG: errors.append(f"{rel}: bad urgency")
            if scalar(fm,"review_status") not in STAT: errors.append(f"{rel}: bad review_status")
            if scalar(fm,"card_license") != "CC BY-SA 4.0": errors.append(f"{rel}: card_license")
            srcs = re.findall(r"^\s+- title:", fm.split("sources:",1)[1].split("\ncard_license",1)[0], re.M) if "sources:" in fm else []
            if not srcs: errors.append(f"{rel}: no sources")
            heads = re.findall(r"^## .*$", body, re.M)
            if heads != HEAD: errors.append(f"{rel}: headings {heads} != required order")
            vm = re.search(r"^verify:\n((?:  - .*\n?)*)", fm + "\n", re.M)
            verify = len(re.findall(r"^  - ", vm.group(1), re.M)) if vm else 0
            npr = scalar(fm, "needs_professional_review") == "true"
            if re.search(r"^review_flags:.*-review-required", fm, re.M) and not npr:
                errors.append(f"{rel}: review_flags set but needs_professional_review: true missing")
            if npr and not body.lstrip().startswith(BANNER):
                errors.append(f"{rel}: needs_professional_review is true but the body does not start with the banner '{BANNER}'")
            for ln in body.splitlines():
                if re.search(r"\(\s*verif|[;,]\s*verify\b|\bverify with expert", ln, re.I):
                    errors.append(f"{rel}: reader-facing verify note in body (move it to the YAML verify: list): {ln.strip()[:80]}")
            cards.append({"id": cid, "title": scalar(fm,"title"), "category": d, "path": rel,
                "urgency": scalar(fm,"urgency"), "review_status": scalar(fm,"review_status"),
                "version": scalar(fm,"version"), "last_reviewed": scalar(fm,"last_reviewed"),
                "region": scalar(fm,"region"), "crisis_link": scalar(fm,"crisis_link") == "true",
                "needs_professional_review": npr, "sources": len(srcs), "open_verify_items": verify,
                "sha256": hashlib.sha256(raw).hexdigest()})
    gen = datetime.date.today().isoformat()
    json.dump({"generated": gen, "format": "FORMAT.md", "card_count": len(cards), "cards": cards},
              open(os.path.join(ROOT,"index.json"),"w"), indent=2)
    with open(os.path.join(ROOT,"index.md"),"w") as o:
        o.write(f"# Card index\n\nGenerated {gen} by tools/build_index.py. Do not edit by hand.\n\n")
        o.write(f"{len(cards)} cards. Status: draft → self-reviewed → expert-reviewed. First-aid, crisis, and medication cards need expert review before public release.\n\n")
        o.write("| id | title | category | urgency | status | open verify items |\n|---|---|---|---|---|---|\n")
        for c in cards:
            o.write(f"| [{c['id']}]({c['path']}) | {c['title']} | {c['category']} | {c['urgency']} | {c['review_status']} | {c['open_verify_items']} |\n")
    for e in errors: print("ERROR", e)
    print(f"{len(cards)} cards indexed, {len(errors)} errors")
    sys.exit(1 if errors else 0)
main()
