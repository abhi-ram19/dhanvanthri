#symptoms checker
symptoms_data = {
    "cold": {
        "symptoms": ["runny nose", "sneezing", "sore throat", "cough"],
        "description": "A common viral infection with mild symptoms. Rest, fluids, and over-the-counter meds help."
    },
    "flu": {
        "symptoms": ["fever", "chills", "body ache", "fatigue", "cough"],
        "description": "A viral infection causing fever and fatigue. Stay hydrated and rest well."
    },
    "covid-19": {
        "symptoms": ["fever", "dry cough", "loss of taste", "loss of smell", "fatigue"],
        "description": "Coronavirus infection. Isolate and consult a doctor if symptoms worsen."
    },
    "allergy": {
        "symptoms": ["sneezing", "itchy eyes", "runny nose"],
        "description": "Reaction to allergens. Antihistamines may help."
    },
    "asthma": {
        "symptoms": ["shortness of breath", "chest tightness", "wheezing", "cough"],
        "description": "Chronic lung condition. Use inhaler and avoid triggers."
    },
    "migraine": {
        "symptoms": ["headache", "nausea", "sensitivity to light", "visual disturbances"],
        "description": "Severe headache often accompanied by nausea and light sensitivity."
    },
    "diabetes": {
        "symptoms": ["frequent urination", "increased thirst", "fatigue", "blurred vision"],
        "description": "A chronic condition that affects blood sugar regulation. Consult a doctor."
    },
    "hypertension": {
        "symptoms": ["headache", "dizziness", "blurred vision", "shortness of breath"],
        "description": "High blood pressure. Monitor regularly and take prescribed medication."
    },
    "anemia": {
        "symptoms": ["fatigue", "pale skin", "shortness of breath", "dizziness"],
        "description": "Low red blood cell count. Iron supplements and diet can help."
    },
    "dehydration": {
        "symptoms": ["dry mouth", "fatigue", "dark urine", "dizziness"],
        "description": "Lack of adequate fluids. Increase water intake immediately."
    },
    "food poisoning": {
        "symptoms": ["vomiting", "diarrhea", "stomach cramps", "fever"],
        "description": "Caused by contaminated food. Hydrate and rest; seek help if severe."
    },
    "malaria": {
        "symptoms": ["fever", "chills", "sweating", "headache", "nausea"],
        "description": "Parasitic infection from mosquito bites. Immediate treatment needed."
    },
    "typhoid": {
        "symptoms": ["high fever", "abdominal pain", "weakness", "loss of appetite"],
        "description": "Bacterial infection from contaminated food/water. Antibiotics required."
    },
    "pneumonia": {
        "symptoms": ["fever", "cough", "chest pain", "shortness of breath"],
        "description": "Lung infection. May need antibiotics or hospitalization."
    },
    "bronchitis": {
        "symptoms": ["cough with mucus", "chest discomfort", "fatigue", "mild fever"],
        "description": "Inflammation of bronchial tubes. Rest and fluids help."
    },
    "sinusitis": {
        "symptoms": ["facial pain", "nasal congestion", "headache", "runny nose"],
        "description": "Sinus infection causing facial pressure. Decongestants may help."
    },
    "conjunctivitis": {
        "symptoms": ["red eyes", "itchy eyes", "watery discharge", "swollen eyelids"],
        "description": "Also known as pink eye. Often viral; maintain eye hygiene."
    },
    "chickenpox": {
        "symptoms": ["itchy rash", "fever", "fatigue", "loss of appetite"],
        "description": "Viral infection with blisters. Isolate and rest."
    },
    "measles": {
        "symptoms": ["rash", "fever", "cough", "red eyes", "runny nose"],
        "description": "Highly contagious virus. Vaccination prevents it."
    },
    "mumps": {
        "symptoms": ["swollen cheeks", "jaw pain", "fever", "headache"],
        "description": "Viral infection causing swollen glands. Rest and fluids help."
    },
    "hepatitis A": {
        "symptoms": ["jaundice", "fatigue", "abdominal pain", "dark urine"],
        "description": "Liver infection from contaminated food. Usually self-limiting."
    },
    "hepatitis B": {
        "symptoms": ["jaundice", "nausea", "abdominal discomfort", "fatigue"],
        "description": "Serious liver infection. Requires medical monitoring."
    },
    "urinary tract infection": {
        "symptoms": ["burning urination", "frequent urination", "pelvic pain", "cloudy urine"],
        "description": "Common bacterial infection. Antibiotics needed."
    },
    "appendicitis": {
        "symptoms": ["lower right abdominal pain", "nausea", "fever", "loss of appetite"],
        "description": "Inflamed appendix. Needs urgent medical attention."
    },
    "arthritis": {
        "symptoms": ["joint pain", "stiffness", "swelling", "reduced motion"],
        "description": "Inflammation of joints. Pain management and therapy can help."
    },
    "tuberculosis": {
        "symptoms": ["chronic cough", "weight loss", "fever", "night sweats"],
        "description": "Bacterial lung infection. Long-term treatment needed."
    },
    "depression": {
        "symptoms": ["persistent sadness", "loss of interest", "fatigue", "sleep issues"],
        "description": "Mental health condition. Professional support recommended."
    },
    "anxiety": {
        "symptoms": ["excessive worry", "restlessness", "racing heart", "difficulty concentrating"],
        "description": "Mental health condition. Therapy and relaxation techniques help."
    },
    "eczema": {
        "symptoms": ["dry skin", "itching", "red patches", "swelling"],
        "description": "Skin condition causing irritation. Moisturizers and creams relieve symptoms."
    },
    "psoriasis": {
        "symptoms": ["red patches", "scaly skin", "itching", "joint pain"],
        "description": "Chronic skin condition. Medications can reduce symptoms."
    },
    "dengue": {
        "symptoms": ["high fever", "headache", "muscle pain", "skin rash", "nausea"],
        "description": "Mosquito-borne viral illness. Requires hydration and rest."
    },
    "chikungunya": {
        "symptoms": ["joint pain", "fever", "rash", "headache", "muscle pain"],
        "description": "Viral infection spread by mosquitoes. Rest and pain relief recommended."
    },
    "gastroenteritis": {
        "symptoms": ["diarrhea", "vomiting", "stomach cramps", "fever"],
        "description": "Inflammation of the stomach and intestines. Stay hydrated."
    },
    "tonsillitis": {
        "symptoms": ["sore throat", "difficulty swallowing", "fever", "swollen tonsils"],
        "description": "Inflammation of tonsils. May be viral or bacterial."
    },
    "otitis media": {
        "symptoms": ["ear pain", "hearing loss", "fever", "fluid discharge"],
        "description": "Middle ear infection, common in children. May need antibiotics."
    },
    "whooping cough": {
        "symptoms": ["severe coughing", "vomiting after coughing", "fatigue", "runny nose"],
        "description": "Bacterial infection. Vaccine-preventable and treated with antibiotics."
    },
    "rheumatic fever": {
        "symptoms": ["fever", "joint pain", "rash", "chest pain"],
        "description": "Inflammatory disease following strep throat. Needs medical treatment."
    },
    "scabies": {
        "symptoms": ["intense itching", "rash", "blisters", "burrow tracks"],
        "description": "Skin infestation by mites. Requires medicated creams."
    },
    "ringworm": {
        "symptoms": ["circular rash", "itchy skin", "red patches", "scaling"],
        "description": "Fungal infection of the skin. Antifungal cream helps."
    },
    "impetigo": {
        "symptoms": ["red sores", "blisters", "itching", "crusting"],
        "description": "Highly contagious bacterial skin infection. Treat with antibiotics."
    },
    "cholecystitis": {
        "symptoms": ["upper right abdominal pain", "nausea", "vomiting", "fever"],
        "description": "Inflamed gallbladder. May require surgery."
    },
    "pancreatitis": {
        "symptoms": ["abdominal pain", "nausea", "vomiting", "fever"],
        "description": "Inflammation of pancreas. Requires hospitalization in severe cases."
    },
    "gallstones": {
        "symptoms": ["abdominal pain", "nausea", "indigestion", "jaundice"],
        "description": "Hardened deposits in the gallbladder. May need surgical removal."
    },
    "acid reflux": {
        "symptoms": ["heartburn", "chest pain", "regurgitation", "difficulty swallowing"],
        "description": "Stomach acid flows into esophagus. Antacids can help."
    },
    "ibs": {
        "symptoms": ["abdominal pain", "bloating", "diarrhea", "constipation"],
        "description": "Chronic bowel disorder. Managed with diet and stress control."
    },
    "celiac disease": {
        "symptoms": ["diarrhea", "bloating", "fatigue", "weight loss"],
        "description": "Immune reaction to gluten. Requires lifelong gluten-free diet."
    },
    "lactose intolerance": {
        "symptoms": ["bloating", "gas", "diarrhea", "abdominal pain"],
        "description": "Inability to digest lactose. Avoid dairy products."
    }
}

