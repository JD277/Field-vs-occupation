import pandas as pd
import joblib
from sklearn.preprocessing import MinMaxScaler
field_of_study_mapping = {
"Medicine": 0, "Education": 1, "Arts": 2, "Computer Science": 3, "Business": 4,
"Mechanical Engineering": 5, "Biology": 6, "Law": 7, "Economics": 8, "Psychology": 9
}

current_occupation_mapping = {
"Business Analyst": 0, "Economist": 1, "Biologist": 2, "Doctor": 3, "Lawyer": 4,
"Software Developer": 5, "Artist": 6, "Psychologist": 7, "Teacher": 8, "Mechanical Engineer": 9
}

gender_mapping = {"Male": 0, "Female": 1}

industry_growth_mapping = {"Low": 0, "Medium": 1, "High": 2}

family_influence_mapping = {"None": 0, "Low": 1, "Medium": 2, "High": 3}

education_mapping = {"High School": 0, "Bachelor's": 1, "Master's": 2, "PhD": 3}
class Model:
    def __init__(self, model_name):
        try:
            match model_name:
                case "tf": 
                    self.model = joblib.load('model_tensorflow.pkl')
                case "sk":
                    self.model = joblib.load('model_sklearn.pkl')
        except Exception as e:
            print(f"Error loading model: {e}")
            return
    def predict(self,
            field_of_study="Arts",
            current_occupation="Artist",
            age=25,
            gender="Female",
            years_of_exp=3,
            education="Bachelor's",
            industry="Medium",
            job_satisfaction=7,
            work_life_balance=8,
            job_opportunities=50,
            Salary=50000,
            job_security=5,
            career_change_interest=0,
            skills_gap=3,
            family_influence="Low",
            mentorship_available=1,
            certifications=0,
            freelancing_experience=0,
            geographic_mobility=1,
            professional_networks=5,
            career_change_events=1,
            technology_adoption=6):
    

            # Convertir strings en números usando los diccionarios de mapeo
        field_of_study = field_of_study_mapping.get(field_of_study, -1)
        current_occupation = current_occupation_mapping.get(current_occupation, -1)
        gender = gender_mapping.get(gender, -1)
        industry = industry_growth_mapping.get(industry, -1)
        family_influence = family_influence_mapping.get(family_influence, -1)
        education = education_mapping.get(education, -1)
    
        # Verificar si se encontró un valor válido
        if -1 in [field_of_study, current_occupation, gender, industry, family_influence, education]:
            print("Error: Se ingresó un valor no válido en una variable categórica.")
            return None

        data = {
        'field_of_study': field_of_study,
        'current_occupation': current_occupation,
        'age': age,
        'gender': gender,
        'years_of_exp': years_of_exp,
        'education': education,
        'industry': industry,
        'job_satisfaction': job_satisfaction,
        'work_life_balance': work_life_balance,
        'job_opportunities': job_opportunities,
        'Salary': Salary,
        'job_security': job_security,
        'career_change_interest': career_change_interest,
        'skills_gap': skills_gap,
        'family_influence': family_influence,
        'mentorship_available': mentorship_available,
        'certifications': certifications,
        'freelancing_experience': freelancing_experience,
        'geographic_mobility': geographic_mobility,
        'professional_networks': professional_networks,
        'career_change_events': career_change_events,
        'technology_adoption': technology_adoption
    }
        df = pd.DataFrame([data])
        scalar = MinMaxScaler()
        df = scalar.fit_transform(df)
        result = self.model.predict(df)
        print(result)
        return result


ai = Model("tf")

ai.predict("Medicine", "Doctor", 50, "Male", 2, "Bachelor's")
    