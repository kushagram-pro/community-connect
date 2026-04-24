def compute_score(volunteer, need):
    reasons = []

    # --- Semantic match ---
    if need["category"] in volunteer["skills"]:
        semantic = 1.0
        reasons.append(f"Skill match: {need['category']}")

    else:
        semantic = 0.5
        reasons.append("Partial skill match")

      # --- Distance ---
    distance = volunteer.get("distance", 1)
    max_distance = volunteer["max_distance"]
    
    if distance > max_distance: 
        return 0, ["Too far"]
    
    proximity = max(0, 1 - (distance / max_distance))
    reasons.append(f"{distance} km away")

    # --- Availability --- 
    availability = 1 if volunteer["available"] else 0
    if availability: 
        reasons.append("Available now")

    # --- Travel willingness ---
    travel = volunteer.get("travel_willingness", 1)

    score = (
        0.5 * semantic +
        0.3 * proximity +
        0.1 * availability +
        0.1 * travel
    )

    return score, reasons

def match_volunteers(need, volunteers):
    results = []

    for v in volunteers:
        score, reasons = compute_score(v, need)

        if score == 0:
            continue

        results.append({
            "id": v.get("id", "unknown"),
            "score": round(score, 3),
            "reasons": reasons,
            "explanation": " | ".join(reasons),
            "confidence": round(score, 2)
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    return results[:3]