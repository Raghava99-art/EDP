import csv
from pathlib import Path
from app.services.search_engine import get_search_engine

DATA = Path(__file__).resolve().parents[1] / "data" / "sample_questions.csv"

def main():
    engine = get_search_engine()
    total = 0
    correct = 0
    with DATA.open(newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            results = engine.search(row["question"], top_k=1)
            predicted = results[0]["category"] if results else "No result"
            expected = row["expected_category"]
            hit = predicted.casefold() == expected.casefold()
            total += 1
            correct += int(hit)
            print(f"Q: {row['question']}\nExpected: {expected} | Predicted: {predicted} | {'PASS' if hit else 'CHECK'}\n")
    print(f"Top-1 category match: {correct}/{total} ({correct / total:.1%})")

if __name__ == "__main__":
    main()