# disease data ,first aid data,first_aid_names,hospitals
first_aid_names = [
    "Emergency Bleeding", "Minor Burns", "Nosebleed", "Choking (Adult)", "Fainting",
    "Fracture", "Seizure", "Poisoning", "Heat Stroke", "Hypothermia",
    "Sprain", "Eye Injury", "Electric Shock", "Animal Bite", "Bee Sting",
    "Chemical Burn", "Heart Attack", "Asthma Attack", "Drowning", "Head Injury",
    "CPR", "Allergic Reaction", "Diabetic Emergency", "Shock", "Object in Eye"
]

first_aid_keys = [
    "emergency_bleeding", "minor_burns", "nosebleed", "choking_adult", "fainting",
    "fracture", "seizure", "poisoning", "heat_stroke", "hypothermia",
    "sprain", "eye_injury", "electric_shock", "animal_bite", "bee_sting",
    "chemical_burn", "heart_attack", "asthma_attack", "drowning", "head_injury",
    "cpr", "allergic_reaction", "diabetic_emergency", "shock", "object_in_eye"
]


first_aid_mapping = {str(i + 1): key for i, key in enumerate(first_aid_keys)}

# Sample first aid data
first_aid_data = {
    
    "emergency_bleeding": (
        "🆘 *First Aid Guide – Emergency Bleeding*\n\n"
        "1️⃣ Clean the wound gently with *hydrogen peroxide* or clean water.\n"
        "2️⃣ Use a clean *cloth or cotton* to apply pressure and stop bleeding.\n"
        "3️⃣ Take a painkiller like *Paracetamol* if available.\n\n"
        "⚠️ *Note:* If the bleeding is severe or the accident is serious, consult a doctor immediately."
    ),

    "burns_minor": (
        "🔥 *First Aid Guide – Minor Burns*\n\n"
        "1️⃣ Cool the burn under *cold running water* for at least 10 minutes.\n"
        "2️⃣ Avoid applying *ice, butter, or toothpaste*.\n"
        "3️⃣ Cover with a *clean non-stick bandage*.\n\n"
        "⚠️ *Note:* For large or facial burns, seek medical help immediately."
    ),

    "nosebleed": (
        "👃 *First Aid Guide – Nosebleed*\n\n"
        "1️⃣ Sit upright and *lean slightly forward*.\n"
        "2️⃣ Pinch the *soft part* of your nose for 10 minutes.\n"
        "3️⃣ Apply a *cold compress* on the nose bridge.\n\n"
        "⚠️ *Note:* If bleeding continues beyond 20 minutes, get medical help."
    ),

    "choking_adult": (
        "😮 *First Aid Guide – Choking (Adult)*\n\n"
        "1️⃣ Ask if the person can *cough or speak*.\n"
        "2️⃣ If not, perform the *Heimlich maneuver*.\n"
        "3️⃣ Give *inward and upward abdominal thrusts* until the object is dislodged.\n\n"
        "⚠️ *Note:* Call emergency services if they become unconscious."
    ),

    "fainting": (
        "😵 *First Aid Guide – Fainting*\n\n"
        "1️⃣ Lay the person *flat on their back*.\n"
        "2️⃣ Elevate their legs *12 inches above the heart*.\n"
        "3️⃣ Loosen any *tight clothing*.\n\n"
        "⚠️ *Note:* If unresponsive for over a minute, call emergency help."
    ),

    "fracture": (
        "🦴 *First Aid Guide – Fracture (Broken Bone)*\n\n"
        "1️⃣ *Immobilize* the injured area using a splint.\n"
        "2️⃣ *Do not attempt* to realign the bone.\n"
        "3️⃣ Apply a *cold pack* to reduce swelling.\n\n"
        "⚠️ *Note:* Get professional medical assistance immediately."
    ),

    "seizure": (
        "⚡ *First Aid Guide – Seizure*\n\n"
        "1️⃣ *Do not restrain* the person.\n"
        "2️⃣ Move objects away to prevent injury.\n"
        "3️⃣ Turn them *on their side* after the seizure ends.\n\n"
        "⚠️ *Note:* Call for help if the seizure lasts more than 5 minutes."
    ),

    "poisoning": (
        "☠️ *First Aid Guide – Poisoning*\n\n"
        "1️⃣ Call *poison control or emergency services* immediately.\n"
        "2️⃣ Do *not induce vomiting* unless advised.\n"
        "3️⃣ Provide information about the substance ingested.\n\n"
        "⚠️ *Note:* Time is critical, act fast."
    ),

    "heatstroke": (
        "🌡️ *First Aid Guide – Heat Stroke*\n\n"
        "1️⃣ Move the person to a *cool and shaded area*.\n"
        "2️⃣ Remove excess clothing and apply *cool, wet cloths*.\n"
        "3️⃣ Give *sips of water* if conscious.\n\n"
        "⚠️ *Note:* Call emergency services immediately."
    ),

    "hypothermia": (
        "🥶 *First Aid Guide – Hypothermia*\n\n"
        "1️⃣ Move the person to a *warm, dry location*.\n"
        "2️⃣ Remove any *wet clothing*.\n"
        "3️⃣ Use *blankets* to gradually warm the person.\n\n"
        "⚠️ *Note:* Do not use direct heat; get medical help."
    ),

    "sprain": (
        "🦶 *First Aid Guide – Sprain*\n\n"
        "1️⃣ Follow the *R.I.C.E* method: Rest, Ice, Compress, Elevate.\n"
        "2️⃣ Apply a *cold pack* for 15-20 minutes every 2 hours.\n"
        "3️⃣ Use an *elastic bandage* for compression.\n\n"
        "⚠️ *Note:* If swelling or pain persists, consult a doctor."
    ),

    "eye_injury": (
        "👁️ *First Aid Guide – Eye Injury*\n\n"
        "1️⃣ Do *not rub* the eye.\n"
        "2️⃣ Rinse with *clean water or saline solution*.\n"
        "3️⃣ Cover the eye with a *sterile dressing*.\n\n"
        "⚠️ *Note:* Seek immediate medical attention."
    ),

    "electric_shock": (
        "⚡ *First Aid Guide – Electric Shock*\n\n"
        "1️⃣ *Do not touch* the person until the source is off.\n"
        "2️⃣ Turn off the power source *safely*.\n"
        "3️⃣ Check for *breathing and pulse*. Perform CPR if needed.\n\n"
        "⚠️ *Note:* Always call emergency services."
    ),

    "animal_bite": (
        "🐕 *First Aid Guide – Animal Bite*\n\n"
        "1️⃣ Wash the bite with *soap and water* for 5 minutes.\n"
        "2️⃣ Apply an *antiseptic*.\n"
        "3️⃣ Cover with a *clean bandage* and watch for signs of infection.\n\n"
        "⚠️ *Note:* Seek medical help for tetanus or rabies concerns."
    ),

    "bee_sting": (
        "🐝 *First Aid Guide – Bee Sting*\n\n"
        "1️⃣ Remove the stinger by *scraping* (not squeezing).\n"
        "2️⃣ Wash the area with *soap and water*.\n"
        "3️⃣ Apply *ice* to reduce swelling.\n\n"
        "⚠️ *Note:* Watch for signs of allergic reaction."
    ),

    "chemical_burn": (
        "🧪 *First Aid Guide – Chemical Burn*\n\n"
        "1️⃣ Remove any *contaminated clothing*.\n"
        "2️⃣ Rinse the skin with *running water for 20 minutes*.\n"
        "3️⃣ Cover with a *clean, dry cloth*.\n\n"
        "⚠️ *Note:* Seek urgent medical care."
    ),

    "heart_attack": (
        "❤️ *First Aid Guide – Heart Attack*\n\n"
        "1️⃣ Call *emergency services immediately*.\n"
        "2️⃣ Keep the person *calm and seated*.\n"
        "3️⃣ If available, give *aspirin* (unless allergic).\n"
        "4️⃣ *Monitor their breathing*. If they become unconscious and stop breathing, *start CPR immediately*.\n\n"
        "⚠️ *Note:* Do not let them walk or strain themselves."
    ),

    "asthma_attack": (
        "😤 *First Aid Guide – Asthma Attack*\n\n"
        "1️⃣ Help the person use their *inhaler*.\n"
        "2️⃣ Keep them calm and in a *seated position*.\n"
        "3️⃣ If breathing doesn’t improve, call emergency help.\n\n"
        "⚠️ *Note:* Do not leave them alone."
    ),

    "drowning": (
        "🌊 *First Aid Guide – Drowning*\n\n"
        "1️⃣ Pull the person to safety *without endangering yourself*.\n"
        "2️⃣ Check for *breathing and pulse*. Begin CPR if needed.\n"
        "3️⃣ Place them in the *recovery position* if breathing returns.\n\n"
        "⚠️ *Note:* Always call emergency help immediately."
    ),

    "head_injury": (
        "🧠 *First Aid Guide – Head Injury*\n\n"
        "1️⃣ Keep the person *still and calm*.\n"
        "2️⃣ Apply a *cold pack* to reduce swelling.\n"
        "3️⃣ Watch for *vomiting, drowsiness, or confusion*.\n\n"
        "⚠️ *Note:* Seek immediate medical attention if symptoms worsen."
    ),

    "cpr": (
        "❤️‍🩹 *First Aid Guide – CPR (Cardiopulmonary Resuscitation)*\n\n"
        "1️⃣ Check if the person is *unresponsive and not breathing* or only gasping.\n"
        "2️⃣ Call *emergency services* or ask someone nearby to do it.\n"
        "3️⃣ Place your hands *center of the chest*, one over the other.\n"
        "4️⃣ Push hard and fast – about *100 to 120 compressions per minute*, 2 inches deep.\n"
        "5️⃣ If trained, give *2 rescue breaths* after every 30 compressions.\n\n"
        "⚠️ *Note:* Don’t stop until medical help arrives or the person starts breathing."
    ),

    "allergic_reaction": (
        "🤧 *First Aid Guide – Allergic Reaction*\n\n"
        "1️⃣ Help the person take their *antihistamine or epinephrine injector (EpiPen)* if they have one.\n"
        "2️⃣ Keep them *calm and seated*.\n"
        "3️⃣ Monitor breathing – start CPR if necessary.\n\n"
        "⚠️ *Note:* Severe reactions require emergency services immediately."
    ),

    "diabetic_emergency": (
        "🍬 *First Aid Guide – Diabetic Emergency (Low Blood Sugar)*\n\n"
        "1️⃣ Give a *quick sugar source* like juice, candy, or glucose tablets.\n"
        "2️⃣ Let them rest and monitor for improvement.\n"
        "3️⃣ If unconscious, do *not give food or drink*. Call emergency help.\n\n"
        "⚠️ *Note:* High sugar is less urgent than low sugar. Treat low sugar fast."
    ),

    "shock": (
        "😨 *First Aid Guide – Shock*\n\n"
        "1️⃣ Lay the person down and *elevate their legs* unless injured.\n"
        "2️⃣ Keep them *warm and calm*.\n"
        "3️⃣ Do not give anything to eat or drink.\n\n"
        "⚠️ *Note:* Always call emergency help."
    ),

    "object_in_eye": (
        "🧼 *First Aid Guide – Object in Eye*\n\n"
        "1️⃣ Do *not rub the eye*.\n"
        "2️⃣ Rinse with *clean water or saline*.\n"
        "3️⃣ Blink several times or pull upper eyelid over lower to dislodge.\n\n"
        "⚠️ *Note:* If it doesn’t come out or causes severe pain, see an eye doctor immediately."
    )
}

