def mood_today(mood:str):
    if mood == "happy":
        return f"Today, I am feeling {mood}"
    elif mood == "sad":
        return f"Today, I am feeling {mood}"
    else:
        return f"Today, I am neutral"

print(mood_today(""))
