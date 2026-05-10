def chatbot():
    print("🤖 Engineering Admission Chatbot")
    print("Ask about admission, marks, fees, departments, exams, documents")
    print("Type 'exit' to stop\n")

    while True:
        user = input("You: ").lower()

        if user == "exit":
            print("Bot: Thank you! Best of luck for your admission 👋")
            break

        elif "admission" in user:
            print("Bot: Admission process includes entrance exam, merit list, CAP rounds, and document verification.")

        elif "eligibility" in user:
            print("Bot: You must pass 12th with Physics, Chemistry, and Mathematics.")

        elif "marks" in user or "percentage" in user:
            print("Bot: Minimum 50% marks required (45% for reserved category).")

        elif "entrance" in user or "exam" in user:
            print("Bot: You can appear for JEE or MHT-CET for engineering admission.")

        elif "fees" in user:
            print("Bot: Fees range from ₹50,000 to ₹2,00,000 per year depending on college.")

        elif "department" in user or "branch" in user:
            print("Bot: Available departments include Computer, IT, Mechanical, Civil, Electronics, and AI/DS.")

        elif "computer" in user:
            print("Bot: Computer Engineering focuses on programming, AI, and software development.")

        elif "mechanical" in user:
            print("Bot: Mechanical Engineering deals with machines, thermodynamics, and manufacturing.")

        elif "civil" in user:
            print("Bot: Civil Engineering focuses on construction, buildings, and infrastructure.")

        elif "it" in user:
            print("Bot: IT focuses on networking, databases, and software systems.")

        elif "documents" in user:
            print("Bot: Required documents: 10th & 12th marksheet, CET/JEE scorecard, ID proof, photos.")

        elif "college" in user:
            print("Bot: Admission is done through CAP (Centralized Admission Process).")

        elif "cutoff" in user:
            print("Bot: Cutoff depends on college, branch, and entrance exam score.")

        elif "hostel" in user:
            print("Bot: Most colleges provide hostel facilities with separate fees.")

        elif "placement" in user:
            print("Bot: Top colleges provide good placements with companies like TCS, Infosys, etc.")

        else:
            print("Bot: Sorry, I didn’t understand. Ask about marks, fees, departments, exams, etc.")


# Run chatbot
chatbot()