disease_data = {
    "fever": {
        "description": "A fever is usually when your body temperature is 38°C or higher. You may feel warm, cold, or shivery.",
        "medication": "Take paracetamol / Dolo650 and stay hydrated.",
        "home_remedy": "Drink warm water with honey and ginger."
    },
    "cold": {
        "description": "A cold is a viral infection that causes sneezing, congestion, and a sore throat.",
        "medication": "Take antihistamines like Cetirizine.",
        "home_remedy": "Drink warm fluids and inhale steam."
    },
    "cough": {
        "description": "A cough is a reflex action to clear your airways of mucus and irritants.",
        "medication": "Use cough syrups like Benadryl.",
        "home_remedy": "Drink honey-lemon water."
    },
    "headache": {
        "description": "A headache can be caused by stress, dehydration, or lack of sleep.",
        "medication": "Take ibuprofen or paracetamol.",
        "home_remedy": "Rest in a quiet place and apply a cold compress."
    },
    "anemia": {
        "description": "Anemia is a condition where the body doesn't have enough red blood cells or hemoglobin.",
        "medication": "Take iron supplements or vitamin B12 injections.",
        "home_remedy": "Eat iron-rich foods, avoid tea and coffee, and take vitamin C supplements."
    },
    "bursitis": {
        "description": "Bursitis is an inflammation of the fluid-filled sacs that cushion joints and reduce friction.",
        "medication": "Take anti-inflammatory medication or pain relievers.",
        "home_remedy": "Apply ice or heat, rest the affected joint, and try physical therapy."
    },
    "cellulitis": {
        "description": "Cellulitis is a bacterial skin infection that causes redness, swelling, and pain.",
        "medication": "Take antibiotics or pain relievers.",
        "home_remedy": "Apply warm compresses, elevate the affected area, and rest."
    },
    "diverticulitis": {
        "description": "Diverticulitis is an inflammation of the diverticula, small pouches in the wall of the colon.",
        "medication": "Take antibiotics or pain relievers.",
        "home_remedy": "Follow a liquid diet, avoid solid foods, and try probiotics."
    },
    "gingivitis": {
        "description": "Gingivitis is an inflammation of the gums, which can cause redness, swelling, and bleeding.",
        "medication": "Use antibacterial mouthwash or take antibiotics.",
        "home_remedy": "Brush and floss regularly, avoid sugary foods, and try saltwater rinses."
    },
    "hypertension": {
        "description": "Hypertension is high blood pressure, which can increase the risk of heart disease and stroke.",
        "medication": "Take blood pressure medication or diuretics.",
        "home_remedy": "Exercise regularly, follow a low-sodium diet, and try stress-reducing techniques."
    },
    "menstrual_cramps": {
        "description": "Menstrual cramps cause painful cramps in the abdomen during menstruation.",
        "medication": "Take pain relievers or hormonal birth control.",
        "home_remedy": "Apply heat, try relaxation techniques, and exercise regularly."
    },
    "plantar_fasciitis": {
        "description": "Plantar fasciitis is an inflammation of the band of tissue that runs along the bottom of the foot.",
        "medication": "Take anti-inflammatory medication or pain relievers.",
        "home_remedy": "Apply ice or heat, stretch the foot, and try orthotics."
    },
    "rosacea": {
        "description": "Rosacea is a skin condition that causes redness, flushing, and acne-like symptoms.",
        "medication": "Take antibiotics or use topical creams.",
        "home_remedy": "Avoid triggers like spicy foods, use gentle skincare products, and try cool compresses."
    },
    "tendinitis": {
        "description": "Tendinitis is an inflammation of the tendons, which connect muscles to bones.",
        "medication": "Take anti-inflammatory medication or pain relievers.",
        "home_remedy": "Apply ice or heat, rest the affected area, and try physical therapy."
    },
    "piles": {
        "description": "Piles are swollen veins in the anus or rectum that can cause pain, itching, and bleeding.",
        "medication": "Take pain relievers, use creams or suppositories, or try oral medications.",
        "home_remedy": "Eat a high-fiber diet, stay hydrated, avoid straining during bowel movements, and try warm baths."
    },
    "tonsillitis": {
        "description": "Tonsillitis is an inflammation of the tonsils that can cause sore throat, fever, and difficulty swallowing.",
        "medication": "Take antibiotics or pain relievers.",
        "home_remedy": "Gargle with salt water, drink warm liquids, and try throat lozenges."
    },
    "acid_reflux": {
        "description": "Acid reflux is a condition where stomach acid flows back up into the esophagus, causing heartburn and discomfort.",
        "medication": "Take antacids or acid reducers.",
        "home_remedy": "Avoid triggers like spicy foods, eat smaller meals, and elevate your head while sleeping."
    },
    "athletes_foot": {
        "description": "Athlete's foot is a fungal infection that causes itching, redness, and cracking on the feet.",
        "medication": "Use antifungal creams or powders.",
        "home_remedy": "Keep your feet clean and dry, wear breathable shoes, and change your socks regularly."
    },
    "boils": {
        "description": "Boils are painful, pus-filled bumps on the skin that can cause fever and swelling.",
        "medication": "Apply antibiotic ointments or take oral antibiotics.",
        "home_remedy": "Apply warm compresses, avoid squeezing or popping the boil, and keep the area clean."
    },
    "canker_sores": {
        "description": "Canker sores are painful, open sores in the mouth that can cause discomfort and difficulty eating.",
        "medication": "Apply topical anesthetics or take oral pain relievers.",
        "home_remedy": "Avoid spicy or acidic foods, apply cold compresses, and try saltwater rinses."
    },
    "dermatitis": {
        "description": "Dermatitis is a skin condition that causes redness, itching, and inflammation.",
        "medication": "Use topical corticosteroids or take oral antihistamines.",
        "home_remedy": "Avoid triggers like soaps and detergents, apply cool compresses, and moisturize the skin."
    },
    "dry_eyes": {
        "description": "Dry eyes are a condition where the eyes don't produce enough tears, causing dryness and discomfort.",
        "medication": "Use artificial tears or take oral medications.",
        "home_remedy": "Blink regularly, avoid screens for long periods, and use humidifiers."
    },
    "earwax_buildup": {
        "description": "Earwax buildup is a condition where excess earwax accumulates in the ear canal, causing discomfort and hearing loss.",
        "medication": "Use ear drops or take oral medications.",
        "home_remedy": "Avoid using cotton swabs, try ear irrigation, and dry your ears after showering."
    },
    "heat_rash": {
        "description": "Heat rash is a skin condition that causes redness, itching, and small bumps due to excessive heat and sweating.",
        "medication": "Apply topical creams or take oral antihistamines.",
        "home_remedy": "Stay cool, avoid strenuous activities, and apply cool compresses."
    },
    "hives": {
        "description": "Hives are itchy, raised welts on the skin that can cause discomfort and swelling.",
        "medication": "Take antihistamines or apply topical creams.",
        "home_remedy": "Avoid triggers like certain foods and stress, apply cool compresses, and try oatmeal baths."
    },
    "yeast_infection": {
        "description": "Yeast infections are fungal infections that cause itching, redness, and discharge in the vagina or mouth.",
        "medication": "Use antifungal creams or take oral medications.",
        "home_remedy": "Practice good hygiene, avoid tight clothing, and try probiotics."
    },
    "insomnia": {
        "description": "Insomnia is a sleep disorder that makes it difficult to fall asleep or stay asleep.",
        "medication": "Take sleep aids or melatonin supplements.",
        "home_remedy": "Establish a bedtime routine, avoid caffeine and electronics before bedtime, and create a relaxing sleep environment."
    },
    "migraines": {
        "description": "Migraines are severe headaches that can cause nausea, vomiting, and sensitivity to light.",
        "medication": "Take triptans or ergotamines.",
        "home_remedy": "Avoid triggers like certain foods and stress, apply cold or warm compresses, and practice relaxation techniques."
    },
    "motion_sickness": {
        "description": "Motion sickness is a condition that causes nausea, vomiting, and dizziness when traveling.",
        "medication": "Take antihistamines or scopolamine patches.",
        "home_remedy": "Choose a seat in the front or middle of a vehicle, avoid reading or screens, and take breaks during long trips."
    },
    "otitis_media": {
        "description": "Otitis media is an infection of the middle ear that can cause ear pain, fever, and hearing loss.",
        "medication": "Take antibiotics or pain relievers.",
        "home_remedy": "Apply warm compresses, avoid sticking objects in your ears, and try ear drops."
    },
    "pharyngitis": {
        "description": "Pharyngitis is an inflammation of the throat that can cause pain, redness, and difficulty swallowing.",
        "medication": "Take antibiotics or pain relievers.",
        "home_remedy": "Gargle with salt water, drink warm liquids, and try throat lozenges."
    },
    "pneumonia": {
        "description": "Pneumonia is an infection of the lungs that can cause coughing, fever, and difficulty breathing.",
        "medication": "Take antibiotics or antiviral medication.",
        "home_remedy": "Drink plenty of fluids, get plenty of rest, and try humidifiers."
    },
    "psoriasis": {
        "description": "Psoriasis is a skin condition that causes red, scaly patches and inflammation.",
        "medication": "Use topical corticosteroids or take oral medications.",
        "home_remedy": "Apply moisturizers, avoid triggers like stress and cold weather, and try ultraviolet light therapy."
    },
    "rhinitis": {
        "description": "Rhinitis is an allergic reaction that causes sneezing, runny nose, and congestion.",
        "medication": "Take antihistamines or decongestants.",
        "home_remedy": "Avoid triggers like pollen and dust, use nasal sprays, and try immunotherapy."
    },
    "ringworm": {
        "description": "Ringworm is a fungal infection that causes a ring-shaped rash and itching.",
        "medication": "Use antifungal creams or take oral medications.",
        "home_remedy": "Apply cool compresses, avoid scratching, and keep the area clean."
    },
    "sinus": {
        "description": "Sinusitis or sinus is an inflammation of the sinuses that can cause congestion, headaches, and facial pain.",
        "medication": "Take antibiotics or decongestants.",
        "home_remedy": "Use nasal sprays, try steam inhalation, and apply warm compresses."
    },
    "constipation": {
        "description": "Constipation is a condition where bowel movements are infrequent or difficult.",
        "medication": "Take laxatives or fiber supplements.",
        "home_remedy": "Drink plenty of water, exercise regularly, and eat fiber-rich foods."
    },
    "tuberculosis": {
        "description": "Tuberculosis is a bacterial infection that causes coughing, fever, and weight loss.",
        "medication": "Take antibiotics for at least 6 months.",
        "home_remedy": "Rest, eat a healthy diet, and avoid close contact with others."
    },
    "influenza": {
        "description": "Influenza is a viral infection that causes fever, cough, and body aches.",
        "medication": "Take antiviral medication or pain relievers.",
        "home_remedy": "Stay hydrated, rest, and use a humidifier."
    },
    "diarrhea": {
        "description": "Diarrhea is a condition where stools are loose and frequent.",
        "medication": "Take anti-diarrheal medication.",
        "home_remedy": "Drink plenty of fluids, eat bland foods, and try probiotics."
    },
    "ear_infection": {
        "description": "Ear infections occur when bacteria or viruses infect the middle ear.",
        "medication": "Take antibiotics or pain relievers.",
        "home_remedy": "Apply warm compresses and avoid sticking objects in your ears."
    },
    "eczema": {
        "description": "Eczema is a skin condition that causes itching, redness, and dryness.",
        "medication": "Use topical corticosteroids or moisturizers.",
        "home_remedy": "Avoid triggers like soaps and detergents, and apply cool compresses."
    },
    "food_poisoning": {
        "description": "Food poisoning occurs when you eat contaminated food, causing symptoms like nausea and vomiting.",
        "medication": "Take anti-nausea medication or antibiotics.",
        "home_remedy": "Drink plenty of fluids, eat bland foods, and avoid solid foods for a while."
    },
    "gerd": {
        "description": "GERD is a condition where stomach acid flows back up into the esophagus, causing heartburn and discomfort.",
        "medication": "Take antacids or acid reducers.",
        "home_remedy": "Avoid triggers like spicy foods, eat smaller meals, and elevate your head while sleeping."
    },
    "head_lice": {
        "description": "Head lice are tiny parasites that live on human hair, causing itching and discomfort.",
        "medication": "Use medicated shampoos or cream rinses.",
        "home_remedy": "Use fine-tooth combs to remove lice and nits, and wash clothing and bedding in hot water."
    },
    "hypothyroidism": {
        "description": "Hypothyroidism is a condition where the thyroid gland doesn't produce enough hormones, causing fatigue and weight gain.",
        "medication": "Take thyroid hormone replacement medication.",
        "home_remedy": "Eat foods rich in iodine, avoid soy and cruciferous vegetables, and exercise regularly."
    },
    "impetigo": {
        "description": "Impetigo is a skin infection that causes red sores and blisters.",
        "medication": "Use antibiotic creams or take oral antibiotics.",
        "home_remedy": "Apply warm compresses, avoid scratching, and keep the area clean."
    },
    "allergies": {
        "description": "Allergies occur when your body reacts to a foreign substance, causing symptoms like itching, sneezing, and runny nose.",
        "medication": "Take antihistamines or use nasal sprays.",
        "home_remedy": "Use saline nasal sprays and avoid exposure to allergens."
    },
    "asthma": {
        "description": "Asthma is a chronic lung disease that causes wheezing, coughing, and shortness of breath.",
        "medication": "Use inhalers and take corticosteroids.",
        "home_remedy": "Avoid triggers like dust and pollen, and use a humidifier."
    },
    "bronchitis": {
        "description": "Bronchitis is an inflammation of the bronchial tubes, causing coughing and mucus production.",
        "medication": "Take antibiotics and use bronchodilators.",
        "home_remedy": "Drink warm liquids and use a humidifier."
    },
    "conjunctivitis": {
        "description": "Conjunctivitis is an eye infection that causes redness, itching, and discharge.",
        "medication": "Use antibiotic eye drops.",
        "home_remedy": "Apply warm compresses and avoid touching your eyes."
    }
}

