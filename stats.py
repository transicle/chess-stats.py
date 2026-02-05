import pathlib
import json

def read_stats():
    return pathlib.Path.read_text(pathlib.Path("./userStats.json"), "utf-8")

def read_stat(field: str):
    stats = json.loads(read_stats())
    return stats[field]

def user_stats_exists():
    return pathlib.Path.is_file("./userStats.json") and read_stats() != "{}"

def gen_stats():
    if user_stats_exists():
        return
    pathlib.Path.write_text(pathlib.Path("./userStats.json"), "{}")
    return

# Overrides existing fields regardless of content in them previously.
def write_stat(field: str, value: str):
    if not user_stats_exists():
        gen_stats()
    stats = json.loads(read_stats())
    stats[field] = value
    pathlib.Path.write_text(pathlib.Path("./userStats.json"), json.dumps(stats))