# Example 01
style = "formatted"
f"This is a {style} string"

# Example 02
import math
r = 3.6

f"A circle with radius {r} has area {math.pi * r * r:.2f}"

# Example 03
import math
r = 3.8

f"Diameter {(diam := 2 * r)} gives circumference {math.pi * diam:.2f}"

# Example 04
python = 3.8
f"{python=}"

# Example 05
python = 3.7
>>> f"python={python}"

# Example 06
name = "Eric"
f"{name = }"

f"{name = :>10}"

# Example 07
f"{name.upper()[::-1] = }"