# Sample hospital data
hospitals = {
    "visakhapatnam": [
        {"name": "King George Hospital (KGH)", "address": "KGH Road, Waltair Uplands, Visakhapatnam, Andhra Pradesh 530002", "contact": "+91 891 274 1543"},
        {"name": "Apollo Hospitals", "address": "1-11-111, Waltair Main Road, Visakhapatnam, Andhra Pradesh 530002", "contact": "+91 891 660 7700"},
        {"name": "CARE Hospitals", "address": "Plot No. 2, Andhra University Road, Visakhapatnam, Andhra Pradesh 530003", "contact": "+91 891 271 1111"},
        {"name": "Mahatma Gandhi Cancer Hospital & Research Institute", "address": "Kanchara Nayanamma Rd, Akkayyapalem, Visakhapatnam, Andhra Pradesh 530016", "contact": "+91 891 279 4500"},
        {"name": "SevenHills Hospital", "address": "Plot No. 1, Beach Road, Visakhapatnam, Andhra Pradesh 530003", "contact": "+91 891 273 2555"},
        {"name": "Visakha Institute of Medical Sciences (VIMS)", "address": "Near Gandhi Hospital, Maharanipeta, Visakhapatnam, Andhra Pradesh 530002", "contact": "+91 891 273 2682"},
        {"name": "L.V. Prasad Eye Institute", "address": "2-14-5, Daba Gardens, Visakhapatnam, Andhra Pradesh 530020", "contact": "+91 891 255 6545"},
        {"name": "Rainbow Children's Hospital", "address": "Near Madhurawada, Visakhapatnam, Andhra Pradesh 530048", "contact": "+91 891 272 2222"},
        {"name": "Dr. Agarwal's Healthcare Ltd", "address": "10-1-5, Daba Gardens, Visakhapatnam, Andhra Pradesh 530020", "contact": "+91 891 275 0636"},
        {"name": "Maxivision Eye Hospitals", "address": "Daba Gardens, Visakhapatnam, Andhra Pradesh 530020", "contact": "+91 891 255 4777"}
    ],
        "gajuwaka": [
            {"name": "RK Hospital", "address": "1-42-1, Gajuwaka, Visakhapatnam, Andhra Pradesh 530026", "contact": "+91 891 279 1795"},
            {"name": "Simhagiri Hospital", "address": "Near Gajuwaka Bus Stand, Visakhapatnam, Andhra Pradesh 530026", "contact": "+91 891 272 6969"},
        {"name": "Shri Rama Hospital", "address": "Near Gajuwaka, Visakhapatnam, Andhra Pradesh 530026", "contact": "+91 891 274 7777"},
        {"name": "Geeta Hospital", "address": "Gajuwaka, Visakhapatnam, Andhra Pradesh 530026", "contact": "+91 891 274 1066"},
        {"name": "Sujahta Hospital", "address": "Gajuwaka, Visakhapatnam, Andhra Pradesh 530026", "contact": "+91 891 273 5050"},
        {"name": "St. Ann's Hospital", "address": "Gajuwaka, Visakhapatnam, Andhra Pradesh 530026", "contact": "+91 891 273 8888"},
        {"name": "Bhavani Homoeo Hospital", "address": "Gajuwaka, Visakhapatnam, Andhra Pradesh 530026", "contact": "+91 891 275 3333"},
        {"name": "Gowtham Homoeo Clinic", "address": "Gajuwaka, Visakhapatnam, Andhra Pradesh 530026", "contact": "+91 891 276 0999"},
        {"name": "Sri Venkateswara Nursing Home", "address": "Gajuwaka, Visakhapatnam, Andhra Pradesh 530026", "contact": "+91 891 273 5555"},
        {"name": "Padmaja Hospital", "address": "Gajuwaka, Visakhapatnam, Andhra Pradesh 530026", "contact": "+91 891 273 4444"}
    ],
    "anakapalle": [
        {"name": "Medicover Woman and Child Hospital", "address": "Anakapalle, Visakhapatnam, Andhra Pradesh 531001", "contact": "+91 891 272 7676"},
        {"name": "Simhadri Hospitals", "address": "Anakapalle, Visakhapatnam, Andhra Pradesh 531001", "contact": "+91 891 273 7676"},
        {"name": "Tirumala Jyoti Hospital", "address": "Anakapalle, Visakhapatnam, Andhra Pradesh 531001", "contact": "+91 891 275 6767"},
        {"name": "Hyma Nethralayam", "address": "Anakapalle, Visakhapatnam, Andhra Pradesh 531001", "contact": "+91 891 277 3333"},
        {"name": "Viswam Superspeciality Hospitals", "address": "Anakapalle, Visakhapatnam, Andhra Pradesh 531001", "contact": "+91 891 275 3434"},
        {"name": "M.B Multispeciality Hospitals", "address": "Anakapalle, Visakhapatnam, Andhra Pradesh 531001", "contact": "+91 891 276 4444"},
        {"name": "Ramsaranya Hospital Pvt Ltd", "address": "Anakapalle, Visakhapatnam, Andhra Pradesh 531001", "contact": "+91 891 277 5555"},
        {"name": "Sun Rise Hospital", "address": "Anakapalle, Visakhapatnam, Andhra Pradesh 531001", "contact": "+91 891 277 6666"},
        {"name": "Asian Institute of Nephrology and Urology", "address": "Anakapalle, Visakhapatnam, Andhra Pradesh 531001", "contact": "+91 891 276 7777"},
        {"name": "Dr. Pavanis Best Vision Advanced Eye Hospital", "address": "Anakapalle, Visakhapatnam, Andhra Pradesh 531001", "contact": "+91 891 275 8888"}
    ]
}

