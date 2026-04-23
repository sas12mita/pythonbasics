question=[
    "Who is the prime minister of Nepal",
    "what is 2+3",
    "Capital city of Nepal",
    ]
answer=[
    "Balendra Shah",
    "5",
    "kathmandu"
]
def quiz(question,answer):
    for i in range(len(question)):
        q=input(question[i])
        if q==answer[i]