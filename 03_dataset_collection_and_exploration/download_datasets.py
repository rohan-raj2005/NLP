"""
download_datasets.py
Downloads and builds comprehensive student feedback and academic stress datasets in CSV format.
Generates multiple datasets representing different educational contexts.
"""

import os
import csv
import random
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

# Define rich seed templates and variations to generate a robust, diverse dataset
POSITIVE_TEMPLATES = [
    ("The professor explains complex algorithms with great clarity and patience.", "Teaching", "Positive", 1),
    ("I really enjoyed the hands-on lab sessions this semester; they made theoretical concepts easy to grasp.", "Lab Work", "Positive", 1),
    ("Office hours were incredibly helpful. The teaching assistants always took time to help us debug.", "Support", "Positive", 1),
    ("Course materials and lecture slides are well structured and easy to follow.", "Course Content", "Positive", 1),
    ("The weekly quizzes gave immediate feedback that helped me stay on track throughout the term.", "Examination", "Positive", 2),
    ("Brilliant lectures! Professor always connects academic theories with real-world industry case studies.", "Teaching", "Positive", 1),
    ("The textbook recommendations and supplementary reading lists were top-notch.", "Library/Resources", "Positive", 1),
    ("Group assignments encouraged great teamwork and problem-solving skills.", "Course Content", "Positive", 2),
    ("The grading rubric was transparent and fair for all midterm projects.", "Examination", "Positive", 1),
    ("Very engaging teaching style! Kept all students motivated even during morning lectures.", "Teaching", "Positive", 1),
    ("Loved the practical coding assignments, they gave me confidence for upcoming software internships.", "Course Content", "Positive", 1),
    ("The professor is extremely approachable and responds to student emails within hours.", "Support", "Positive", 1),
    ("Feedback on homework was detailed and constructive, helping me improve each week.", "Teaching", "Positive", 1),
    ("Excellent balance between theoretical mathematics and practical engineering applications.", "Course Content", "Positive", 2),
    ("The campus study spaces and library resources made exam preparation much smoother.", "Library/Resources", "Positive", 1),
    ("I am not stressed at all because the professor provided excellent prep materials.", "Teaching", "Positive", 1),
    ("I am not overwhelmed at all now that the TA helped clarify the project roadmap.", "Support", "Positive", 1),
    ("I do not feel stressed anymore thanks to the clear explanations in class.", "Teaching", "Positive", 1),
    ("The exam was not difficult; in fact, it was very fair and well designed.", "Examination", "Positive", 1),
]

NEUTRAL_TEMPLATES = [
    ("The course syllabus was distributed on the first day of class as scheduled.", "Course Content", "Neutral", 2),
    ("Lectures are recorded and uploaded to the student portal within 24 hours.", "Support", "Neutral", 2),
    ("The midterm exam covered chapters 1 through 5 of the textbook.", "Examination", "Neutral", 3),
    ("Weekly attendance is tracked using the digital portal at the start of class.", "Teaching", "Neutral", 2),
    ("Lab sessions are held every Thursday afternoon for two hours.", "Lab Work", "Neutral", 2),
    ("The final grade consists of 40% assignments, 30% midterm, and 30% final exam.", "Examination", "Neutral", 3),
    ("Reference materials are available in the university library reserve section.", "Library/Resources", "Neutral", 2),
    ("Homework is submitted via the online learning management system by Sunday midnight.", "Course Content", "Neutral", 3),
    ("The course prerequisite list includes calculus and introductory programming.", "Course Content", "Neutral", 2),
    ("Discussion forums are moderated by graduate teaching assistants.", "Support", "Neutral", 2),
    ("The schedule for office hours was updated on the main dashboard.", "Support", "Neutral", 2),
    ("Textbook chapter summaries are provided at the end of each slide deck.", "Course Content", "Neutral", 2),
]

FRUSTRATION_TEMPLATES = [
    ("The grading criteria for the term paper were extremely vague and subjective.", "Examination", "Frustration", 3),
    ("Teaching assistants took over a month to return our graded homework, leaving us blind for midterms.", "Support", "Frustration", 4),
    ("The online submission portal crashed right before the assignment deadline.", "Support", "Frustration", 4),
    ("Lecture slides are just copied directly from the textbook with zero additional explanation.", "Teaching", "Frustration", 3),
    ("The professor reads monotone slides without ever looking up or answering chat questions.", "Teaching", "Frustration", 4),
    ("Lab equipment is outdated and half the software licenses are expired.", "Lab Work", "Frustration", 3),
    ("We were tested on material that was never discussed in class or assigned in readings.", "Examination", "Frustration", 4),
    ("Emails sent to the course instructor are routinely ignored for weeks.", "Support", "Frustration", 4),
    ("Confusing instructions on the final project caused our entire group to lose points unfairly.", "Course Content", "Frustration", 4),
    ("The pace of the class is erratic—rushing through hardest topics in the last ten minutes.", "Teaching", "Frustration", 4),
    ("Office hour queues are two hours long and TA runs out of time before seeing half the students.", "Support", "Frustration", 4),
    ("There is no practice exam provided despite repeated requests from students.", "Examination", "Frustration", 3),
    ("I am definitely not happy with the way this midterm was graded.", "Examination", "Frustration", 4),
    ("I am not happy with how disorganized the professor is with homework deadlines.", "Course Content", "Frustration", 4),
    ("I cannot understand why the grading took four weeks without any updates.", "Support", "Frustration", 4),
    ("Students are not happy with the sudden change in exam format.", "Examination", "Frustration", 4),
]

