# Define the conditional probability tables (CPTs)
#     'R_t_C_t': {
#         'True': 0.96,
#         'False': 0.04
#     },
#     'R_t_C_f': {
#         'True': 0.85,
#         'False': 0.15
#     },
#     'R_f_C_t': {
#         'True': 0.7,
#         'False0': 0.3
#     },
#     'R_f_C_f': {
#         'True': 0.08,
#         'False': 0.92
#     }
# }
cpt_cold_given_runny_nose = {'True': 0.85, 'False': 0.15}
cpt_cold_given_cough = {'True': 0.7, 'False': 0.3}

cpt_runny_nose = {'True': 0.2, 'False': 0.8}
cpt_cough = {'True': 0.3, 'False': 0.7}

# symtoms input:
a = input("Do u have runny nose(True/False):")
b = input("Do u have cough(True/False):")

# Define the evidence (observed symptoms)
evidence = {
    'RunnyNose': a,
    'Cough': b,
    # 'Cold': 'True'
}

# Calculate joint probability
joint_probability = (
    cpt_cold_given_runny_nose[evidence['RunnyNose']] *
    cpt_cold_given_cough[evidence['Cough']] *
    cpt_runny_nose[evidence['RunnyNose']] *
    cpt_cough[evidence['Cough']]

)
print("cpt_cold_given_runny_nose * cpt_cold_given_cough * cpt_runny_nose * cpt_cough")
print(f"{cpt_cold_given_runny_nose[evidence['RunnyNose']]}*", end="  ")
print(f"{cpt_cold_given_cough[evidence['Cough']]}*", end="  ")
print(f"{cpt_runny_nose[evidence['RunnyNose']]}*", end="  ")
print(f"{cpt_cough[evidence['Cough']]}*")

# Query the network to find the probability of having a cold given the symptoms
probability_cold = joint_probability
print(f"Probability of having a cold: {probability_cold:.2f}")