"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["600005"],
            "answer": [6],
        },
        {
            "input": ["6000050"],
            "answer": [6, 50],
        },
        {
            "input": ["045349"],
            "answer": [0, 4, 5, 34],
            "explanation": "5+7=?"
        },
        {
            "input": ["77777777777777777777777"],
            "answer": [7, 77, 777, 7777, 77777, 777777],
        },
    ],
    "Extra": [
        {
            "input": ["122333444455555666666"],
            "answer": [1, 2, 23, 33, 44, 445, 555, 566, 666],
        },
        {
            "input": ["2718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921817413596629043572900334295260"],
            "answer": [2, 7, 18, 28, 182, 845, 904, 5235, 36028, 74713, 526624, 977572, 4709369, 9959574, 96696762, 772407663, 3535475945, 7138217852, 51664274274, 66391932003, 599218174135, 966290435729],
        },
        {
            "input": ["1234" * 80],
            "answer": [1,
 2,
 3,
 4,
 12,
 34,
 123,
 412,
 3412,
 34123,
 41234,
 123412,
 341234,
 1234123,
 4123412,
 34123412,
 341234123,
 412341234,
 1234123412,
 3412341234,
 12341234123,
 41234123412,
 341234123412,
 3412341234123,
 4123412341234,
 12341234123412,
 34123412341234,
 123412341234123,
 412341234123412,
 3412341234123412,
 34123412341234123,
 41234123412341234,
 123412341234123412,
 341234123412341234],
        },
    ]
}