import random
#health tips
health_tips = [
    "Drink plenty of water to stay hydrated.",
    "Take short walks during breaks to stay active.",
    "Eat fruits and vegetables daily.",
    "Get 7-8 hours of sleep for better recovery.",
    "Wash your hands frequently to avoid infections.",
    "Avoid skipping breakfast – it fuels your day!",
    "Stretch regularly to improve flexibility.",
    "Limit sugary drinks and junk food.",
    "Practice deep breathing to reduce stress.",
    "Keep a regular sleep schedule.",
    "Avoid staring at screens for too long – follow the 20-20-20 rule.",
    "Add nuts and seeds to your diet for healthy fats.",
    "Practice mindful eating – eat slowly and without distractions.",
    "Spend time in sunlight for natural Vitamin D.",
    "Don’t ignore mental health – talk to someone if you're stressed.",
    "Include protein in every meal to support muscles.",
    "Use stairs instead of elevators when possible.",
    "Do regular check-ups and health screenings.",
    "Stay connected with friends and loved ones.",
    "Limit alcohol and avoid smoking.",
    "Maintain good posture to avoid back pain.",
    "Keep your surroundings clean to prevent illness.",
    "Chew your food thoroughly to aid digestion.",
    "Don’t overeat – stop when you're about 80% full.",
    "Try to include probiotic-rich foods like curd or yogurt.",
    "Avoid late-night snacking.",
    "Stay informed, but don’t obsess over negative news.",
    "Take tech-free time daily to unwind.",
    "Exercise at least 30 minutes a day.",
    "Practice gratitude – it boosts your mood.",
    "Don’t self-medicate – always consult a doctor.",
    "Keep a water bottle nearby as a reminder to drink water.",
    "Plan your meals to avoid impulsive unhealthy eating.",
    "Meditate or journal to clear your mind."
]

