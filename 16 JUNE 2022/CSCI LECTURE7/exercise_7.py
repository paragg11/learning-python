"""
Lecture 7 - Lists part 1
"""

if __name__ == "__main__":
    print("*" * 100)
    scores = [59, 61, 63, 63, 68, 64, 58]
    print(scores)
    planets = ['Mercury', 'Venus', 'Earth', 'Mras', 'Jupiter',
               'Saturn', 'Neptune', 'Uranus', 'Pluto']
    print(planets)
    planets[3] = 'Mars'
    print(planets)
    print(scores[4])

    print("*" * 100)
    s = 'abc'
    print(s[0])
    print(s[1])

    print("*" * 100)
    print("Average Scores = {:.2f}".format(sum(scores) / len(scores)))
    print("Max Score =", max(scores))
    print("Min Score =", min(scores))

    print("*" * 100)
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune', 'Uranus', 'Pluto']
    planets = planets.sort()
    print(planets)

    print("*" * 100)
    