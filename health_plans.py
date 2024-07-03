def suggest_health_plans(interpreted_query):
    # Basic rules-based health plan suggestions
    health_plans = []

    if "weight loss" in interpreted_query.lower():
        health_plans.append("Plan 1: Balanced diet with calorie restriction and regular exercise.")
        health_plans.append("Plan 2: High-protein diet with strength training.")

    elif "diabetes" in interpreted_query.lower():
        health_plans.append("Plan 1: Low-carb diet with regular blood sugar monitoring.")
        health_plans.append("Plan 2: High-fiber diet with medication adherence.")

    elif "heart health" in interpreted_query.lower():
        health_plans.append("Plan 1: Low-sodium diet with cardiovascular exercise.")
        health_plans.append("Plan 2: Mediterranean diet with stress management.")

    else:
        health_plans.append("Plan 1: General healthy diet with regular physical activity.")
        health_plans.append("Plan 2: Regular check-ups and a balanced diet.")

    return health_plans
