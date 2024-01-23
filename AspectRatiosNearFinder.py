'''
    script to calculate closest common aspect ratios for strange device aspect ratios(talkin' to yuou, apple)
'''

def closest_common_aspect_ratio(ratio, common_ratios):
    # Calculate the decimal value of the input ratio
    ratio_value = ratio[0] / ratio[1]
    # Initialize minimum difference as infinity
    min_diff = float('inf')
    # Variable to store the closest common aspect ratio
    closest_ratio = None

    # Iterate over each common aspect ratio
    for cr in common_ratios:
        # Calculate the decimal value of the common aspect ratio
        cr_value = cr[0] / cr[1]
        # Calculate the absolute difference between the input ratio and the common ratio
        diff = abs(ratio_value - cr_value)
        # If this difference is the smallest found so far, update min_diff and closest_ratio
        if diff < min_diff:
            min_diff = diff
            closest_ratio = cr

    # Return the closest common aspect ratio
    return closest_ratio

# List of common aspect ratios
common_aspect_ratios = [(16, 9), (16, 10), (4, 3), (3, 4), (3, 2), (2, 3), (2, 1), (1, 2)]

# List of uncommon aspect ratios to be compared
uncommon_aspect_ratios = [
    (828, 1792), (1125, 2436), (1242, 2688), (1170, 2532), (1170, 2532), 
    (1284, 2778), (1080, 2340), (640, 1136), (750, 1334), (1080, 1920), 
    (1440, 2880), (1080, 2160), (1440, 2960), (1080, 2220), (1080, 2280), 
    (1440, 3040), (1440, 2560), (720, 1280), (1440, 3120), (1176, 2400), 
    (1080, 2310), (720, 1440), (1080, 2400), (1440, 3168), (1536, 2152), 
    (720, 1480), (1440, 3088), (1440, 3200), (1080, 2636), (1768, 2208), 
    ]

# Dictionary to store the closest common aspect ratio for each uncommon ratio
closest_ratios = {}
# Iterate over each uncommon aspect ratio
for ratio in uncommon_aspect_ratios:
    # Find the closest common aspect ratio for the current ratio
    closest = closest_common_aspect_ratio(ratio, common_aspect_ratios)
    # If a closest ratio is found, add it to the dictionary
    if closest:
        closest_ratios[f"{ratio[0]}:{ratio[1]}"] = f"{closest[0]}:{closest[1]}"

# Print the closest common aspect ratios for each uncommon ratio
print("Closest Common Aspect Ratios:")
for k, v in closest_ratios.items():
    print(f"{k} -> {v}")
