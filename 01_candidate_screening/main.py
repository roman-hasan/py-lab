candidate_name = input("Candidate Full Name: ").strip().title()
candidate_age = int(input("Candidate Age: "))
education_level = input("Education Level (Bachelor's / Master's): ").strip().lower()
years_of_experience = int(input("Years of Experience (Number): "))
has_relevant_experience = input("Relevant Experience (Yes/No): ").strip().lower() == "yes"
skills_score = int(input("Skills Assessment Score: "))
interview_score = int(input("Interview Assessment Score: "))
is_available = input("Available for Joining (Yes/No): ").strip().lower() == "yes"


hiring_status = None
offered_salary = 0
performance_bonus = 0
decision_reason = ""

is_eligible_by_age = candidate_age >= 18
is_eligible_by_education = education_level == "bachelor's" or education_level == "master's"
is_eligible_by_experience = years_of_experience >= 1

is_eligible_by_assessment = skills_score >= 60 and interview_score >= 60


# Hiring Decision

if not is_eligible_by_age or not is_eligible_by_education or not is_eligible_by_experience or not is_available:
    hiring_status = "Rejected"
    if not is_eligible_by_age:
        decision_reason = "Minimum age requirement not met."
    elif not is_eligible_by_education:
        decision_reason = "Education requirement not met."
    elif not is_eligible_by_experience:
        decision_reason = "Minimum experience requirement not met."
    elif not is_available:
        decision_reason = "Joining availability not confirmed."

else:

    if not is_eligible_by_assessment:
        hiring_status = "On Hold"
        if skills_score < 60:
            decision_reason += "Skills assessment score below minimum requirement. \n"
        if interview_score < 60:
            decision_reason += "Interview assessment score below minimum requirement. \n"

    else:
        hiring_status = "Selected"

        if years_of_experience <= 2:
            offered_salary = 30000
        elif years_of_experience <= 5:
            offered_salary = 40000
        else:
            offered_salary = 50000

        if skills_score >= 80 and interview_score >= 80:
            performance_bonus = 5000
            offered_salary += performance_bonus

        if not has_relevant_experience:
            offered_salary -= 5000


# Final Assessment Report

print("\n ******* Candidate Assessment Report *******")
print(f"Candidate Name: {candidate_name}")
print(f"Hiring Status: {hiring_status}")
print(f"Decision Reason: {decision_reason if decision_reason else 'No issues found.'}")
print(f"Monthly Salary Offer: {offered_salary}")
