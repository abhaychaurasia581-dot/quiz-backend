
from quiz.models import Question, Option

data = [
    {
        "text": "What does HTML stand for?",
        "options": [
            {"text": "HyperText Markup Language", "is_correct": True},
            {"text": "HighText Machine Language", "is_correct": False},
            {"text": "Hyperloop Text Markup Language", "is_correct": False},
            {"text": "None of the above", "is_correct": False},
        ]
    },
    {
        "text": "Which company created React?",
        "options": [
            {"text": "Google", "is_correct": False},
            {"text": "Microsoft", "is_correct": False},
            {"text": "Facebook (Meta)", "is_correct": True},
            {"text": "Twitter", "is_correct": False},
        ]
    },
    {
        "text": "What is the correct file extension for Python files?",
        "options": [
            {"text": ".js", "is_correct": False},
            {"text": ".py", "is_correct": True},
            {"text": ".pt", "is_correct": False},
            {"text": ".python", "is_correct": False},
        ]
    },
]

for item in data:
    q = Question.objects.create(text=item["text"])
    for opt in item["options"]:
        Option.objects.create(question=q, **opt)

print(f"✅ Created {len(data)} questions!")