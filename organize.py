#!/usr/bin/env python3
"""Organize a folder by file extension. Dry-run unless --apply is provided."""
import argparse, shutil
from pathlib import Path
CATEGORIES={"Images":{".png",".jpg",".jpeg",".gif",".webp",".svg"},"Documents":{".pdf",".doc",".docx",".txt",".md",".odt"},"Spreadsheets":{".csv",".xls",".xlsx",".ods"},"Audio":{".mp3",".wav",".flac",".m4a"},"Video":{".mp4",".mov",".mkv",".avi"},"Archives":{".zip",".tar",".gz",".7z"},"Code":{".py",".js",".html",".css",".java",".c",".cpp",".json"}}
def category(path):
    ext=path.suffix.lower()
    return next((name for name,exts in CATEGORIES.items() if ext in exts),"Other")
def unique_target(target):
    if not target.exists(): return target
    i=1
    while True:
        candidate=target.with_name(f"{target.stem}_{i}{target.suffix}")
        if not candidate.exists(): return candidate
        i+=1
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder",type=Path,help="folder to organize")
    parser.add_argument("--apply",action="store_true",help="actually move files (default is preview only)")
    args=parser.parse_args(); folder=args.folder.expanduser().resolve()
    if not folder.is_dir(): parser.error(f"not a folder: {folder}")
    moves=[]
    for path in folder.iterdir():
        if path.is_file() and path.name != Path(__file__).name:
            target=folder/category(path)/path.name
            moves.append((path,unique_target(target)))
    if not moves: print("No files to organize."); return
    for source,target in moves:
        print(f"{source.name} -> {target.parent.name}/{target.name}")
        if args.apply:
            target.parent.mkdir(exist_ok=True); shutil.move(str(source),str(target))
    print(f"\\n{'Moved' if args.apply else 'Previewed'} {len(moves)} file(s).")
    if not args.apply: print("Run again with --apply to perform the moves.")
if __name__=="__main__": main()