#emeregency contacts
emergency_contacts = {
    "Ambulance": "📞 102",
    "Police": "📞 100 / 112",
    "Fire Department": "📞 101",
    "Crime Stopper": "📞 1090",
    "Women & Child Helpline (Disha)": "📞 1091 / 181",
    "Railway Enquiry": "📞 131 / 135",
    "Railway Reservation": "📞 139",
    "Electricity Complaints": "📞 155333",
    "Water Supply Issues": "📞 155313",
    "Traffic Help": "📞 1073",
    "Arogyasri Medical Help": "📞 104",
    "General Emergency (All-in-One)": "📞 108",
    "Voter Services": "📞 1950",
    "BSNL Customer Care": "📞 198",
    "Spandana Public Grievance": "📞 1902",
    "Sand & Excise Grievance": "📞 14500",
    "Anti-Corruption Helpline": "📞 14400",
    "Visakhapatnam City Police Control": "📞 0891-2562709",
    "Commissioner of Police (Vizag)": "📞 7995095799",
    "District Fire Officer (Vizag)": "📞 9949991050",
    "DISHA SOS Helpline (Women Safety)": "📞 181 / 112"
}

meditation_guide = """
🧘‍♀️ *Mini Meditation Guide*

1. Sit comfortably and close your eyes.
2. Breathe in deeply through your nose... hold for 3 seconds.
3. Slowly exhale through your mouth.
4. Focus only on your breath.
5. Repeat for 1–2 minutes.

You can do this anytime you feel stressed. Stay calm. Stay centered. 🌿
"""

