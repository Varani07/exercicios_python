capitals = {
    "New York": "Albany",
    "California": "Sacramento",
    "Texas": "Austin"
}

inverted = {capital: state for state, capital in capitals.items() if len(state) != len(capital)}
print(inverted)

# ==========================================================================

def stations_to_numbers(channels):
    return {channel: number for number, channel in channels.items()}

def coaster_conversion(coasters):
    return {roller:round(heights * 3.28084) for roller, heights in coasters.items()}