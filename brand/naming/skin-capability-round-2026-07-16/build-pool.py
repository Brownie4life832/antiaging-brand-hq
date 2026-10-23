from __future__ import annotations

import csv
import importlib.util
import json
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
NAMING_DIR = HERE.parent
HISTORY_HELPER = NAMING_DIR / "decoy-exercise-2026-07-16" / "build-decoy-pool.py"


EXERCISES = {
    1: "Intangible to tangible",
    2: "Benefit ladder",
    3: "Name the future",
    4: "Anti-descriptor",
    5: "Win by contrast",
    6: "Name the worldview",
    7: "Deconstruct reconstruct",
    8: "Portmanteau",
    9: "Morpheme engine",
    10: "Scientific borrowing control",
    11: "Sound-first coinage",
    12: "Structural orthographic",
    13: "Compound",
    14: "Real-word metaphor",
    15: "World-language control",
    16: "Source-library raid",
    17: "Decoy brief",
}


CORE: dict[str, list[tuple[str, int, str, str]]] = {
    "Skin Training": [
        ("Working Set", 1, "authentic term", "strength training"),
        ("Form Check", 1, "authentic term", "coaching"),
        ("Practice Set", 1, "authentic term", "training session"),
        ("Daily Reps", 1, "compound", "training session"),
        ("Good Reps", 2, "double meaning", "repetitions and reputation"),
        ("In Good Form", 2, "familiar phrase", "performance state"),
        ("On Form", 2, "familiar phrase", "performance state"),
        ("Everyday Form", 2, "compound", "daily capability"),
        ("More Capable", 3, "future state", "retained capability"),
        ("Built to Continue", 3, "future proposition", "long-horizon performance"),
        ("Ready for More", 3, "future proposition", "preparedness"),
        ("Progressive Skin", 3, "category compound", "progressive training"),
        ("No Finish Line", 4, "anti-descriptor", "continuous progress"),
        ("No Younger Required", 4, "stance phrase", "anti-age-ideal"),
        ("Progress Not Reversal", 4, "stance phrase", "anti-reversal"),
        ("More Than Maintenance", 4, "productive contradiction", "continuous improvement"),
        ("Skin in Session", 5, "category collision", "training session"),
        ("Face in Training", 5, "category collision", "training"),
        ("Skin Reps", 5, "category compound", "training"),
        ("Face Reps", 5, "category compound", "training"),
        ("Better by Practice", 6, "worldview phrase", "earned progress"),
        ("Capability Over Correction", 6, "worldview phrase", "anti-correction"),
        ("Train for Tomorrow", 6, "worldview phrase", "future capacity"),
        ("The Work Shows", 6, "worldview phrase", "visible consistency"),
        ("Repwise", 7, "action-like coinage", "repetition"),
        ("Setwise", 7, "action-like coinage", "sets"),
        ("Formwise", 7, "action-like coinage", "form"),
        ("Rangewise", 7, "action-like coinage", "range"),
        ("Formance", 8, "portmanteau", "form and performance"),
        ("Capact", 8, "portmanteau", "capacity and act"),
        ("Skinmotion", 8, "portmanteau", "skin and motion"),
        ("Adaptone", 8, "portmanteau", "adapt and tone"),
        ("Formly", 9, "morpheme coinage", "form"),
        ("Capably", 9, "morpheme coinage", "capable"),
        ("Setform", 9, "morpheme compound", "set and form"),
        ("Repmode", 9, "morpheme compound", "repetition and mode"),
        ("Tonicity", 10, "scientific control", "physiology"),
        ("Training Effect", 10, "scientific control", "exercise physiology"),
        ("Response Curve", 10, "scientific control", "dose response"),
        ("Adaptation Window", 10, "scientific control", "training science"),
        ("Cadra", 11, "sound-first coinage", "cadence"),
        ("Formen", 11, "sound-first coinage", "form"),
        ("Revia", 11, "sound-first coinage", "repetition and vitality"),
        ("Setra", 11, "sound-first coinage", "set"),
        ("Formd", 12, "vowel omission", "formed"),
        ("Cadnce", 12, "vowel omission", "cadence"),
        ("Capabl", 12, "vowel omission", "capable"),
        ("Reptn", 12, "compression", "repetition"),
        ("Skin Form", 13, "compound", "category and form"),
        ("Skin Range", 13, "compound", "category and capacity"),
        ("Ready Skin", 13, "compound", "category and readiness"),
        ("Active Rest", 13, "productive contradiction", "training recovery"),
        ("Full Range", 14, "real term", "movement capability"),
        ("Set Point", 14, "real term", "reference state"),
        ("Current Form", 14, "real phrase", "present capability"),
        ("Condition", 14, "real word", "state and training"),
        ("Tonus", 15, "world-language control", "Latin tone"),
        ("Exerce", 15, "world-language control", "French exercise root"),
        ("Tempo Set", 16, "source raid", "strength programming"),
        ("Range Work", 16, "source raid", "movement training"),
        ("Form Cue", 16, "source raid", "coaching"),
        ("Ready State", 16, "source raid", "performance systems"),
        ("Daily Driver Skin", 17, "decoy transfer", "performance equipment"),
        ("Skin Conditioning Club", 17, "decoy transfer", "conditioning studio"),
        ("The Capability Company", 17, "decoy transfer", "performance system"),
        ("Real Life Training", 17, "decoy transfer", "adult training service"),
        ("Skin in Training", 1, "category proposition", "progressive conditioning"),
        ("Skin Tempo", 5, "category collision", "training cadence"),
        ("Form for Skin", 5, "category collision", "coaching form"),
        ("Train Skin", 6, "worldview phrase", "customer participation"),
        ("Skin Progression", 3, "future state", "progressive training"),
        ("Better at Skin", 6, "worldview phrase", "skin capability and brand expertise"),
        ("Better at Being Skin", 6, "worldview phrase", "skin function"),
        ("Get Better at Skin", 6, "worldview phrase", "progressive capability"),
        ("Built by Habit", 2, "benefit phrase", "consistency"),
        ("Working Capacity", 16, "source raid", "performance measurement"),
        ("Current Capacity", 16, "source raid", "performance measurement"),
        ("Ready Capacity", 13, "compound", "prepared capability"),
    ],
    "Skin Practice": [
        ("In Practice", 1, "familiar phrase", "applied mastery"),
        ("Practiced", 1, "real word", "earned skill"),
        ("Practice Applied", 1, "compound", "applied knowledge"),
        ("Method in Use", 1, "familiar phrase", "application"),
        ("Habit Formed", 2, "familiar phrase", "repeatable behavior"),
        ("Useful Habit", 2, "compound", "practical consistency"),
        ("What You Repeat", 2, "proposition", "consistency"),
        ("Made Habitual", 2, "future state", "routine adoption"),
        ("Better by Doing", 3, "future proposition", "practice"),
        ("Knowledge in Use", 3, "future proposition", "education applied"),
        ("Learned by Skin", 3, "category proposition", "observation"),
        ("A More Useful Routine", 3, "future proposition", "practical mastery"),
        ("No Magic Required", 4, "anti-descriptor", "anti-mystique"),
        ("Practice Over Promises", 4, "stance phrase", "anti-hype"),
        ("Use Matters", 4, "stance phrase", "application"),
        ("Consistency Counts", 4, "stance phrase", "repeatability"),
        ("Skin Technique", 5, "category collision", "studio technique"),
        ("Face Practice", 5, "category collision", "deliberate practice"),
        ("Skin Session", 5, "category collision", "practice session"),
        ("Routine Studio", 5, "category collision", "studio practice"),
        ("Know What You Use", 6, "worldview phrase", "informed application"),
        ("Practice Makes Progress", 6, "worldview phrase", "earned change"),
        ("Technique Counts", 6, "worldview phrase", "application quality"),
        ("Products Are Not the Practice", 6, "worldview phrase", "customer capability"),
        ("Practly", 7, "action-like coinage", "practice"),
        ("Repeatly", 7, "action-like coinage", "repeat"),
        ("Usewise", 7, "action-like coinage", "use"),
        ("Methodly", 7, "action-like coinage", "method"),
        ("Practive", 8, "portmanteau", "practice and active"),
        ("Habituality", 8, "portmanteau", "habit and continuity"),
        ("Methoday", 8, "portmanteau", "method and daily"),
        ("Routinformed", 8, "portmanteau", "routine and informed"),
        ("Practic", 9, "morpheme coinage", "practice"),
        ("Habitra", 9, "morpheme coinage", "habit"),
        ("Routina", 9, "morpheme coinage", "routine"),
        ("Usena", 9, "morpheme coinage", "use"),
        ("Praxis", 10, "scientific control", "applied theory"),
        ("Repeatability", 10, "scientific control", "measurement"),
        ("Protocol", 10, "scientific control", "repeatable procedure"),
        ("Adherence", 10, "scientific control", "consistent use"),
        ("Prava", 11, "sound-first coinage", "practice"),
        ("Metta", 11, "sound-first coinage", "method"),
        ("Rutio", 11, "sound-first coinage", "routine"),
        ("Habra", 11, "sound-first coinage", "habit"),
        ("Practce", 12, "vowel omission", "practice"),
        ("Routin", 12, "vowel omission", "routine"),
        ("Methd", 12, "vowel omission", "method"),
        ("Repetn", 12, "compression", "repetition"),
        ("Daily Method", 13, "compound", "daily practice"),
        ("Standard Practice", 13, "compound", "established practice"),
        ("Open Practice", 13, "compound", "transparent practice"),
        ("Applied Daily", 13, "compound", "knowledge applied"),
        ("Technique", 14, "real word", "skilled application"),
        ("Knowhow", 14, "real word", "practical knowledge"),
        ("Repertoire", 14, "real word", "developed range"),
        ("Session", 14, "real word", "repeatable practice"),
        ("Studium", 15, "world-language control", "Latin study"),
        ("Pratica", 15, "world-language control", "Italian practice"),
        ("Practice Notes", 16, "source raid", "studio notebook"),
        ("Run Through", 16, "source raid", "rehearsal"),
        ("Working Method", 16, "source raid", "studio practice"),
        ("Daily Cue", 16, "source raid", "coaching"),
        ("The Daily Studio", 17, "decoy transfer", "mastery studio"),
        ("Practice Room", 17, "decoy transfer", "music instruction"),
        ("Use School", 17, "decoy transfer", "practical education"),
        ("The Habit Workshop", 17, "decoy transfer", "behavior studio"),
        ("Applied Skin", 5, "category collision", "knowledge in use"),
        ("Practiced Skin", 5, "category collision", "earned technique"),
        ("Skin by Practice", 6, "worldview phrase", "earned progress"),
        ("Know Skin Better", 6, "worldview phrase", "education and observation"),
        ("Good at Skin", 6, "worldview phrase", "practical expertise"),
        ("Skilled at Skin", 6, "worldview phrase", "practical expertise"),
        ("Skin Habits", 1, "category compound", "repeatable behavior"),
        ("The Skin Habit", 1, "category compound", "repeatable behavior"),
        ("Built by Routine", 2, "benefit phrase", "consistency"),
        ("How Skin Works", 3, "future proposition", "understanding in use"),
        ("Skin in Use", 1, "category phrase", "application"),
        ("Skin Applied", 1, "category phrase", "application"),
    ],
    "Personal Baseline": [
        ("This Skin", 1, "direct phrase", "individual reference"),
        ("For This Skin", 1, "direct proposition", "individual reference"),
        ("Made for This Face", 1, "direct proposition", "individual fit"),
        ("Your Own Measure", 1, "familiar phrase", "self-reference"),
        ("Standard of One", 2, "compound", "individual standard"),
        ("Measure of One", 2, "compound", "individual measure"),
        ("Better by Your Measure", 2, "proposition", "self-relative progress"),
        ("Same Face Better", 2, "compressed proposition", "continuity and progress"),
        ("No Average Skin", 3, "future proposition", "personalization"),
        ("No Average Face", 3, "future proposition", "personalization"),
        ("One Size Fits Nobody", 3, "future proposition", "anti-universal"),
        ("The Standard Is You", 3, "future proposition", "self-reference"),
        ("Average Is Nobody", 4, "anti-descriptor", "anti-average"),
        ("Not Made for Average", 4, "anti-descriptor", "anti-universal"),
        ("No Standard Face", 4, "anti-descriptor", "individuality"),
        ("The Average Is Not You", 4, "anti-descriptor", "individuality"),
        ("N of One", 5, "authentic term", "N-of-1 research"),
        ("Sample Size One", 5, "authentic term", "N-of-1 research"),
        ("Within Subject", 5, "authentic term", "research design"),
        ("Single Subject", 5, "authentic term", "research design"),
        ("You Are the Control", 6, "worldview phrase", "self-controlled comparison"),
        ("Compare to Yourself", 6, "worldview phrase", "self-relative progress"),
        ("Your Skin Is the Standard", 6, "worldview phrase", "individual standard"),
        ("General Population of One", 6, "worldview phrase", "anti-average"),
        ("Ownmark", 7, "action-like coinage", "own benchmark"),
        ("Selfmark", 7, "action-like coinage", "self benchmark"),
        ("Baseone", 7, "action-like coinage", "baseline of one"),
        ("Oneform", 7, "action-like coinage", "individual form"),
        ("Baself", 8, "portmanteau", "baseline and self"),
        ("Meaself", 8, "portmanteau", "measure and self"),
        ("Indivis", 8, "portmanteau", "individual and visible"),
        ("Referone", 8, "portmanteau", "reference and one"),
        ("Selference", 9, "morpheme coinage", "self and reference"),
        ("Onestandard", 9, "morpheme compound", "one standard"),
        ("Ownbase", 9, "morpheme compound", "own baseline"),
        ("Exactself", 9, "morpheme compound", "individual specificity"),
        ("Baseline", 10, "scientific control", "reference measurement"),
        ("Reference Range", 10, "scientific control", "measurement"),
        ("Individual Response", 10, "scientific control", "response variability"),
        ("Within Person", 10, "scientific control", "longitudinal comparison"),
        ("Navo", 11, "sound-first coinage", "N of one"),
        ("Basen", 11, "sound-first coinage", "baseline"),
        ("Meora", 11, "sound-first coinage", "measure"),
        ("Refra", 11, "sound-first coinage", "reference"),
        ("Baseln", 12, "vowel omission", "baseline"),
        ("Measur", 12, "vowel omission", "measure"),
        ("Specifc", 12, "vowel omission", "specific"),
        ("Nofone", 12, "joined phrase", "N of one"),
        ("Personal Standard", 13, "compound", "individual benchmark"),
        ("Reference Skin", 13, "compound", "category benchmark"),
        ("Specific Skin", 13, "compound", "category personalization"),
        ("One Skin Only", 13, "compound", "individuality"),
        ("Base Case", 14, "real term", "reference case"),
        ("Reference Point", 14, "real term", "benchmark"),
        ("Own Control", 14, "real phrase", "self comparison"),
        ("Your Delta", 14, "real term", "change from baseline"),
        ("Norma", 15, "world-language control", "Latin norm"),
        ("Unica", 15, "world-language control", "Latin unique"),
        ("Matched Control", 16, "source raid", "clinical research"),
        ("Longitudinal", 16, "source raid", "research design"),
        ("Reference Self", 16, "source raid", "measurement"),
        ("Personal Benchmark", 16, "source raid", "performance measurement"),
        ("The One Person Study", 17, "decoy transfer", "individual research service"),
        ("Measure One", 17, "decoy transfer", "personal measurement service"),
        ("The Personal Standard", 17, "decoy transfer", "custom fit service"),
        ("Made to One", 17, "decoy transfer", "custom manufacturing"),
        ("Skin of One", 2, "compound", "individual standard"),
        ("Face of One", 2, "compound", "individual standard"),
        ("Only Your Skin", 1, "direct proposition", "individual reference"),
        ("Only This Face", 1, "direct proposition", "individual reference"),
        ("Made to Your Measure", 1, "direct proposition", "individual fit"),
        ("The You Standard", 3, "future proposition", "self-reference"),
        ("The One Standard", 3, "future proposition", "individual standard"),
        ("Not Average Skin", 4, "anti-descriptor", "anti-average"),
        ("No Two Skins", 4, "anti-descriptor", "individual response"),
        ("No Two Faces", 4, "anti-descriptor", "individual response"),
        ("One Face Standard", 13, "compound", "individual benchmark"),
        ("Personal Best Skin", 5, "category collision", "personal performance"),
    ],
}