#dummy doctor
import random
dummy_responses = [
    "🤖 Doctor's Reply:\n\nThanks for reaching out! Based on your symptoms, we suggest you go to the *Treatment* section, type your condition, and you'll get suitable medication. If symptoms persist or worsen, please consult a real doctor.",
    
    "🤖 Doctor's Reply:\n\nStay hydrated, take enough rest, and avoid stress. For medicine suggestions, please visit the *Treatment* section. If it becomes severe, don’t hesitate to see a doctor.",
    
    "🤖 Doctor's Reply:\n\nSorry to hear that! You can find relevant medicines in the *Treatment* option. Continue the suggested meds until you're completely fine. If things don’t improve, kindly consult a physician.",
    
    "🤖 Doctor's Reply:\n\nIt sounds like a common condition. Go to the *Treatment* section and find your illness to get medicine suggestions. Monitor your symptoms closely, and if they increase, please visit a healthcare provider.",
    
    "🤖 Doctor's Reply:\n\nWe’re here to guide you! For your issue, try exploring the *Treatment* tab to know the medications. Always take proper rest and consult a doctor if you’re feeling worse.",
    
    "🤖 Doctor's Reply:\n\nThanks for your query. Please go to the *Treatment* section for medication recommendations related to your condition. If you're still unwell after a couple of days, consider seeing a doctor.",
    
    "🤖 Doctor's Reply:\n\nAppreciate you reaching out. The *Treatment* section is designed to guide you with medications. However, if this feels serious or lasts long, professional medical help is advised.",
    
    "🤖 Doctor's Reply:\n\nYour health matters! Please go to the *Treatment* section to explore meds that match your symptoms. If things don’t get better soon, consulting a doctor is the best choice.",
    
    "🤖 Doctor's Reply:\n\nSorry to hear that you're unwell. Use the *Treatment* option to get medicine suggestions. Don’t delay visiting a doctor if it doesn’t get better in a few days.",
    
    "🤖 Doctor's Reply:\n\nHi! Thanks for sharing your concern. We recommend checking the *Treatment* feature to get the right medications. Take care and see a doctor if it continues."
]


#health facts
health_facts = [
    "🧠 Your brain uses about 20% of your body’s total oxygen and calories.",
    "🫀 The human heart can beat over 3 billion times in a lifetime.",
    "🦴 You’re born with 300 bones, but as you grow, they fuse to 206.",
    "👂 Your ears continue to grow throughout your life!",
    "😴 Sleep is crucial for memory consolidation and immune function.",
    "💧 Water makes up around 60% of the human body.",
    "🍎 An apple a day may not keep the doctor away, but it’s rich in fiber and antioxidants.",
    "👁️ Your eyes can distinguish about 10 million different colors.",
    "🧬 Every cell in your body contains the same DNA (except red blood cells).",
    "💪 Regular exercise improves mental health and boosts mood.",
    "🦷 Enamel is the hardest substance in the human body.",
    "🥦 A diet rich in vegetables can lower the risk of many chronic diseases.",
    "🧂 Too much salt in your diet can increase blood pressure.",
    "🧴 Sunscreen helps prevent skin cancer and premature aging.",
    "😃 Smiling can boost your immune system and lower stress.",
    "🧘‍♀️ Meditation reduces anxiety, improves focus, and enhances self-awareness.",
    "🦠 Your gut houses trillions of beneficial bacteria.",
    "🧃 Vitamin C supports immune health and skin repair.",
    "🩸 Blood makes up about 7-8% of your body weight.",
    "👃 You can detect over 1 trillion different scents.",
    "🫁 Lungs can hold up to 6 liters of air at full capacity.",
    "🤸‍♂️ Stretching improves flexibility and reduces injury risk.",
    "👶 Babies have about 10,000 taste buds — more than adults!",
    "🧊 Cold showers can increase alertness and improve circulation.",
    "☀️ Just 15 minutes of sun exposure a day helps your body produce vitamin D.",
    "📵 Blue light from screens can interfere with sleep cycles.",
    "🥗 A balanced diet includes carbs, proteins, fats, vitamins, and minerals.",
    "👣 The average person walks about 100,000 miles in their lifetime.",
    "🛌 Lack of sleep is linked to heart disease, diabetes, and obesity.",
    "🦷 Brushing and flossing daily can prevent gum disease and tooth loss.",
    "🧃 Hydration affects your energy, mood, and brain performance.",
    "🥦 Broccoli contains more vitamin C than oranges per gram.",
    "🚶‍♂️ Walking just 30 minutes a day can improve heart health.",
    "🍫 Dark chocolate (in moderation) is good for heart and brain health.",
    "🧘‍♂️ Deep breathing activates your parasympathetic nervous system, calming the body.",
    "🦴 Calcium and vitamin D are vital for strong bones.",
    "🎧 Listening to music can reduce stress and boost happiness.",
    "😷 Handwashing prevents the spread of infections.",
    "🛁 A warm bath can ease muscle tension and promote relaxation.",
    "🍌 Bananas are rich in potassium, which helps regulate blood pressure.",
    "📖 Reading regularly improves brain connectivity and function.",
    "☕ Moderate coffee intake is linked to lower risk of several diseases.",
    "🚰 Dehydration can impair concentration and physical performance.",
    "🧠 Brain cells start dying within 5 minutes without oxygen.",
    "🥬 Leafy greens support eye health and reduce inflammation.",
    "🧴 Moisturizing daily keeps your skin healthy and protected.",
    "📵 Taking screen breaks reduces eye strain and mental fatigue.",
    "🧄 Garlic has natural antibacterial and antiviral properties.",
    "🏃 Regular physical activity can add years to your life.",
]

