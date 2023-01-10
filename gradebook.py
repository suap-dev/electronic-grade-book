from typing import Literal
from typeguard import typechecked
import pandas as pd
from datetime import datetime

class Subject:
    __slots__ = ['__subject_name', '__teachers_name', '__grades']
    
    valid_grades = Literal[
        '1',        
        '2',
        '2+',
        '3',
        '3+',
        '4',
        '4+',
        '5',
        '5+',
        '6'
    ]
    weights = Literal[1, 2, 3, 4]
    
    @typechecked
    def __init__(self, subject_name: str, teacher: str=None) -> None:
        self.__teachers_name = teacher
        self.__subject_name = subject_name
        self.__grades = pd.DataFrame(
            columns=[
                'grade',  
                'weight', 
                'comment',
                'date',
                
                'valid',
                'invalidation reason',
                'invalidation date'
            ]
        )
        
    @typechecked
    def add_grade(self, grade: valid_grades, weight: weights=1, comment: str=None) -> None:
        self.__grades = self.__grades.append(
            {
                'date'      : datetime.now(),
                'grade'     : grade,
                'weight'    : weight,
                'comment'   : comment,
                
                'valid'                 : True,                
                'invalidation reason'   : None,
                'invalidation date'     : None
            },
            ignore_index=True
        )
    
    @typechecked
    def invalidate_grade(self, index: int, reason: str) -> None:
        self.__grades.loc[index,'valid'] = False
        self.__grades.loc[index,'invalidation reason'] = reason
        self.__grades.loc[index,'invalidation date'] = datetime.now()
     
    @typechecked   
    def get_grades(self) -> pd.DataFrame:        
        return self.__grades.copy()
    
    grades = property(get_grades)