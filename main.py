def build_roster(registrations):
    rosters = {}  # course_id -> set of student_ids

    # Build sets of students per course (automatically removes duplicates)
    for student_id, course_id in registrations:
        if course_id not in rosters:
            rosters[course_id] = set()
        rosters[course_id].add(student_id)

    # Convert each set to a sorted list
    final_result = {}
    for course_id, students in rosters.items():
        final_result[course_id] = sorted(students)

    return final_result


if __name__ == "__main__":
    # Optional manual test
    sample = [
        ("s1", "CS101"),
        ("s2", "CS101"),
        ("s1", "MATH200"),
        ("s1", "CS101"),  # duplicate registration
    ]
    print(build_roster(sample))