skincare_haircare_tips = [
    "Use a gentle cleanser that suits your skin type.",
    "Don't forget to apply sunscreen, even on cloudy days.",
    "Stay hydrated – your skin and hair will thank you!",
    "Avoid using heat on your hair too often to prevent damage.",
    "Include vitamin-rich foods like leafy greens and berries in your diet.",
    "Always remove makeup before sleeping.",
    "Use conditioner only on the ends of your hair to avoid scalp build-up.",
    "Exfoliate your skin 1-2 times a week to remove dead cells.",
    "Oil your hair once a week to maintain strength and shine.",
    "Avoid touching your face frequently to prevent breakouts.",
    "Use a silk pillowcase to reduce hair frizz and prevent skin creases.",
    "Apply moisturizer right after washing your face to lock in moisture.",
    "Trim your hair every 6-8 weeks to avoid split ends.",
    "Use lukewarm water for washing your face and hair to avoid dryness.",
    "Incorporate antioxidant-rich serums like Vitamin C into your skincare.",
    "Let your hair air dry when possible to minimize heat damage.",
    "Apply aloe vera gel to soothe irritated skin and scalp.",
    "Massage your scalp regularly to improve blood circulation and promote hair growth.",
    "Use products with hyaluronic acid for deep skin hydration.",
    "Protect your hair from sun damage by wearing a hat or scarf.",
    "Avoid overwashing your face and hair – balance is key.",
    "Choose non-comedogenic products to avoid clogging pores.",
    "Use dry shampoo sparingly to avoid scalp build-up.",
    "Test new skincare products on a small area before full application.",
    "Deep condition your hair once a week for extra nourishment.",
    "Avoid popping pimples to prevent scarring and infection.",
    "Clean your makeup brushes regularly to prevent bacteria buildup.",
    "Use cold water to rinse your hair for extra shine.",
    "Apply a face mask once a week based on your skin’s needs.",
    "Get adequate sleep – it’s essential for skin and hair health.",
]

nearby_pharmacy = {
    "vizag": [
        {"name": "Heal & Care Pharmacy", "address": "Dwaraka Nagar", "contact": "+91 9177333864"},
        {"name": "Lifeline Drugstore", "address": "MVP Colony", "contact": "+91 7702988813"},
        {"name": "Bay City Pharmacy", "address": "Beach Road", "contact": "+91 8912788483"},
        {"name": "Apollo Pharmacy Siripuram", "address": "Siripuram", "contact": "+91 9177333864"},
        {"name": "Mohan Medical Shop", "address": "Balayya Sastri Layout, Seethammadara", "contact": "+91 7702988813"},
        {"name": "Sri Venkateswara Medical & General Stores", "address": "Sheela Nagar", "contact": "+91 8912788483"},
        {"name": "Central Pharmacy", "address": "Maharani Peta", "contact": "+91 8912788483"},
        {"name": "Archana Pharmacy", "address": "Allipuram Main Road", "contact": "+91 8912788483"},
        {"name": "Safeway Pharmaci", "address": "Dondaparthy, Akkayyapalem", "contact": "+91 8912788483"},
        {"name": "Health City Medicals", "address": "Health City", "contact": "+91 8912788483"},
    ],
    "gajuwaka": [
        {"name": "Apollo Pharmacy", "address": "Kanithi Road, Near VJ Internet Services", "contact": "+91 8041019163"},
        {"name": "Nizam Medicals Center", "address": "Sriharipuram", "contact": "Not Available"},
        {"name": "SN Medicals & Stationery", "address": "Gajuwaka", "contact": "Not Available"},
        {"name": "New Raja Medicals", "address": "Gajuwaka", "contact": "Not Available"},
        {"name": "Praveen Medicals", "address": "Gajuwaka", "contact": "Not Available"},
        {"name": "Sai Santosh Medicals", "address": "Gajuwaka", "contact": "Not Available"},
        {"name": "Ssv Medicals 24 Hours Service", "address": "Gajuwaka", "contact": "Not Available"},
        {"name": "Apollo Pharmacy", "address": "Himachalnagar, Gajuwaka", "contact": "+91 9121107294"},
        {"name": "Sai Shri Ganapathi Medicals And General Stores", "address": "Chaitanya Nagar, Gajuwaka", "contact": "+91 9704376789"},
        {"name": "Renuka Medical And General Stores", "address": "Sheela Nagar", "contact": "+91 9491801779"},
    ],
    "anakapalli": [
        {"name": "Apollo Pharmacy", "address": "Nehru Chowk, Near 4 Road Junction", "contact": "+91 8041019185"},
        {"name": "MedPlus Pharmacy", "address": "Wood Peta Yard, Madugula Road", "contact": "Not Available"},
        {"name": "Apollo Pharmacy", "address": "Satya Sai Nagar, Kumari Complex", "contact": "Not Available"},
        {"name": "Sri Sai Srinivasa Medical & General Store", "address": "V.V. Kranthi Apartment, Service Rd, Opposite BHPV Gate, Ramnagar", "contact": "+91 8913207709"},
        {"name": "New J.R Medicals And General Stores", "address": "Adari Complex, Venkateswara Colony Rd, B.H.P.V Post, Venkateswara Colony, Sheela Nagar", "contact": "+91 9848481996"},
        {"name": "Apollo Pharmacy", "address": "Santhipuram, Sankaramatam Road", "contact": "+91 8041019132"},
        {"name": "Apollo Pharmacy", "address": "BS Layout, Seethammadara", "contact": "+91 8041019132"},
        {"name": "Apollo Pharmacy", "address": "Karasa", "contact": "+91 8041019132"},
        {"name": "Apollo Pharmacy", "address": "Anakapalli", "contact": "+91 8041019132"},
        {"name": "Apollo Pharmacy", "address": "Anakapalli", "contact": "+91 8041019132"},
    ],
}