def calculate_final_risk(rule_risk, ml_prediction):

    if ml_prediction == -1:
        rule_risk += 0.5

    return rule_risk