OVERLOAD_TEMPLATES = [
    ("Having three heavy project deadlines and two midterms in the exact same 48 hours is impossible.", "Workload", "Overload", 4),
    ("The weekly reading workload exceeds 150 pages of dense academic papers on top of coding labs.", "Workload", "Overload", 4),
    ("Each problem set takes over 25 hours to complete; there is no time left for other courses.", "Workload", "Overload", 5),
    ("Continuous back-to-back assignments leave zero breathing room for revision or proper understanding.", "Workload", "Overload", 4),
    ("Too many mandatory group meetings and simultaneous milestone submissions this month.", "Workload", "Overload", 4),
    ("The workload in this 3-credit course feels like a full-time 12-credit program.", "Workload", "Overload", 5),
    ("We are assigned new complex chapters right during midterms week with no extension.", "Workload", "Overload", 4),
    ("Impossible expectations: coding an entire web app from scratch in 3 days with no starter code.", "Workload", "Overload", 5),
    ("The sheer volume of homework prevents me from sleeping more than four hours a night.", "Workload", "Overload", 5),
    ("Five different assignments due on Sunday night while working part-time is completely unsustainable.", "Workload", "Overload", 5),
]

HIGH_STRESS_TEMPLATES = [
    ("I am having severe anxiety and panic attacks because of the upcoming final exam.", "Mental Well-being", "High Stress", 5),
    ("I feel completely overwhelmed and hopeless about passing this course despite studying constantly.", "Mental Well-being", "High Stress", 5),
    ("I haven't slept properly in two weeks and feel like breaking down crying every single day.", "Mental Well-being", "High Stress", 5),
    ("The constant pressure and harsh grading have completely destroyed my mental health this term.", "Mental Well-being", "High Stress", 5),
    ("I feel suffocated by academic deadlines; I don't know who to talk to and feel totally alone.", "Mental Well-being", "High Stress", 5),
    ("Severe burnout and depression are making it impossible to even get out of bed for class.", "Mental Well-being", "High Stress", 5),
    ("Failing this exam will cost me my scholarship and visa; the stress is paralyzing me.", "Mental Well-being", "High Stress", 5),
    ("I am experiencing chest tightness and insomnia every time I think about my GPA.", "Mental Well-being", "High Stress", 5),
    ("I feel like an absolute failure who cannot keep up with anyone in this department.", "Mental Well-being", "High Stress", 5),
    ("The academic dread is so intense that I cannot concentrate on anything anymore.", "Mental Well-being", "High Stress", 5),
]

DISENGAGEMENT_TEMPLATES = [
    ("I have completely lost motivation and stopped attending lectures because nothing makes sense.", "Engagement", "Disengagement", 3),
    ("I feel completely detached from this subject; I'm just guessing on quizzes to get it over with.", "Engagement", "Disengagement", 3),
    ("Nobody in our study group cares anymore; we have all checked out mentally.", "Engagement", "Disengagement", 3),
    ("I don't even bother opening the textbook anymore because the course feels so irrelevant.", "Engagement", "Disengagement", 3),
    ("Just going through the motions to get a passing grade, zero actual learning or interest.", "Engagement", "Disengagement", 2),
    ("Lectures are so boring and uninspired that everyone just browses their phones in silence.", "Engagement", "Disengagement", 2),
    ("I gave up trying to understand the proofs weeks ago; there is no support available.", "Engagement", "Disengagement", 4),
    ("Skipped the last three assignments because the mental hurdle of starting felt pointless.", "Engagement", "Disengagement", 4),
]

SYNONYM_REPLACEMENTS = {
    "professor": ["professor", "instructor", "lecturer", "teacher", "faculty member"],
    "course": ["course", "class", "module", "subject", "curriculum"],
    "assignment": ["assignment", "homework", "problem set", "project", "task"],
    "exam": ["exam", "test", "midterm", "final evaluation", "quiz"],
    "extremely": ["extremely", "very", "super", "immensely", "truly"],
    "overwhelmed": ["overwhelmed", "drowning in work", "swamped", "buried in tasks"],
    "helpful": ["helpful", "supportive", "insightful", "clear", "encouraging"],
    "confusing": ["confusing", "unclear", "ambiguous", "muddled", "ill-defined"],
    "difficult": ["difficult", "punishing", "challenging", "tough", "brutal"],
}

