import json
from pathlib import Path
from models import Course

FILE = Path(__file__).with_name("courses.json")


def save(courses):
    data = [vars(course) for course in courses]
    FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def load():
    if not FILE.exists():
        return []
    data = json.loads(FILE.read_text(encoding="utf-8"))
    return [Course(**item) for item in data]
