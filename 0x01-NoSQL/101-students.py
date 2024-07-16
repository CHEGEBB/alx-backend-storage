#!/usr/bin/env python3
'''
101-students.py file
'''


def top_students(mongo_collection):
    '''
    Prints all students in a school collection sorted by average score.
    '''
    students = mongo_collection.aggregate(
        [
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': {
                            '$avg': '$topics.score',
                        },
                    },
                    'topics': 1,
                },
            },
            {
                '$sort': {'averageScore': -1},
            },
        ]
    )
    return students