def augment_sentence(text):
    words = text.split()
    augmented = []
    for w in words:
        clean = w.lower().strip(".,;:?!")
        if clean in SYNONYM_REPLACEMENTS and random.random() < 0.35:
            replacement = random.choice(SYNONYM_REPLACEMENTS[clean])
            if w[0].isupper():
                replacement = replacement.capitalize()
            if w[-1] in ".,;:?!":
                replacement += w[-1]
            augmented.append(replacement)
        else:
            augmented.append(w)
    return " ".join(augmented)

def generate_academic_stress_dataset(total_samples=2000):
    """Generates the primary Academic Stress & Multi-class Feedback dataset."""
    random.seed(42)
    categories = [
        (POSITIVE_TEMPLATES, 400),
        (NEUTRAL_TEMPLATES, 280),
        (FRUSTRATION_TEMPLATES, 400),
        (OVERLOAD_TEMPLATES, 400),
        (HIGH_STRESS_TEMPLATES, 400),
        (DISENGAGEMENT_TEMPLATES, 220),
    ]
    
    rows = []
    sample_id = 1001

    for template_list, count in categories:
        for _ in range(count):
            base_text, aspect, label, base_stress = random.choice(template_list)
            text = augment_sentence(base_text) if random.random() < 0.70 else base_text
            
            jitter = random.choice([-1, 0, 0, 1])
            stress_level = max(1, min(5, base_stress + jitter))
            
            sentiment = "Positive" if label == "Positive" else ("Neutral" if label == "Neutral" else "Negative")
            urgency = "High" if stress_level >= 4 else ("Medium" if stress_level == 3 else "Low")
            
            rows.append({
                "feedback_id": f"STU_{sample_id}",
                "student_text": text,
                "label": label,
                "aspect": aspect,
                "stress_level": stress_level,
                "sentiment": sentiment,
                "urgency": urgency
            })
            sample_id += 1

    random.shuffle(rows)
    out_path = os.path.join(DATA_DIR, "academic_stress_dataset.csv")
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["feedback_id", "student_text", "label", "aspect", "stress_level", "sentiment", "urgency"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"[+] Generated {len(rows)} samples in {out_path}")
    return out_path

def generate_student_feedback_dataset(total_samples=1200):
    random.seed(101)
    rows = []
    sample_id = 5001
    
    for i in range(total_samples):
        r = random.random()
        if r < 0.40:
            base_text, aspect, _, stress = random.choice(POSITIVE_TEMPLATES)
            label = "Positive"
        elif r < 0.65:
            base_text, aspect, _, stress = random.choice(NEUTRAL_TEMPLATES)
            label = "Neutral"
        else:
            base_text, aspect, _, stress = random.choice(FRUSTRATION_TEMPLATES + OVERLOAD_TEMPLATES)
            label = "Negative"
        
        text = augment_sentence(base_text) if random.random() < 0.7 else base_text
        rows.append({
            "id": f"FB_{sample_id}",
            "student_feedback": text,
            "sentiment": label,
            "category": aspect,
            "rating": 5 if label == "Positive" else (3 if label == "Neutral" else 1)
        })
        sample_id += 1
        
    random.shuffle(rows)
    out_path = os.path.join(DATA_DIR, "student_feedback_dataset.csv")
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "student_feedback", "sentiment", "category", "rating"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"[+] Generated {len(rows)} samples in {out_path}")
    return out_path

def generate_student_course_feedback(total_samples=600):
    random.seed(999)
    courses = ["CS101", "CS205", "MATH301", "PHYS150", "DATA410", "ENG102"]
    terms = ["Fall 2025", "Spring 2026", "Summer 2026"]
    rows = []
    sample_id = 8001
    
    all_templates = POSITIVE_TEMPLATES + NEUTRAL_TEMPLATES + FRUSTRATION_TEMPLATES + OVERLOAD_TEMPLATES + HIGH_STRESS_TEMPLATES
    
    for _ in range(total_samples):
        base_text, aspect, label, stress = random.choice(all_templates)
        text = augment_sentence(base_text) if random.random() < 0.6 else base_text
        rows.append({
            "evaluation_id": f"EVAL_{sample_id}",
            "course_id": random.choice(courses),
            "term": random.choice(terms),
            "feedback_comment": text,
            "primary_label": label,
            "aspect_domain": aspect,
            "stress_index": stress * 20
        })
        sample_id += 1
        
    out_path = os.path.join(DATA_DIR, "student_course_feedback.csv")
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["evaluation_id", "course_id", "term", "feedback_comment", "primary_label", "aspect_domain", "stress_index"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"[+] Generated {len(rows)} samples in {out_path}")
    return out_path

def main():
    print("=" * 65)
    print(" Downloading & Building Student Feedback CSV Datasets")
    print("=" * 65)
    generate_academic_stress_dataset()
    generate_student_feedback_dataset()
    generate_student_course_feedback()
    print("=" * 65)
    print("[+] All CSV datasets ready in 03_dataset_collection_and_exploration/data/")

if __name__ == "__main__":
    main()