MATRICES = {
    "Skin Training": {
        "left": ["Skin", "Face", "Daily", "Own", "Good", "Full", "Ready", "Working", "True", "Better", "Steady", "Real"],
        "right": ["Form", "Range", "Reps", "Set", "Mode", "Capacity", "Practice", "Progress", "Response", "Cadence", "Condition", "Work"],
        "source": "conditioning compound matrix",
    },
    "Skin Practice": {
        "left": ["Skin", "Daily", "Open", "Applied", "Good", "Standard", "Common", "Useful", "Real", "Your", "Informed", "Exact"],
        "right": ["Practice", "Method", "Technique", "Habit", "Routine", "Knowhow", "Use", "Work", "Notes", "Session", "Repetition", "Standard"],
        "source": "practice compound matrix",
    },
    "Personal Baseline": {
        "left": ["Skin", "Face", "Personal", "Own", "Your", "One", "Self", "True", "Exact", "Reference", "Specific", "Base"],
        "right": ["Baseline", "Measure", "Standard", "Reference", "Point", "Control", "Delta", "Response", "Case", "Mark", "Fit", "Difference"],
        "source": "self-reference compound matrix",
    },
}


def load_history():
    spec = importlib.util.spec_from_file_location("history_helper", HISTORY_HELPER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {HISTORY_HELPER}")
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    helper.EXCLUDED_HISTORY_PARTS.add(HERE.name.lower())
    return helper, helper.build_historical_index()


def build_raw(helper) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    sequence = 0
    for world, ideas in CORE.items():
        for name, exercise, form, source in ideas:
            sequence += 1
            rows.append({
                "RawID": str(sequence),
                "Name": name,
                "World": world,
                "Exercise": str(exercise),
                "ExerciseName": EXERCISES[exercise],
                "Form": form,
                "Source": source,
                "Normalized": helper.normalize(name),
            })
    for world, matrix in MATRICES.items():
        for left in matrix["left"]:
            for right in matrix["right"]:
                if left.lower() == right.lower():
                    continue
                sequence += 1
                name = f"{left} {right}"
                rows.append({
                    "RawID": str(sequence),
                    "Name": name,
                    "World": world,
                    "Exercise": "13",
                    "ExerciseName": EXERCISES[13],
                    "Form": "compound matrix",
                    "Source": matrix["source"],
                    "Normalized": helper.normalize(name),
                })
    return rows


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    helper, (history, history_source_counts) = load_history()
    raw = build_raw(helper)
    fields = ["RawID", "Name", "World", "Exercise", "ExerciseName", "Form", "Source", "Normalized"]
    write_csv(HERE / "raw-pool.csv", raw, fields)

    seen: dict[str, str] = {}
    survivors: list[dict[str, str]] = []
    rejections: list[dict[str, str]] = []
    for row in raw:
        norm = row["Normalized"]
        if norm in history:
            rejections.append({**row, "RejectReason": "historical exact", "Collision": history[norm]})
        elif norm in seen:
            rejections.append({**row, "RejectReason": "internal duplicate", "Collision": seen[norm]})
        else:
            seen[norm] = row["Name"]
            survivors.append(row)

    write_csv(HERE / "deduped-pool.csv", survivors, fields)
    write_csv(HERE / "dedupe-rejections.csv", rejections, fields + ["RejectReason", "Collision"])

    audit = {
        "raw_count": len(raw),
        "raw_by_world": dict(Counter(row["World"] for row in raw)),
        "raw_by_exercise": dict(Counter(row["Exercise"] for row in raw)),
        "historical_index_count": len(history),
        "deduped_count": len(survivors),
        "deduped_by_world": dict(Counter(row["World"] for row in survivors)),
        "deduped_by_exercise": dict(Counter(row["Exercise"] for row in survivors)),
        "rejections": len(rejections),
        "rejection_reasons": dict(Counter(row["RejectReason"] for row in rejections)),
        "largest_history_sources": history_source_counts.most_common(12),
    }
    (HERE / "pool-audit.json").write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(audit, indent=2))


if __name__ == "__main__":
    main()
